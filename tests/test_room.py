"""Tests for random-walk room/stage generation."""

import random

from game.world.room import generate_room, start_tile

GRID_WIDTH = 20
GRID_HEIGHT = 15


def test_generate_room_non_empty():
    floor_tiles = generate_room(GRID_WIDTH, GRID_HEIGHT, rng=random.Random(1))
    assert len(floor_tiles) > 0


def test_generate_room_within_bounds():
    floor_tiles = generate_room(GRID_WIDTH, GRID_HEIGHT, rng=random.Random(2))
    for x, y in floor_tiles:
        assert 0 <= x < GRID_WIDTH
        assert 0 <= y < GRID_HEIGHT


def test_generate_room_includes_start_tile():
    floor_tiles = generate_room(GRID_WIDTH, GRID_HEIGHT, rng=random.Random(3))
    assert start_tile(GRID_WIDTH, GRID_HEIGHT) in floor_tiles


def test_generate_room_varies_between_seeds():
    room_a = generate_room(
        GRID_WIDTH, GRID_HEIGHT, min_steps=20, max_steps=30, rng=random.Random(4)
    )
    room_b = generate_room(
        GRID_WIDTH, GRID_HEIGHT, min_steps=150, max_steps=200, rng=random.Random(5)
    )
    assert room_a != room_b
    assert len(room_a) != len(room_b)
