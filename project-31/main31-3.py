import tkinter
import tkinter.font
import random

lotto_num=range(1,46)

def buttonClick():
    for i in range(5):
        # 랜덤 숫자 6개를 map함수 사용하여 문자열로 변환
        # map(함수, 리스트): 리스트의 요소를 지정된 함수로 처리.
        lottoPick=map(str,random.sample(lotto_num,6))
        # 문자열 리스트를 합쳐서 하나의 문자열로 변환, 중간에 ,추가
        lottoPick =','.join(lottoPick)
        
        lottoPick = str(i+1) + '회: ' + lottoPick
        print(lottoPick)
        
        listbox.insert(i, lottoPick)
    listbox.pack()

window=tkinter.Tk()
window.title("lotto")
window.geometry("400x200+800+300")
window.resizable(False,False)

button=tkinter.Button(window,overrelief="solid",text="번호확인",width=15,command=buttonClick, repeatdelay=1000, repeatinterval=100)
button.pack()

font=tkinter.font.Font(size=20)
# 윈도우 창에 표시할 리스트박스의 속성
# selectmode: 리스트박스의 항목 선택 방법
listbox=tkinter.Listbox(window,selectmode="extended",height=5,font=font)
listbox.insert(0,"1회: ")
listbox.insert(0,"2회: ")
listbox.insert(0,"3회: ")
listbox.insert(0,"4회: ")
listbox.insert(0,"5회: ")
listbox.pack()

window.mainloop()