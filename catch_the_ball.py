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

def new_ball_1():
    '''
    Рисует первый шарик.
    х1 -- координата центра шара по Ox, случайное целое число в диапазоне (100, 1100)
    y1 -- координата центра шара по Oy, случайное целое число в диапазоне (100, 900)
    r1 -- радиус шара, случайное целое число в диапазоне (10, 100)
    color -- цвет шара, выбирается случайно из COLORS
    '''
    global x1, y1, r1
    x1 = randint(100, 1100)
    y1 = randint(100, 900)
    r1 = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x1, y1), r1)

def new_ball_2():
    '''
    Рисует второй шарик.
    х2 -- координата центра шара по Ox, случайное целое число в диапазоне (100, 1100)
    y2 -- координата центра шара по Oy, случайное целое число в диапазоне (100, 900)
    r2 -- радиус шара, случайное целое число в диапазоне (10, 100)
    color -- цвет шара, выбирается случайно из COLORS
    '''
    global x2, y2, r2
    x2 = randint(100, 1100)
    y2 = randint(100, 900)
    r2 = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x2, y2), r2)

def click(event):
    '''
    Возвращает данные о шариках
    x1 -- координата центра первого шарика по Ox
    y1 -- координата центра первого шарика по Oy
    r1 -- радуис первого шарика
    x2 -- координата центра второго шарика по Ox
    y2 -- координата центра второго шарика по Oy
    r2 -- радуис второго шарика
    '''
    return x1, y1, r1, x2, y2, r2

def hit(x_c, y_c, x1, y1, r1, x2, y2, r2):
    '''
    Определяет, попал ли игрок хотя бы по одному шарику.
    x_c, y_c -- координаты клика по Ox, Oy
    x1, y1 -- координаты центра первого шарика по Ox, Oy
    r1 -- радиус первого шарика
    x2, y2 -- координаты центра второго шарика по Ox, Oy
    r2 -- радиус второго шарика
    '''
    return ((((x1 - x_c) ** 2 + (y1 - y_c) ** 2) <= r1 ** 2) or
            (((x2 - x_c) ** 2 + (y2 - y_c) ** 2) <= r2 ** 2))

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
            if hit(event.pos[0], event.pos[1], click(event)[0], click(event)[1],
                   click(event)[2], click(event)[3], click(event)[4], click(event)[5]):
                print("Попал!")
                counter += 1
    new_ball_1()
    new_ball_2()
    pygame.display.update()
    screen.fill(BLACK)

print("Ваш счёт:", counter)

pygame.quit()