import random

def binary_search_game():
    # 1부터 100 사이의 숫자 중 하나를 무작위로 선택
    secret_number = random.randint(1, 100)
    # 추측할 숫자의 범위를 지정
    min_number = 1
    max_number = 100
    # 사용자가 선택한 숫자의 횟수를 저장할 변수 초기화
    guess_count = 0
    
    # 사용자가 숫자를 맞출 때까지 반복 (while True는 무한반복)
    while True:
        # 추측할 숫자 계산(이진탐색 기법 - https://woodforest.tistory.com/32)
        guess = (min_number + max_number) // 2
        # 추측한 숫자 출력
        print("I guess the number is", guess)
        # 사용자에게 입력을 받음
        user_input = input("Is my guess correct, higher, or lower? Enter c/h/l: ")
        # 사용자 입력에 따라 다음 단계 결정
        if user_input == "c":
            # 숫자를 맞췄으므로 종료
            print("I guessed the number in", guess_count, "guesses!")
            break
        elif user_input == "h":
            # 추측한 숫자보다 큰 숫자를 추측해야 함
            min_number = guess + 1
        elif user_input == "l":
            # 추측한 숫자보다 작은 숫자를 추측해야 함
            max_number = guess - 1
        else:
            # 잘못된 입력
            print("Invalid input. Please enter c/h/l.")
            continue
        # 추측한 숫자의 횟수 증가
        guess_count += 1
        
binary_search_game()
