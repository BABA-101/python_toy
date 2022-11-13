import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

path=r'project-34\paint.ui'
from_class=uic.loadUiType(path)[0]

class WindowClass(QMainWindow,from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.brushColor=Qt.black
        
        #lb_canvas를 ㄹㅇ canvas로 설정
        self.canvas = QtGui.QPixmap(self.lb_canvas.width(),self.lb_canvas.height())
        self.canvas.fill(QtGui.QColor("white"))
        self.lb_canvas.setPixmap(self.canvas) # setPixmap: 문자열 대신 이미지가 표시 (QPixmap 객체를 추가하는 것)
        
        # 각 버튼 색 변경, 버튼 클릭 시 동작하는 슬롯 연결
        self.btn_black.clicked.connect(self.btn_clicked)
        # setStyleSheet: 색상 사용자 정의. 여러 형식 존재하나, 아래처럼 사용 시 배경컬러 속성 직접 설정.
        self.btn_black.setStyleSheet("background:black")
        
        self.btn_red.clicked.connect(self.btn_clicked)
        self.btn_red.setStyleSheet("background:red")
        
        self.btn_blue.clicked.connect(self.btn_clicked)
        self.btn_blue.setStyleSheet("background:blue")
        
        self.btn_clear.clicked.connect(self.btn_clear_clicked)
    
    
    def btn_clicked(self):
        btn_value=self.sender().objectName()
        print(btn_value)
        
    def btn_clear_clicked(self):
        print("모두 지움")
        
    # 마우스 클릭 시 마우스의 좌표를 출력하는 함수
    # 마우스 버튼을 누르고 있는 동안 마우스가 움직일 때마다 호출됨
    def mouseMoveEvent(self,e):
        print(e.x(),e.y())


if __name__ == "__main__":
    app=QApplication(sys.argv)
    myWindow=WindowClass()
    myWindow.show()
    app.exec_()