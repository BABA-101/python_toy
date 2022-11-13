import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

path=r'project-33\cal.ui'
from_class=uic.loadUiType(path)[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
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
        
        self.le_view.setEnabled(False)
        self.text_value= " " #초기화
        
    def btn_clicked(self):
        btn_value=self.sender().text()
        if btn_value == 'C':
            print("clear")
            self.le_view.setText("0")
            self.text_value= " " #clear 되었으니 text_value 변수도 초기화
            
        elif btn_value== '=':
            print("=")
            try:
                # eval(): 계산해줌, 단 인자가 str타입 이어야 함.
                resultValue=eval(self.text_value.lstrip("0"))
                self.le_view.setText(str(resultValue))
            except:
                self.le_view.setText("error")
        # 숫자/수식 버튼 클릭 시 self.text_value 변수에 값을 더해나감.
        # print()
        else:
            self.text_value=self.text_value + btn_value
            print(self.text_value)
            self.le_view.setText(self.text_value)
        
if __name__ == "__main__":
    app=QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()