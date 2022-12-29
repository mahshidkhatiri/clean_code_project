import pygame
class PacmanAct():
    def __init__(self,pacman,rull):
        self.bot=pacman
        self.rull=rull
    def turn_right(self,faces):
        index = faces.index(self.bot.face)
        '270 darage be chap = 90 darage be rast'
        self.bot.image = pygame.transform.rotate(self.bot.image, 270)
        self.bot.face=faces[(index+1)%len(faces)]
    def turn_left(self,faces):
        index = faces.index(self.bot.face)
        'charkhesh ax 90 darage be chap'
        self.bot.image = pygame.transform.rotate(self.bot.image, 90)
        self.bot.face=faces[(index-1)%len(faces)]
    def move(self):
        if self.bot.face=="east" and self.bot.x+100<self.rull.x_max:
            self.bot.x+=100
        elif self.bot.face=="north" and self.bot.y-100>=self.rull.y_min:
            self.bot.y-=100
        elif self.bot.face=="west" and self.bot.x-100>=self.rull.x_min:
            self.bot.x-=100
        elif self.bot.face=="south" and self.bot.y+100<self.rull.y_max:
            self.bot.y+=100
    def replacement(self,x_new_place,y_new_place,face_new_place,faces):
        self.bot.x=x_new_place*100
        self.bot.y=(y_new_place+1)*100
        index = faces.index(self.bot.face)
        index_new = faces.index(face_new_place)
        while index!=index_new:
            self.bot.image = pygame.transform.rotate(self.bot.image, 90)
            index=(index-1)%len(faces)
        self.bot.face=face_new_place