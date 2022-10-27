# pyautogui: 마우스와 키보드를 자동으로 제어하기 위해 사용
import pyautogui
import time

while True:
    # 마우스의 좌표 출력
    print(pyautogui.position())
    time.sleep(1)