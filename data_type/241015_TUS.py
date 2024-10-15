num = int(input("숫자입력 : "))
if num == 0:
    print("입력한 숫자는 0")
elif num > 0 :
    print("입력한 숫자는 양수")
else:
    print("입력한 숫자는 음수")

num = int(input("숫자입력 : "))
if num % 2 == 0:
    print("짝수")
else :
    print("홀수")

num = int(input("숫자입력 : "))
if num % 3 == 0:
    print("3의 배수")
else:
    print("3의 배수 아님")

num = int(input("숫자입력 : "))
if num % 3 == 0 and num % 5 == 0:
    print("3과 5의 배수")
else:
    print("3과 5의 배수 아님")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket :
    print("택시를 타고 가라")
else :
    if card :
        print("택시를 타고 가라")
    else :
        print("걸어가라")

# 위와 같이 다양한 조건을 판단해야 할 경우 elif를 사용하여 표현가능
if 'money' in pocket :  # pocket에 money가 있으면
    print("택시를 타고 가라")
elif card :
    print("택시를 타고 가라") # pocket에 money는 없지만 card가 있으면
else :
    print("걸어가라") # pocket에 money도 없고 card도 없으면


a = int(input("a를 입력해주세요 > "))
b = int(input("b를 입력해주세요 > "))
c = int(input("c를 입력해주세요 > "))

# 가장 큰 수 찾기
if a > b :
    if a > c :
        print(f"a 숫자 {a}이 가장 큽니다.")
    else :
        print(f"c 숫자 {c}이 가장 큽니다.")
elif b > c :
    print(f"b 숫자 {b}이 가장 큽니다.")
else :
    print(f"c 숫자 {c}이 가장 큽니다.")

# 가장 작은 수 찾기
if a < b and a < c :
    print(f"a 숫자 {a}이 가장 작습니다.")
elif b > a > c:
    print(f"c 숫자 {c}이 가장 작습니다.")
elif b < c :
    print(f"b 숫자 {b}이 가장 작습니다.")
else :
    print(f"c 숫자 {c}이 가장 작습니다.")

# 사용자에게 중국집 메뉴를 입력받음
# 사용자가 입력한 중국집 메뉴를 주문받는다
menu = input("메뉴를 입력하세요 > ")
price = int(input("돈을 지불해주세요 > "))

if menu == "짜장면" and price >= 5000 :
    print("짜장면 하나요")
    print(f"거스름돈 {price - 5000}원 입니다")
elif menu == "짬뽕" and price >= 5500 :
    print("짬뽕 하나요")
    print(f"거스름돈 {price - 5500}원 입니다")
elif menu == "볶음밥" and price >= 6000 :
    print("볶음밥 하나요")
    print(f"거스름돈 {price - 6000}원 입니다")
else :
    print("죄송합니다. 없는 메뉴이거나 돈이 부족합니다.")

menu_list = {'짜장면' : 5000, '짬뽕' : 5500, '볶음밥' : 6000}
if menu in menu_list.keys() :
    if price >= menu_list[menu] :
        print(f"{menu} 하나요")
        print(f"거스름돈 {price - menu_list[menu]}원 입니다.")
    else :
        print("죄송합니다. 돈이 부족합니다")
else :
    print("죄송합니다. 없는 메뉴입니다")

# 예제 11_1
com = '보'
user_input = input("사용자 가위, 바위, 보 중 하나를 입력하세요 : ")
input_test = ['가위', '바위', '보']

if user_input in input_test :
    if user_input == com :
        print("비겼습니다")
    elif user_input == "가위" :
        print("이겼습니다")
    elif user_input == "바위" :
        print("졌습니다")
else :
    print("가위, 바위, 보 중 하나를 입력해야 합니다.")

# 예제 11_2
com = input("com 가위, 바위, 보 중 하나를 입력하세요 : ")
user_input = input("사용자 가위, 바위, 보 중 하나를 입력하세요 : ")
if user_input in input_test and com in input_test:
    if user_input == com :
        print("비겼습니다")
    elif ( user_input == '가위' and com == '바위' ) or ( user_input == '바위' and com == '보' ) or ( user_input == '보' and com == '가위' ) :
        print("졌습니다")
    elif ( user_input == '가위' and com == '보' ) or ( user_input == '바위' and com == '가위' ) or ( user_input == '보' and com == '바위' ) :
        print("이겼습니다")
else :
    print("가위, 바위, 보 중 하나를 입력해야 합니다.")


# 예제 12
user_age = int(input("나이를 입력하세요 : "))
if user_age < 8 :
    print("요금은 0원 입니다")
elif user_age < 60 :
    print("요금은 5,000원 입니다")
