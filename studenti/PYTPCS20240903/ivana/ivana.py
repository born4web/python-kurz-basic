import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Prvni hra")
clock = pygame.time.Clock()
running = True

player_color = (0, 128, 255)
player_size = 50
player_x = 375
player_y = 275
player_speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))
    pygame.display.flip()
    clock.tick(60)

pygame.quit() 