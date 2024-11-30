user = pygame.image.load('./Characters/Hero.png')
user = pygame.transform.scale(user,(150,150))
user_r = user.get_rect()
user_r.center = (width//2,height//2)