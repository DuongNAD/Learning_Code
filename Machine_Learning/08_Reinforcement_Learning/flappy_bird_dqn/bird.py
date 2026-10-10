import pygame 

class Bird:
    def __init__(self,x=50,y=256):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 24
        self.color = (255,255,0) # Yellow

    def draw(self, screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))