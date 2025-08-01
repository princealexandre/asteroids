import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        points = self.triangle()
        color = (255, 255, 255)
        width = 2
        pygame.draw.polygon (screen, color, points, width)

    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            
    def shoot (self):
        if self.shoot_timer >0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        direction = pygame.Vector2 (0, 1)
        velocity = direction.rotate (self.rotation)
        shot.velocity = velocity * PLAYER_SHOOT_SPEED

    def rotate (self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt