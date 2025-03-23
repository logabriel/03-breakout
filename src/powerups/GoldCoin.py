from typing import TypeVar
import pygame
from src.powerups.PowerUp import PowerUp
from src.utilities.timer import Timer
import settings

class GoldCoin(PowerUp):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, frame=0)  
        self.multiplier = 2
        self.duration = 10
        self.active = True
        self.texture = settings.TEXTURES["coin"]
        self.x = x
        self.y = y

    def render(self, surface: pygame.Surface) -> None:
        if self.active:
            surface.blit(
                self.texture,
                (self.x, self.y)
            )

    def take(self, play_state: TypeVar("PlayState")) -> None:
        play_state.score_multiplier = self.multiplier
        
        play_state.floating_texts.append({
            "text": f"x{self.multiplier}!",
            "x": self.x,
            "y": self.y,
            "duration": 1.5,
            "color": (255, 215, 0)
        })
        
        settings.SOUNDS["grow_up"].play()  
        
        Timer.after(self.duration, self, play_state)
        self.active = False

    def reset_multiplier(self, play_state: TypeVar("PlayState")) -> None:
        play_state.score_multiplier = 1
        play_state.floating_texts.append({
            "text": "Multiplier expired!",
            "x": play_state.paddle.x,
            "y": play_state.paddle.y - 20,
            "duration": 1.0,
            "color": (255, 0, 0)
        })

    def update(self, dt: float) -> None:
        if self.active:
            self.y += settings.POWERUP_SPEED * dt
            if self.y > settings.VIRTUAL_HEIGHT:
                self.active = False

    def collides(self, paddle):
        powerup_rect = pygame.Rect(self.x, self.y, self.texture.get_width(), self.texture.get_height())
        return powerup_rect.colliderect(paddle.get_collision_rect())

