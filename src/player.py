import pygame
import settings


class Player:
    def __init__(self, x: int, y: int):
        self.rect = pygame.Rect(x, y, 32, 32)
        self.pos_x = float(x)
        self.pos_y = float(y)
        self.stamina = float(settings.PLAYER_MAX_STAMINA)
        self.hp = int(settings.PLAYER_MAX_HP)

    def update(self, dt: float, keys) -> None:
        dx = (keys[pygame.K_d] or keys[pygame.K_RIGHT]) - (keys[pygame.K_a] or keys[pygame.K_LEFT])
        dy = (keys[pygame.K_s] or keys[pygame.K_DOWN]) - (keys[pygame.K_w] or keys[pygame.K_UP])

        length = (dx * dx + dy * dy) ** 0.5
        if length > 0:
            dx /= length
            dy /= length

        is_moving = length > 0
        wants_sprint = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]
        sprinting = is_moving and wants_sprint and self.stamina > 0

        speed = settings.PLAYER_SPRINT_SPEED if sprinting else settings.PLAYER_SPEED
        self.pos_x += dx * speed * 60.0 * dt
        self.pos_y += dy * speed * 60.0 * dt

        self.pos_x = max(0.0, min(self.pos_x, float(settings.SCREEN_WIDTH - self.rect.width)))
        self.pos_y = max(0.0, min(self.pos_y, float(settings.SCREEN_HEIGHT - self.rect.height)))
        self.rect.topleft = (int(self.pos_x), int(self.pos_y))

        if sprinting:
            self.stamina = max(0.0, self.stamina - settings.STAMINA_DRAIN * dt)
        else:
            self.stamina = min(float(settings.PLAYER_MAX_STAMINA), self.stamina + settings.STAMINA_REGEN * dt)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, settings.COLOR_PLAYER, self.rect)