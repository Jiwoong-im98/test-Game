"""Player entity: tile-based position and rendering."""

import pygame

from game.settings import COLOR_PLAYER, TILE_SIZE


class Player:
    """The player-controlled character, positioned on the tile grid."""

    def __init__(self, tile_x: int, tile_y: int):
        self.tile_x = tile_x
        self.tile_y = tile_y

    def move(self, dx: int, dy: int, floor_tiles: set[tuple[int, int]]):
        """Move by one tile if the destination is part of the floor."""
        new_tile = (self.tile_x + dx, self.tile_y + dy)
        if new_tile in floor_tiles:
            self.tile_x, self.tile_y = new_tile

    def draw(self, surface):
        """Draw the player as a colored rectangle at its tile position."""
        rect = pygame.Rect(
            self.tile_x * TILE_SIZE, self.tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE
        )
        pygame.draw.rect(surface, COLOR_PLAYER, rect)
