import pygame

class TextBox():
    _textboxes = []

    def __init__(self,width,height,x,y,title):
        self._textboxes.append(self)
        self.active = False
        self.text = ''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.title = title
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def remove(self):
        self._textboxes.remove(self)


    def addText(self,addText,limit):
        if addText == "delete":
            self.text = self.text[:-1]
        elif addText == " " or addText == "~" or addText == "\t" or len(self.text)==limit:
            pass
        else:
            self.text += addText




    def makeTextBox(self,encode,screen):

        font = pygame.font.Font(None, 32)


        color_active = pygame.Color('azure')
        color_passive = pygame.Color('gray15')
        
        if self.active:
            color_user = color_active
        else:
            color_user = color_passive

        pygame.draw.rect(screen, color_user, self.rect,1)
        displaytext = ""



        user_title = font.render(self.title, False, (255, 255, 255))
        user_surface = font.render(self.text, True, (255, 255, 255))
        if encode:
            displaytext = "*" * len(self.text)
            user_surface = font.render(displaytext, True, (255, 255, 255))
        screen.blit(user_title, (self.x, self.y-self.height))
        screen.blit(user_surface, (self.rect.x +5, self.rect.y + 5))


    @property
    def textboxes(self):
        return self._textboxes




