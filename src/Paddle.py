"""
ISPPV1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Paddle.
"""

import pygame

import settings

from src.Cannon import Cannon
from typing import TypeVar

class Paddle:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.width = 64
        self.height = 16

        # By default, the blue paddle
        self.skin = 0

        # By default, the 64-pixels-width paddle.
        self.size = 1

        self.texture = settings.TEXTURES["spritesheet"]
        self.frames = settings.FRAMES["paddles"]

        # The paddle only move horizontally
        self.vx = 0

        # The paddle has two cannons
        self.cannon_left = Cannon(self.x, self.y + 12 + 16, 0,)
        self.cannon_right = Cannon(self.x, self.y + 12 + 16, 1,)

    def resize(self, size: int) -> None:
        self.size = size
        self.width = (self.size + 1) * 32

    def dec_size(self):
        self.resize(max(0, self.size - 1))

    def inc_size(self):
        self.resize(min(3, self.size + 1))

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, dt: float) -> None:
        next_x = self.x + self.vx * dt

        if not self.cannon_left.active_cannon:
            if self.vx < 0:
                self.x = max(0, next_x)
            else:
                self.x = min(settings.VIRTUAL_WIDTH - self.width, next_x)
        else:
            if self.vx < 0:
                self.x = max(0 + self.cannon_left.width, next_x)
            else:
                self.x = min(settings.VIRTUAL_WIDTH - self.width - self.cannon_left.width, next_x)
            
            self.cannon_left.update(dt, self.x - self.cannon_left.width)
            self.cannon_right.update(dt, self.x + self.width)

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(self.texture, (self.x, self.y), self.frames[self.skin][self.size])
        
        if self.cannon_left.active_cannon and self.cannon_right.active_cannon:
            self.cannon_left.render(surface)
            self.cannon_right.render(surface)
    
    def fire(self, play_state: TypeVar("PlayState")) -> None:
        if self.cannon_left.active_cannon and self.cannon_right.active_cannon:
            self.cannon_left.fire(self.cannon_left.x, self.cannon_left.y, play_state)
            self.cannon_right.fire(self.cannon_right.x, self.cannon_right.y, play_state)