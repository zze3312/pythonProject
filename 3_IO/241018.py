# 함수 : 기능단위의 소스 묶음
#  - def 함수이름(매개변수) :
#         수행할 문장
#         수행할 문장
#         수행할 문장
#         ...
# 매개변수(parameter) : 함수에서 정의할때
# 인수(argument) : 함수호출 시
#
# 함수 호출 : 리턴받을변수 = 함수명(인수)
# 매개변수 없는 함수 : def 함수명 () :


def add(a, b) :
    return a + b

num1 = 10
num2 = 20

result = add(num1, num2)
print(result)

# 날짜관련 함수
import datetime
day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 4, 5)

diff = day2 - day1
print(diff.days)

day = datetime.date(2024, 10, 18)
print(day.weekday()) # 월요일 0부터 시작
print(day.isoweekday()) # 월요일 1부터 시작

# 시간관련 함수
import time
print(time.time())

# 년, 월, 일, 시간, 요일 등의 날짜 정보 출력
localtime = time.localtime(time.time())
print(localtime)

# 보기 편하게 바꾸는 기능
print(time.asctime(localtime))
print(time.ctime())

# 시간형식을 문자열로 변환
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))

# delay를 주는 함수 : sleep
for i in range(10) :
    print(i)
    #time.sleep(1)

# 임의의 숫자를 발생시키는 함수
import random
print(random.random())

def random_pop(data) :
    number = random.randint(0, len(data) - 1)
    return data.pop(number)

data = [1, 2, 3, 4, 5]
while data :
    print(random_pop(data))

i = 0
while i < 6:
    number = random.randint(1, 45)
    print(number)
    i += 1

# 중복제거
lottoList = []
i = 0
while i < 6:
    number = random.randint(1, 45)
    if number in lottoList :
        continue
    lottoList.append(number)
    i += 1
print(lottoList)

number = random.randint(1, 10)
userNumber = int(input("1-10 숫자를 입력해주세요 : "))
if number > userNumber :
    print(f"컴퓨터 : {number} / 사용자 : {userNumber} 컴퓨터의 숫자가 더 큽니다")
elif number < userNumber:
    print(f"컴퓨터 : {number} / 사용자 : {userNumber} 사용자의 숫자가 더 큽니다")
else :
    print(f"컴퓨터 : {number} / 사용자 : {userNumber} 사용자와 컴퓨터의 숫자가 같습니다")

# 야구게임
import random

def num_chk(num) :
    chk_yn = True
    if len(num) != 4 :
        print("입력하신 숫자가 4개를 넘거나 부족합니다. 다시 입력해 주세요")
        return False

    for c in num :
        if c == '0' :
            print("0이 있습니다. 다시입력해주세요")
            chk_yn = False
            break
        elif num.count(c) > 1 :
            print("입력하신 숫자에 중복이 있습니다. 다시 입력해 주세요")
            chk_yn = False
            break
        try :
            idx = int(c)
        except :
            print("숫자가 아닌 문자가 있습니다 다시 입력해 주세요")
            chk_yn = False
            break

    return chk_yn

def game(comnum, usernum) :
    strike_cnt = 0
    ball_cnt = 0

    for c_idx in range(4):
        for u_idx in range(4):
            if comnum[c_idx] == int(usernum[u_idx]):
                if c_idx == u_idx:
                    strike_cnt += 1
                else:
                    ball_cnt += 1
    if strike_cnt == 0 and ball_cnt == 0:
        print("결과 : 아웃")
    else:
        print(f"결과 : [{strike_cnt}] 스트라이크 / [{ball_cnt}] 볼")
    return strike_cnt

com_number = []
i = 0
while i < 4 :
    random_num = random.randint(1, 9)
    if random_num in com_number :
        continue
    com_number.append(random_num)
    i += 1

count = 0
print("숫자야구를 시작합니다.")
print("-" * 30)

while True:
    user_number = input("1 - 9까지의 숫자 4자리를 입력하세요 : ")
    count += 1
    if num_chk(user_number) :
        strk_cnt = game(com_number, user_number)
        if strk_cnt == 4 :
            print("-" * 30)
            print("축하합니다. 정답입니다!")
            print(f"[{count}]번 만에 맞췄습니다")
            break
    else :
        continue


#금붕어
from random import random, randint

MAX_GOLD_FISH = 10000
now_gf = 1 #현재 금붕어 쌍
#gf_name1 = input("금붕어의 애칭을 지어주세요 : ")
#gf_name2 = input("금붕어 짝꿍의 애칭을 지어주세요 : ")
turn_cnt = 0

while True :
    turn_cnt += 1
    die_gf = 0
    new_gf = 0

    if turn_cnt > 1 :
        for gf in range(now_gf):
            new_gf += randint(1, 5)  # 새로태어난 금붕어 쌍
        die_gf = randint(1, 5) # 2회턴부터 죽는 금붕어 쌍

    total_gf = (now_gf + new_gf - die_gf) * 2

    if total_gf > 0 :
        now_gf = total_gf
        print(f"{turn_cnt}회차 현재 금붕어 수 {total_gf}마리 입니다")

        if total_gf > MAX_GOLD_FISH :
            print(f"{turn_cnt}회차 만에 어항이 터졌습니다")
            break
    else :
        print(f"{turn_cnt}회차 만에 다 죽었습니다")
        break