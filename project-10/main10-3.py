from tracemalloc import start
import pyautogui
import time
import pyperclip

pyautogui.moveTo(1525,231,0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey("ctrl","v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

start_x=1004
start_y=276
end_x=1831
end_y=776

# 스크린샷 찍기. region=(시작좌표 x, 시작좌표 y, x크기, y크기)
pyautogui.screenshot(r'project-10\서울날씨.png', region=(start_x,start_y,end_x-start_x,end_y-start_y))