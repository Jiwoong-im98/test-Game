"""Player entity: tile-based position and rendering."""

import pygame

from game.settings import COLOR_PLAYER, TILE_SIZE


class Player:
    """The player-controlled character, positioned on the tile grid."""

    def __init__(self, tile_x: int, tile_y: int):
        self.tile_x = tile_x
        self.tile_y = tile_y

    def move(self, dx: int, dy: int, grid_width: int, grid_height: int):
        """Move by one tile in the given direction, clamped to the grid."""
        self.tile_x = max(0, min(grid_width - 1, self.tile_x + dx))
        self.tile_y = max(0, min(grid_height - 1, self.tile_y + dy))

    def draw(self, surface):
        """Draw the player as a colored rectangle at its tile position."""
        rect = pygame.Rect(
            self.tile_x * TILE_SIZE, self.tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE
        )
        pygame.draw.rect(surface, COLOR_PLAYER, rect)
