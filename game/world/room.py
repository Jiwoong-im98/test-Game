"""Stage/room generation via random-walk ("drunkard's walk")."""

import random

NEIGHBOR_OFFSETS = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def start_tile(grid_width: int, grid_height: int) -> tuple[int, int]:
    """The grid-center tile where a room's random walk (and the player) start."""
    return grid_width // 2, grid_height // 2


def generate_room(
    grid_width: int,
    grid_height: int,
    min_steps: int = 80,
    max_steps: int = 200,
    rng: random.Random | None = None,
) -> set[tuple[int, int]]:
    """Generate an irregular, connected floor shape via a random walk.

    Starts at the grid center and takes a random number of steps in
    [min_steps, max_steps], each moving to a random orthogonal neighbor
    (clamped to grid bounds), collecting every visited tile into a set.
    """
    if rng is None:
        rng = random.Random()

    x, y = start_tile(grid_width, grid_height)
    floor_tiles = {(x, y)}

    steps = rng.randint(min_steps, max_steps)
    for _ in range(steps):
        dx, dy = rng.choice(NEIGHBOR_OFFSETS)
        x = max(0, min(grid_width - 1, x + dx))
        y = max(0, min(grid_height - 1, y + dy))
        floor_tiles.add((x, y))

    return floor_tiles
