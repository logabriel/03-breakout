"""
Assignment 3: Breakout
Author: Gabriel Perez 

This file contains the Power Up specialization to add two cannons to the game palette.
"""


import random
from typing import TypeVar

import settings
from src.powerups.PowerUp import PowerUp


class PairCannons(PowerUp):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 3)

    def take(self, play_state: TypeVar("PlayState")) -> None:
        if not play_state.paddle.cannon_left.active_cannon:        
            play_state.paddle.cannon_left.active_cannon = True
            play_state.paddle.cannon_right.active_cannon = True

        self.active = False