import pygame
from sys import exit
import random

pygame.init()
pygame.display.set_caption("Hello World")
screen = pygame.display.set_mode((1080, 960))
clock = pygame.time.Clock()  # clock to set the frame rate

y_pos = 0  # not needed except to make it move, sets it's position
x_pos = random.randrange(0, 1080)  # not needed except to make it move, sets it's position
moving_down = False  # sets the moving down variable so that the circle can move
center_x = list(screen.get_size())[0]/2  # finds the center of the screen
raindrop_speed = 1
raindrop_y = 0


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

    def Draw(self):
        pygame.draw.circle(screen, (50, 50, 100), (self.xpos, self.ypos), 5)


random_rain = random.randrange(0, list(screen.get_size())[0])
drop = Raindrops(random_rain, 200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()  # everything above here is needed otherwise it will crash when you close

        if event.type == pygame.KEYDOWN and event.key == pygame.K_0:  # when 0 is pressed
            moving_down = True

        if event.type == pygame.KEYUP and event.key == pygame.K_0:  # when 0 is not pressed
            moving_down = False

    pressed_key = pygame.key.get_pressed()  # checks which keys are being pressed

    screen.fill((100, 100, 100))  # sets the screen colour
    # circle = pygame.draw.circle(screen, (50, 50, 100), (center_x, raindrop_y), 5)  # draws the circle
    # circle = pygame.draw.circle(screen, colour, position, size)

    y_pos += 3  # adds to the y position
    raindrop_y += raindrop_speed  # speeds the raindrop up
    raindrop_speed += 0.5  # adds to the raindrop speed position

    if raindrop_y > list(screen.get_size())[1]:  # gets the bottom of the screen and resets postion and speed
        raindrop_y = 0
        raindrop_speed = 1

    if pressed_key[pygame.K_RIGHT]:  # button pressed
        x_pos += 1  # adds 1 to the x position

    if moving_down is True:  # other way to move the circle
        y_pos += 1

    drop.Draw()
    drop.Move()

    pygame.display.flip()  # might not need if background is rendering last
    pygame.display.update()  # needs to be the last thing in the game
    clock.tick(60)  # sets frame rate so every thing moves at the same speed


