"""Tests for the pure isometric tile-to-screen coordinate transform."""

from game.iso import diamond_points, tile_to_screen


def test_tile_to_screen_at_origin_tile():
    # (tile_x - tile_y) = 0 and (tile_x + tile_y) = 0, so screen == origin.
    assert tile_to_screen(0, 0, 100, 50) == (100, 50)


def test_tile_to_screen_known_offset():
    # TILE_WIDTH=64, TILE_HEIGHT=32 -> half-width=32, half-height=16.
    # tile_x - tile_y = 2, tile_x + tile_y = 4
    # screen_x = 100 + 2*32 = 164, screen_y = 50 + 4*16 = 114
    assert tile_to_screen(3, 1, 100, 50) == (164, 114)


def test_tile_to_screen_negative_diff():
    # tile_x - tile_y = -5, tile_x + tile_y = 5
    # screen_x = 100 + (-5)*32 = -60, screen_y = 50 + 5*16 = 130
    assert tile_to_screen(0, 5, 100, 50) == (-60, 130)


def test_diamond_points_shape():
    points = diamond_points(100, 50, 64, 32)
    assert points == [(100, 34), (132, 50), (100, 66), (68, 50)]
