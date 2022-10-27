# 여러 지역 날씨를 자동으로 검색 후 저장하는 코드
# 코드 실행 전, 한영키 눌러서 영어로 바꿔놓을 것.
# 범용적인 사용이 어렵기에 한글변수명은 추천하지 않음. 그냥 테스트용으로 작성
import pyautogui
import time
import pyperclip

날씨 = ["서울 날씨", "시흥 날씨", "청주 날씨", "부산 날씨", "강원도 날씨"]

#상단 주소창
addr_x=1177
addr_y=69
start_x=1004
start_y=276
end_x=1831
end_y=776

for 지역날씨 in 날씨:
    pyautogui.moveTo(addr_x,addr_y)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    # 해당 문자를 interval마다 타이핑한다
    pyautogui.write("www.naver.com", interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(1)

    pyperclip.copy(지역날씨)
    pyautogui.hotkey("ctrl","v")
    time.sleep(0.5)

    pyautogui.write(['enter'])
    time.sleep(1)
    저장경로 = 'project-10\\' + 지역날씨 + '.png'
    pyautogui.screenshot(저장경로,region=(start_x,start_y,end_x-start_x,end_y-start_y))