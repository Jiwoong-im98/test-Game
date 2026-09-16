"""Rendering for rolled dice as pseudo-3D isometric cube icons."""

import pygame

from game.settings import COLOR_DIE_LEFT, COLOR_DIE_RIGHT, COLOR_DIE_TOP, COLOR_UI_TEXT

DIRECTION_LETTERS = {
    "up": "U",
    "down": "D",
    "left": "L",
    "right": "R",
}


def draw_die(
    surface: pygame.Surface,
    font: pygame.font.Font,
    center_x: int,
    center_y: int,
    size: int,
    direction: str,
    number: int,
) -> pygame.Rect:
    """Draw one die as an isometric cube (top/left/right shaded faces).

    The top face carries the direction letter and pick number. Returns the
    icon's bounding rect, usable for click hit-testing.
    """
    half_w = size // 2
    half_h = size // 4
    depth = size // 2

    top = (center_x, center_y - half_h)
    right = (center_x + half_w, center_y)
    bottom = (center_x, center_y + half_h)
    left = (center_x - half_w, center_y)
    bottom_deep = (bottom[0], bottom[1] + depth)
    left_deep = (left[0], left[1] + depth)
    right_deep = (right[0], right[1] + depth)

    pygame.draw.polygon(surface, COLOR_DIE_LEFT, [left, bottom, bottom_deep, left_deep])
    pygame.draw.polygon(
        surface, COLOR_DIE_RIGHT, [bottom, right, right_deep, bottom_deep]
    )
    pygame.draw.polygon(surface, COLOR_DIE_TOP, [top, right, bottom, left])

    letter = DIRECTION_LETTERS[direction]
    label = font.render(f"{number}:{letter}", True, COLOR_UI_TEXT)
    surface.blit(label, label.get_rect(center=(center_x, center_y)))

    return pygame.Rect(left[0], top[1], right[0] - left[0], bottom_deep[1] - top[1])
