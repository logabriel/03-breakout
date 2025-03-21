"""
Assignment 3: Breakout
Author: Gabriel Perez 

This file contains the class Cannon
"""

import pygame

import settings
from gale.factory import Factory
from src.CannonBall import CannonBall
from typing import TypeVar

class Cannon:
    def __init__(self, x: int, y: int, side_cannon: int) -> None:
        self.x = x
        self.y = y
        self.width = 12
        self.height = 24
        self.side_cannon = side_cannon # 0: left, 1: right
        self.texture = settings.TEXTURES["cannons"]
        self.active_cannon = False
        self.cannon_ball_factory = Factory(CannonBall)

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, dt: float, position: float) -> None:
        self.x = position

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(self.texture, (self.x, self.y), settings.FRAMES["cannons"][self.side_cannon])

    def fire(self, x: int, y: int, play_state: TypeVar("PlayState")) -> None:
        cannon_ball = self.cannon_ball_factory.create(x, y)
        
        play_state.balls.append(cannon_ball)