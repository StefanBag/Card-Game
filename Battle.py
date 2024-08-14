import socket

import pygame

import CardGameClient
import Screen
from TextBox import TextBox


class Battle:

    def __init__(self, player1, player2, screen):
        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 800
        self.player1 = player1
        self.player2 = player2
        self.screen = screen

    def BattleScreen(self):
        user_textbox = TextBox(self.SCREEN_WIDTH/6, self.SCREEN_HEIGHT/25, int(self.SCREEN_WIDTH / 8), int(self.SCREEN_HEIGHT * 0.3), "USERNAME")
        pass_textbox = TextBox(self.SCREEN_WIDTH/6, self.SCREEN_HEIGHT/25, int(self.SCREEN_WIDTH / 8), int(self.SCREEN_HEIGHT * 0.4), "PASSWORD")
        confirmpass_textbox = TextBox(self.SCREEN_WIDTH/6, self.SCREEN_HEIGHT/25, int(self.SCREEN_WIDTH / 8), int(self.SCREEN_HEIGHT * 0.5), "CONFIRM PASSWORD")

        while True:
            self.screen.fill((0, 0, 0))
            Screen.eventListener(self.player1)
            Screen.eventListener(self.player2)


            # if back_button.draw(screen):
            #         removeAllTextBoxes()
            #         menuScreen()
            pygame.display.flip()
