"""
ISPPV1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class to define the Play state.
"""

import random

import pygame

from gale.factory import AbstractFactory
from gale.state import BaseState
from gale.input_handler import InputData
from gale.text import render_text
from src.CannonBall import CannonBall
from src.powerups.GoldCoin import GoldCoin
from src.utilities.floating_text import FloatingText

import settings
import src.powerups


class PlayState(BaseState):
    def enter(self, **params: dict):
        self.level = params["level"]
        self.score = params["score"]
        self.lives = params["lives"]
        self.paddle = params["paddle"]
        self.balls = params["balls"]
        self.brickset = params["brickset"]
        self.live_factor = params["live_factor"]
        self.points_to_next_live = params["points_to_next_live"]
        self.points_to_next_grow_up = (
            self.score
            + settings.PADDLE_GROW_UP_POINTS * (self.paddle.size + 1) * self.level
        )
        self.powerups = params.get("powerups", [])
        self.score_multiplier = 1
        self.floating_texts = []

        if not params.get("resume", False):
            self.balls[0].vx = random.randint(-80, 80)
            self.balls[0].vy = random.randint(-170, -100)
            settings.SOUNDS["paddle_hit"].play()

        self.powerups_abstract_factory = AbstractFactory("src.powerups")

        self.timer_attached_ball = params.get("timer_attached_ball", 0)

    def update(self, dt: float) -> None:
        self.paddle.update(dt)

        for ball in self.balls:
            ball.update(dt)
            ball.solve_world_boundaries()

            # Check collision with the paddle
            if ball.collides(self.paddle) and not ball.sticky:
                settings.SOUNDS["paddle_hit"].stop()
                settings.SOUNDS["paddle_hit"].play()
                ball.rebound(self.paddle)
                ball.push(self.paddle.get_collision_rect(), self.paddle.vx)
            elif ball.collides(self.paddle) and ball.sticky:
                settings.SOUNDS["paddle_hit"].stop()
                settings.SOUNDS["paddle_hit"].play()
                ball.attached_paddle(self.paddle.x)

            #check attached ball with paddle
            if ball.sticky:
                self.timer_attached_ball += dt

            if self.timer_attached_ball >= 7:
                self.timer_attached_ball = 0
                for ball in self.balls:
                    ball.sticky = False
            
            if ball.attached_ball:
                ball.set_position_ball(self.paddle.x)
            
            # Check collision with brickset
            if not ball.collides(self.brickset):
                continue

            brick = self.brickset.get_colliding_brick(ball.get_collision_rect())

            if brick is None:
                continue

            brick.hit()
            self.score += brick.score() * self.score_multiplier

            if type(ball) == CannonBall:
                ball.active = False

            ball.rebound(brick)

            # Check earn life
            if self.score >= self.points_to_next_live:
                settings.SOUNDS["life"].play()
                self.lives = min(3, self.lives + 1)
                self.live_factor += 0.5
                self.points_to_next_live += settings.LIVE_POINTS_BASE * self.live_factor

            # Check growing up of the paddle
            if self.score >= self.points_to_next_grow_up:
                settings.SOUNDS["grow_up"].play()
                self.points_to_next_grow_up += (
                    settings.PADDLE_GROW_UP_POINTS * (self.paddle.size + 1) * self.level
                )
                self.paddle.inc_size()

            # Chance to generate two more balls
            if random.random() < settings.POWERUP_SPAWN_CHANCE:
                r = brick.get_collision_rect()
                self.powerups.append(
                    self.powerups_abstract_factory.get_factory("TwoMoreBall").create(
                        r.centerx - 8, r.centery - 8
                    )
                )
            
            # Chance to generate attached ball
            if random.random() < settings.POWERUP_SPAWN_CHANCE:
                r = brick.get_collision_rect()
                self.powerups.append(
                    self.powerups_abstract_factory.get_factory("AttachedBall").create(
                        r.centerx - 8, r.centery - 8
                    )
                )
            
            # Chance to generate pair cannons
            if random.random() < settings.POWERUP_SPAWN_CHANCE:
                r = brick.get_collision_rect()
                self.powerups.append(
                    self.powerups_abstract_factory.get_factory("PairCannons").create(
                        r.centerx - 8, r.centery - 8
                    )
                )
            
            # Chance to generate GoldCoin
            if random.random() < settings.POWERUP_SPAWN_CHANCE:
                r = brick.get_collision_rect()
                self.powerups.append(GoldCoin(r.centerx - 8, r.centery - 8))

        # Removing all balls that are not in play
        self.balls = [ball for ball in self.balls if ball.active]

        self.brickset.update(dt)

        if not self.balls:
            self.lives -= 1
            if self.lives == 0:
                self.state_machine.change("game_over", score=self.score)
            else:
                self.paddle.dec_size()
                self.state_machine.change(
                    "serve",
                    level=self.level,
                    score=self.score,
                    lives=self.lives,
                    paddle=self.paddle,
                    brickset=self.brickset,
                    points_to_next_live=self.points_to_next_live,
                    live_factor=self.live_factor,
                )

        # Update powerups
        for powerup in self.powerups[:]: 
            powerup.update(dt)
            if powerup.active and powerup.collides(self.paddle):  # Comprobar si está activo
                powerup.take(self)
            elif not powerup.active:  # Eliminar si ya no está activo
                self.powerups.remove(powerup)

        # Update floating texts
        for text in self.floating_texts[:]:
            text["y"] -= 1  # Mover hacia arriba
            text["duration"] -= dt
            if text["duration"] <= 0:
                self.floating_texts.remove(text)

        # Check victory
        if self.brickset.size == 1 and next(
            (True for _, b in self.brickset.bricks.items() if b.broken), False
        ):
            self.state_machine.change(
                "victory",
                lives=self.lives,
                level=self.level,
                score=self.score,
                paddle=self.paddle,
                balls=self.balls,
                points_to_next_live=self.points_to_next_live,
                live_factor=self.live_factor,
            )

    def render(self, surface: pygame.Surface) -> None:
        heart_x = settings.VIRTUAL_WIDTH - 120

        i = 0
        # Draw filled hearts
        while i < self.lives:
            surface.blit(
                settings.TEXTURES["hearts"], (heart_x, 5), settings.FRAMES["hearts"][0]
            )
            heart_x += 11
            i += 1

        # Draw empty hearts
        while i < 3:
            surface.blit(
                settings.TEXTURES["hearts"], (heart_x, 5), settings.FRAMES["hearts"][1]
            )
            heart_x += 11
            i += 1

        render_text(
            surface,
            f"Score: {self.score}",
            settings.FONTS["tiny"],
            settings.VIRTUAL_WIDTH - 80,
            5,
            (255, 255, 255),
        )

        self.brickset.render(surface)

        self.paddle.render(surface)

        for ball in self.balls:
            ball.render(surface)

        for powerup in self.powerups:
            powerup.render(surface)

        for text in self.floating_texts[:]:
            render_text(
                surface,
                text["text"],
                settings.FONTS["small"],
                text["x"],
                text["y"],
                text["color"],
            )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "move_left":
            if input_data.pressed:
                self.paddle.vx = -settings.PADDLE_SPEED
            elif input_data.released and self.paddle.vx < 0:
                self.paddle.vx = 0
        elif input_id == "move_right":
            if input_data.pressed:
                self.paddle.vx = settings.PADDLE_SPEED
            elif input_data.released and self.paddle.vx > 0:
                self.paddle.vx = 0
        elif input_id == "enter":
            if input_data.pressed:
                for ball in self.balls:
                    if ball.attached_ball:
                        if self.paddle.vx < 0:
                            ball.vx = random.randint(-80, -50)
                            ball.vy = random.randint(-170, -100)
                            ball.attached_ball = False
                        elif self.paddle.vx > 0:
                            ball.vx = random.randint(50, 80)
                            ball.vy = random.randint(-170, -100)
                            ball.attached_ball = False
                        elif self.paddle.vx == 0:
                            ball.vx = 0
                            ball.vy = random.randint(-170, -100)
                            ball.attached_ball = False
        elif input_id == "fire":
            if input_data.released:
                self.paddle.fire(self)
                self.paddle.cannon_left.active_cannon = False
                self.paddle.cannon_right.active_cannon = False
        elif input_id == "pause" and input_data.pressed:
            self.state_machine.change(
                "pause",
                level=self.level,
                score=self.score,
                lives=self.lives,
                paddle=self.paddle,
                balls=self.balls,
                brickset=self.brickset,
                points_to_next_live=self.points_to_next_live,
                live_factor=self.live_factor,
                powerups=self.powerups,
                timer_attached_ball=self.timer_attached_ball,
            )
