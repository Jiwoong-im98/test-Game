"""Tests for Player tile movement logic."""

from game.entities.player import Player

FLOOR_TILES = {(5, 5), (6, 5), (5, 6), (4, 5), (5, 4)}


def test_move_up_onto_floor():
    player = Player(5, 5)
    player.move(0, -1, FLOOR_TILES)
    assert (player.tile_x, player.tile_y) == (5, 4)


def test_move_down_onto_floor():
    player = Player(5, 5)
    player.move(0, 1, FLOOR_TILES)
    assert (player.tile_x, player.tile_y) == (5, 6)


def test_move_left_onto_floor():
    player = Player(5, 5)
    player.move(-1, 0, FLOOR_TILES)
    assert (player.tile_x, player.tile_y) == (4, 5)


def test_move_right_onto_floor():
    player = Player(5, 5)
    player.move(1, 0, FLOOR_TILES)
    assert (player.tile_x, player.tile_y) == (6, 5)


def test_move_up_blocked_off_floor():
    floor_tiles = {(5, 5), (6, 5), (5, 6)}
    player = Player(5, 5)
    player.move(0, -1, floor_tiles)
    assert (player.tile_x, player.tile_y) == (5, 5)


def test_move_down_blocked_off_floor():
    floor_tiles = {(5, 5), (6, 5), (5, 4)}
    player = Player(5, 5)
    player.move(0, 1, floor_tiles)
    assert (player.tile_x, player.tile_y) == (5, 5)


def test_move_left_blocked_off_floor():
    floor_tiles = {(5, 5), (6, 5), (5, 6)}
    player = Player(5, 5)
    player.move(-1, 0, floor_tiles)
    assert (player.tile_x, player.tile_y) == (5, 5)


def test_move_right_blocked_off_floor():
    floor_tiles = {(5, 5), (5, 6), (5, 4)}
    player = Player(5, 5)
    player.move(1, 0, floor_tiles)
    assert (player.tile_x, player.tile_y) == (5, 5)
