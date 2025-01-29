import pygame
import random
import math

from yeah import clock

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Happy New Year 2025!")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Firework class
class Firework:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = height
        self.y_speed = random.randint(5, 8)
        self.exploded = False
        self.particles = []
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

    def move(self):
        if not self.exploded:
            self.y -= self.y_speed
            if self.y <= random.randint(50, 300):
                self.explode()

    def explode(self):
        self.exploded = True
        num_particles = random.randint(50, 100)
        for _ in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 6)
            vx = math.cos(angle) * speed
            vy = math.sin(angle) * speed
            self.particles.append([(self.x, self.y), (vx, vy), 255])

    def update_particles(self):
        for particle in self.particles:
            particle[0] = (particle[0][0] + particle[1][0], particle[0][1] + particle[1][1])
            particle[2] -= 2
            if particle[2] <= 0:
                self.particles.remove(particle)

    def draw(self, screen):
        if not self.exploded:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 3)
        else:
            for particle in self.particles:
                pygame.draw.circle(screen, (*self.color, particle[2]), (int(particle[0][0]), int(particle[0][1])), 2)

# Flower class
class Flower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = []
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.create_particles()

    def create_particles(self):
        num_petals = random.randint(5, 8)
        for i in range(num_petals):
            angle = (2 * math.pi / num_petals) * i
            for _ in range(10):
                speed = random.uniform(1, 3)
                vx = math.cos(angle) * speed
                vy = math.sin(angle) * speed
                self.particles.append([(self.x, self.y), (vx, vy), 255])

    def update_particles(self):
        for particle in self.particles:
            particle[0] = (particle[0][0] + particle[1][0], particle[0][1] + particle[1][1])
            particle[2] -= 1
            if particle[2] <= 0:
                self.particles.remove(particle)

    def draw(self, screen):
        for particle in self.particles:
            pygame.draw.circle(screen, (*self.color, particle[2]), (int(particle[0][0]), int(particle[0][1])), 2)

# Fireworks and Flowers lists
fireworks = []
flowers = []

# Font setup
font_large = pygame.font.Font(None, 64)
font_small = pygame.font.Font(None, 32)

text1 = font_large.render("Happy New Year 2025!", True, WHITE)
text1_rect = text1.get_rect(center=(width // 2, height // 2 - 60))

text2 = font_small.render("I'm glad I met you in 2024!", True, WHITE)
text2_rect = text2.get_rect(center=(width // 2, height // 2))

text3 = font_small.render("Wishing you a very happy new year,", True, WHITE)
text3_rect = text3.get_rect(center=(width // 2, height // 2 + 40))

text4 = font_small.render("May Allah bless you, guide you and protect you", True, WHITE)
text4_rect = text4.get_rect(center=(width // 2, height // 2 + 80))

text5 = font_small.render("in the upcoming years as well.", True, WHITE)
text5_rect = text5.get_rect(center=(width // 2, height // 2 + 120))

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    if random.random() < 0.1:
        fireworks.append(Firework())

    for firework in fireworks:
        firework.move()
        if firework.exploded:
            firework.update_particles()
        firework.draw()

        if firework.exploded and len(firework,particles) == 0:
            fireworks.remove(firework)

    if random.random() < 0.02:
        flowers.append(Flower(random.randint(0, width), random.randint(0, height)))

    for flower in flowers:
        flower.update_particles()
        flower.draw(screen)

        if len(flower.particles) == 0:
            flowers.remove(flower)

    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)
    screen.blit(text4,text4_rect)
    screen.blit(text5,text5_rect)

    pygame.display.flip()
    clock.tick


pygame.quit()
