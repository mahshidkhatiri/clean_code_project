import pygame 
from message import message_to_screen
green=(0,155,0)
class ReportPossition():
    def __init__(self,pacman):
        self.bot=pacman
    def showPossition(self,screen):
        x,y,face=self.bot.getter()
        message_to_screen(screen,"Column:{0},Row:{1},face:{2}".format(x,y,face),green,30,10,10)
        pygame.display.update()