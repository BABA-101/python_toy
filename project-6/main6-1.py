# 문자열을 순서대로 배열하는 코드
# 입력한 모든 문자열이 순서대로 출력. (3자리)
import itertools

passwd_string="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for len in range(1,4):
    # itertools.product(): 두 개 이상의 리스트끼리의 cartesian product 계산해서 interator로 반환
    # repeat은 길이인듯? len = 1~3, 문자열 길이도 1~3
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attemp in to_attempt:
        # 리스트로 반환된 값을 문자열로 변환. 
        # ".join(리스트)"는 리스트의 값을 문자열로 변환하는 역할을 함.
        passwd = ' '.join(attemp)
        print(passwd)