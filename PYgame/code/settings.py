import os

sourceFileDir = os.path.abspath("C:/IVELWL/CDCA_FYP/PYgame")

# game setup
WIDTH = 1280
HEIGTH = 720
FPS = 60
TILESIZE = 64

# weapons
weapon_data = {
    "sword": {"cooldown": 100, "damage": 15, "graphic": sourceFileDir + "/graphics/weapons/sword/full.png"},
    "lance": {"cooldown": 400, "damage": 30, "graphic": sourceFileDir + "/graphics/weapons/lance/full.png"},
    "axe": {"cooldown": 300, "damage": 20, "graphic": sourceFileDir + "/graphics/weapons/axe/full.png"},
    "rapier": {"cooldown": 50, "damage": 8, "graphic": sourceFileDir + "/graphics/weapons/rapier/full.png"},
    "sai": {"cooldown": 80, "damage": 10, "graphic": sourceFileDir + "/graphics/weapons/sai/full.png"},
}