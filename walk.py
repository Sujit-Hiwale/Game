import pygame
import sys

pygame.init()

info = pygame.display.Info()
width = info.current_w
height = info.current_h

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Maker")
map_image = pygame.image.load('./Maps/image.png')
map_image = pygame.transform.scale(map_image,(width,height))
sprite_sheet = pygame.image.load('./Characters/c.png').convert_alpha()

frame_width = 64
frame_height = 64
frames_per_row = 4
frames_per_col = 4

user = pygame.image.load('./Characters/c.png')
user = pygame.transform.scale(user,(150,150))
user_r = user.get_rect()
user_r.center = (width//2,height//2)

def extract_frames(sprite_sheet, frame_width, frame_height, frames_per_row, frames_per_col):
    frames = {
        'walk_right': [],
        'walk_left': [],
        'walk_up' : [],
        'walk_down' : [],
        'stand': []
    }
    for row in range(frames_per_col):
        for col in range(frames_per_row):
            frame = sprite_sheet.subsurface(pygame.Rect(col * frame_width, row * frame_height, frame_width, frame_height))
            if row == 0:
                frames['walk_left'].append(frame)
            elif row == 1:
                frames['stand'].append(frame)
    frames['walk_right'] = [pygame.transform.flip(frame, True, False) for frame in frames['walk_left']]

    frames['walk_up'] = [pygame.transform.rotate(frame, 90) for frame in frames['walk_left']]
    
    frames['walk_down'] = [pygame.transform.rotate(frame, -90) for frame in frames['walk_left']]
    return frames

frames = extract_frames(sprite_sheet, frame_width, frame_height, frames_per_row, frames_per_col)

current_animation = 'stand'
current_frame = 0
animation_speed = 5
animation_counter = 0

x, y = width // 2, height // 2
velocity = 1

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocity
        current_animation = 'walk_left'
        animation_counter += 1
    elif keys[pygame.K_RIGHT]:
        x += velocity
        current_animation = 'walk_right'
        animation_counter += 1
    elif keys[pygame.K_UP]:
        y -= velocity
        current_animation = 'walk_up'
        animation_counter += 1
    elif keys[pygame.K_DOWN]:
        y += velocity
        current_animation = 'walk_down'
        animation_counter += 1
    else:
        current_animation = 'stand'
        animation_counter = 0
        current_frame = 0

    if animation_counter >= animation_speed:
        current_frame = (current_frame + 1) % len(frames[current_animation])
        animation_counter = 0

    screen.blit(map_image,(0,0))
    screen.blit(frames[current_animation][current_frame], (x, y))
    pygame.display.flip()
    clock.tick(60)