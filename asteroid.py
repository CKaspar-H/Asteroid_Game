import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import sys


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    
    def update(self, dt):
       self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return # small asteroid, we're done
        
        log_event("asteroid_split")
        angle_pos = random.uniform(20, 50)
        angle_neg = random.uniform(-20, -50)
        vec_a = self.velocity.rotate(angle_pos)
        vec_b = self.velocity.rotate(angle_neg)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a = Asteroid(self.position.x, self.position.y, new_radius)
        b = Asteroid(self.position.x, self.position.y, new_radius)
        a.velocity = vec_a * 1.2
        b.velocity = vec_b * 1.2
            