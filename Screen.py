import datetime
import socket
import time

import pygame
import sys
# create display window
from pygame import mixer
from Button import Button
from Connect import Connect
from TextBox import TextBox


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800


def removeAllTextBoxes():
    for user in TextBox._textboxes:
        user.remove()

def errorMessage(string, screen):
    font = pygame.font.Font(None, 32)
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(SCREEN_WIDTH - 500, 0, 500, 100))
    errormsg = font.render(string, False, (255, 255, 255))
    screen.blit(errormsg, ((SCREEN_WIDTH - errormsg.get_rect().width) - (500 - errormsg.get_rect().width) / 2, 50))
    pygame.display.flip()
    time.sleep(2)


def eventListener(conn):
    CHARLIMIT = 15
    for event in pygame.event.get():
        # if game was closed
        if event.type == pygame.QUIT:
            conn.send("~EXIT~")

            sys.exit(1)
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
                        user.addText("delete", CHARLIMIT)
                    else:
                        # gets the specific key that was pressed and adds it to user_text, gets information
                        user.addText(event.unicode, CHARLIMIT)





