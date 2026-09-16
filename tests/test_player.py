"""Tests for Player tile movement logic."""

from game.entities.player import Player

GRID_WIDTH = 20
GRID_HEIGHT = 15


def test_move_up():
    player = Player(5, 5)
    player.move(0, -1, GRID_WIDTH, GRID_HEIGHT)
    assert (player.tile_x, player.tile_y) == (5, 4)


def test_move_down():
    player = Player(5, 5)
    player.move(0, 1, GRID_WIDTH, GRID_HEIGHT)
    assert (player.tile_x, player.tile_y) == (5, 6)


def test_move_left():
    player = Player(5, 5)
    player.move(-1, 0, GRID_WIDTH, GRID_HEIGHT)
    assert (player.tile_x, player.tile_y) == (4, 5)


def test_move_right():
    player = Player(5, 5)
    player.move(1, 0, GRID_WIDTH, GRID_HEIGHT)
    assert (player.tile_x, player.tile_y) == (6, 5)


def test_clamp_left_edge():
    player = Player(0, 5)
    player.move(-1, 0, GRID_WIDTH, GRID_HEIGHT)
    assert player.tile_x == 0


def test_clamp_right_edge():
    player = Player(GRID_WIDTH - 1, 5)
    player.move(1, 0, GRID_WIDTH, GRID_HEIGHT)
    assert player.tile_x == GRID_WIDTH - 1


def test_clamp_top_edge():
    player = Player(5, 0)
    player.move(0, -1, GRID_WIDTH, GRID_HEIGHT)
    assert player.tile_y == 0


def test_clamp_bottom_edge():
    player = Player(5, GRID_HEIGHT - 1)
    player.move(0, 1, GRID_WIDTH, GRID_HEIGHT)
    assert player.tile_y == GRID_HEIGHT - 1
