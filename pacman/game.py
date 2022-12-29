import pygame
import time
from pacman_class import Pacman
from pacman_act_class import PacmanAct
from report import ReportPossition
from game_rull import Rull
from game_background import background
pygame.init()
pygame.display.set_caption('Pacman')
img = pygame.image.load('./images/pacman.png')
pygame.display.set_icon(img)
pacman_image=pygame.image.load('./images/pacman.png')
pacman_image = pygame.transform.scale(pacman_image, (90,90))
faces=["north","east","south","west"]
c = pygame.time.Clock()
height=600
width=500
margin=100
f = open("./map.txt", "r")
'baz kardan text'
pacman=Pacman(pacman_image) 
pacman_rull=Rull(height,width,margin)       
running = True
line=f.readline().rstrip("\n")
while running:
    screen=background(height,width)
    pacman.add(screen) 
    pacman_act=PacmanAct(pacman,pacman_rull)
    pacman_report=ReportPossition(pacman)
    print(line.rstrip("\n"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if line=="MOVE":
        pacman_act.move()
    elif line=="LEFT":
        pacman_act.turn_left(faces)
    elif line=="RIGHT":
        pacman_act.turn_right(faces)
    elif line=="REPORT":
        pacman_report.showPossition(screen)
    elif line=="":
        pygame.display.update()
        time.sleep(2)
        break
    else:
        line_list=line.split(" ")
        if line_list[0]=="PLACE":
            location=line_list[1].split(",")
            'joda kardan x,y,f az text baraye jabejaee pacman'
            pacman_act.replacement(int(location[0]), int(location[1]),location[2].lower(),faces)
    line=f.readline().rstrip("\n")
    pygame.display.update()
    time.sleep(2)
    c.tick(4)
pygame.quit()