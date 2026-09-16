"""Global game settings and constants.

Isometric ("quarter view") rendering: tiles are 64x32 diamonds
(TILE_WIDTH x TILE_HEIGHT, standard 2:1 ratio). The fixed 20x15 tile
grid, projected with tile_to_screen(), spans a diamond region of
1120x560px (see game/iso.py); SCREEN_WIDTH/HEIGHT below add margin so
no tile is clipped, and ISO_ORIGIN_X/Y center that diamond region in
the window.
"""

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
FPS = 60
TILE_WIDTH = 64
TILE_HEIGHT = 32
ISO_ORIGIN_X = 520
ISO_ORIGIN_Y = 36

# Colors (R, G, B)
COLOR_BACKGROUND = (0, 0, 0)
COLOR_WALL = (80, 80, 90)
COLOR_FLOOR = (140, 120, 100)
COLOR_PLAYER = (255, 255, 255)
COLOR_ENEMY = (200, 60, 60)
COLOR_GRID_LINE = (255, 255, 255)
