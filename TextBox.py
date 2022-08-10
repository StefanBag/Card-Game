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

    def addText(self,addText):
        if addText == "delete":
            self.text = self.text[:-1]
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

        pygame.draw.rect(screen, color_user, self.rect, 2)
        displaytext = ""

        if encode:
            for x in self.text:
                displaytext += "*"

        user_title = font.render(self.title, False, (255, 255, 255))
        user_surface = font.render(self.text, True, (255, 255, 255))
        if encode:
            user_surface = font.render(displaytext, True, (255, 255, 255))
        screen.blit(user_title, (self.x, self.y-25))
        screen.blit(user_surface, (self.rect.x + 5, self.rect.y + 5))
        self.rect.w = max(200, user_surface.get_width() + 10)

    @property
    def textboxes(self):
        return self._textboxes




