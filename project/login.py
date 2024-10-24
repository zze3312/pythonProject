import sys

from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import *
from PyQt5 import uic

import funtion

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("login.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(6)
        self.btn_join.clicked.connect(self.go_join)
        self.btn_submit.clicked.connect(self.join)
        self.btn_cancel.clicked.connect(self.go_home)
        self.btn_login.clicked.connect(self.login)

    def login(self):
        userId = self.login_id.text()
        userPwd = self.login_pwd.text()

        if funtion.user.login(self, userId, userPwd):
            self.go_main()
        else:
            QMessageBox.information(self, "실패", "로그인 실패하셨습니다")


    def join(self):
        userId = self.join_id.text()
        userPwd = self.join_pwd.text()
        userPwdChk = self.join_pwd_chk.text()
        userTel = self.join_tel.text()

        if userId == '':
            print("아이디를 입력해주세요")
            return 0
        if userPwd == '':
            print("비밀번호를 입력해주세요")
            return 0
        if userPwdChk == '':
            print("비밀번호 확인을 입력해주세요")
            return 0
        if userTel == '':
            print("연락처를 입력해주세요")
            return 0

        if userPwd != userPwdChk:
            print("비밀번호가 일치하지 않습니다")
            return 0

        if funtion.user.join(self, userId, userPwd, userTel):
            QMessageBox.information(self, "성공", "회원가입 되셨습니다")
            self.join_id.setText("")
            self.join_pwd.setText("")
            self.join_pwd_chk.setText("")
            self.join_tel.setText("")
            self.go_home()
        else:
            QMessageBox.information(self, "실패", "회원가입 실패하셨습니다")

    def go_home(self):
        self.stackedWidget.setCurrentIndex(0)

    def go_join(self):
        self.stackedWidget.setCurrentIndex(1)

    def go_main(self):
        self.stackedWidget.setCurrentIndex(2)


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()