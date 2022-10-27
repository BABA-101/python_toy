# 스레드를 이용해서 일정 시간마다 동작하는 코드 만들기
import pyautogui
import pyperclip
import time
import threading

def send_message():
    # send_message 함수를 10초 후에 실행, 자신의 함수에서 10초 후에 자신이 함수를 다시 불러오는 것.
    # 즉, send_message 함수를 10초마다 실행함
    threading.Timer(10,send_message).start()

    picPosition=pyautogui.locateOnScreen(r'project-11\pic_1.png')
    print(picPosition)

    if picPosition is None:
        picPosition = pyautogui.locateOnScreen(r'project-11\pic_2.png')
        print(picPosition)

    if picPosition is None:
        picPosition=pyautogui.locateOnScreen(r'project-11\pic_3.png')
        print(picPosition)

    clickPosition = pyautogui.center(picPosition)
    pyautogui.doubleClick(clickPosition)

    pyperclip.copy('이 메시지는 자동으로 보내는 메시지입니다.')
    pyautogui.hotkey("ctrl","v")
    time.sleep(1.0)

    pyautogui.write(['enter'])
    time.sleep(1.0)

    pyautogui.write(['escape'])
    time.sleep(1.0)

# 처음 한번 실행해주면, 스스로 threading.Timer에 의해 10초마다 불려짐
send_message()
