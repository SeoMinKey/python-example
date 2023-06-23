import pygame # 1. pygame 선언
import random #    random 선언

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
WHITE = (255,255,255)
screen_size = (1080, 720)
screen = pygame.display.set_mode(screen_size)

done = True
clock = pygame.time.Clock()

airplane = pygame.image.load('plane.png')
airplane_size = (120, 90)
airplane = pygame.transform.scale(airplane, airplane_size)

# 4. pygame 무한루프
def runGame():
    global done, airplane
    airplane_x = 20
    airplane_y = 24
    circle_x = random.randint(0,screen_size[0])
    circle_y = random.randint(0,screen_size[1])
    sysfont = pygame.font.SysFont(None, 50)
    score = 0

    while done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 종료조건
                done=False

            if event.type == pygame.KEYDOWN: # 키보드 입력
                if event.key == pygame.K_UP:
                    airplane_y -= 50
                elif event.key == pygame.K_DOWN:
                    airplane_y += 50
                elif event.key == pygame.K_LEFT:
                    airplane_x -= 70
                elif event.key == pygame.K_RIGHT:
                    airplane_x += 70

                if airplane_y + airplane_size[1] >= screen_size[1]: # 창 벗어남 방지
                    airplane_y = screen_size[1] - airplane_size[1]
                elif airplane_y <= 0:
                    airplane_y = 0
                if airplane_x + airplane_size[0] >= screen_size[0]:
                    airplane_x = screen_size[0] - airplane_size[0]
                elif airplane_x <= 0:
                    airplane_x = 0

            if (circle_y in range(airplane_y, airplane_y + airplane_size[1] + 1)) and (circle_x in range(airplane_x, airplane_x + airplane_size[0] + 1)):# 충돌 감지
                circle_x = random.randint(0,screen_size[0])
                circle_y = random.randint(0,screen_size[1])
                score += 1

        pygame.draw.circle(screen, (255,0,0), (circle_x, circle_y), 20)
        screen.blit(airplane, (airplane_x, airplane_y))
        text = sysfont.render(f"score: {score}", True, (0, 0, 255)) 
        screen.blit(text, (10,10))
        pygame.display.update()

runGame()
pygame.quit()