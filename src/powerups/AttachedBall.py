import random
from typing import TypeVar

import settings
from src.Ball import Ball
from src.powerups.PowerUp import PowerUp


class AttachedBall(PowerUp):
    """
    Power-up to adhere ball to paddle.
    """

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 1)

    def take(self, play_state: TypeVar("PlayState")) -> None:        
        for ball in play_state.balls:
            ball.sticky = True

        play_state.timer_attached_ball = 0

        self.active = False