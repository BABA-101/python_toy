import tkinter
import tkinter.font
import random

lotto_num=range(1,46)

def buttonClick():
    print(random.sample(lotto_num,6))

window=tkinter.Tk()
window.title("lotto")
window.geometry("400x200+800+300")
window.resizable(False,False)

# Button(윈도우 창,  overrelief=버튼에 마우스 올렸을 때 테두리 모양,command=사용자정의함수실행, repeatdelay=버튼 누른 상태에서 command 함수까지 실행시간,repeatinterval=버튼 누른 상태에서 command 실행 반복시간  )
button = tkinter.Button(window, overrelief="solid",text="번호확인",width=15,command=buttonClick,repeatdelay=1000,repeatinterval=100)
button.pack()

window.mainloop()