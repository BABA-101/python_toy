# 좌표를 이용하여 메시지를 자동으로 보내는 코드
import pyautogui
import pyperclip
import time

# 이미지를 통해 좌표찾기
picPosition = pyautogui.locateOnScreen(r'project-11\pic_1.png')
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen(r'project-11\pic_2.png')
    print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen(r'project-11\pic_3.png')
    print(picPosition)

# 이미지에서 찾은 좌표의 중간 좌표값을 찾아서 더블클릭
# center(): 해당 영역의 가운데 위치를 튜플로 반환
clickPosition=pyautogui.center(picPosition)
pyautogui.doubleClick(clickPosition)

pyperclip.copy('이 메시지는 자동으로 보내는 메시지입니다.')
pyautogui.hotkey("ctrl","v")
time.sleep(1.0)

pyautogui.write(['enter'])
time.sleep(1.0)

pyautogui.write(['escape']) #esc
time.sleep(1.0)
