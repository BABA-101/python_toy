from tkinter import *
from tkinter.filedialog import *

def new_file():
    text_area.delete(1.0,END)

# SAVE 메뉴를 눌렀을 때 
def save_file():
    # asksaveasfile: SaveAs 대화 상자를 만들고 쓰기 전용 모드로 열린 파일 객체를 반환
    f = asksaveasfile(mode='w',defaultextension='.txt',filetypes=[('Text files','.txt')])
    text_save=str(text_area.get(1.0,END))
    f.write(text_save) # 파일 객체 write
    f.close()

# Maker 메뉴를 눌렀을 떄
def maker():
    # Toplevel: 다른 위젯들을 포함하는 외부 윈도우를 생성
    help_view=Toplevel(window)
    help_view.geometry("300x25+800+300")
    help_view.title("Maker")
    lb=Label(help_view,text="bibi")
    lb.pack()
    
window=Tk()
window.title("notepad")
window.geometry("400x400+800+800")
window.resizable(False,False)

menu=Menu(window)
menu_1=Menu(menu,tearoff=0)
menu_1.add_command(label="New File",command=new_file)
menu_1.add_command(label="Save", command=save_file)
menu_1.add_separator()
menu_1.add_command(label="Exit",command=window.destroy)
menu.add_cascade(label="File",menu=menu_1)

menu_2=Menu(menu,tearoff=0)
menu_2.add_command(label='Maker',command=maker)
menu.add_cascade(label='Maker',menu=menu_2)

text_area=Text(window)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N+E+S+W)

window.config(menu=menu)
window.mainloop()