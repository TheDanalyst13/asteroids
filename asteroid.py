import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new1 = Asteroid(self.position.x, self.position.y, new_radius)
            new1.velocity = self.velocity.rotate(angle) * 1.2

            new2 = Asteroid(self.position.x, self.position.y, new_radius)
            new2.velocity = self.velocity.rotate(-angle) * 1.2
