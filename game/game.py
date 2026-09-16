"""Core Game class: window setup and main loop."""

import pygame

from game.entities.player import Player
from game.iso import diamond_points, tile_to_screen
from game.settings import (
    COLOR_BACKGROUND,
    COLOR_GRID_LINE,
    FPS,
    ISO_ORIGIN_X,
    ISO_ORIGIN_Y,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TILE_HEIGHT,
    TILE_WIDTH,
)
from game.world.room import generate_room, start_tile

GRID_WIDTH = 20
GRID_HEIGHT = 15

MOVE_KEYS = {
    pygame.K_UP: (0, -1),
    pygame.K_w: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_s: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_a: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_d: (1, 0),
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

    def run(self):
        """Run the main loop until quit."""
        while self.running:
            self._handle_events()
            self.screen.fill(COLOR_BACKGROUND)
            self._draw_floor()
            self.player.draw(self.screen, self.origin_x, self.origin_y)
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

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key in MOVE_KEYS:
                    dx, dy = MOVE_KEYS[event.key]
                    self.player.move(dx, dy, self.floor_tiles)
