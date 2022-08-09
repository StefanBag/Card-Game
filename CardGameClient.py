import pygame

# create display window
import CardGameClient
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
back_img = pygame.image.load('back.png').convert_alpha()

#creates buttons
start_img = pygame.transform.scale(start_img, (350, 100))
login_img = pygame.transform.scale(login_img, (350, 100))
exit_img = pygame.transform.scale(exit_img, (350, 100))
background_img = pygame.transform.scale(background_img, (1200, 800))
back_img = pygame.transform.scale(back_img, (50, 50))

# create button instances
signup_button = Button((SCREEN_WIDTH * 0.5) - (start_img.get_width() / 2),
                       (SCREEN_HEIGHT * 0.25) - (start_img.get_height() / 2), start_img, scale)
login_button = Button((SCREEN_WIDTH * 0.5) - (start_img.get_width() / 2),
                      (SCREEN_HEIGHT * 0.50) - (start_img.get_height() / 2), login_img, scale)
exit_button = Button((SCREEN_WIDTH * 0.5) - (start_img.get_width() / 2),
                     (SCREEN_HEIGHT * 0.74) - (start_img.get_height() / 2), exit_img, scale)
back_button = Button(0,0, back_img, scale)

# game loop



def signup():
    print("true")
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([1200, 800])
    font = pygame.font.Font(None, 32)
    user_text = ''
    pass_text = ''

    # makes the username box rectangle: x, y, wide ,tall
    user_rect = pygame.Rect(150, 200, 140, 32)
    # makes the password box rectangle: x, y, wide ,tall
    pass_rect = pygame.Rect(150, 300, 140, 32)
    color_active = pygame.Color('azure')
    color_passive = pygame.Color('gray15')

    # updates which box is selected and the color that goes with it
    active_user = False
    active_pass = False

    while True:
        for event in pygame.event.get():
            # if game was closed
            if event.type == pygame.QUIT:
                return 1
                # checks that if you have clicked on the box or outside of it
            if event.type == pygame.MOUSEBUTTONDOWN:
                if user_rect.collidepoint(pygame.mouse.get_pos()):
                    active_user = True
                else:
                    active_user = False
                if pass_rect.collidepoint(pygame.mouse.get_pos()):

                    active_pass = True
                else:
                    active_pass = False

            # checks if any button was pressed
            if event.type == pygame.KEYDOWN:
                # short form for if active == true
                if active_user:
                    # ablitiy to backspace/delete, looks if backspace is pressed
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        # gets the specific key that was pressed and adds it to user_text, gets information
                        user_text += event.unicode
                if active_pass:
                    if event.key == pygame.K_BACKSPACE:
                        pass_text = pass_text[:-1]
                    else:
                        # gets the specific key that was pressed and adds it to user_text, gets information
                        pass_text += event.unicode

        screen.fill((0, 0, 0))
        if back_button.draw(screen):
            break

        if active_user:
            color_user = color_active
        else:
            color_user = color_passive
        if active_pass:
            color_pass = color_active
        else:
            color_pass = color_passive
        # makes user box, border size
        pygame.draw.rect(screen, color_user, user_rect, 2)
        # makes pass box, border size
        pygame.draw.rect(screen, color_pass, pass_rect, 2)
        displaytext = ""
        for x in pass_text:
            displaytext += "*"

        # adds titles
        user_title = font.render('USERNAME', False, (255, 255, 255))
        pass_title = font.render('PASSWORD', False, (255, 255, 255))

        # adds type able words
        user_surface = font.render(user_text, True, (255, 255, 255))
        pass_surface = font.render(displaytext, True, (255, 255, 255))

        # title position
        screen.blit(user_title, (150, 175))
        screen.blit(pass_title, (150, 275))
        # center the words by moving 5 pixels
        screen.blit(user_surface, (user_rect.x + 5, user_rect.y + 5))
        screen.blit(pass_surface, (pass_rect.x + 5, pass_rect.y + 5))
        # makes user box start with space and not narrow
        user_rect.w = max(200, user_surface.get_width() + 10)
        pass_rect.w = max(200, pass_surface.get_width() + 10)

        pygame.display.flip()
        clock.tick(60)


while True:
    screen.fill((0, 0, 0))
    screen.blit(background_img, (0, 0))

    if signup_button.draw(screen):
        if signup() == 1:
            pygame.quit()
    if login_button.draw(screen):
        print('LOGIN')

    if exit_button.draw(screen):
        pygame.quit()

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

pygame.quit()
