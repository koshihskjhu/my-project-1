import pygame
import settings
from enemy import Enemy
from player import Player


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.GAME_TITLE)
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 28)
        self.running = True
        self.reset()

    def reset(self) -> None:
        self.player = Player(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2)
        self.enemy = Enemy(60, 60)
        self.score = 0.0

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.player.update(dt, keys)
        self.enemy.update(dt, self.player.rect)
        self.score += dt

        if self.player.rect.colliderect(self.enemy.rect):
            self.reset()

    def draw(self) -> None:
        self.screen.fill(settings.COLOR_BG)
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)

        hud = self.font.render(
            f"HP: {self.player.hp}  Stamina: {int(self.player.stamina)}  Time: {int(self.score)}s",
            True,
            settings.COLOR_HUD_TEXT,
        )
        self.screen.blit(hud, (16, 16))
        pygame.display.flip()

    def run(self) -> None:
        while self.running:
            dt = self.clock.tick(settings.FPS) / 1000.0
            self.handle_events()
            self.update(dt)
            self.draw()
        pygame.quit()