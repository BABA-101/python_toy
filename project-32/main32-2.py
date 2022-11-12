from tkinter import *
from tkinter.filedialog import *

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

menu=Menu(window) 
menu_1=Menu(menu,tearoff=0)
menu_1.add_command(label="New File")
menu_1.add_command(label="Save",command=save_file)
menu_1.add_separator()

menu_1.add_command(label="Exit", command=window.destroy)
menu.add_cascade(label='File',menu=menu_1)

menu_2=Menu(menu, tearoff=0)
menu_2.add_command(label="Maker",command=maker)
menu_2.add_cascade(label="Maker",menu=menu_2)

# Text(window)통해 해당 윈도우 창에 텍스트 입력 가능
text_area=Text(window)

# grid_행/열configure(행/열 값, 가중치)
# 행/열값이란, 행/열로 얼마나 더 글씨가 이어지는가
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)

# sticky 통해서 동/서/남/북 위치조절, 동서남북 방향으로 붙인 것
text_area.grid(sticky=N+E+S+W)

window.config(menu=menu)

window.mainloop()