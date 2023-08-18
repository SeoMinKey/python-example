# 보석을 다양하게 넣어서 게임 완성하기
import os
import math
import pygame
import random

# 집게 클래스
class Claw(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.original_image = image
        self.rect = image.get_rect(center=position)

        self.offset = pygame.math.Vector2(default_offset_x_claw, 0)
        self.position = position

        self.direction = LEFT # 집게의 이동 방향
        self.angle_speed = 2.5 # 집게의 각도 변경 폭 (좌우 이동 속도)
        self.angle = 10 # 최초 각도 정의 (오른쪽 끝)

    def update(self, to_x):
        if self.direction == LEFT: # 왼쪽 방향으로 이동하고 있다면
            self.angle += self.angle_speed # 이동 속도만큼 각도 증가
        elif self.direction == RIGHT: # 오른쪽 방향으로 이동하고 있다면
            self.angle -= self.angle_speed

        # 만약에 허용 각도 범위를 벗어나면?
        if self.angle > 170:
            self.angle = 170
            self.set_direction(RIGHT)
        elif self.angle < 10:
            self.angle = 10
            self.set_direction(LEFT)

        self.offset.x += to_x
        self.rotate() # 회전 처리

    def rotate(self):        
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1) # 회전 대상 이미지, 회전 각도, 이미지 크기(scale)
        offset_rotated = self.offset.rotate(self.angle)
        self.rect = self.image.get_rect(center=self.position+offset_rotated)

    def set_direction(self, direction):
        self.direction = direction

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.line(screen, BLACK, self.position, self.rect.center, 5) # 직선 그리기

    def set_init_state(self):
        self.offset.x = default_offset_x_claw
        self.angle = 10
        self.direction = LEFT

# 보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position, price, speed):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center=position)
        self.price = price
        self.speed = speed

    def set_position(self, position, angle):
        r = self.rect.size[0] // 2 # 동그라미 이미지 기준으로 반지름
        rad_angle = math.radians(angle) # 각도
        to_x = r * math.cos(rad_angle) # 삼각형의 밑변
        to_y = r * math.sin(rad_angle) # 삼각형의 높이
        self.rect.center = (position[0] + to_x, position[1] + to_y)

def setup_gemstone():
    small_gold_price, small_gold_speed = 300, 10
    big_gold_price, big_gold_speed = 600, 8
    stone_price, stone_speed = 100, 15
    diamond_price, diamond_speed = -10, 17

    big_gold_spot = [(300, 550), (680, 750), (1280, 900), (1580, 650)]
    diamond_spot = [(100, 500), (400, 400), (600, 600), (250, 730), (440, 850), (870, 640), (1000, 900), (1280, 550), (1400, 720), (1580, 950), (1700, 480), (1780, 770)]
    stone_spot = [(180, 900), (440, 700), (600, 430), (860, 800), (1000, 570), (1200, 680), (1420, 500), (1580, 810)]
    small_gold_spot = [(120, 700), (610, 960), (1000, 740), (1500, 970), (1750, 650)]

    # 작은 금
    random.shuffle(small_gold_spot)
    for i in range(0, 4):
        gemstone_group.add(Gemstone(pygame.transform.rotozoom(gemstone_images[0], random.randrange(-80, 80), 1), small_gold_spot[i], small_gold_price, small_gold_speed)) # 그룹에 추가
    
    # 큰 금
    random.shuffle(big_gold_spot)
    for i in range(0, 2):
        gemstone_group.add(Gemstone(pygame.transform.rotozoom(gemstone_images[1], random.randrange(-20, 20), 1), big_gold_spot[i], big_gold_price, big_gold_speed))

    # 돌
    random.shuffle(stone_spot)
    for i in range(0, 5):
        gemstone_group.add(Gemstone(pygame.transform.rotozoom(gemstone_images[2], random.randrange(-90, 90), 1), stone_spot[i], stone_price, stone_speed))

    # 다이아몬드
    random.shuffle(diamond_spot)
    for i in range(0, 9):
        gemstone_group.add(Gemstone(pygame.transform.rotozoom(gemstone_images[3], random.randrange(-50, 50), 1), diamond_spot[i], diamond_price, diamond_speed))

def update_score(score):
    global curr_score
    curr_score += score

def display_score():
    game_font = pygame.font.Font(text_font, 70)
    txt_curr_score = game_font.render(f"현재 점수 : {curr_score:,}", True, BLACK)
    screen.blit(txt_curr_score, (50, 50))

    game_font = pygame.font.Font(text_font, 70)
    txt_goal_score = game_font.render(f"목표 점수 : {goal_score:,}", True, BLACK)
    screen.blit(txt_goal_score, (50, 130))

def display_time(time):
    game_font = pygame.font.Font(text_font, 70)
    txt_timer = game_font.render(f"시간 : {time}", True, BLACK)
    screen.blit(txt_timer, (screen_width - 370, 50))

def display_game_text(text, line):
    game_font = pygame.font.Font(text_font, 130) # 큰 폰트
    txt_game_over = game_font.render(text, True, WHITE)
    rect_game_over = txt_game_over.get_rect(center=(int(screen_width / 2), int(screen_height / 2) + line)) # 화면 중앙에 표시
    screen.blit(txt_game_over, rect_game_over)

def game_set():
    global curr_score, to_x, start_ticks, caught_gemstone, claw
    curr_score = 0
    to_x = 0
    caught_gemstone = None
    gemstone_group.empty()
    setup_gemstone()
    claw.set_init_state()
    start_ticks = pygame.time.get_ticks()

