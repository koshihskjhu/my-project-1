import random
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = pygame.Rect(WIDTH // 2 - 20, HEIGHT // 2 - 20, 40, 40)
coin = pygame.Rect(random.randint(20, WIDTH - 40), random.randint(20, HEIGHT - 40), 24, 24)
enemy = pygame.Rect(60, 60, 36, 36)

player_speed = 5
enemy_speed = 3
score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    dx = (keys[pygame.K_d] or keys[pygame.K_RIGHT]) - (keys[pygame.K_a] or keys[pygame.K_LEFT])
    dy = (keys[pygame.K_s] or keys[pygame.K_DOWN]) - (keys[pygame.K_w] or keys[pygame.K_UP])

    player.x = max(0, min(WIDTH - player.width, player.x + dx * player_speed))
    player.y = max(0, min(HEIGHT - player.height, player.y + dy * player_speed))

    if enemy.x < player.x:
        enemy.x += enemy_speed
    elif enemy.x > player.x:
        enemy.x -= enemy_speed

    if enemy.y < player.y:
        enemy.y += enemy_speed
    elif enemy.y > player.y:
        enemy.y -= enemy_speed

    if player.colliderect(coin):
        score += 1
        coin.x = random.randint(20, WIDTH - 40)
        coin.y = random.randint(20, HEIGHT - 40)

    if player.colliderect(enemy):
        score = 0
        player.center = (WIDTH // 2, HEIGHT // 2)
        enemy.topleft = (60, 60)

    screen.fill((20, 24, 30))
    pygame.draw.rect(screen, (80, 200, 120), player)
    pygame.draw.rect(screen, (250, 204, 21), coin)
    pygame.draw.rect(screen, (220, 60, 60), enemy)

    text = font.render(f"Score: {score}", True, (240, 240, 240))
    screen.blit(text, (16, 16))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()