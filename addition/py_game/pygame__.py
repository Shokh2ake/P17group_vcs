import pygame

pygame.init()

size = (800, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Frist game")
player_rect = pygame.Rect(0, 0, 50, 50)
player_rect.center = (size[0] // 2, size[1] // 2)

running = True
while running:
    key = pygame.key.get_pressed()
    screen.fill((67, 98, 32))
    mouse = pygame.mouse.get_pos()
    pygame.mouse.set_visible(False)
    # player_rect.x = mouse[0]
    # player_rect.y = mouse[1]
    player_rect.center = mouse

    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            running = False

    pygame.draw.circle(screen, "red", player_rect.center, 100)


    for i in range(1, 9):
        pygame.draw.line(screen, "white", (0, 100 * i), (size[0], 100 * i), 10)
    for j in range(1, 9):
        pygame.draw.line(screen, "whitr", (100*j, 0), (100*j, size[1]), 10)
    pygame.display.update()
pygame.quit()
