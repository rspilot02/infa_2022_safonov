import math
from random import choice, randint

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = 0x000000
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
WIDTH = 800
HEIGHT = 600

class Ball:

    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        r - радиус мяча
        vx - начальная горизонтальная скорость мяча
        vy - начальная вертикальная скорость мяча
        color - цвет мяча
        live - начальный таймер жизни мяча (сколько фреймов мяч будет жить)
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 90

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if (self.x + self.r >= WIDTH) or (self.x - self.r <= 0):
            self.vx *= -0.85
            if self.x + self.r >= WIDTH:
                self.x = WIDTH - self.r - 1
            else:
                self.x = 1 + self.r
        if (self.y + self.r >= HEIGHT):
            self.vy *= -0.85
            self.vy += 1
            self.y = HEIGHT - self.r - 1

        self.x += self.vx
        self.y += self.vy
        self.vy += 1

    def draw(self):
        """
        Рисует мячик по его координатам и радиусу.
        """
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
            )

    def hittest(self, obj):
        '''Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.'''
        return (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (obj.r + self.r) ** 2



class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        """
        Момент перед выстрелом.
        """
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """
        an - угол с горизонтом, под которым производится выстрел
        """
        if event:
            if event.pos[0]-20 != 0:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
            else:
                self.an = math.atan((event.pos[1] - 450) / (event.pos[0] - 19))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """
        Рисует пушку в зависимости от положения мыши.
        """
        pygame.draw.polygon(screen, self.color, [[40, 460],
                                                 [40, 440],
                                                 [40 + self.f2_power * math.cos(self.an), 440 + self.f2_power * math.sin(self.an)],
                                                 [40 + self.f2_power * math.cos(self.an), 460 + self.f2_power * math.sin(self.an)]])

    def power_up(self):
        """
        Увеличение силы выстрела со временем.
        """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen):
        self.screen = screen
        self.points = 0
        self.live = 1
        self.color = RED
    # self.new_target()

    def new_target(self):
        """
        Инициализация новой цели.
        x, y - координаты
        r - радиус
        color - цвет
        """
        self.x = randint(500, 780)
        self.y = randint(100, 550)
        self.r = randint(10, 40)
        self.live = 1
        self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель и соответствующее начисление очков."""
        self.points += points

    def draw(self):
        """
        Рисование мишени.
        x, y - координаты
        r - радиус
        """
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
target2 = Target(screen)
finished = False
target.new_target()
target2.new_target()

f1 = pygame.font.Font(None, 35)
counter = 0
points = 0

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    target2.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
            counter += 1
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        b.live -= 1
        if b.hittest(target) and target.live:
            target.live = 0
            b.live = 0
            points += 1
            pygame.draw.rect(screen, WHITE, (0, 0, 800, 600))
            image = pygame.image.load("BSOD_Windows_8.svg")
            screen.blit(image, image.get_rect())
            text1 = f1.render(f'Вы попали в мишень за {counter} выстрел(-а/-ов)', True, (255, 255, 255))
            screen.blit(text1, (230, 200))
            text2 = f1.render(f'Счёт: {points}', True, (255, 255, 255))
            screen.blit(text2, (420, 245))
            pygame.display.update()
            counter = 0
            clock.tick(1/2)
            target.new_target()
        if b.hittest(target2) and target2.live:
            target2.live = 0
            b.live = 0
            points += 1
            # target.hit()
            pygame.draw.rect(screen, WHITE, (0, 0, 800, 600))
            image = pygame.image.load("BSOD_Windows_8.svg")
            screen.blit(image, image.get_rect())
            text1 = f1.render(f'Вы попали в мишень за {counter} выстрел(-а/-ов)', True, (255, 255, 255))
            screen.blit(text1, (230, 200))
            text2 = f1.render(f'Счёт: {points}', True, (255, 255, 255))
            screen.blit(text2, (420, 245))
            pygame.display.update()
            counter = 0
            clock.tick(1/2)
            target2.new_target()
        if b.live <= 0:
            balls.pop(balls.index(b))
    gun.power_up()

pygame.quit()