# 사전작업: Qt Designer로 cal.ui 제작
# 해당 코드 실행해도 아무런 동작 X
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic # ui파일 파이썬에 로드

path=r'project-33\cal.ui'
# loadUiType(): ui 파일을 불러온 후, 생성된 form 클래스, Qt base 클래스로 이루어진 튜플 반환
# from_class: cal.ui
from_class=uic.loadUiType(path)[0]

# WindowClass 생성, QMainWindow와 Qt Designer에서 만든 화면 객체 from_class를 상속받음
class WindowClass(QMainWindow, from_class):
    def __init__(self): #생성자
        super().__init__() # 부모클래스 초기화
        # setupUi 함수에 QMainWindow 객체 세팅 (ui 생성)
        self.setupUi(self)
        
if __name__ == "__main__":
    #  QApplication 객체를 통해 exec_ 메서드 호출하여 이벤트 루프 생성
    app= QApplication(sys.argv)
    myWindow=WindowClass()
    myWindow.show()
    app.exec_()