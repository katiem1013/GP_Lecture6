import pygame
from sys import exit
import random

pygame.init()
pygame.display.set_caption("Hello World")
screen = pygame.display.set_mode((1080, 960))
clock = pygame.time.Clock()  # clock to set the frame rate




class Raindrops:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.raindrop_y = 0
        self.raindrop_speed = 1

    def Move(self):
        self.ypos += self.raindrop_speed
        self.raindrop_speed += 1
        if self.ypos > list(screen.get_size())[1]:
            self.ypos = 0
            self.raindrop_speed = 1
            self.xpos = random.randrange(0, list(screen.get_size())[0])

    def Draw(self):
        pygame.draw.circle(screen, (50, 50, 100), (self.xpos, self.ypos), 5)


drops = []
for x in range(100):
    random_x = random.randrange(0, list(screen.get_size())[0])
    random_y = random.randrange(0, list(screen.get_size())[1])
    drops.append(Raindrops(random_x, random_y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()  # everything above here is needed otherwise it will crash when you close

    screen.fill((100, 100, 100))  # sets the screen colour

    for drop in drops:
        drop.Draw()
        drop.Move()


    pygame.display.flip()  # might not need if background is rendering last
    pygame.display.update()  # needs to be the last thing in the game
    clock.tick(60)  # sets frame rate so every thing moves at the same speed


