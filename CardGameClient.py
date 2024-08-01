import datetime
import socket
import time

import pygame
import sys
# create display window
from pygame import mixer

import Player
import Screen
from Button import Button
from Connect import Connect
from TextBox import TextBox

errormsgtimer = datetime.datetime.now() + datetime.timedelta(seconds=3)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
CHARLIMIT = 15
response = " "

SCALE = 1
mixer.init()
mixer.music.load('Hunter X Hunter - Opening 1 ｜ Departure!.mp3')
mixer.music.play(-1)
mixer.music.set_volume(0.1)
clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

# load button images
start_img = pygame.image.load('pics/real sign up.png').convert_alpha()
login_img = pygame.image.load('pics/real login.png').convert_alpha()
login2_img = pygame.image.load('pics/login.png').convert_alpha()
exit_img = pygame.image.load('pics/Exit.png').convert_alpha()
background_img = pygame.image.load('pics/background.png').convert_alpha()
back_img = pygame.image.load('pics/back.png').convert_alpha()
continue_img = pygame.image.load('pics/continue.png').convert_alpha()
muteMusic_img = pygame.image.load('pics/muteMusic.png').convert_alpha()
play_img = pygame.image.load('pics/Play.png').convert_alpha()
search_img = pygame.image.load('pics/Play.png').convert_alpha()
# creates buttons images
search_img = pygame.transform.scale(search_img, (SCREEN_WIDTH/24, SCREEN_HEIGHT/25))
start_img = pygame.transform.scale(start_img, (SCREEN_WIDTH/4, SCREEN_HEIGHT/8))
login_img = pygame.transform.scale(login_img, (SCREEN_WIDTH/4, SCREEN_HEIGHT/8))
login2_img = pygame.transform.scale(login2_img, (SCREEN_WIDTH/6, SCREEN_HEIGHT/4))
exit_img = pygame.transform.scale(exit_img, (SCREEN_WIDTH/4, SCREEN_HEIGHT/8))
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
back_img = pygame.transform.scale(back_img, (SCREEN_WIDTH/24, SCREEN_HEIGHT/16))
continue_img = pygame.transform.scale(continue_img, (SCREEN_WIDTH/6, SCREEN_HEIGHT/4))
muteMusic_img = pygame.transform.scale(muteMusic_img, (SCREEN_WIDTH/12, SCREEN_HEIGHT/8))
play_img = pygame.transform.scale(play_img, (SCREEN_WIDTH/4, SCREEN_HEIGHT/8))
# create button instances

search_button = Button(SCREEN_WIDTH*0.4 + SCREEN_WIDTH/6,
                           (SCREEN_HEIGHT*0.15), search_img, SCALE)
signup_button = Button((SCREEN_WIDTH * 0.5) - (start_img.get_width() / 2),
                       (SCREEN_HEIGHT * 0.25) - (start_img.get_height() / 2), start_img, SCALE)
login_button = Button((SCREEN_WIDTH * 0.5) - (login_img.get_width() / 2),
                      (SCREEN_HEIGHT * 0.50) - (login_img.get_height() / 2), login_img, SCALE)
login2_button = Button((SCREEN_WIDTH * 0.125),
                       (SCREEN_HEIGHT * 0.60), login2_img, SCALE)
exit_button = Button((SCREEN_WIDTH * 0.5) - (exit_img.get_width() / 2),
                     (SCREEN_HEIGHT * 0.75) - (exit_img.get_height() / 2), exit_img, SCALE)
back_button = Button(0, 0, back_img, SCALE)
muteMusic = Button((SCREEN_WIDTH) - (muteMusic_img.get_width()),
                   (SCREEN_HEIGHT) - (muteMusic_img.get_height()), muteMusic_img, SCALE)
continue_button = Button((SCREEN_WIDTH * 0.125), (SCREEN_HEIGHT * 0.60), continue_img, SCALE)
play_button = Button((SCREEN_WIDTH * 0.125), (SCREEN_HEIGHT * 0.20), play_img, SCALE)

