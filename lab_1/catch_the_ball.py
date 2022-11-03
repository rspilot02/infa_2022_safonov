import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 120
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
    Рисует первый шарик в каджый момент времени.
    х1 -- координата центра шара по Ox
    y1 -- координата центра шара по Oy
    r1 -- радиус шара
    vx1, vy1 -- составляющие скорости шара по Ox и по Oy
    '''
    global x1, y1, r1, vx1, vy1
    if ((y1 + r1 >= 900) or (y1 - r1 <= 0)):
        vy1 *= -1
    if ((x1 + r1 >= 1200) or (x1 - r1) <= 0):
        vx1 *= -1
    x1 += vx1
    y1 += vy1
    circle(screen, BLUE, (x1, y1), r1)

def new_rec_2():
    '''
    Рисует квадрат в каждый момент времени.
    х2 -- координата левой верхней вершины по Ox
    y2 -- координата левой верхней вершины по Oy
    vx2, vy2 -- составляющие скорости квадрата по Ox и по Oy
    '''
    global x2, y2, vx2, vy2
    if ((y2 + 100 >= 900) or (y2 <= 0)):
        vy2 = -abs(vr[randint(0, 11)]) * vy2 / abs(vy2)
        vx2 = vr[randint(0, 11)]
        if (y2 <= 0):
            y2 = -y2
        elif (y2 + 100 >= 900):
            y2 = y2 - 2*abs(y2 - 800)
    if ((x2 + 100 >= 1200) or (x2 <= 0)):
        if (x2 <= 0):
            x2 = -x2
        elif (x2 + 100 >= 1200):
            x2 = x2 - 2*abs(x2 - 1100)
        vy2 = vr[randint(0, 11)]
        vx2 = -abs(vr[randint(0, 11)]) * vx2 / abs(vx2)
    x2 += vx2
    y2 += vy2
    rect(screen, RED, (x2, y2, 100, 100))

def hit_ball(x_c, y_c, x1, y1, r1):
    '''
    Определяет, попал ли игрок по шарику.
    x_c, y_c -- координаты клика по Ox, Oy
    x1, y1 -- координаты центра шарика по Ox, Oy
    r1 -- радиус первого шарика
    '''
    return (((x1 - x_c) ** 2 + (y1 - y_c) ** 2) <= r1 ** 2)

def hit_rect(x_c, y_c, x2, y2):
    '''
    Определяет, попал ли игрок по квадрату.
    x_c, y_c -- координаты клика по Ox, Oy
    x2, y2 -- координаты левой верхней вершины квадрата по Ox, Oy
    '''
    return (x2 - x_c <= 100) and (y2 - y_c <= 100)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
counter = 0

# Начальные координаты мишеней
x1 = randint(100, 1100)
y1 = randint(100, 800)
r1 = 50

x2 = randint(0, 1100)
y2 = randint(0, 800)

# Скорости мишеней по Ox и Oy в условных единицах
vx1 = 3
vy1 = 3
vr = [-10, -9, -8, -7, -6, -5, 5, 6, 7, 8, 9, 10]
vx2 = vr[randint(0, 11)]
vy2 = vr[randint(0, 11)]

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hit_ball(event.pos[0], event.pos[1], x1, y1, r1):
                print("Хорош! +1")
                counter += 1
            if hit_rect(event.pos[0], event.pos[1], x2, y2):
                print("МЕГАХОРОШ! +3")
                counter += 3
    new_ball_1()
    new_rec_2()
    pygame.display.update()
    screen.fill(BLACK)

print("Ваш счёт:", counter)

pygame.quit()