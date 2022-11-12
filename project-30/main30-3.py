import tkinter
import tkinter.font

window = tkinter.Tk()
window.title("가상화폐 금액표시")
window.geometry("400x200")
window.resizable(False,False)

font = tkinter.font.Font(size=30)
label=tkinter.Label(window,text=" ", font=font)
label.pack() #배치

cnt = 0

# 1000ms마다 cnt 0부터 증가, 
def get_coin_1sec():
    global cnt  # 전역변수 사용 위해 global 선언
    now_btc_price = str(cnt)
    cnt = cnt+1 
    label.config(text=now_btc_price)    # label을 now_btc_price로 변경
    window.after(1000,get_coin_1sec)    # after(지연시간(ms), 실행할 함수)
    
get_coin_1sec()

window.mainloop()