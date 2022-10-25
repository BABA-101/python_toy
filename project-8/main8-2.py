# 메인코드가 동작할 때만 쓰레드가 동작하도록 만들기
import threading
import time

def thread_1():
    while True:
        print("쓰레드 1 동작")
        time.sleep(1.0)

t1=threading.Thread(target=thread_1)
# daemon: 데몬스레드로 만드는 속성. 일반 스레드를 보조하는 역할을 하는 스레드.
# 데몬스레드는 메인 스레드가 종료되면 같이 종료된다.
t1.daemon=True
t1.start()

while True:
    print("main 동작")
    time.sleep(2.0)