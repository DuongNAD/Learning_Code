from bird import Bird
import pygame

pygame.init()
SCREEN_WIDTH = 416
SCREEN_HEIGHT = 512
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy_Bird")

bird = Bird()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((135,206,235))
    bird.draw(screen)
    pygame.display.flip()

pygame.quit()