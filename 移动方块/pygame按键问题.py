'''
谈论和实验pygame按键操作问题
移动方块
'''





import pygame



        
def main():
    pygame.init()


    display_width = 800
    display_height = 600
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('移动方块')
    clock = pygame.time.Clock()

    cube = pygame.image.load('2.png')

    def car(x, y):
        screen.blit(cube, (x, y))

    def gameloop():
        x = display_width * 0.45
        y = display_height * 0.8
        xc = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        xc = -5
                    if event.key == pygame.K_RIGHT:
                        xc = 5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.type == pygame.K_RIGHT:
                        xc = 0
                print(event)
            
            x += xc
            screen.fill((255, 255, 255))
            car(x, y)
            pygame.display.update()
            clock.tick(10)

    gameloop()
    pygame.quit()
    quit()





    


if __name__ == '__main__':
    main()
