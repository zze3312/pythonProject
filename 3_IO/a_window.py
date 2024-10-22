import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("a_window.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn_1.clicked.connect(self.button1Function)
        self.btn_2.clicked.connect(self.button2Function)
        self.radioButton_1.clicked.connect(self.radioFunction)
        self.radioButton_2.clicked.connect(self.radioFunction)
        self.radioButton_3.clicked.connect(self.radioFunction)
        self.radioButton_4.clicked.connect(self.radioFunction)

    def button1Function(self):
        userId = self.let_id.text()
        userPwd = self.let_pw.text()
        userPwdChk = self.let_pw_chk.text()

        if userId == '':
            print("아이디를 입력해주세요")
            return 0
        if userPwd == '':
            print("비밀번호를 입력해주세요")
            return 0
        if userPwdChk == '':
            print("비밀번호 확인을 입력해주세요")
            return 0

        if userPwd != userPwdChk:
            print("비밀번호가 일치하지 않습니다")
            return 0
        else:
            result = f"회원가입된 아이디는 {userId} / 비밀번호는 {userPwd} 입니다"
            QMessageBox.information(self, "가입을 환영합니다", result)
            return 0



    def button2Function(self):
        QMessageBox.warning(self, "경고", "취소버튼입니다")
        self.let_id.setText("")
        self.let_pw.setText("")
        self.let_pw_chk.setText("")

    def radioFunction(self):
        if self.radioButton_1.isChecked():
            print("GroupBox_radioButton_1 Checked")
        elif self.radioButton_2.isChecked():
            print("GroupBox_radioButton_2 Checked")
        elif self.radioButton_3.isChecked():
            print("GroupBox_radioButton_3 Checked")
        elif self.radioButton_4.isChecked():
            print("GroupBox_radioButton_4 Checked")

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()