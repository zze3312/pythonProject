# 24.10.10
# TITLE : 자료형

# 인터프린터 / 컴파일 언어
#  - 인터프린터 : 한줄한줄 작동(Python)
#  - 컴파일 : 한번에 모아서 작동(C)
# 데이터타입 약한타입/강한타입
#  - 약한타입 : 타입구분이 엄격함
#  - 강한타입 : 타입구분이 비교적 덜 엄격함
# 매니지드 / 언매니지드 언어
#  - 메모리를 관리하는 방식
#  - 매니지드 : 언어에서 메모리 관리(Python, Java, C#)
#  - 언매니지드 : 프로그래머가 메모리 관리(C, C++)
# OOP(객체지향) / OOPx

# Python은 ? >> 인터프린터, 약한타입, 매니지드, OOP 언어
# ex) C, C++, Python의 차이 ?

# 내가 만드는 프로그램이 어떤 OS에서 어떤 언어기반으로 어떻게 돌아가는지 알고있자!

# <<자료형>>
# 1. 숫자형
#  - 정수(integer) : 부호 표시에 1bit 사용, unsigned형을 이용하여 부호없이 숫자범위를 늘려서 사용가능, ( integer, int / 32bit, 42억 범위, long / 64bit )
#  - 실수(floating-point) : 지수표현방식 사용가능 ( float )
#  - 8진수(octal), 16진수(hexadecimal) : 8진수 -> 0o 사용, 16진수-> 0x 사용

# ※ Pycharm에서 테스트 해볼때 : Python Console 사용, 데이터 사라짐
#    Console 이용x : print 사용해줘야 데이터 확인가능

# 예제(사칙연산)
a = 3
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 제곱표시 : **
print(a ** b)

print( (10*18**2)+(2*11) )

# 나머지 연산자 : %
print(7 % 3)

# 몫 연산자 : //
print(7 // 3)

a = 14 // 3
b = 14 % 3
print("몫은 %d 입니다" %a)
print("나머지는 %d 입니다" %b)

# 2. 문자열(String)
#  - 문자열을 표시할 때에는 ', "안에 넣으면 됨
#  - 문자(char) : 문자 하나하나를 넣어주는 자료형
#  - 문자열과 숫자는 연산되지 않음
#  - 문자열 + 문자열 = 연결된 문자열
#  - ''', """ 을 사용하는 경우 : 문자열 안에 띄어쓰기, 들여쓰기, 줄바꿈 등 사용하고 싶은 경우
#  - ', " 둘다 사용하는 이유 : 문자열안에 포함시키고 싶은 경우 사용하기 위해

food = "Python's favorite food is perl"
print(food)
bank = " 1000000 payment"
x = food + bank
print(x)

food2 = '"Python is very easy." he says.'
print(food2)

# 역슬래시(\) : 이스케이프 문자
food3 = 'Python\'s favorite food is perl'
print(food3)

# 멀티라인 : \n , tab : \t
multiline = "Life\tis too short\nYou need python."
print(multiline)

# ※ 이스케이프 문자
#  - \n : 문자열 안에서 줄바꿈
#  - \t : 문자열 사이에 탭
#  - \\ : \ 그대로 표현
#  - \' : ' 그대로 표현
#  - \" : " 그대로 표현
#  - \r : 캐리지리턴(줄바꿈문자, 커서 현재줄의 가장 앞으로 이동)
#  - \f : 폼피드(줄바꿈문자, 커서 현재줄의 다움줄로 이동)
#  - \a : 벨소리(출력시 PC에서 '삑'소리)
#  - \b : 백스페이스
#  - \000 : 널문자

# 문자열의 연산
#  - = : 대입연산자 -> 오른쪽에 있는 데이터를 왼쪽에 있는 변수에 저장하겠다는 의미
head = "Python"
tail = " is fun!"
word = head + tail
print ( word )

#  - * : 문자열 반복
line = "=" * 50
print( line )
print("My Program")
print( line )

#  ※ 연산자가 1개 : 단항연산자, 연산자가 2개 : 이항연산자, 연산자가 3개 : 삼항연산자

#  - 문자열의 길이 : len() 함수 사용
# ※ 함수 : 기능을 하는 묶음, 매개변수 : 함수에 넣는 데이터
a = "Life is to short"
print( len(a) )

b = "You need python"
print( len(b) )

# 구문 : 소스코드
# 주석 : # 이후 작성한 내용
#  - 함수에 대한 설명
#  - 누가, 언제 작성했는지, 뭘 할지, 수정사항 수정 이유 등 내용 기입

# 문자열 인덱싱(Indexing) : 문자열 각 문자에 번호를 매겨 해당 번호를 이용하는 방법, 0부터 시작, 음수 : 뒤에서 부터 불러움
# 문자열 슬라이싱(Slicing) : 문자열을 자르는 방법
a = "Life is too short, You need Python"
print(a[5])

