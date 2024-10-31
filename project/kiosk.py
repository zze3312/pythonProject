import sys
import json
import datetime

from PyQt5.QtCore import *
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
    "pay_fin_nomem" : 5,
    "pay_fin_mem" : 6,
    "admin" : 7
}
SUB_PAGE_INDEX = {
    "coffee" : 0,
    "noncoffee" : 1,
    "dessert" : 2,
    "packsccino" : 3,
    "option" : 4
}
ADMIN_PAGE_INDEX = {
    "sales" : 0,
    "member" : 1,
    "pwd_change" : 2
}

page_gubun = ""
# 장바구니 전체 list
carts = list()
# 선택한 하나의 메뉴
cart = dict()
membership_yn = False
membership_tel = ""
membership_total_cnt = 0
membership_new_cnt = 0

order_cnt = 0

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()

        self.setupUi(self)
        self.go_home()
        self.btn_pick_up.clicked.connect(self.pickup_menu)
        self.btn_in_store.clicked.connect(self.instore_menu)
        self.btn_home.clicked.connect(self.go_home)

        # 카테고리 버튼
        self.btn_coffee.clicked.connect(lambda: self.go_category("coffee"))
        self.btn_noncoffee.clicked.connect(lambda: self.go_category("noncoffee"))
        self.btn_dessert.clicked.connect(lambda: self.go_category("dessert"))
        self.btn_packsccino.clicked.connect(lambda: self.go_category("packsccino"))

        # 메뉴별 버튼
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

        # 메뉴창 하단 버튼
        self.btn_plus.clicked.connect(self.cnt_plus)
        self.btn_minus.clicked.connect(self.cnt_minus)
        self.btn_del.clicked.connect(self.menu_del)
        self.cart_clear.clicked.connect(self.fnc_cart_clear)

        # 옵션 버튼
        self.cart_menu_plus.clicked.connect(lambda: self.fnc_option_cnt("menu","plus"))
        self.cart_menu_minus.clicked.connect(lambda: self.fnc_option_cnt("menu","minus"))
        self.shot_plus.clicked.connect(lambda: self.fnc_option_cnt("shot","plus"))
        self.shot_minus.clicked.connect(lambda: self.fnc_option_cnt("shot","minus"))
        self.syrup_plus.clicked.connect(lambda: self.fnc_option_cnt("syrup", "plus"))
        self.syrup_minus.clicked.connect(lambda: self.fnc_option_cnt("syrup", "minus"))
        self.milk_plus.clicked.connect(lambda: self.fnc_option_cnt("milk", "plus"))
        self.milk_minus.clicked.connect(lambda: self.fnc_option_cnt("milk", "minus"))
        self.pearl_plus.clicked.connect(lambda: self.fnc_option_cnt("pearl", "plus"))
        self.pearl_minus.clicked.connect(lambda: self.fnc_option_cnt("pearl", "minus"))

        # 장바구니 담기/취소
        self.btn_option_ok.clicked.connect(self.add_cart)
        self.btn_option_del.clicked.connect(lambda: self.go_category("coffee"))

        # 멤버쉽
        self.btn_submit.clicked.connect(self.go_payment)
        self.btn_mem_go.clicked.connect(self.go_membership)
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
        self.btn_back.clicked.connect(lambda: self.memWidget.setCurrentIndex(0))
        self.btn_mem_ok.clicked.connect(lambda: self.go_payment2("mem"))
        self.btn_mem_pass.clicked.connect(lambda: self.go_payment2("pass"))

        # 관리자
        self.btn_admin.clicked.connect(self.go_admin_sub)
        self.btn_admin_login_close.clicked.connect(lambda: self.admin_login_popup.setHidden(True))
        self.btn_admin_login.clicked.connect(self.admin_login)

        self.btn_sales.clicked.connect(lambda: self.go_admin("sales"))
        self.btn_mem.clicked.connect(lambda: self.go_admin("member"))
        self.btn_pwd.clicked.connect(lambda: self.go_admin("pwd_change"))
        self.btn_update_pwd.clicked.connect(self.update_admin_pwd)

        # 결제
        self.btn_back2.clicked.connect(lambda: self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["menu"]))
        self.btn_del_menu_all.clicked.connect(self.go_home)

        self.btn_pay_card.mousePressEvent = self.fnc_pay
        self.btn_pay_coupon.mousePressEvent = self.fnc_pay
        self.btn_pay_kakao.mousePressEvent = self.fnc_pay
        self.btn_pay_payco.mousePressEvent = self.fnc_pay


    def sales_table_view(self):
        self.sales_table.setColumnWidth(0, 268)
        self.sales_table.setColumnWidth(1, 100)
        self.sales_table.setColumnWidth(2, 100)
        self.sales_table.setColumnWidth(3, 100)

        self.sales_table.clear()
        self.sales_table.setHorizontalHeaderLabels(["메뉴명", "판매량", "판매 금액", "판매일"])


        with open("admin_sales.json", "r") as f:
            sales_list = json.load(f)

        with open("menu.json", "r") as f:
            menu_list = json.load(f)

        rowCnt = len(sales_list)
        self.sales_table.setRowCount(rowCnt)
        self.sales_table.setColumnCount(4)

        sales_list = sorted(sales_list, key=lambda x: (x['sales_date'], -int(x['seq_col']), -int(x['seq_row'])), reverse=True)

        for row in range(rowCnt):
            for menu in menu_list:
                if sales_list[row]["seq_col"] == menu["seq_col"] and sales_list[row]["seq_row"] == menu["seq_row"]:
                    menu_name = menu["name"]
                    break

            item = QTableWidgetItem(menu_name)
            item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.sales_table.setItem(row, 0, item)

            item = QTableWidgetItem(str(sales_list[row]["total_cnt"]))
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.sales_table.setItem(row, 1, item)

            item = QTableWidgetItem(str(sales_list[row]["total_price"]))
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.sales_table.setItem(row, 2, item)

            item = QTableWidgetItem(str(sales_list[row]["sales_date"]))
            item.setTextAlignment(Qt.AlignCenter)
            self.sales_table.setItem(row, 3, item)

    def member_table_view(self):
        self.member_table.setColumnWidth(0, 450)
        self.member_table.setColumnWidth(1, 105)

        self.member_table.clear()
        self.member_table.setHorizontalHeaderLabels(["핸드폰 번호", "스탬프"])

        with open("member.json", "r") as f:
            member_list = json.load(f)

        rowCnt = len(member_list)
        self.member_table.setRowCount(rowCnt)
        self.member_table.setColumnCount(2)

        for row in range(rowCnt):
            item = QTableWidgetItem(str(member_list[row]["tel"]))
            item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.member_table.setItem(row, 0, item)

            item = QTableWidgetItem(str(member_list[row]["stamp_cnt"]))
            item.setTextAlignment(Qt.AlignCenter)
            self.member_table.setItem(row, 1, item)

    def update_admin_pwd(self):
        input_now_pwd = self.input_admin_pwd_now.text()
        input_pwd = self.input_admin_pwd.text()
        input_pwd_chk = self.input_admin_pwd_chk.text()
        change_info = {}

        with open("admin_info.json", 'r') as f:
            now_info = json.load(f)

        change_json = list()

        if len(input_pwd) == 0 or len(input_pwd_chk) == 0 or len(input_now_pwd) == 0:
            QMessageBox.information(self, "알림", "입력을 확인해주세요")
        elif input_pwd != input_pwd_chk:
            QMessageBox.information(self, "알림", "변경할 비밀번호가 일치하지 않습니다")
        elif str(input_now_pwd) != str(now_info[0]["password"]):
            QMessageBox.information(self, "알림", "현재 사용중인 비밀번호가 일치하지 않습니다")
        else:
            change_info["id"] = now_info[0]["id"]
            change_info["password"] = input_pwd
            change_json.append(change_info)

            with open("admin_info.json", "w") as f:
                json.dump(change_json, f)

            QMessageBox.information(self, "알림", "비밀번호가 변경되었습니다. 다시 로그인 해주세요")

            self.input_admin_pwd_now.setText("")
            self.input_admin_pwd.setText("")
            self.input_admin_pwd_chk.setText("")
            self.go_home()
            self.btn_admin.setText("관리자")


    def go_admin(self, cate_name):
        self.admin_widget.setCurrentIndex(ADMIN_PAGE_INDEX[cate_name])
        if cate_name == "sales":
            self.sales_table_view()
        elif cate_name == "member":
            self.member_table_view()


    def admin_login(self):

            with open("admin_info.json", 'r') as f:
                admin_info = json.load(f)[0]

            input_pwd = self.input_user_pwd.text()

            if input_pwd != '':
                if input_pwd == admin_info["password"]:
                    self.admin_login_popup.setHidden(True)
                    self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["admin"])
                    self.go_admin("sales")
                    self.input_user_pwd.setText("")
                    self.btn_admin.setText("홈")
                else:
                    QMessageBox.warning(self, "알림", "비밀번호가 틀렸습니다")
                    self.input_user_pwd.setText("")
            else:
                QMessageBox.warning(self, "알림", "비밀번호를 입력해주세요")


    def go_admin_sub(self):
        admin_btn_gubun = self.btn_admin.text()
        if admin_btn_gubun == "관리자":
            self.admin_login_popup.setHidden(not self.admin_login_popup.isHidden())
        else:
            self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["main"])
            self.btn_admin.setText("관리자")

    def go_category(self, cate_name):
        global cart
        cart = dict()

        self.cart_menu_cnt.setText("1")
        self.shot_cnt.setText("0")
        self.syrup_cnt.setText("0")
        self.milk_cnt.setText("0")
        self.pearl_cnt.setText("0")
        self.subWidget.setCurrentIndex(SUB_PAGE_INDEX[cate_name])

    def fnc_option_cnt(self, option, inc_dec):
        global cart

        total_price = int(self.total_menu_price.text().replace(',',''))
        cart["total_price"] = total_price
        text_label = ""
        dict_key = option + "_cnt"

        if option == "menu":
            text_label = self.cart_menu_cnt
        elif option == "shot":
            text_label = self.shot_cnt
        elif option == "syrup":
            text_label = self.syrup_cnt
        elif option == "milk":
            text_label = self.milk_cnt
        elif option == "pearl":
            text_label = self.pearl_cnt

        cnt = int(text_label.text())
        if inc_dec == "minus":
            if option == "menu" and cnt == 1:
                QMessageBox.information(self, "알림", "최소 수량은 1개입니다")
            elif cnt == 0:
                QMessageBox.information(self, "알림", "최소 수량은 0개입니다")
            else:
                cnt -= 1
                if option == "menu":
                    cart["cnt"] -= 1
                else:
                    cart[dict_key] -= 1
        else:
            if option == "milk" and cnt == 1:
                QMessageBox.information(self, "알림", "최대 수량은 1개입니다")
            else:
                cnt += 1
                if option == "menu":
                    cart["cnt"] += 1
                else:
                    cart[dict_key] += 1

        total_price = (int(cart["price"]) + ((cart["shot_cnt"] + cart["syrup_cnt"] + cart["milk_cnt"]) * 500) + (cart["pearl_cnt"] * 1000)) * cart["cnt"]
        cart["total_price"] = total_price
        self.total_menu_price.setText(str(format(total_price, ',')))
        text_label.setText(str(cnt))


    def go_option(self):
        self.subWidget.setCurrentIndex(SUB_PAGE_INDEX["option"])
        add_info = self.sender().objectName().split('_')
        global cart

        cart["category"] = add_info[1]
        cart["seq_col"] = add_info[2]
        cart["seq_row"] = add_info[3]
        cart["cnt"] = 1
        cart["shot_cnt"] = 0
        cart["syrup_cnt"] = 0
        cart["milk_cnt"] = 0
        cart["pearl_cnt"] = 0


        # 메뉴명/가격 가져오기
        with open("menu.json", "r") as f:
            menu_list = json.load(f)

        for menu in menu_list:
            if cart["category"] == menu["category"] and cart["seq_col"] == menu["seq_col"] and cart["seq_row"] == menu["seq_row"]:
                cart["name"] = menu["name"]
                cart["shot"] = menu["shot"]
                cart["syrup"] = menu["syrup"]
                cart["milk"] = menu["milk"]
                cart["pearl"] = menu["pearl"]
                cart["price"] = menu["price"]
                cart["total_price"] = int(menu["price"])

        # 각 메뉴별 옵션 선택 가능여부 체크
        if cart["shot"] == "Y":
            self.shot_plus.setDisabled(False)
            self.shot_minus.setDisabled(False)
        else:
            self.shot_plus.setDisabled(True)
            self.shot_minus.setDisabled(True)

        if cart["syrup"] == "Y":
            self.syrup_plus.setDisabled(False)
            self.syrup_minus.setDisabled(False)
        else:
            self.syrup_plus.setDisabled(True)
            self.syrup_minus.setDisabled(True)

        if cart["milk"] == "Y":
            self.milk_plus.setDisabled(False)
            self.milk_minus.setDisabled(False)
        else:
            self.milk_plus.setDisabled(True)
            self.milk_minus.setDisabled(True)

        if cart["pearl"] == "Y":
            self.pearl_plus.setDisabled(False)
            self.pearl_minus.setDisabled(False)
        else:
            self.pearl_plus.setDisabled(True)
            self.pearl_minus.setDisabled(True)

        self.cart_menu_name.setText(cart["name"])
        self.total_menu_price.setText(format(int(cart["price"]), ','))


    def go_payment2(self, gubun):
        mem_tel = len(self.mem_tel.text())

        global membership_tel, membership_yn
        membership_tel = ""
        if gubun == "mem" and mem_tel < 17:
            QMessageBox.information(self, "알림", "핸드폰번호를 확인해 주세요")
        else:
            if gubun == "mem":
                # 멤버쉽 정보 저장
                membership_yn = True
                membership_tel = self.mem_tel.text()
                self.mem_tel.setText("010 - ")

            self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["payment2"])
            # 최종 장바구니
            self.cart_list2.setColumnWidth(0, 177)
            self.cart_list2.setColumnWidth(1, 30)
            self.cart_list2.setColumnWidth(2, 30)
            self.cart_list2.setColumnWidth(3, 80)
            self.cart_list2.setColumnWidth(4, 30)
            self.cart_list2.setColumnWidth(5, 50)
            self.cart_list2.setColumnWidth(6, 100)

            self.print_cart_list2()



    def print_cart_list2(self):
        # table widget에 담기
        total = 0
        rowCnt = len(carts)
        colCnt = 7

        # 총 행과 열 개수 지정
        self.cart_list2.setRowCount(rowCnt)
        self.cart_list2.setColumnCount(colCnt)

        # 재접속시 기존에 있던 내용을 clear
        self.cart_list2.clear()
        # clear()이후 헤더 부분이 사라지는 현상이 있어 헤더를 추가해주는 부분 추가
        self.cart_list2.setHorizontalHeaderLabels(["메뉴명", "샷", "시럽", "두유로 변경", "펄", "개수", "금액"])

        # setTextAlignment : table widget 데이터 정렬을 해주는 함수, 해당 값은 | 로 연결해서 여러개 넣을 수 있음 (맨 아래 3줄처럼)
        # - Qt.AlignCenter : 가운데정렬
        # - Qt.AlignVCenter : 세로정렬
        # - Qt.AlignHCenter : 가로정렬
        # - Qt.AlignRight : 오른쪽정렬
        # - Qt.AlignLeft : 왼쪽정렬
        # - Qt.AlignTop : 위쪽정렬
        # - Qt.AlignBottom : 아래쪽 정렬
        # - Qt.AlignTop | Qt.AlignRight : 위, 오른쪽 정렬
        # - Qt.AlignBottom | Qt.AlignLeft : 아래 왼쪽 정렬
        # - Qt.AlignBottom | Qt.AlignRight : 아래 오른쪽 정렬

        # 장바구니에 담긴 메뉴 수 만큼 반복
        for row in range(rowCnt):
            item = QTableWidgetItem(carts[row]["name"])
            item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.cart_list2.setItem(row, 0, item)

            item = QTableWidgetItem(str(carts[row]["shot_cnt"]))
            item.setTextAlignment(Qt.AlignCenter)
            self.cart_list2.setItem(row, 1, item)

            item = QTableWidgetItem(str(carts[row]["syrup_cnt"]))
            item.setTextAlignment(Qt.AlignCenter)
            self.cart_list2.setItem(row, 2, item)

            item = QTableWidgetItem(str(carts[row]["milk_cnt"]))
            item.setTextAlignment(Qt.AlignCenter)
            self.cart_list2.setItem(row, 3, item)

            item = QTableWidgetItem(str(carts[row]["pearl_cnt"]))
            item.setTextAlignment(Qt.AlignCenter)
            self.cart_list2.setItem(row, 4, item)

            item = QTableWidgetItem(str(carts[row]["cnt"]))
            item.setTextAlignment(Qt.AlignCenter)
            self.cart_list2.setItem(row, 5, item)

            item = QTableWidgetItem(str(format(carts[row]["total_price"], ',')))
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.cart_list2.setItem(row, 6, item)

            total += carts[row]["total_price"]

        self.total_price2.setText(str(format(total, ',')))


    def fnc_pay(self, event):
        self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["payment3"])

        global carts, order_cnt, cnt, membership_total_cnt, membership_new_cnt
        total_cnt = 0

        # 관리자 매출에 등록
        with open("admin_sales.json", "r") as fr:
            sales_list = json.load(fr)
        now = datetime.datetime.now()

        for i in range(len(carts)):
            input_sales = dict()
            input_sales["category"] = carts[i]["category"]
            input_sales["seq_col"] = carts[i]["seq_col"]
            input_sales["seq_row"] = carts[i]["seq_row"]
            input_sales["total_cnt"] = carts[i]["cnt"]
            input_sales["total_price"] = carts[i]["total_price"]
            input_sales["sales_date"] = now.strftime("%Y-%m-%d")
            total_cnt += carts[i]["cnt"]
            sales_add = True
            if len(sales_list) > 0:
                for j in range(len(sales_list)):

                    if input_sales["category"] == sales_list[j]["category"] and int(input_sales["seq_col"]) == int(sales_list[j]["seq_col"]) and int(input_sales["seq_row"]) == int(sales_list[j]["seq_row"]) and input_sales["sales_date"] ==  sales_list[j]["sales_date"]:
                        sales_list[j]["total_cnt"] += input_sales["total_cnt"]
                        sales_list[j]["total_price"] += input_sales["total_price"]
                        sales_add = False
                        break

            if sales_add:
                sales_list.append(input_sales)

        with open("admin_sales.json", "w") as fw:
            json.dump(sales_list, fw)

        order_cnt += 1
        self.label_order_cnt.setText(str(order_cnt))

        # 스탬프 추가
        if membership_yn :
            with open("member.json", "r") as fr2:
                member_list = json.load(fr2)

            stamp_ok = False
            mem_info = {"tel": membership_tel, "stamp_cnt": total_cnt}
            membership_new_cnt = mem_info["stamp_cnt"]
            if len(member_list) > 0:
                for member in member_list:
                    if membership_tel == member["tel"]:
                        member["stamp_cnt"] += total_cnt
                        membership_total_cnt = member["stamp_cnt"]
                        stamp_ok = True

            if not stamp_ok:
                member_list.append(mem_info)
                membership_total_cnt = mem_info["stamp_cnt"]

            with open("member.json", "w") as fw2:
                json.dump(member_list, fw2)

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
            self.time_text.setText("5")


    def fnc_result(self):
        global membership_yn
        if membership_yn :
            self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["pay_fin_mem"])

            self.total_stamp_cnt.setText(str(membership_total_cnt))
            self.new_stamp_cnt.setText(str(membership_new_cnt))

            self.timeVar = QTimer()
            self.timeVar.setInterval(3000)
            self.timeVar.start()
            membership_yn = False
            self.timeVar.timeout.connect(self.fnc_result)
        else:
            self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["pay_fin_nomem"])
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
                if len(mem_tel) > 6:
                    mem_tel = mem_tel[:len(mem_tel)-1]
                    if len(mem_tel) == 13:
                        mem_tel = mem_tel[:10]
        if len(mem_tel) <= 17:
            self.mem_tel.setText(mem_tel)

    def go_membership(self):
        self.memWidget.setCurrentIndex(1)
        self.mem_tel.setText("010 - ")

    def fnc_cart_clear(self):
        global carts
        carts = list()
        self.cart_list.clear()
        self.total_price.setText("0")

    def cnt_plus(self):
        sel_index = self.cart_list.currentRow()
        if sel_index > -1:
            carts[sel_index]["cnt"] = carts[sel_index]["cnt"] + 1
            total_price = (int(carts[sel_index]["price"]) + ((carts[sel_index]["shot_cnt"] + carts[sel_index]["syrup_cnt"] + carts[sel_index]["milk_cnt"]) * 500) + (carts[sel_index]["pearl_cnt"] * 1000)) * carts[sel_index]["cnt"]
            carts[sel_index]["total_price"] = total_price
            self.print_cart_list()
        else:
            QMessageBox.information(self, "알림", "음료를 선택해주세요")

    def cnt_minus(self):
        sel_index = self.cart_list.currentRow()
        if sel_index > -1:
            carts[sel_index]["cnt"] = carts[sel_index]["cnt"] - 1
            if carts[sel_index]["cnt"] > 0:
                total_price = (int(carts[sel_index]["price"]) + ((carts[sel_index]["shot_cnt"] + carts[sel_index]["syrup_cnt"] + carts[sel_index]["milk_cnt"]) * 500) + ( carts[sel_index]["pearl_cnt"] * 1000)) * carts[sel_index]["cnt"]
                carts[sel_index]["total_price"] = total_price
            else:
                del carts[sel_index]
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
        self.admin_login_popup.setHidden(True)
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
        total = int(self.total_price.text().replace(',', ''))
        if total > 0:
            self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["payment"])
            self.memWidget.setCurrentIndex(0)
        else:
            QMessageBox.information(self, "알림", "장바구니가 비었습니다")


    def add_cart(self):
        global carts, cart

        # carts에 담기
        # cart에 하나라도 있으면 체크
        if len(carts) > 0:
            incart = False
            carts_index = -1
            for i in range(len(carts)):
                # carts에 있으면
                if cart["category"] == carts[i]["category"] and cart["seq_col"] == carts[i]["seq_col"] and cart["seq_row"] == carts[i]["seq_row"]\
                        and cart["shot_cnt"] == carts[i]["shot_cnt"] and cart["syrup_cnt"] == carts[i]["syrup_cnt"] and cart["milk_cnt"] == carts[i]["milk_cnt"] and cart["pearl_cnt"] == carts[i]["pearl_cnt"]:
                    # 카트에 있는지 여부 T
                    incart = True
                    # 해당 메뉴 index
                    carts_index = i
                    break

            # carts에 있음
            if incart:
                carts[carts_index]["cnt"] = carts[carts_index]["cnt"] + cart["cnt"]
            # carts에 없음
            else:
                # 새로운 항목으로 넣기
                carts.append(cart)
        # cart에 아무것도 없으면
        else:
            carts.append(cart)

        self.print_cart_list()
        self.go_category("coffee")


    def print_cart_list(self):
        # list view에 담기
        global  carts

        total = 0
        self.cart_list.clear()
        if len(carts) > 0:
            for c in carts:
                total = total + c["total_price"]
                total_price = str(c["total_price"])
                if int(total_price) > 0 :
                    if len(c["name"].encode('utf-8')) <= 16:
                        item_str = c["name"] + "\t\t    " + str(c["cnt"]) + "개\t" + str(format(int(total_price), ',')) + "원"
                    elif len(c["name"].encode('utf-8')) >= 33:
                        item_str = c["name"] + " " + str(c["cnt"]) + "개\t" + str(format(int(total_price), ',')) + "원"
                    else:
                        item_str = c["name"] + "\t    " + str(c["cnt"]) + "개\t" + str(format(int(total_price), ',')) + "원"
                    self.cart_list.addItem(item_str)

        self.total_price.setText(str(format(total, ',')))

    def instore_menu(self):
        self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["menu"])
        QMessageBox.information(self, "확인", "매장에서는 일회용컵 사용이 불가합니다")
        self.page_gubun = "instore"

    def pickup_menu(self):
        self.mainWidget.setCurrentIndex(MAIN_PAGE_INDEX["menu"])
        self.page_gubun = "pickup"



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()