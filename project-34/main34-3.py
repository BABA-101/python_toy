# 그림판 만들기
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
        
        self.canvas = QtGui.QPixmap(self.lb_canvas.width(),self.lb_canvas.height())
        self.canvas.fill(QtGui.QColor("white"))
        self.lb_canvas.setPixmap(self.canvas)
        
        self.btn_black.clicked.connect(self.btn_clicked)
        self.btn_black.setStyleSheet("background:black")
        
        self.btn_red.clicked.connect(self.btn_clicked)
        self.btn_red.setStyleSheet("background:red")
        
        self.btn_blue.clicked.connect(self.btn_clicked)
        self.btn_blue.setStyleSheet("background:blue")
        
        self.btn_clear.clicked.connect(self.btn_clear_clicked)
    
    
    def btn_clicked(self):
        btn_value=self.sender().objectName()
        print(btn_value)
        
        # 브러시 색상 변경
        if btn_value == 'btn_black':
            self.brushColor=Qt.black
        elif btn_value == 'btn_red':
            self.brushColor=Qt.red
        elif btn_value == 'btn_blue':
            self.brushColor=Qt.blue
        
    def btn_clear_clicked(self):
        print("모두 지움")
        self.canvas.fill(QtGui.QColor("white"))
        self.lb_canvas.setPixmap(self.canvas)
        

    def mouseMoveEvent(self,e):
        painter=QtGui.QPainter(self.lb_canvas.pixmap()) #드로잉할 도화지는 lb_canvas.pixmap객체이다
        # QPen(brush, width, style=Qt.SolidLine, cap=Qt.SquareCap, join=Qt.BevelJoin)
        # RoundCap: 둥근 선
        painter.setPen(QPen(self.brushColor, 3, Qt.SolidLine,Qt.RoundCap))
        painter.drawPoint(e.x(),e.y()) # 점 그리기 메서드
        painter.end() #페인팅 종료
        self.update() #드로잉 업데이트


if __name__ == "__main__":
    app=QApplication(sys.argv)
    myWindow=WindowClass()
    myWindow.show()
    app.exec_()