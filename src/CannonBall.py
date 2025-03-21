"""
Assignment 3: Breakout
Author: Gabriel Perez 

This file contains the class CannonBall
"""

import random
import settings

from src.Ball import Ball

class CannonBall(Ball):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y)
        self.vy = -80

    def solve_world_boundaries(self) -> None:
        r = self.get_collision_rect()

        if r.top < 0:
            settings.SOUNDS["wall_hit"].stop()
            settings.SOUNDS["wall_hit"].play()
            self.active = False

    def update(self, dt: float) -> None:
        self.y += self.vy * dt