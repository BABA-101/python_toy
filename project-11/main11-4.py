# 일정 간격마다 보내는 코드 (특정 요일 등)
import pyautogui
import pyperclip
import time
import schedule

def send_message():
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

# 10초마다 sned_message 함수를 실행할 스케줄 등록
schedule.every(10).seconds.do(send_message)

# rund_pending()함수는 계속 실행되면서 스케줄에 등록된 함수를 설정된 시간마다 실행.
while True:
    schedule.run_pending()
    time.sleep(1.0)