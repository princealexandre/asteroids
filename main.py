import pygame

from constants import *
from player import Player
from circleshape import CircleShape

def main():
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0, 0, 0,))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

x = SCREEN_WIDTH/2
y = SCREEN_HEIGHT/2
player = Player(x,y)

if __name__ == "__main__":
    main()