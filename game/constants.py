# CONSTANTS.py
import numpy as np

# Port Globals
FIRSTPORT = 50000
TANKPORT = 50001
BULLETPORT = 50002
TERRAINPORT = 50003
SERVER = 'localhost'

# Game Globals
PARALLAX = 2
PIXEL_SIZE = 5
GRAVITY = np.asarray([0, 0.1])
EXPLOSION_SIZE = 8*PIXEL_SIZE
BARWIDTH = 100
BARHEIGHT = 16
MAXHEALTH = 1000
ROCK_LEVEL = 5
MAXBULLET = 5
DAMAGE = 50
