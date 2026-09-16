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
        self.player = Player(GRID_WIDTH // 2, GRID_HEIGHT // 2)

    def run(self):
        """Run the main loop until quit."""
        while self.running:
            self._handle_events()
            self.screen.fill(COLOR_BACKGROUND)
            self._draw_grid()
            self.player.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()

    def _draw_grid(self):
        """Draw white grid lines separating every tile."""
        for x in range(GRID_WIDTH + 1):
            pos_x = x * TILE_SIZE
            pygame.draw.line(
                self.screen, COLOR_GRID_LINE, (pos_x, 0), (pos_x, SCREEN_HEIGHT)
            )
        for y in range(GRID_HEIGHT + 1):
            pos_y = y * TILE_SIZE
            pygame.draw.line(
                self.screen, COLOR_GRID_LINE, (0, pos_y), (SCREEN_WIDTH, pos_y)
            )

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key in MOVE_KEYS:
                    dx, dy = MOVE_KEYS[event.key]
                    self.player.move(dx, dy, GRID_WIDTH, GRID_HEIGHT)
