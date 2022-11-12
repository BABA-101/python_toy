# 랜덤번호
import random

lotto_num=range(1,46)

for i in range(5):
    # sample(): 1~45의 숫자값 중에 6개
    print(random.sample(lotto_num,6))