pygame.init()
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gold Miner")
clock = pygame.time.Clock()
game_font = pygame.font.Font()

# 점수 관련 변수
goal_score = 2500 # 목표 점수
curr_score = 0 # 현재 점수

# 게임 오버 관련 변수
game_result = None # 게임 결과
total_time = 60 # 총 시간
start_ticks = pygame.time.get_ticks() # 현재 tick 을 받아옴

# 게임 관련 변수
default_offset_x_claw = 100 # 중심점으로부터 집게까지의 기본 x 간격
to_x = 0 # x 좌표 기준으로 집게 이미지를 이동시킬 값 저장 변수
caught_gemstone = None # 집게를 뻗어서 잡은 보석 정보

# 속도 변수
move_speed = 30 # 발사할 때 이동 스피드 (x 좌표 기준으로 증가되는 값)
return_speed = 45 # 아무것도 없이 돌아올 때 이동 스피드

# 방향 변수
LEFT = -1 # 왼쪽 방향
STOP = 0 # 이동 방향이 좌우가 아닌 고정인 상태 (집게를 뻗음)
RIGHT = 1 # 오른쪽 방향

# 색깔 변수
RED = (255,0,0) # RGB, 빨간색
BLACK = (0,0,0) # 검은색
WHITE = (255, 255, 255)

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
background = pygame.image.load(os.path.join(current_path, "background.png"))
text_font = os.path.join(current_path, "DungGeunMo.ttf")

# 4개 보석 이미지 불러오기 (작은 금, 큰 금, 돌, 다이아몬드)
gemstone_images = [
    pygame.image.load(os.path.join(current_path, "small_gold.png")).convert_alpha(), # 작은 금
    pygame.image.load(os.path.join(current_path, "big_gold.png")).convert_alpha(), # 큰 금
    pygame.image.load(os.path.join(current_path, "stone.png")).convert_alpha(), # 돌
    pygame.image.load(os.path.join(current_path, "diamond.png")).convert_alpha()] # 다이아몬드

# 보석 그룹
gemstone_group = pygame.sprite.Group()
setup_gemstone() # 게임에 원하는 만큼의 보석을 정의

# 집게
claw_image = pygame.image.load(os.path.join(current_path, "claw.png")).convert_alpha()
claw = Claw(claw_image, (screen_width // 2, 110)) # 가로위치는 화면 가로 크기 기준으로 절반, 세로위치는 위에서 110 px

game = True
while game:
    start = True
    while start:
        screen.blit(background, (0, 0))
        display_game_text('\바다를 지켜라/', -100)
        display_game_text('\청소년 지구방위대/', 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                game = False
            
            if event.type == pygame.KEYDOWN: # 스페이스 버튼 누를 때 집게를 뻗음
                if event.key == pygame.K_SPACE:
                    start = False

        pygame.display.update()

    game_set()

    if not game:
        break

    running = True
    while running:
        clock.tick(30) # FPS 값이 30 으로 고정

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False
            
            if event.type == pygame.KEYDOWN: # 스페이스 누를 때 집게를 뻗음
                if event.key == pygame.K_SPACE:
                    claw.set_direction(STOP) # 좌우 멈춤
                    to_x = move_speed # move_speed 만큼 빠르게 쭉 뻗음

        if claw.rect.left < 0 or claw.rect.right > screen_width or claw.rect.bottom > screen_height:
            to_x = -return_speed

        if claw.offset.x < default_offset_x_claw: # 원위치에 오면
            to_x = 0
            claw.set_init_state() # 처음 상태로 되돌림

            if caught_gemstone: # 잡힌 보석이 있다면
                update_score(caught_gemstone.price) # 점수 업데이트 처리 (나중에)
                gemstone_group.remove(caught_gemstone) # 그룹에서 잡힌 보석 제외
                caught_gemstone = None

        if not caught_gemstone: # 잡힌 보석이 없다면 충돌 체크
            for gemstone in gemstone_group:
                # if claw.rect.colliderect(gemstone.rect): # 직사각형 기준으로 충돌 처리
                if pygame.sprite.collide_mask(claw, gemstone): # 투명 영역은 제외하고 실제 이미지 영역에 대해 충돌 처리
                    caught_gemstone = gemstone # 잡힌 보석
                    to_x = -gemstone.speed # 잡힌 보석의 속도에 - 한 값을 이동 속도로 설정
                    print(claw.offset.x,  default_offset_x_claw)
                    break

        if caught_gemstone:
            caught_gemstone.set_position(claw.rect.center, claw.angle)

        screen.blit(background, (0, 0))

        gemstone_group.draw(screen) # 그룹 내 모든 스프라이트를 screen 에 그림
        claw.update(to_x)
        claw.draw(screen)

        # 점수 정보를 보여줌
        display_score()

        # 시간 계산
        # 1234 -> 1.234 -> 1    
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # ms -> s
        display_time(total_time - int(elapsed_time)) # 시간 표시

        # 만약에 시간이 0 이하이면 게임 종료
        if total_time - int(elapsed_time) <= 0:
            running = False
            if curr_score >= goal_score:
                game_result = "Mission Complete"
            else:
                game_result = "Game Over"
            # 게임 종료 메시지 표시
            display_game_text(game_result, 0)
            pygame.display.update()
            pygame.time.delay(2000) # 2초 정도 대기 후 종료
        
        pygame.display.update()

pygame.quit()