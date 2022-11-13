# 버튼 입력받아 출력시킬 것 

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

path=r'project-33\cal.ui'
from_class=uic.loadUiType(path)[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 각 버튼 클릭하면 btn_clicked 함수 실행
        self.btn_C.clicked.connect(self.btn_clicked)
        self.btn_number0.clicked.connect(self.btn_clicked)
        self.btn_number1.clicked.connect(self.btn_clicked)
        self.btn_number2.clicked.connect(self.btn_clicked)
        self.btn_number3.clicked.connect(self.btn_clicked)
        self.btn_number4.clicked.connect(self.btn_clicked)
        self.btn_number5.clicked.connect(self.btn_clicked)
        self.btn_number6.clicked.connect(self.btn_clicked)
        self.btn_number7.clicked.connect(self.btn_clicked)
        self.btn_number8.clicked.connect(self.btn_clicked)
        self.btn_number9.clicked.connect(self.btn_clicked)
        self.btn_add.clicked.connect(self.btn_clicked)
        self.btn_minus.clicked.connect(self.btn_clicked)
        self.btn_divide.clicked.connect(self.btn_clicked)
        self.btn_multipy.clicked.connect(self.btn_clicked)
        self.btn_result.clicked.connect(self.btn_clicked)
        
        self.le_view.setEnabled(False) # le_view 오브젝트는 비활성화로, 값 입력 불가능
        
    # 버튼 클릭 시 각 버튼의 텍스트 값 출력하는 슬롯
    def btn_clicked(self):
        btn_value=self.sender().text()
        print(btn_value)
        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()