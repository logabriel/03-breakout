import pygame

class FloatingText:
    def __init__(self, text: str, x: int, y: int, duration: float, color: tuple):
        self.text = text
        self.x = x
        self.y = y
        self.duration = duration
        self.color = color
        self.font = pygame.font.Font("assets/fonts/font.ttf", 16)

    def update(self, dt: float):
        self.y -= 50 * dt 
        self.duration -= dt

    def render(self, surface: pygame.Surface):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=(self.x, int(self.y)))
        surface.blit(text_surface, text_rect)

