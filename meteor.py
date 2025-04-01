import pygame
import random
from circleshape import CircleShape
from constants import METEOR_MIN_RADIUS

class Meteor(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "#e9ecef", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= METEOR_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        m1 = self.velocity.rotate(random_angle)
        m2 = self.velocity.rotate(-random_angle)
        new_size = self.radius - METEOR_MIN_RADIUS

        meteor = Meteor(self.position.x, self.position.y, new_size)
        meteor.velocity = m1 * 1.2

        meteor = Meteor(self.position.x, self.position.y, new_size)
        meteor.velocity = m2 * 1.2
