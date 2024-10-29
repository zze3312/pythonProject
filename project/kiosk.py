import sys
import json
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("project.ui")[0]

# 화면번호
MAIN_PAGE_INDEX = {
            "main" : 0,
            "menu" : 1,
            "payment" : 2,
            "payment2" : 3,
            "payment3" : 4,
            "payment4" : 5,
            "admin" : 6
        }

SUB_PAGE_INDEX = {
            "coffee" : 0,
            "noncoffee" : 1,
            "dessert" : 2,
            "packsccino" : 3,
            "option" : 4
        }

with open("menu.json", "r") as menu:
    MENU_LIST = json.load(menu)

page_gubun = ""
carts = list()
cnt=5

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()

        self.setupUi(self)
        self.go_home()
        self.btn_pick_up.clicked.connect(self.pickup_menu)
        self.btn_in_store.clicked.connect(self.instore_menu)
        self.btn_home.clicked.connect(self.go_home)

        self.btn_coffee.clicked.connect(lambda : self.subWidget.setCurrentIndex(SUB_PAGE_INDEX["coffee"]))
        self.btn_noncoffee.clicked.connect(lambda : self.subWidget.setCurrentIndex(SUB_PAGE_INDEX["noncoffee"]))
        self.btn_dessert.clicked.connect(lambda : self.subWidget.setCurrentIndex(SUB_PAGE_INDEX["dessert"]))
        self.btn_packsccino.clicked.connect(lambda : self.subWidget.setCurrentIndex(SUB_PAGE_INDEX["packsccino"]))

        self.menu_coffee_1_1.clicked.connect(self.go_option)
        self.menu_coffee_1_2.clicked.connect(self.go_option)
        self.menu_coffee_1_3.clicked.connect(self.go_option)
        self.menu_coffee_1_4.clicked.connect(self.go_option)
        self.menu_coffee_2_1.clicked.connect(self.go_option)
        self.menu_coffee_2_2.clicked.connect(self.go_option)
        self.menu_coffee_2_3.clicked.connect(self.go_option)
        self.menu_coffee_2_4.clicked.connect(self.go_option)
        self.menu_coffee_3_1.clicked.connect(self.go_option)
        self.menu_coffee_3_2.clicked.connect(self.go_option)
        self.menu_coffee_3_3.clicked.connect(self.go_option)
        self.menu_coffee_3_4.clicked.connect(self.go_option)
        self.menu_noncoffee_1_1.clicked.connect(self.go_option)
        self.menu_noncoffee_1_2.clicked.connect(self.go_option)
        self.menu_noncoffee_1_3.clicked.connect(self.go_option)
        self.menu_noncoffee_1_4.clicked.connect(self.go_option)
        self.menu_noncoffee_2_1.clicked.connect(self.go_option)
        self.menu_noncoffee_2_2.clicked.connect(self.go_option)
        self.menu_noncoffee_2_4.clicked.connect(self.go_option)
        self.menu_noncoffee_2_4.clicked.connect(self.go_option)
        self.menu_noncoffee_3_1.clicked.connect(self.go_option)
        self.menu_noncoffee_3_2.clicked.connect(self.go_option)
        self.menu_noncoffee_3_3.clicked.connect(self.go_option)
        self.menu_noncoffee_3_4.clicked.connect(self.go_option)
        self.menu_dessert_1_1.clicked.connect(self.go_option)
        self.menu_dessert_1_2.clicked.connect(self.go_option)
        self.menu_dessert_1_3.clicked.connect(self.go_option)
        self.menu_dessert_1_4.clicked.connect(self.go_option)
        self.menu_dessert_2_1.clicked.connect(self.go_option)
        self.menu_dessert_2_2.clicked.connect(self.go_option)
        self.menu_dessert_2_3.clicked.connect(self.go_option)
        self.menu_dessert_2_4.clicked.connect(self.go_option)
        self.menu_dessert_3_1.clicked.connect(self.go_option)
        self.menu_dessert_3_2.clicked.connect(self.go_option)
        self.menu_dessert_3_3.clicked.connect(self.go_option)
        self.menu_dessert_3_4.clicked.connect(self.go_option)
        self.menu_packsccino_1_1.clicked.connect(self.go_option)
        self.menu_packsccino_1_2.clicked.connect(self.go_option)
        self.menu_packsccino_1_3.clicked.connect(self.go_option)
        self.menu_packsccino_1_4.clicked.connect(self.go_option)
        self.menu_packsccino_2_1.clicked.connect(self.go_option)
        self.menu_packsccino_2_2.clicked.connect(self.go_option)
        self.menu_packsccino_2_3.clicked.connect(self.go_option)
        self.menu_packsccino_2_4.clicked.connect(self.go_option)
        self.menu_packsccino_3_1.clicked.connect(self.go_option)
        self.menu_packsccino_3_2.clicked.connect(self.go_option)
        self.menu_packsccino_3_3.clicked.connect(self.go_option)
        self.menu_packsccino_3_4.clicked.connect(self.go_option)
        self.btn_plus.clicked.connect(self.cnt_plus)
        self.btn_minus.clicked.connect(self.cnt_minus)
        self.btn_del.clicked.connect(self.menu_del)
        self.cart_clear.clicked.connect(self.fnc_cart_clear)

        self.btn_submit.clicked.connect(self.go_payment)
        self.btn_mem_go.clicked.connect(lambda : self.memWidget.setCurrentIndex(1))
        self.btn_mem_0.clicked.connect(self.membership_input)
        self.btn_mem_1.clicked.connect(self.membership_input)
        self.btn_mem_2.clicked.connect(self.membership_input)
        self.btn_mem_3.clicked.connect(self.membership_input)
        self.btn_mem_4.clicked.connect(self.membership_input)
        self.btn_mem_5.clicked.connect(self.membership_input)
        self.btn_mem_6.clicked.connect(self.membership_input)
        self.btn_mem_7.clicked.connect(self.membership_input)
        self.btn_mem_8.clicked.connect(self.membership_input)
        self.btn_mem_9.clicked.connect(self.membership_input)
        self.btn_del_all.clicked.connect(self.membership_input)
        self.btn_del_one.clicked.connect(self.membership_input)
        self.btn_back.clicked.connect(lambda : self.memWidget.setCurrentIndex(0))
        self.btn_mem_ok.clicked.connect(lambda : self.go_payment2("mem"))
        self.btn_mem_pass.clicked.connect(lambda: self.go_payment2("pass"))
        self.btn_admin.clicked.connect(lambda : self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["admin"]))

        self.btn_back2.clicked.connect(lambda : self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["menu"]))
        self.btn_del_menu_all.clicked.connect(self.go_home)

        self.btn_pay_card.mousePressEvent = self.fnc_pay
        self.btn_pay_coupon.mousePressEvent = self.fnc_pay
        self.btn_pay_kakao.mousePressEvent = self.fnc_pay
        self.btn_pay_payco.mousePressEvent = self.fnc_pay


    def go_option(self):
        self.subWidget.setCurrentIndex(SUB_PAGE_INDEX["option"])
        add_info = self.sender().objectName().split('_')

        cart = dict()
        cart["category"] = add_info[1]
        cart["seq_col"] = add_info[2]
        cart["seq_row"] = add_info[3]

        # 메뉴명/가격 가져오기
        with open("menu.json", "r") as f:
            menu_list = json.load(f)

        for menu in menu_list:
            if cart["category"] == menu["category"] and cart["seq_col"] == menu["seq_col"] and cart["seq_row"] == menu[
                "seq_row"]:
                cart["name"] = menu["name"]
                cart["price"] = menu["price"]




    def go_payment2(self, gubun):
        mem_tel = len(self.mem_tel.text())
        if gubun == "mem" and mem_tel < 17:
            QMessageBox.information(self, "알림", "핸드폰번호를 확인해 주세요")
        else:
            self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["payment2"])
            self.print_cart_list2()


    def print_cart_list2(self):
        # list view에 담기
        total = 0
        self.cart_list2.clear()
        for c in carts:
            total = total + (int(c["price"]) * c["cnt"])
            total_price = str(int(c["price"]) * c["cnt"])
            if int(total_price) > 0 :
                print(len(c["name"].encode('utf-8')))
                if len(c["name"].encode('utf-8')) <= 22:
                    item_str = c["name"] + "\t\t\t" + str(c["cnt"]) + "개\t" + total_price + "원"
                else:
                    item_str = c["name"] + "  \t\t" + str(c["cnt"]) + "개\t" + total_price + "원"
                self.cart_list2.addItem(item_str)

        self.total_price2.setText(str(total))


    def fnc_pay(self, event):
        self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["payment3"])
        global cnt
        cnt = 5

        self.timeVar = QTimer()
        self.timeVar.setInterval(1000)
        self.timeVar.timeout.connect(self.fnc_count)
        self.timeVar.start()

    def fnc_count(self):
        global cnt
        cnt -= 1
        self.time_text.setText(str(cnt))
        if cnt == 0:
            self.timeVar.stop()
            self.fnc_result()


    def fnc_result(self):
        self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["payment4"])
        self.timeVar = QTimer()
        self.timeVar.setInterval(3000)
        self.timeVar.start()
        self.timeVar.timeout.connect(self.go_home)

    def membership_input(self):
        num = self.sender().objectName().split('_')[2]
        mem_tel = self.mem_tel.text()
        try:
            int(num)
            if len(mem_tel) < 6:
                mem_tel = '010 - '
            elif len(mem_tel) == 10:
                mem_tel += " - "
            mem_tel += num
        except:
            if num == 'all':
                mem_tel = '010 - '
            else:
                mem_tel = mem_tel[:len(mem_tel)-1]
                if len(mem_tel) == 13:
                    mem_tel = mem_tel[:10]
        if len(mem_tel) <= 17:
            self.mem_tel.setText(mem_tel)

    def fnc_cart_clear(self):
        global carts
        carts = list()
        self.cart_list.clear()
        self.total_price.setText("0")

    def cnt_plus(self):
        sel_index = self.cart_list.currentRow()
        if sel_index > -1:
            carts[sel_index]["cnt"] = carts[sel_index]["cnt"] + 1
            self.print_cart_list()
        else:
            QMessageBox.information(self, "알림", "음료를 선택해주세요")

    def cnt_minus(self):
        sel_index = self.cart_list.currentRow()
        if sel_index > -1:
            carts[sel_index]["cnt"] = carts[sel_index]["cnt"] - 1
            self.print_cart_list()
        else:
            QMessageBox.information(self, "알림", "음료를 선택해주세요")

    def menu_del(self):
        sel_index = self.cart_list.currentRow()
        if sel_index > -1:
            del carts[sel_index]
            self.print_cart_list()
        else:
            QMessageBox.information(self, "알림", "음료를 선택해주세요")

    def go_home(self):
        self.timeVar = QTimer()
        self.timeVar.setInterval(100)
        self.timeVar.stop()

        self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["main"])
        self.subWidget.setCurrentIndex(SUB_PAGE_INDEX["coffee"])
        global carts
        carts = list()
        self.cart_list.clear()
        self.total_price.setText("0")

    def go_payment(self):
        total = int(self.total_price.text())
        if total > 0:
            self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["payment"])
            self.memWidget.setCurrentIndex(0)
        else:
            QMessageBox.information(self, "알림", "장바구니가 비었습니다")


    def add_cart(self, cart):
        global carts

        # carts에 담기
        # cart에 하나라도 있으면 체크
        if len(carts) > 0:
            incart = False
            carts_index = -1
            for i in range(len(carts)):
                # carts에 있으면
                if cart["category"] == carts[i]["category"] and cart["seq_col"] == carts[i]["seq_col"] and cart["seq_row"] == carts[i]["seq_row"]:
                    # 카트에 있는지 여부 T
                    incart = True
                    # 해당 메뉴 index
                    carts_index = i
                    break

            # carts에 있음
            if incart:
                carts[carts_index]["cnt"] = carts[carts_index]["cnt"] + 1
            # carts에 없음
            else:
                # 새로운 항목으로 넣기
                cart["cnt"] = 1
                carts.append(cart)
        # cart에 아무것도 없으면
        else:
            cart["cnt"] = 1
            carts.append(cart)

        self.print_cart_list()


    def print_cart_list(self):
        # list view에 담기
        total = 0
        self.cart_list.clear()
        for c in carts:
            total = total + (int(c["price"]) * c["cnt"])
            total_price = str(int(c["price"]) * c["cnt"])
            if int(total_price) > 0 :
                if len(c["name"].encode('utf-8')) <= 16:
                    item_str = c["name"] + "\t\t    " + str(c["cnt"]) + "개\t" + total_price + "원"
                elif len(c["name"].encode('utf-8')) >= 33:
                    item_str = c["name"] + " " + str(c["cnt"]) + "개\t" + total_price + "원"
                else:
                    item_str = c["name"] + "\t    " + str(c["cnt"]) + "개\t" + total_price + "원"
                self.cart_list.addItem(item_str)

        self.total_price.setText(str(total))

    def instore_menu(self):
        self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["menu"])
        QMessageBox.information(self, "확인", "매장에서는 일회용컵 사용이 불가합니다")
        page_gubun = "instore"

    def pickup_menu(self):
        self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["menu"])
        page_gubun = "pickup"



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()