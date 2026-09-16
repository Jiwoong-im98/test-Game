"""Global game settings and constants.

Resolution: 640x480 with TILE_SIZE=32 gives an exact 20x15 tile grid,
which keeps future tile-based room rendering simple (no partial tiles
at the screen edges). Plain pixel values, no internal-surface scaling
for now.
"""

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60
TILE_SIZE = 32

# Colors (R, G, B)
COLOR_BACKGROUND = (20, 20, 28)
COLOR_WALL = (80, 80, 90)
COLOR_FLOOR = (140, 120, 100)
COLOR_PLAYER = (60, 160, 220)
COLOR_ENEMY = (200, 60, 60)
