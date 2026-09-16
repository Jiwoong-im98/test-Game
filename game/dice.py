"""Dice rolling logic: random direction picks (no pygame dependency)."""

import random

DIRECTIONS = ["up", "down", "left", "right"]

DIRECTION_DELTAS = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
}


def roll_dice(count: int = 3, rng: random.Random | None = None) -> list[str]:
    """Roll `count` dice, each landing on a random direction."""
    if rng is None:
        rng = random.Random()

    return [rng.choice(DIRECTIONS) for _ in range(count)]
