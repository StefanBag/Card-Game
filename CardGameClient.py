import datetime
import threading
import time

import pygame
import sys
# create display window
from pygame import mixer
from Button import Button
from TextBox import TextBox

#sys.stdout = open('errormsg.txt', 'w')
#sys.stderr= open('errormsg1.txt', 'w')

errormsgtimer = datetime.datetime.now()+ datetime.timedelta(seconds=3)
cdtimer = 200
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


scale = 1
mixer.init()
mixer.music.load('Hunter X Hunter - Opening 1 ｜ Departure!.mp3')
mixer.music.play(-1)



screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

# load button images
start_img = pygame.image.load('real sign up.png').convert_alpha()
login_img = pygame.image.load('real login.png').convert_alpha()
exit_img = pygame.image.load('Exit.png').convert_alpha()
background_img = pygame.image.load('elements.jpg').convert_alpha()
back_img = pygame.image.load('back.png').convert_alpha()
continue_img = pygame.image.load('continue.png').convert_alpha()
#creates buttons
start_img = pygame.transform.scale(start_img, (350, 100))
login_img = pygame.transform.scale(login_img, (350, 100))
exit_img = pygame.transform.scale(exit_img, (350, 100))
background_img = pygame.transform.scale(background_img, (1200, 800))
back_img = pygame.transform.scale(back_img, (50, 50))
continue_img = pygame.transform.scale(continue_img, (200, 200))
# create button instances
signup_button = Button((SCREEN_WIDTH * 0.5) - (start_img.get_width() / 2),
                       (SCREEN_HEIGHT * 0.25) - (start_img.get_height() / 2), start_img, scale)
login_button = Button((SCREEN_WIDTH * 0.5) - (start_img.get_width() / 2),
                      (SCREEN_HEIGHT * 0.50) - (start_img.get_height() / 2), login_img, scale)
exit_button = Button((SCREEN_WIDTH * 0.5) - (start_img.get_width() / 2),
                     (SCREEN_HEIGHT * 0.75) - (start_img.get_height() / 2), exit_img, scale)
back_button = Button(0,0, back_img, scale)
continue_button = Button((SCREEN_WIDTH * 0.125),  (SCREEN_HEIGHT * 0.60), continue_img, scale)

#creates textboxes
user_textbox = TextBox(200,32,150,200,"USERNAME")
pass_textbox = TextBox(200,32,150,300,"PASSWORD")
confirmpass_textbox = TextBox(200,32,150,400,"CONFIRM PASSWORD")

# game loop

def errorMessage(string):
    font = pygame.font.Font(None, 32)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(SCREEN_WIDTH-500, 0, 500, 100))
    errormsg = font.render(string, False, (255, 255, 255))
    screen.blit(errormsg, ((SCREEN_WIDTH-errormsg.get_rect().width)-(500-errormsg.get_rect().width)/2, 50))






def signup():
    global errormsgtimer
    print("true")
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([1200, 800])

    # updates which box is selected and the color that goes with it

    while True:
        for event in pygame.event.get():
            # if game was closed
            if event.type == pygame.QUIT:
                return 1
                # checks that if you have clicked on the box or outside of it
            if event.type == pygame.MOUSEBUTTONDOWN:
                for user in TextBox._textboxes:
                    if user.rect.collidepoint(pygame.mouse.get_pos()):
                        user.active = True
                    else:
                        user.active = False


            # checks if any button was pressed
            if event.type == pygame.KEYDOWN:
                for user in TextBox._textboxes:
                    # short form for if active == true
                    if user.active:
                        # ablitiy to backspace/delete, looks if backspace is pressed
                        if event.key == pygame.K_BACKSPACE:
                            user.addText("delete")
                        else:
                            # gets the specific key that was pressed and adds it to user_text, gets information
                            user.addText(event.unicode)

        screen.fill((0, 0, 0))

        if back_button.draw(screen):
            break






        user_textbox.makeTextBox(False,screen)
        pass_textbox.makeTextBox(True, screen)
        confirmpass_textbox.makeTextBox(True, screen)
        if continue_button.draw(screen):
            errormsgtimer = datetime.datetime.now() + datetime.timedelta(seconds=2)
            while errormsgtimer > datetime.datetime.now():
                errorMessage("THIS USERNAME IS ALREADY TAKEN")
                pygame.display.flip()
                print("x")

        pygame.display.flip()
        clock.tick(60)


while True:
    screen.fill((0, 0, 0))
    screen.blit(background_img, (0, 0))

    if signup_button.draw(screen):
        if signup() == 1:
            pygame.quit()
            #sys.stdout.close()
    if login_button.draw(screen):
        print('LOGIN')

    if exit_button.draw(screen):
        pygame.quit()
        #sys.stdout.close()

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            sys.stdout.close()
            pygame.quit()

    pygame.display.update()

