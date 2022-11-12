# 가상회폐 금액표시 GUI
# tkinter: 파이썬에서 GUI 프로그램 만들 때 

import tkinter

# 가장 상위 레벨의 윈도우 창을 생성
window = tkinter.Tk() 
window.title("가상화폐 금액표시")
# geometry("width * heigh + x + y ")
window.geometry("400x200")
# 윈도우 창 크기 조절 가능 여부를 설정
window.resizable(False,False)

# 윈도우 창에 Label 위젯을 설정
label=tkinter.Label(window,text='hello')
label.pack() # pack() 통하여 배치

# 윈도우가 종료될 때까지 윈도우창 실행
window.mainloop()