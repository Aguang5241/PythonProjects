'''
每隔一段时间随记生成不同大小和颜色的小球
'''
from random import randint
from enum import Enum, unique
import pygame

@unique
class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    GRAY = (242, 242, 242)
    WHITE = (255, 255, 255)

    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return(r, g, b)
    
class Ball():
    def __init__(self, x, y, radius, sx, sy, color = Color.RED):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)
    
    def move(self, screen):
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or self.x + self.sx >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or self.y + self.sy >= screen.get_height():
            self.sy = -self.sy
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption('冒泡泡')
    
    balls = []
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #if event.type == pygame.MOUSEMOTION:
            while len(balls) <= 10:
                x, y = randint(10, 700), randint(10, 500)
                sx, sy = randint(-5, 5), randint(-5, 5)
                radius = randint(5, 30)
                color = Color.random_color()
                ball = Ball(x, y, radius, sx, sy, color)
                balls.append(ball)
                    
        screen.fill((255, 255, 255))
        
        for ball in balls:
            ball.draw(screen)
            ball.move(screen)
        
        pygame.display.flip()
        pygame.time.delay(50)
        
            


















if __name__ == '__main__':
    main()