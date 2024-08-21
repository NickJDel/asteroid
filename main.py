import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers =(updateable, drawable)
    Asteroid.containers =(updateable, drawable, asteroids)
    AsteroidField.containers =(updateable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updateable:
            obj.update(dt)   

        for obj in asteroids:
            if obj.collision_check(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen) 

        pygame.display.flip()

        dt = clock.tick(60) / 1000






if __name__ == "__main__":
    main()