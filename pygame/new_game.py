import pygame

pygame.init()

screen_size = (1080, 720)
screen = pygame.display.set_mode(screen_size)
WHITE = (255,255,255)

done = True
clock = pygame.time.Clock()

bg_img = pygame.image.load('python-example/pygame/img/bg.jpg')

def runGame():
    global done

    while done:
        screen.blit(bg_img, (0,0))
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 종료조건
                done=False

    pygame.display.update()


runGame()
pygame.quit()