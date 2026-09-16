"""Pure isometric tile-to-screen coordinate math (no pygame dependency)."""

from game.settings import TILE_HEIGHT, TILE_WIDTH


def tile_to_screen(
    tile_x: int, tile_y: int, origin_x: int, origin_y: int
) -> tuple[int, int]:
    """Project tile-grid coordinates to isometric screen pixel coordinates."""
    screen_x = origin_x + (tile_x - tile_y) * (TILE_WIDTH // 2)
    screen_y = origin_y + (tile_x + tile_y) * (TILE_HEIGHT // 2)
    return screen_x, screen_y


def diamond_points(
    center_x: int, center_y: int, width: int, height: int
) -> list[tuple[int, int]]:
    """The 4 corner points (top, right, bottom, left) of a diamond centered here."""
    half_w = width // 2
    half_h = height // 2
    return [
        (center_x, center_y - half_h),
        (center_x + half_w, center_y),
        (center_x, center_y + half_h),
        (center_x - half_w, center_y),
    ]
