import pygame
import os
from pygame.event import clear 

WIDTH,HEIGHT = 900,500 
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40
pygame.display.set_caption("test_game 0.0.2")
FPS =60
VEL = 5 
Bullet_vel = 150
red_bullets = []
yellow_bullets = []
max_bullets = 15
BORDER = pygame.Rect(450,0,10,500)


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE , (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE , (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)


def draw_window(red , yellow ):
    white = (255,255,255)
    black = (0,0,0)
    pygame.draw.rect(WIN, black, pygame.Rect(458,0,10,500))
    pygame.display.update()
    WIN.fill(white)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP , (red.x,red.y))

    

def yellow_handle_movement(key_pressed , yellow):
    if key_pressed[pygame.K_a] and yellow.x -VEL > 0 :
        yellow.x -= VEL
    if key_pressed[pygame.K_d] and yellow.x + VEL +yellow.width < BORDER.x:
        yellow.x += VEL
    if key_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL
    if key_pressed[pygame.K_s] and yellow.y + VEL + 15 + yellow.height < HEIGHT:
        yellow.y += VEL

def red_handle_movement(key_pressed , red ):
    if key_pressed[pygame.K_LEFT]  and red.x -VEL > BORDER.x + BORDER.width :
        red.x -= VEL
    if key_pressed[pygame.K_RIGHT] and red.x + VEL +red.width < WIDTH:
        red.x += VEL
    if key_pressed[pygame.K_UP]    and red.y - VEL > 0:
        red.y -= VEL
    if key_pressed[pygame.K_DOWN]  and red.y + VEL + 15 + red.height < HEIGHT:
        red.y += VEL

def handle_bullets():
    

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < max_bullets :
                    bullet = pygame.Rect(yellow.x + yellow.width,yellow.y +yellow.height/2 -2,10,5)
                    yellow_bullets.append(bullet)

                if event.key ==pygame.K_RCTRL and len(red_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x,red.y +red.height/2 -2,10,5)
                    red_bullets.append(bullet)

        print(red_bullets,yellow_bullets)    
        key_pressed = pygame.key.get_pressed()
        yellow_handle_movement(key_pressed , yellow)
        red_handel_movement(key_pressed , red )
        draw_window(red,yellow)

    pygame.quit()

if __name__ == "__main__":
    main()
