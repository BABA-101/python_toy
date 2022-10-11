import random

random_number = random.randint(1, 100)
print(random_number)

# ----------------------------------------------------------------
print(random.random())  #0.0 ~ 0.999999
print(random.uniform(1, 100))   #실수값
print(random.randint(1, 2))  # 정수값 반환 end 포함
print(random.randrange(1, 2))  # 정수값 반환, end는 미포함
print(random.randrange(10))  # 0부터 10사이
print(
    random.choice([10, 20, 30, 40])
)  # 안에 type을 집어넣는다. 문자열, 리스트, 튜플, range 등.. 무작위 원소 하나 선택
