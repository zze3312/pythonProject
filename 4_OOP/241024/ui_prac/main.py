import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("main.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QWidget, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        # ProgressBar의 값 0으로 셋팅
        self.progressBar.setValue(0)
        # ProgressBar의 시그널
        self.progressBar.valueChanged.connect(self.printValue)

        # QTimer를 이용하여 매초마다 ProgressBar의 값이 1씩 늘어나게 설정합니다.
        # QTimer의 Interval을 1000으로 설정한 후, ProgrssBar의 값이 늘어나게 하는 함수를 연결하고 QTimer를 시작합니다.
        self.timeVar = QTimer()
        self.timeVar.setInterval(100)
        self.timeVar.timeout.connect(self.progressBarTimer)
        self.timeVar.start()

    def progressBarTimer(self):
        self.time = self.progressBar.value()
        self.time += 1
        self.progressBar.setValue(self.time)

        # ProgressBar의 값이 최댓값 이상이 되면 Timer를 중단시켜 ProgressBar의 값이 더이상 증가하지 않게 합니다.
        if self.time >= self.progressBar.maximum():
            self.timeVar.stop()

    def printValue(self):
        print(self.progressBar.value())


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()