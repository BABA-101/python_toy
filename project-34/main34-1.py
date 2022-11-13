import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

path=r'project-34\paint.ui'
from_class=uic.loadUiType(path)[0]

class WindowClass(QMainWindow,from_class):
    def __init__(self): #self: 인스턴스 자신을 의미
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    myWindow=WindowClass()
    myWindow.show()
    app.exec_()

