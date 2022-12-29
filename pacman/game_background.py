import pygame
def background(height,width):
    screen = pygame.display.set_mode((width,height)) 
    for i in range(1,width//100):
        pygame.draw.line(screen, (255, 0, 0),[i*100,100],[i*100,height], 3)
    for j in range(1,height//100):
        pygame.draw.line(screen, (255, 0, 0),[0,j*100],[width,j*100], 3)
    return screen
