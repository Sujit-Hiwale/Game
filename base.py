import pygame
import sys

pygame.init()

width, height = 800, 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Map Display")
map_image = pygame.image.load('./Maps/Castle1.jpg')
map_image = pygame.transform.scale(map_image,(width,height))

user = pygame.image.load('./Characters/Hero.png')
user = pygame.transform.scale(user,(150,150))
user_r = user.get_rect()
user_r.center = (width//2,height//2)

black = (0,0,0)
white = (255,255,255)

speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        user_r.x -= speed
    if keys[pygame.K_RIGHT]:
        user_r.x += speed
    if keys[pygame.K_UP]:
        user_r.y -= speed
    if keys[pygame.K_DOWN]:
        user_r.y += speed

    screen.blit(map_image,(0,0))
    screen.blit(user,user_r)
    pygame.display.flip()
