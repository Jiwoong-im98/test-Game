"""Player entity: tile-based position and rendering."""

import pygame

from game.iso import diamond_points, tile_to_screen
from game.settings import COLOR_PLAYER, TILE_HEIGHT, TILE_WIDTH

PLAYER_SCALE = 0.6


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

    def draw(self, surface, origin_x: int, origin_y: int):
        """Draw the player as a filled diamond, inset within its tile."""
        center_x, center_y = tile_to_screen(
            self.tile_x, self.tile_y, origin_x, origin_y
        )
        points = diamond_points(
            center_x,
            center_y,
            int(TILE_WIDTH * PLAYER_SCALE),
            int(TILE_HEIGHT * PLAYER_SCALE),
        )
        pygame.draw.polygon(surface, COLOR_PLAYER, points)
