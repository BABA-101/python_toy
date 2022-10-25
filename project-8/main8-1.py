#쓰레드를 사용한 실습
import threading
import time

def thread_1():
    while True:
        print("쓰레드 1 동작")
        # 1초마다 해당 출력문 출력
        time.sleep(1.0)

# 쓰레드 설정
t1=threading.Thread(target=thread_1)
t1.start()

while True:
    print("main 동작")
    time.sleep(2.0)


# 코드 실행 후 터미널에 ctrl Z눌러서 인터럽트 발생.
# 그럼 main함수는 중단되나, 쓰레드 1은 여전히 통작.
# 쓰레드가 독립적으로 동작하도록 설정되어 있기 때문이다.