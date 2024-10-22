import sys

# 파일 읽기 함수
#  - read() : 파일 내용을 문자열로 받음
#  - readline() : 파일 내용의 한줄을 읽어옴
#  - readlines() : 파일 내용의 전체를 줄단위로 잘라서 리스트에 가져옴
#  - strip() : 줄바꿈 문자를 제거함

# with문 사용 : with문을 빠져나가면 자동으로 파일객체 닫힘
# with open(파일명, 파일모드) as 파일객체명
#     실행할 내용

# 프로그램 실행 시에 인수받기 : sys모듈 사용
#  1. import sys
#  2. sys.argv[1:] : argv[0]은 파일명, argv[1]부터 실행시 입력해준 argument가 들어옴

args = sys.argv[1:]
for i in args:
    print(i)

for i in args:
    print(i.upper(), end=" ")
print("")

# 문제 1
def if_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

# 문제 2
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1, 2))
print(avg_numbers(1, 2, 3, 4, 5))

# 문제 3
input1 = int(input("첫 번째 숫자를 입력하세요: "))
input2 = int(input("두 번째 숫자를 입력하세요: "))

total = input1 + input2
print(f"두 수의 합은 {total}입니다")

# 문제 4 : 3번
print("you" "need" "python")
print("you" + "need" + "python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

# 문제 5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.readlines())

# 문제 6
user_input = input("저장할 내용을 입력하세요: ")
f = open('test.txt', 'a')
f.write(user_input)
f.write("\n")
f.close()

# 문제 7
f = open('test2.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')
f = open('test2.txt', 'w')
f.write(body)
f.close()

# 문제 8
args = sys.argv[1:]
result = 0
for i in args:
    result = result + int(i)
print(result)

# 클래스:  비슷한 기능을 하는 내용을 묶은 객체

result = 0
def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))

result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

# 클래스 생성 : class 클래스명:
# 메서드 생성 : 함수 생성방법과 같음
# __init__ : class 호출 시 초기화 해줌

class Calculater:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculater()
cal2 = Calculater()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


cal1 = FourCal(1, 2)
cal2 = FourCal(3, 4)

print(cal1.first)
print(cal1.second)

print(cal2.first)
print(cal2.second)

print(cal1.add())
print(cal2.add())