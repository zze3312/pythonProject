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
        self.btn_search.clicked.connect(self.search)
        self.btn_cancel2.clicked.connect(self.go_home)
        self.btn_search_page.clicked.connect(self.go_search)
        self.search_gubun1.clicked.connect(self.chk_gubun) # 아이디 찾기
        self.search_gubun2.clicked.connect(self.chk_gubun) # 비밀번호 찾기

        self.btn_add.clicked.connect(self.addListWidget)
        self.btn_insert.clicked.connect(self.insertListWidget)
        self.btn_clear.clicked.connect(self.clearListWidget)
        self.btn_remove.clicked.connect(self.removeListWidget)
        self.btn_print.clicked.connect(self.printListWidget)
        self.btn_print_multi.clicked.connect(self.printMultiListWidget)

        self.btn_pte.clicked.connect(self.printTextEdit)
        self.btn_cte.clicked.connect(self.clearTextEdit)
        self.btn_sf.clicked.connect(self.setTextFont)
        self.btn_sfi.clicked.connect(self.setFontItalic)
        self.btn_sfcr.clicked.connect(self.setFontColorRed)
        self.input_fs.valueChanged.connect(self.setFontSize)

    def printTextEdit(self):
        print(self.textEdit.toPlainText())

    def clearTextEdit(self):
        self.textEdit.clear()

    def setTextFont(self):
        fontvar = QFont("Sans Bold", 20)
        self.textEdit.setCurrentFont(fontvar)

    def setFontItalic(self):
        self.textEdit.setFontItalic(True)

    def setFontColorRed(self):
        colorvar = QColor(255, 0, 0)
        self.textEdit.setTextColor(colorvar)

    def setFontSize(self):
        self.fontSize = self.input_fs.value()
        self.textEdit.setFontPointSize(self.fontSize)

    def printMultiListWidget(self):
        # 선택된 아이템들 list형식으로 가져옴
        self.selectedItems = self.list_widget.selectedItems()

        for item in self.selectedItems:
            print(item.text())

    def printListWidget(self):
        print(self.list_widget.currentItem().text())

    def removeListWidget(self):
        self.listRow = self.list_widget.currentRow()
        self.list_widget.takeItem(self.listRow)

    def clearListWidget(self):
        self.list_widget.clear()

    def insertListWidget(self):
        self.insertRow = self.insert_spin.value()
        self.inputList2 = self.input_list2.text()
        self.list_widget.insertItem(self.insertRow, self.inputList2)

    def addListWidget(self):
        self.inputList = self.input_list.text()
        self.list_widget.addItem(self.inputList)

    def search(self):
        userId = self.search_id.text()
        userTel = self.search_tel.text()
        gubun = ""
        msg = ""

        if self.search_gubun1.isChecked():
            gubun = "아이디 찾기"
            msg = f""
        elif self.search_gubun2.isChecked():
            gubun = "비밀번호 찾기"

        result, id, pw = funtion.user.search(self, userId, userTel)

        if result:
            QMessageBox.information(self, gubun, "로그인 실패하셨습니다")
        else:
            pass

    def chk_gubun(self):
        if self.search_gubun1.isChecked():
            self.label_id2.setHidden(True)
            self.search_id.setHidden(True)
        elif self.search_gubun2.isChecked():
            self.label_id2.setHidden(False)
            self.search_id.setHidden(False)

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

    def go_search(self):
        self.stackedWidget.setCurrentIndex(2)
        self.chk_gubun()

    def go_main(self):
        self.stackedWidget.setCurrentIndex(3)


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()