"""Core Game class: window setup and main loop."""

import pygame

from game.dice import DIRECTION_DELTAS, roll_dice
from game.dice_render import draw_die
from game.entities.player import Player
from game.iso import diamond_points, tile_to_screen
from game.settings import (
    COLOR_BACKGROUND,
    COLOR_GRID_LINE,
    COLOR_UI_BAR_BG,
    COLOR_UI_TEXT,
    FPS,
    ISO_ORIGIN_X,
    ISO_ORIGIN_Y,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TILE_HEIGHT,
    TILE_WIDTH,
    UI_BAR_HEIGHT,
)
from game.world.room import generate_room, start_tile

GRID_WIDTH = 20
GRID_HEIGHT = 15

DICE_PICK_KEYS = {
    pygame.K_1: 0,
    pygame.K_2: 1,
    pygame.K_3: 2,
}


class Game:
    """Owns the pygame window, clock, and main loop."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("test-game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.origin_x = ISO_ORIGIN_X
        self.origin_y = ISO_ORIGIN_Y
        self.floor_tiles = generate_room(GRID_WIDTH, GRID_HEIGHT)
        start_x, start_y = start_tile(GRID_WIDTH, GRID_HEIGHT)
        self.player = Player(start_x, start_y)
        self.font = pygame.font.SysFont(None, 28)
        self.pending_dice: list[str] | None = None
        self.dice_rects: list[pygame.Rect] = []

    def run(self):
        """Run the main loop until quit."""
        while self.running:
            self._handle_events()
            self.screen.fill(COLOR_BACKGROUND)
            self._draw_floor()
            self.player.draw(self.screen, self.origin_x, self.origin_y)
            self._draw_ui_bar()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()

    def _draw_floor(self):
        """Draw a white brick-line diamond outline for each generated floor tile."""
        for tile_x, tile_y in self.floor_tiles:
            center_x, center_y = tile_to_screen(
                tile_x, tile_y, self.origin_x, self.origin_y
            )
            points = diamond_points(center_x, center_y, TILE_WIDTH, TILE_HEIGHT)
            pygame.draw.polygon(self.screen, COLOR_GRID_LINE, points, 2)

    def _draw_ui_bar(self):
        """Draw the bottom UI bar: roll prompt, or the 3 rolled dice to pick from."""
        bar_top = SCREEN_HEIGHT - UI_BAR_HEIGHT
        pygame.draw.rect(
            self.screen, COLOR_UI_BAR_BG, (0, bar_top, SCREEN_WIDTH, UI_BAR_HEIGHT)
        )
        if self.pending_dice is None:
            text = self.font.render("SPACE: Roll dice", True, COLOR_UI_TEXT)
            text_rect = text.get_rect(midleft=(20, bar_top + UI_BAR_HEIGHT // 2))
            self.screen.blit(text, text_rect)
        else:
            self._draw_dice(bar_top)

    def _draw_dice(self, bar_top: int):
        """Draw the 3 rolled dice as isometric cube icons, caching their click rects."""
        box_size = 60
        gap = 30
        center_y = bar_top + UI_BAR_HEIGHT // 2
        self.dice_rects = []
        for index, direction in enumerate(self.pending_dice):
            center_x = 20 + index * (box_size + gap) + box_size // 2
            rect = draw_die(
                self.screen,
                self.font,
                center_x,
                center_y,
                box_size,
                direction,
                index + 1,
            )
            self.dice_rects.append(rect)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self._handle_click(event.pos)

    def _handle_keydown(self, key):
        if key == pygame.K_ESCAPE:
            self.running = False
        elif key == pygame.K_SPACE:
            if self.pending_dice is None:
                self.pending_dice = roll_dice()
        elif key in DICE_PICK_KEYS:
            self._pick_die(DICE_PICK_KEYS[key])

    def _handle_click(self, pos: tuple[int, int]):
        if self.pending_dice is None:
            return
        for index, rect in enumerate(self.dice_rects):
            if rect.collidepoint(pos):
                self._pick_die(index)
                return

    def _pick_die(self, index: int):
        if self.pending_dice is None or index >= len(self.pending_dice):
            return
        dx, dy = DIRECTION_DELTAS[self.pending_dice[index]]
        self.player.move(dx, dy, self.floor_tiles)
        self.pending_dice = None
        self.dice_rects = []
