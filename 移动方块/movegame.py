bif = '1.png'
mif = '2.png'
import sys
import pygame as p
from pygame.locals import *

p.init()

screen = p.display.set_mode((640, 360))
screen.fill((242, 242, 242))
mouse_c = p.image.load(mif)

x, y = 0, 0
movex, movey = 0, 0

while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()

        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                movex -= 1
            if event.key == p.K_RIGHT:
                movex += 1
            elif event.key == p.K_UP:
                movey += 1
            elif event.key == p.K_DOWN:
                movey -= 1
        if event.type == p.KEYUP:
            if event.key == p.K_LEFT:
                movex == 0
            if event.key == p.K_RIGHT:
                movex == 0
            elif event.key == p.K_UP:
                movey == 0
            elif event.key == p.K_DOWN:
                movey == 0

x += movex
y += movey

screen.blit(screen, (0, 0))
screen.blit(mouse_c, (x, y))

p.display.update()