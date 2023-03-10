import pygame
from sys import exit
import random

pygame.init()
pygame.display.set_caption("Hello World")
screen = pygame.display.set_mode((1080, 960))
clock = pygame.time.Clock()  # clock to set the frame rate

cloud_image = pygame.image.load('download.png').convert_alpha()
cloud_y = 0
cloud_x = screen.get_size()[1]/2

player_surf = pygame.image.load('hooman_umbrella.png').convert_alpha()
player_surf.set_colorkey((255, 255, 255))
player_rect = player_surf.get_rect(topleft = (540, 500))


class Raindrops:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.raindrop_y = 0
        self.raindrop_speed = 1
        self.size = random.randrange(3, 5)

        self.rect = pygame.Rect(self.xpos, self.ypos, self.size, self.size)
        self.active = True

    def Move(self):
        self.ypos += self.raindrop_speed
        self.rect.y = self.ypos
        self.rect.x = self.xpos
        self.raindrop_speed += 1

        if self.rect.colliderect(player_rect):
            self.active = False

        if self.ypos > list(screen.get_size())[1]:
            y_min = cloud_y + cloud_image.get_size()[1] / 2
            y_max = cloud_y + cloud_image.get_size()[1]
            self.ypos = random.randrange(200, 700)
            self.raindrop_speed = 1
            range = cloud_image.get_size()[0]
            self.xpos = random.randrange(cloud_y + 150, range - 150)
            self.active = True

    def Draw(self):
        if self.active:
            pygame.draw.circle(screen, (50, 50, 100), (self.xpos, self.ypos), 5)


drops = []
for x in range(100):
    random_x = random.randrange(cloud_x, cloud_x + cloud_image.get_size()[0])
    y_min = cloud_y + cloud_image.get_size()[1] / 2
    y_max = cloud_y + cloud_image.get_size()[1]
    random_y = random.randrange(cloud_y, 700)
    drops.append(Raindrops(random_x, random_y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()  # everything above here is needed otherwise it will crash when you close

    screen.fill((100, 100, 100))  # sets the screen colour

    for drop in drops:
        drop.Draw()
        drop.Move()

    screen.blit(cloud_image, (0, -150))
    screen.blit(player_surf, player_rect)

    pygame.display.flip()  # might not need if background is rendering last
    pygame.display.update()  # needs to be the last thing in the game
    clock.tick(60)  # sets frame rate so every thing moves at the same speed


