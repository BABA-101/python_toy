# tkinter GUI >메모장
from tkinter import *
# filedialog: filedialog박스를 사용하기 위한,
from tkinter.filedialog import *

# 각 메뉴 선택 시 동작하는 함수
def new_file():
    pass
def save_file():
    pass
def maker():
    pass

window=Tk()
window.title("notepad")
window.geometry("400x400+800+300")
window.resizable(False,False)

# window창 상단바 첫번째 메뉴 구성. 새 파일/저장/종료
# Menu(window): 윈도우 창 
menu=Menu(window) 

# tearoff : 하위메뉴의 분리 기능 사용 유/무
menu_1=Menu(menu,tearoff=0)
menu_1.add_command(label='new file',command=new_file)
menu_1.add_command(label='save', command=save_file)
menu_1.add_separator() # 구분선 생성
menu_1.add_command(label='exit',command=window.destroy)
# add_cascade(label="상위 메뉴 이름", menu=연결할 상위 메뉴), 상단바 메뉴와 아래 메뉴들 합체
menu.add_cascade(label='File',menu=menu_1)

menu_2=Menu(menu,tearoff=0)
menu_2.add_command(label='From',command=maker)
menu.add_cascade(label='from',menu=menu_2)

#윈도우창에 메뉴 등록
window.config(menu=menu)

window.mainloop()