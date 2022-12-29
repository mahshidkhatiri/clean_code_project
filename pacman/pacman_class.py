class Pacman():
    def __init__(self,image):
        self.x=0
        self.y=100
        self.face="east"
        self.image=image
    def add(self,screen):
        screen.blit(self.image,(self.x,self.y))
    def getter(self):
        return(self.x//100,self.y//100-1,self.face)
