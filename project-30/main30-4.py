# 1초마다 get_coin_1sec 함수 불러와서 label 업데이트 (1씩증가)

# .exe 파일로 만들기
# pyinstaller -w -F main30-4.py 

import tkinter
import tkinter.font
import pyupbit
import threading
import time

coin_price = 0

# 1초마다 KRW-BTC 가져와서 전역변수 coin_price에 저장
def get_coin_price():
    global coin_price
    while True:
        coin_price = pyupbit.get_current_price("KRW-BTC")
        time.sleep(1.0)

# 스레드 프로그램 생성
t1 = threading.Thread(target=get_coin_price)
t1.daemon=True # 메인 쓰레드가 종료되면 같이 종료되는 쓰레드
t1.start()

window = tkinter.Tk()
window.title("비트코인 실시간 가격")
window.geometry("400x50")
window.resizable(False,False)

font = tkinter.font.Font(size=30)
label=tkinter.Label(window, text=" ", font=font)
label.pack()

def get_coin_1sec():
    global coin_price
    now_btc_price=str(coin_price)
    label.config(text=now_btc_price)
    window.after(1000,get_coin_1sec)

get_coin_1sec()
window.mainloop()