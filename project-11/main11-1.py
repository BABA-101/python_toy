# 오토마우스는 사진으로 좌표를 찾는 기능이 있다.
# 사전작업: PC카카오톡에서 본인 프로필 사진을 3가지 경우 모두 캡처하여 저장ㅇ
# 그냥 두었을 때, 마우스를 올렸으르 때, 클릭했을 때
import pyautogui

picPosition=pyautogui.locateOnScreen(r'project-11\pic_1.png)
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen(r'project-11\pic_2.png')
    print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen(r'project-11\pic_3.png')
    print(picPosition)