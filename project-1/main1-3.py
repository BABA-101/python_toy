import random

random_number = random.randint(1, 100)
game_count = 1

while True:
    try:
        my_number = int(input("1~100 사이 숫자 입력>> "))

        if my_number > random_number:
            print("다운")
        elif my_number < random_number:
            print("업")
        elif my_number == random_number:
            print(f"추카추카. 시도 횟수: {game_count}")
            break

        game_count += 1
    except:
        print("에러 발생. 숫자를 입력하셈")
