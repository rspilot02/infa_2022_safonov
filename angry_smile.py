import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (238, 255, 0)

rect(screen, white, (0, 0, 800, 800))
circle(screen, black, (400, 400), 201, width = 1)
circle(screen, yellow, (400, 400), 200, width = 0)
circle(screen, red, (320, 350), 50)
circle(screen, black, (320, 350), 51, width = 1)
circle(screen, red, (480, 350), 35)
circle(screen, black, (480, 350), 36, width = 1)
circle(screen, black, (320, 350), 25)
circle(screen, black, (480, 350), 18)
rect(screen, black, (300, 460, 200, 30))
polygon(screen, black, [(280,220), (380,320),
                               (370,330), (270,230)])
polygon(screen, black, [(520,230), (420,330),
                               (430,340), (530,240)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()