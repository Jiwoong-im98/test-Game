"""Core Game class: window setup and main loop."""

import pygame

from game.settings import COLOR_BACKGROUND, FPS, SCREEN_HEIGHT, SCREEN_WIDTH


class Game:
    """Owns the pygame window, clock, and main loop."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("test-game")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        """Run the main loop until quit."""
        while self.running:
            self._handle_events()
            self.screen.fill(COLOR_BACKGROUND)
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
