import pygame
import os
import sys
import random

# 초기화
pygame.init()

current_path = os.path.dirname(__file__)

# 화면 설정
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Custom Image Dino Run")

# 이미지 로드
dino_image = pygame.image.load(os.path.join(current_path, "dino1.png"))
dino_image = pygame.transform.scale(dino_image, (200, 200))

obstacle_image = pygame.image.load(os.path.join(current_path, "obstacle.png"))
obstacle_image = pygame.transform.scale(obstacle_image, (100, 140))

background_image = pygame.image.load(os.path.join(current_path, "background1.png"))
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# 색깔 정의
white = (255, 255, 255)
black = (0, 0, 0)

# 공룡 설정
dino_x = 100
dino_y = screen_height - dino_image.get_height()
dino_speed_y = 0
jump_strength = 27
gravity = 1

# 바닥 설정
ground_height = 40

# 점수 설정
score = 0
font = pygame.font.Font(None, 72)

# 장애물 설정
obstacle_x = screen_width
obstacle_y = screen_height - obstacle_image.get_height() - ground_height
obstacle_speed = 10

# 게임 상태 설정
game_over = False

def restart_game():
    global dino_x, dino_y, dino_speed_y, obstacle_x, obstacle_y, score, game_over
    dino_x = 100
    dino_y = screen_height - dino_image.get_height()
    dino_speed_y = 0
    obstacle_x = screen_width
    obstacle_y = screen_height - obstacle_image.get_height() - ground_height
    score = 0
    game_over = False

# 게임 루프
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and dino_y == screen_height - dino_image.get_height():
        dino_speed_y = -jump_strength

    dino_speed_y += gravity
    dino_y += dino_speed_y

    if dino_y >= screen_height - dino_image.get_height():
        dino_y = screen_height - dino_image.get_height()
        dino_speed_y = 0

    # 장애물 이동 및 충돌 검사
    if not game_over:
        obstacle_x -= obstacle_speed
        if obstacle_x < -obstacle_image.get_width():
            obstacle_x = screen_width
            obstacle_y = screen_height - obstacle_image.get_height() - ground_height
            score += 1
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_image.get_width(), obstacle_image.get_height())
        dino_rect = pygame.Rect(dino_x, dino_y, dino_image.get_width(), dino_image.get_height())
        if obstacle_rect.colliderect(dino_rect):
            game_over = True

    # 화면 업데이트
    screen.blit(background_image, (0, 0))
    screen.blit(dino_image, (dino_x, dino_y))
    screen.blit(obstacle_image, (obstacle_x, obstacle_y))
    pygame.draw.rect(screen, black, (0, screen_height - ground_height, screen_width, ground_height))

    # 게임 오버 표시
    if game_over:
        game_over_text = font.render("Game Over", True, black)
        screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2))

    # 점수 표시
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))

    # 화면 업데이트
    pygame.display.flip()

    clock.tick(60)  # 초당 프레임 설정

    # 게임 재시작
    if game_over and keys[pygame.K_SPACE]:
        restart_game()

# 게임 종료
pygame.quit()
sys.exit()