conn = Connect()
conn.connect()



def signup():
    user_textbox = TextBox(SCREEN_WIDTH/6, SCREEN_HEIGHT/25, int(SCREEN_WIDTH / 8), int(SCREEN_HEIGHT * 0.3), "USERNAME")
    pass_textbox = TextBox(SCREEN_WIDTH/6, SCREEN_HEIGHT/25, int(SCREEN_WIDTH / 8), int(SCREEN_HEIGHT * 0.4), "PASSWORD")
    confirmpass_textbox = TextBox(SCREEN_WIDTH/6, SCREEN_HEIGHT/25, int(SCREEN_WIDTH / 8), int(SCREEN_HEIGHT * 0.5), "CONFIRM PASSWORD")

    while True:
        screen.fill((0, 0, 0))
        Screen.eventListener(conn)

        if back_button.draw(screen):
            Screen.removeAllTextBoxes()
            menuScreen()

        user_textbox.makeTextBox(False, screen)
        pass_textbox.makeTextBox(True, screen)
        confirmpass_textbox.makeTextBox(True, screen)
        if continue_button.draw(screen):
            if confirmpass_textbox.text != pass_textbox.text:
                Screen.errorMessage("PASSWORDS DO NOT MATCH")
                response = ""
            else:
                response = conn.send("~SIGNUP~ " + user_textbox.text + " " + pass_textbox.text)
            if response == "SUCCESSFUL SIGNUP":
                Screen.removeAllTextBoxes()
                menuScreen()
            else:
                Screen.errorMessage(response, screen)

        pygame.display.flip()


def login():
    user_textbox = TextBox(SCREEN_WIDTH/6, SCREEN_HEIGHT/25, int(SCREEN_WIDTH / 8), int(SCREEN_HEIGHT * 0.3), "USERNAME")
    pass_textbox = TextBox(SCREEN_WIDTH/6, SCREEN_HEIGHT/25, int(SCREEN_WIDTH / 8), int(SCREEN_HEIGHT * 0.4), "PASSWORD")

    while True:
        screen.fill((0, 0, 0))
        Screen.eventListener(conn)

        if back_button.draw(screen):
            Screen.removeAllTextBoxes()
            menuScreen()

        user_textbox.makeTextBox(False, screen)
        pass_textbox.makeTextBox(True, screen)

        if login2_button.draw(screen):
            response = conn.send("~LOGIN~ " + user_textbox.text + " " + pass_textbox.text)
            if response == "LOGIN SUCCESSFUL":
                conn.user = user_textbox.text

                Screen.removeAllTextBoxes()
                playScreen()
            else:
                Screen.errorMessage(response, screen)

        pygame.display.flip()
        clock.tick(60)




def playScreen():
    search_textbox = TextBox(SCREEN_WIDTH/6, SCREEN_HEIGHT/25, int(SCREEN_WIDTH * 0.4), int(SCREEN_HEIGHT * 0.15), "")


    while True:
        screen.fill((0, 50, 100))
        Screen.eventListener(conn)
        if back_button.draw(screen):
            Screen.removeAllTextBoxes()
            menuScreen()

        search_textbox.makeTextBox(False, screen)
        if search_button.draw(screen):
            response = conn.send("~SEARCH~ " + search_textbox.text)

        pygame.display.flip()


#                                                   MAIN SCREEN
# ***********************************************************************************************************************

def menuScreen():
    while True:
        screen.fill((0, 0, 0))
        screen.blit(background_img, (0, 0))
        Screen.eventListener(conn)
        if signup_button.draw(screen):
            signup()
            # sys.stdout.close()
        if login_button.draw(screen):
            login()

        if exit_button.draw(screen):
            conn.send("~EXIT~")
            sys.exit(1)
            # sys.stdout.close()
        if muteMusic.draw(screen):
            if mixer.music.get_volume() == 0:
                mixer.music.set_volume(0.1)
            else:
                mixer.music.set_volume(0)

        pygame.display.update()
