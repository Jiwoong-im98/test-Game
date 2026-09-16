"""Tests for dice rolling logic."""

import random

from game.dice import DIRECTIONS, roll_dice


def test_roll_dice_returns_count_results():
    results = roll_dice(3, rng=random.Random(1))
    assert len(results) == 3


def test_roll_dice_results_are_valid_directions():
    results = roll_dice(3, rng=random.Random(2))
    for direction in results:
        assert direction in DIRECTIONS


def test_roll_dice_varies_between_seeds():
    results_a = roll_dice(10, rng=random.Random(3))
    results_b = roll_dice(10, rng=random.Random(4))
    assert results_a != results_b
