import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''
    Рисует новый шарик.
    х -- координата центра шара по Ox, случайное целое число в диапазоне (100, 1100)
    y -- координата центра шара по Oy, случайное целое число в диапазоне (100, 900)
    r -- радиус шара, случайное целое число в диапазоне (10, 100)
    color -- цвет шара, выбирается случайно из COLORS
    '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def click(event):
    '''
    Возвращает данные о шарике
    x -- координата центра шарика по Ox
    y -- координата центра шарика по Oy
    r -- радуис шарика
    '''
    return x, y, r

def hit(x_c, y_c, x, y, r):
    '''
    Определяет, попал ли игрок по шарику.
    x_c, y_c -- координаты клика по Ox, Oy
    x, y -- координаты центра шарика по Ox, Oy
    r -- радиус шарика
    '''
    return ((x - x_c) ** 2 + (y - y_c) ** 2) <= r ** 2

pygame.display.update()
clock = pygame.time.Clock()
finished = False
counter = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hit(event.pos[0], event.pos[1], click(event)[0], click(event)[1], click(event)[2]):
                print("Попал!")
                counter += 1

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

print("Ваш счёт:", counter)

pygame.quit()