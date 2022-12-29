import pygame
def message_to_screen(screen,msg,color,size,x,y):
    font=pygame.font.SysFont(None,size)
    screen_text=font.render(msg,True,color)
    screen.blit(screen_text,[x,y])