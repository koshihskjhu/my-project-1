import pygame
import settings


class Enemy:
    def __init__(self, x: int, y: int, speed: float | None = None):
        self.rect = pygame.Rect(x, y, 34, 34)
        self.pos_x = float(x)
        self.pos_y = float(y)
        self.speed = float(speed if speed is not None else settings.KILLER_SPEED)

    def update(self, dt: float, target_rect: pygame.Rect) -> None:
        dx = target_rect.centerx - self.rect.centerx
        dy = target_rect.centery - self.rect.centery
        dist = (dx * dx + dy * dy) ** 0.5

        if dist > 0:
            nx = dx / dist
            ny = dy / dist
            self.pos_x += nx * self.speed * 60.0 * dt
            self.pos_y += ny * self.speed * 60.0 * dt

        self.pos_x = max(0.0, min(self.pos_x, float(settings.SCREEN_WIDTH - self.rect.width)))
        self.pos_y = max(0.0, min(self.pos_y, float(settings.SCREEN_HEIGHT - self.rect.height)))
        self.rect.topleft = (int(self.pos_x), int(self.pos_y))

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, settings.COLOR_KILLER, self.rect)