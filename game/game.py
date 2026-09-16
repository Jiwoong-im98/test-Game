"""Core Game class: window setup and main loop."""

import pygame

from game.entities.player import Player
from game.settings import (
    COLOR_BACKGROUND,
    COLOR_GRID_LINE,
    FPS,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TILE_SIZE,
)
from game.world.room import generate_room, start_tile

GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE

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
        self.floor_tiles = generate_room(GRID_WIDTH, GRID_HEIGHT)
        start_x, start_y = start_tile(GRID_WIDTH, GRID_HEIGHT)
        self.player = Player(start_x, start_y)

    def run(self):
        """Run the main loop until quit."""
        while self.running:
            self._handle_events()
            self.screen.fill(COLOR_BACKGROUND)
            self._draw_floor()
            self.player.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()

    def _draw_floor(self):
        """Draw a white grid-line outline for each generated floor tile."""
        for tile_x, tile_y in self.floor_tiles:
            rect = pygame.Rect(
                tile_x * TILE_SIZE, tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE
            )
            pygame.draw.rect(self.screen, COLOR_GRID_LINE, rect, 1)

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
