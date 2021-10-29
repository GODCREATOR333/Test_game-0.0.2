import pygame
import os
from pygame.event import clear 

WIDTH,HEIGHT = 900,500 
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40
pygame.display.set_caption("test_game 0.0.2")
FPS =60

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE , (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE , (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

def draw_window(red , yellow ):
    white = (255,255,255)
    WIN.fill(white)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP , (red.x,red.y))
    pygame.display.update()

def main():
    red = pygame.Rect(700,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    run = True
    Clock = pygame.time.Clock()
    while run :
        Clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 

        draw_window(red,yellow)

    pygame.quit()

if __name__ == "__main__":
    main()