else :
    print("요금은 2,500원 입니다")

# 예제 13
user_age = int(input("나이를 입력하세요 : "))
if user_age < 8 :
    print("요금은 0원 입니다")
elif user_age < 60 :
    print("요금은 5,000원 입니다")
else :
    print("요금은 0원 입니다")

# 예제 14
user_grade = dict()
user_grade["kor"] = int(input("국어점수를 입력해 주세요 : "))
user_grade["eng"] = int(input("영어점수를 입력해 주세요 : "))
user_grade["mat"] = int(input("수학점수를 입력해 주세요 : "))

user_sum = user_grade["kor"] + user_grade["eng"] + user_grade["mat"]
subject_cnt = len(list(user_grade.keys()))
user_avg = user_sum / subject_cnt

user_sum2 = 0
for i in list(user_grade.keys()) :
    user_sum2 = user_sum2 + int(user_grade[i])
user_avg2 = user_sum2 / subject_cnt
print(user_avg2)

if user_avg >= 90 :
    print("a 학생의 등급은 A 입니다")
elif user_avg >= 80 :
    print("a 학생의 등급은 B 입니다")
elif user_avg >= 70 :
    print("a 학생의 등급은 C 입니다")
elif user_avg >= 60 :
    print("a 학생의 등급은 D 입니다")
else :
    print("a 학생의 등급은 F 입니다")


# 자판기 만들기_김지현
menu_list = {
    "1" : "코카콜라_1200",
    "2" : "칠성사이다_800",
    "3" : "데자와_700",
    "4" : "솔의눈_700",
    "5" : "환타_900"
}

print("="*30)
print("{0:^30}".format("메뉴"))
print("="*30)
print(f'{"주문번호":<8}{"메뉴":<12}{"가격":<10}')
for i in list(menu_list.keys()) :
    menu_nm = menu_list[i].split("_")[0]
    menu_price = menu_list[i].split("_")[1]

    print(f"{i:<10}{menu_nm:<12}{menu_price:<10}")

print("="*30)
user_sel = input("주문하실 메뉴의 주문번호를 입력하세요 > ")

if user_sel in list(menu_list.keys()) :
    menu_nm = menu_list[user_sel].split("_")[0]
    menu_price = menu_list[user_sel].split("_")[1]
    print(f"주문하신 메뉴는 {menu_nm}, 가격은 {menu_price}입니다\n")

    user_sel_cnt = int(input("주문하실 개수를 입력해주세요 > "))
    total_price = user_sel_cnt * int(menu_price)
    print(f"총 {total_price}원 입니다.\n")

    user_payment = int(input("지불하실 금액을 입력해주세요 > "))
    if user_payment >= total_price :
        result_price = user_payment - total_price
        print(f"주문하신 메뉴{menu_nm} {user_sel_cnt}개, {user_payment}원 지불하셨고 거스름돈은 {result_price}입니다\n")
    else :
        print("지불하신 금액이 부족합니다 금액을 확인해주세요\n")
else :
    print("주문번호가 잘못되었습니다.")


menu_list2 = (
    "코카콜라_1200",
    "칠성사이다_800",
    "데자와_700",
    "솔의눈_700",
    "환타_900"
)

print("="*30)
print("{0:^30}".format("메뉴"))
print("="*30)
print(f'{"주문번호":<8}{"메뉴":<12}{"가격":<10}')
for i in (0, 1, 2, 3, 4) :
    menu_nm = menu_list2[i].split("_")[0]
    menu_price = menu_list2[i].split("_")[1]

    print(f"{i + 1:<10}{menu_nm:<12}{menu_price:<10}")

print("="*30)

user_sel = int(input("주문하실 메뉴의 주문번호를 입력하세요 > "))

if user_sel in (1, 2, 3, 4, 5) :
    menu_nm = menu_list2[user_sel - 1].split("_")[0]
    menu_price = menu_list2[user_sel - 1].split("_")[1]
    print(f"주문하신 메뉴는 {menu_nm}, 가격은 {menu_price}입니다\n")

    user_sel_cnt = int(input("주문하실 개수를 입력해주세요 > "))
    total_price = user_sel_cnt * int(menu_price)
    print(f"총 {total_price}원 입니다.\n")

    user_payment = int(input("지불하실 금액을 입력해주세요 > "))
    if user_payment >= total_price :
        result_price = user_payment - total_price
        print(f"주문하신 메뉴{menu_nm} {user_sel_cnt}개, {user_payment}원 지불하셨고 거스름돈은 {result_price}입니다\n")
    else :
        print("지불하신 금액이 부족합니다 금액을 확인해주세요\n")
else :
    print("주문번호가 잘못되었습니다.")
