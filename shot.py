import pygame
from constants import *
from circleshape import CircleShape

SHOT_RADIUS = 5

class Shot (CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    def update(self, dt):
        self.position += self.velocity * dt
    