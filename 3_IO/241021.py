def calc (i, j, choice) :
    if choice == '+' :
        return i + j
    elif choice == '-' :
        return i - j
    elif choice == '*' :
        return i * j
    elif choice == '/' :
        if j == 0 :
            return "계산 불가"
        else :
            return i / j
    elif choice == '%' :
        if j == 0 :
            return "계산 불가"
        else :
            return i % j

print(calc(1, 0, '%'))
print(calc(i = 1, j = 0, choice='+'))

# 여러개의 파라미터를 받는 함수 : def 함수명(*파라미터) : 
def add_many(*args) :
    result = 0
    for i in args :
        result = result + i
    return result

add_many(1, 2, 3)

def add_mul (choice, *args) :

    if choice == '+' :
        result = 0
        for i in args :
            result = result + i
        return result
    elif choice == '*' :
        result = 1
        for i in args:
            result = result * i
        return result

print(add_mul('+', 1, 2, 3, 4, 5))
print(add_mul('*', 1, 2, 3, 4, 5))

# return 을 2개 이상 주면 튜플형식으로 출력됨
def add_and_mul (a, b) :
    return a + b, a * b

print(add_and_mul(1, 4))

result1, result2 = add_and_mul(4, 10)
print(f"result1 : {result1} / result2 : {result2}")

# 파라미터 초기화
#  - 함수 정의 시 초기값을 미리 설정해 줄 수 있음
def say_myself (name, age, man = True) :
    print(f"나의 이름은 {name}입니다")
    print(f"나이는 {age}살 입니다")
    if man :
        print("남자입니다")
    else :
        print("여자입니다")


say_myself('james', 20)

# 함수 내부의 변수와 외부에 있는 변수는 별개
a = 1
def vertest (a) :
    a = a + 1

vertest(a)
print(a)

# 함수 내에서 함수외부값을 가져와 수정하는 방법 : return, global
#  - return
def vartest2(a) :
    a = a + 1
    return a

a = vartest2(a)
print(a)

#  - global
a = 1
def vartest():
    global a
    a = a + 1
    return a

vartest()
print(a)

# lambda : 간단한 함수 정의
#  - 함수명 = lambda 매개변수1, 매개변수2, ... : 매개변수 표현식
add = lambda a, b : a + b
result = add(5, 6)
print(result)


# 출력 : print()
#  - ()안에 문자열은 +로 연결가능
#  - ()안에 문자열 띄어쓰기는 , 로 연결
#  - end 파라미터로 마지막에 올 문자 결정
# 사용자 입력 : input("안내문구")

# 파일 읽기 : open(파일명, 파일열기모드)
# 파일 쓰기 : write(쓸 내용)
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = f"{i}번째 줄입니다\n"
    f.write(data)
f.close()

f = open("새파일.txt", 'r')
lines = f.readline()
print(lines)
for line in lines:
    print(line)
f.close()
