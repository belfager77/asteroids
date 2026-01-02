import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import *

class Asteroid(CircleShape):

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position+=self.velocity*dt

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        ra=random.uniform(20,50)
        nv1=self.velocity.rotate(ra)
        nv2=self.velocity.rotate(0-ra)
        nr=self.radius-ASTEROID_MIN_RADIUS
        a1=Asteroid(self.position.x,self.position.y,nr)
        a2=Asteroid(self.position.x,self.position.y,nr)
        a1.velocity=nv1*1.2
        a2.velocity=nv2*1.2