'''
多个赛道，每个赛道上刷小车（参照实例）
控制的小车躲过其他小车（距离或者边界判定）
P.S. 记录最高里程
'''
from threading import Thread
from random import randint, choice
from time import time, sleep

import pygame

class Color(object):
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return r, g, b

class Car():
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color
    
    def move(self):
        if self._y < 600:
            self._y += randint(0, 10)
        else:
            self._color = Color.random_color()
            self._y = 0
            self._x = choice([80, 180, 280, 380, 480])

    def draw(self, screen):
        pygame.draw.rect(screen, self._color, (self._x, self._y, 40, 80), 0)
  
def main():

    class BackgroundTask(Thread):

        def run(self):
            while True:
                screen.fill(Color.GRAY)
                pygame.draw.line(screen, Color.BLACK, (50, 0), (50, 600), 6)
                pygame.draw.line(screen, Color.RED, (150, 0), (150, 600), 3)
                pygame.draw.line(screen, Color.RED, (250, 0), (250, 600), 3)
                pygame.draw.line(screen, Color.RED, (350, 0), (350, 600), 3)
                pygame.draw.line(screen, Color.RED, (450, 0), (450, 600), 3)
                pygame.draw.line(screen, Color.BLACK, (550, 0), (550, 600), 6)
                
                for car in cars:
                    car.draw(screen)
                    car.move()

                pygame.display.flip()
                sleep(0.05)
                
    
    cars = []
    for index in range(3):
        temp = Car(80 + 200 * index, 10, Color.random_color())
        cars.append(temp)



    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('赛车吧！少年')
    clock = pygame.time.Clock()

    def car(a):
        pygame.draw.rect(screen, Color.BLACK, (a, 500, 40, 80), 0)


    BackgroundTask(daemon=True).start()

    a = 0
    a_move = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    a_move = -5
                if event.key == pygame.K_RIGHT:
                    a_move = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.type == pygame.K_RIGHT:
                    a_move = 0
            print(event)
        a += a_move
        car(a)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
                
if __name__ == '__main__':
    main()