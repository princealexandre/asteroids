import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
    
    def draw (self, screen):
        color = (255, 255, 255)
        position = self.rect.center
        radius = self.radius
        width = 2
        pygame.draw.circle (screen, color, self.position, self.radius, width)

    def split (self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS :
            return
        else:
            new_angle = random.uniform(20,50)
            vector1 = self.velocity.rotate(new_angle)
            vector2 = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vector1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = vector2 * 1.2


    def update (self, dt):
        self.position += self.velocity * dt