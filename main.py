import pygame
import sys
from constants import *
from player import Player
from meteor import Meteor
from meteorfield import MeteorField
from shot import Shot

def main():
    print("Starting Meteors!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    meteors = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)

    Meteor.containers = (meteors, updatable, drawable)
    MeteorField.containers = updatable
    meteor_field = MeteorField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0

    running = True

    # Game Loop
    while running:
        # Handle closing game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)

        for meteor in meteors:
            for shot in shots:
                if meteor.collides_with(shot):
                    shot.kill()
                    meteor.split()
            if meteor.collides_with(player):
                print("Game over!")
                sys.exit()

        # Paint Screen
        screen.fill("#343a40")

        for obj in drawable:
            obj.draw(screen)

        # Re-render
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
