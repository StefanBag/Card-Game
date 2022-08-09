import pygame

# create display window
from Button import Button

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

scale = 1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

# load button images
start_img = pygame.image.load('real sign up.png').convert_alpha()
login_img = pygame.image.load('real login.png').convert_alpha()
exit_img = pygame.image.load('Exit.png').convert_alpha()
background_img = pygame.image.load('elements.jpg').convert_alpha()


start_img = pygame.transform.scale(start_img,(350,100))
login_img = pygame.transform.scale(login_img,(350,100))
exit_img = pygame.transform.scale(exit_img,(350,100))
background_img = pygame.transform.scale(background_img,(1200,800))

# create button instances
signup_button = Button((SCREEN_WIDTH*0.5)-(start_img.get_width()/2), (SCREEN_HEIGHT*0.25)-(start_img.get_height()/2), start_img, scale)
login_button = Button((SCREEN_WIDTH*0.5)-(start_img.get_width()/2), (SCREEN_HEIGHT*0.50)-(start_img.get_height()/2), login_img, scale)
exit_button = Button((SCREEN_WIDTH*0.5)-(start_img.get_width()/2), (SCREEN_HEIGHT*0.74)-(start_img.get_height()/2), exit_img, scale)

# game loop
run = True
while run:

    screen.fill((0,0,0))
    screen.blit(background_img, (0, 0))
    if signup_button.draw(screen):
        print('START')
    if login_button.draw(screen):
        print('LOGIN')
    if exit_button.draw(screen):
        pygame.quit()




    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
