# 네이버: 자동으로 서울 날씨 검색하는 코드 만들기
# pyperclip: 한글로 클립보드 이용 위해 
import pyautogui
import time
import pyperclip

# 0.2초동안 이동, vscode와 네이버 반씩 나눠서 클릭하도록 함.
# 좌표는 main10-1.py로 확인
pyautogui.moveTo(1525,231,0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
# 두개의 키 동시에 누르기
pyautogui.hotkey("ctrl","v")
time.sleep(0.5)

# 엔터키 입력
pyautogui.write(["enter"])
time.sleep(1)