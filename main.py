import datetime
import pygame

import CardGameClient

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
errormsgtimer = datetime.datetime.now() + datetime.timedelta(seconds=3)
currentScreen = 0

while True:

    if currentScreen == 0:
        currentScreen = CardGameClient.menuScreen()
    elif currentScreen == 1:
        currentScreen = CardGameClient.signup()
    elif currentScreen == 2:
        currentScreen = CardGameClient.login()
    elif currentScreen == 3:
        currentScreen = CardGameClient.playScreen()
    else:
        break




