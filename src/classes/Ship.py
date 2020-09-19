from src.enums.Rotations import Rotations
import random


class Ship:
    type = 'Ship'
    size = 2

    def __init__(self):
        self.rotation = random.choice(list(Rotations))
