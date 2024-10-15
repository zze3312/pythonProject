# 딕셔너리 자료형(hash map) : key, value를 이용하여 데이터를 가져올 수 있는 자료형
#  - 기본 형식 : {key1 : value1, key2 : value2, key3 : value3, ...}
#  - key를 통해 value를 얻기 때문에 순번x

# 딕셔너리 쌍 추가하기 : 딕셔너리명[KEY] = VALUE
a = {1 : 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
a[3] = [1, 2, 3]
print(a)

# 딕셔너리 요소 삭제하기 : del 딕셔너리명[KEY]
del a['name']
print(a)

# 딕셔너리에서 key를 사용해 value 얻기
grade = {'pey' : 10, 'julliet' : 99}
print('pey')

a = {1 : 'a', 1 : 'b'}
print(a[1]) # >>> b : key값이 중복되면 덮어써짐 (오류발생x)

# print(a['test']) : KeyError: 'test' (존재하지 않는 키 호출 x)
# a = {[1, 2] : 'hi'} : TypeError: unhashable type: 'list' (해쉬에 list타입 사용 불가)

# 딕셔너리 관련 함수
#  - keys : key리스트
a = {'name' : 'pey', 'phone' : '010-9999-1234', 'birth' : '1118'}
print(a.keys())

# dict_keys() 사용
for k in a.keys() :
    print(k)

# dict_keys() > 리스트형으로 변환
print(list(a.keys()))

# value 리스트 생성
print(a.values())

# dict_values()도 dict_keys()와 같은 방식으로 사용 가능
for k in a.values() :
    print(k)

print(a.values())

# key-value 쌍 얻기
print(a.items())
# dict_items()도 dict_keys()와 같은 방식으로 사용 가능
for k in a.items() :
    print(k)
    print("요소 : %s" % k[0])

print(a.items())

# clear() : key:value 쌍 모두 삭제
# a.clear()
# print(a)

# get() : key로 value 얻기
print(a.get('name'))
print(a.get('email')) # >>> None : 해당데이터 없으면 None

# in() : 해당 key가 딕셔너리 안에 있는지 확인
print('name' in a)
print('email' in a)

# 집합자료형 : 집합에 관련된 것 관리 (set() 사용)
s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2)
#  - 중복 삭제
#  - 순서x

#  - 리스트, 튜플로 변환 가능
l1 = list(s1)
print(l1)
t1 = tuple(s1)
print(t1)

# 교집합, 합집합, 차집합 구하기
a1 = set([1, 2, 3, 4, 5, 6])
a2 = set([4, 5 ,6 ,7 ,8 ,9])

#  - &, intersection() : 교집합
print(a1 & a2)
print(a1.intersection(a2))

#  - |, union() : 합집합
print(a1 | a2)
print(a1.union(a2))

#  - -, difference : 차집합
print(a1 - a2)
print(a1.difference(a2))

# 집합 자료형 관련 함수
#  - add : 값 1개 추가
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

#  - update : 값 여러개 추가
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

#  - remove : 특정 값 제거
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)

# 불(boolean) 자료형 : 참(true)/거짓(false)을 나타내는 자료형
#  - True : 참
#  - False : 거짓
#  ※ True/False 는 파이썬 예약어, 첫문자 대문자로 작성해야함
a = True
print(type(a)) # >>> <class 'bool'> : 불자료형
print(1 == 1)
print(type(1 == 1))  #  - 비교연산자의 결과는 bool형태로 나오게 됨
print(type(2 < 1))
#  ※ 비교연산자 중 동일여부를 확인하는 연산자 : == ( = : 대입연산자)

# 자료형의 참/거짓
#  - 데이터의 유무에 따라 참/거짓
print(bool("python")) # True
print(bool("")) # False
print(bool([1, 2, 3])) # True
print(bool([])) # False
print(bool((1, 2, 3))) # True
print(bool(())) # False
print(bool({'a' : 1})) # True
print(bool({})) # False
print(bool(1)) # True
print(bool(0)) # False
print(bool(None)) # False

a = [1, 2, 3, 4]
while a :
    print(a.pop())
    print(a)

if [] :
    print("참")
else :
    print("거짓")

if [1, 2, 3] :
    print("참")
else :
    print("거짓")

# 변수 : 자료형 데이터의 값
#  - 변수명 = 변수에 저장할 값
#  - 파이썬에서의 변수는 해당 메모리의 주소를 가리킴
#  - id() : 해당 주소값을 확인
a = [1, 2, 3]
print(id(a))

b = a
print(b)
print(id(b)) # b에 대입되는것은 a의 메모리 주소값 > a를 변경했을 때 b도 같이 변경됨
a[1] = 4
print(b)

print(a is b) # 같은 값을 가리키고 있으므로 True로 나오게 됨

# 리스트의 내용을 복사하고 싶을 때
#  - [:] : 슬라이싱 이용하기
a = [1, 2, 3]
b = a[:]
print(id(a))
print(id(b)) # 서로 다른 메모리에 할당되는 것을 확인할 수 있음

#  - copy() : copy 모듈 이용
from copy import copy # copy모듈에 있는 copy함수 import
c = copy(a)
print(id(a))
print(id(c)) # 서로 다른 메모리에 할당되는 것을 확인할 수 있음
print(a is c) # 서로 다른 메모리에 저장되어 있으므로 False 로 나옴

# 변수를 여러개 선언 할 때
a, b = ('python', 'life')
print(a)
print(b)
(a, b) = 'python', 'life'
print(a)
print(b)
[a, b] = ['python', 'life']
print(a)
print(b)

print(a, b)

# 여러개의 변수에 같은 값 대입
a = b = 'python'
print(a)
print(b)

a = 3
b = 5
print(f"a : {a}, a의 주소 : {id(a)}")
print(f"b : {b}, b의 주소 : {id(b)}")
a, b = b, a
print(f"a : {a}, a의 주소 : {id(a)}")
print(f"b : {b}, b의 주소 : {id(b)}")
a, b = int(b), int(a)
print(f"a : {a}, a의 주소 : {id(a)}")
print(f"b : {b}, b의 주소 : {id(b)}")
a, b = copy(b), copy(a)
print("=" * 50)
print(f"a : {a}, a의 주소 : {id(a)}")
print(f"b : {b}, b의 주소 : {id(b)}")

print(f"a : {a}, a의 주소 : {id(a)}")
print(f"b : {b}, b의 주소 : {id(b)}")

# 1. 평균점수 구하기
hong_kor = 80
hong_eng = 75
hong_math = 55
hong_sum = hong_kor + hong_eng + hong_math
hong_avg = hong_sum / 3
print(f"홍길동 성적 평균 : {hong_avg}")

scores = [80, 75, 55]
score_sum = scores[0] + scores[1] + scores[2]
score_avg = score_sum / len(scores)
print(score_avg)

# 2. 홀수, 짝수 판별하기
if 13 % 2 == 0 :
    print("짝수입니다")
else :
    print("홀수입니다")

# 3. 주민등록번호 나누기
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# 4. 주민등록번호 인덱싱
print(f"홍길동의 주민등록번호 성별값은 {pin[7]} 입니다")

# 5. 문자열 바꾸기 ( : > # )
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# 6. 리스트의 역순 정렬하기 [1, 3, 5, 4, 2] > [1, 2, 3, 4, 5] > [5, 4, 3, 2, 1]
list_a = [1, 3, 5, 4, 2]
print(list_a)
list_a.sort()
print(list_a)
list_a.reverse()
print(list_a)

# 7. 리스트를 문자열로 만들기
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# 8. 튜플 더하기 : (1, 2, 3) > +4 > (1, 2, 3, 4)
a = (1, 2, 3)
a = a + (4,)
print(a)

# 9. 딕셔너리의 키
a = dict()
print(a)

# 오류가 발생하는 이유
a['name'] = 'python' # 오류x
print(a)
a[('a', )] = 'python' # 오류x
print(a)
#a[[1]] = 'python' # 딕셔너리의 key값에는 리스트를 넣을 수 없음
#print(a)
a[250] = 'python' # 오류x
print(a)

# 10. 딕셔너리 값 추출하기 (결과 : {'A' : 90, 'C' : 70})
a = {'A' : 90, 'B' : 80, 'C' : 70}
result = a.pop('B')
print(a)
print(result)

# 11. 리스트에서 중복 제거
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# 12. 파이썬 변수
# a = b = [1, 2, 3]
# a[1] = 4
# print(b)
# 처음 내 생각 : b는 그대로 일 것이다.(오답)
a = b = [1, 2, 3]
a[1] = 4
print(b)
# 틀린이유 : 내 생각에는 a와 b가 별개의 메모리에 저장될 것 이라고 생각했다
#          하지만 a와 b는 같은 메모리 주소를 공유하고 있었다
#          따라서 a를 수정하였으나 b도 같이 수정되는 현상을 확인할 수 있었다
print(f"a의 메모리주소 : {id(a)}")
print(f"b의 메모리주소 : {id(b)}")

# 사용자의 입력 활용 : input()
# a = input("a 숫자를 입력해주세요 : ")
# b = input("b 숫자를 입력해주세요 : ")
# print(f"a + b 결과 : {int(a) + int(b)}")

# print()의 마지막에 줄바꿈 존재, 사용 안하려면 end 파라미터 사용
print("a", end = " ")
print("b", end = " ")
print("c")

# height = input("세로를 입력해주세요 : ")
# weight = input("가로를 입력해주세요 : ")
# print(f"가로 : {weight} / 세로 : {height} / 넓이 : {int(weight) * int(height)}")

# 3과 5 덧셈과 곱셈
# a = 3
# b = 5
# add = int(a) + int(b)
# mul = int(a) * int(b)
# print(f"add : {add} / mul : {mul}")

# 두 수 입력받아 덧셈, 곱셈하기
# a = input("a를 입력하세요 : ")
# b = input("b를 입력하세요 : ")
# print(f"a + b = {int(a) + int(b)} / a * b : {int(a) * int(b)}")

# 몫과 나머지 구하기
# a = input("a를 입력하세요 : ")
# b = input("b를 입력하세요 : ")
# print(f"a / b = {int(a) / int(b)} / a % b : {int(a) % int(b)}")

# 사각형 넓이 구하기
# a = input("가로를 입력하세요 : ")
# b = input("세로를 입력하세요 : ")
# print(f"넓이 : {int(a) * int(b)}")

# 총점과 평균구하기
# a = input("과목1 점수를 입력하세요 : ")
# b = input("과목2 점수를 입력하세요 : ")
# c = input("과목3 점수를 입력하세요 : ")
# sum = int(a) + int(b) + int(c)
# print(f"총점 : {sum} / 평균 : {sum/3}")

# 센치미터 단위의 길이를 미터와 센치미터로 변환하기
# cm = input("길이를 입력해 주세요 : (cm) ")
# m = int(cm) // 100
# cm = int(cm) % 100
# print(f"변환된 값 : {m}m {cm}cm")

# 초 단위의 시간을 시간, 분, 초로 변환하기
# s = input("변환할 초를 입력해주세요 : ")
# h = int(s) // (60*60)
# s = int(s) % (60*60)
# m = int(s) // 60
# s = int(s) % 60
# print(f"변환된 값 : {h}시간 {m}분 {s}초")

# 조건문
#   if (조건) :
#       실행할 문장       # 조건에 해당할 경우 실행
#   else :
#       실행할 문장       # 조건에 해당하지 않을 경우 실행
#  - 조건문 사용 시 들여쓰기가 if문 안에 있다는 것을 의미
#  - 조건문, 반복문 등 콜론(:) 누락시키지 않게 주의

money = True
if money :
    print("택시를 타고 가라")
else :
    print("걸어가라")

money = 2000
if money >= 3000 :
    print("택시를 타고 가라")
else :
    print("걸어가라")

# 관계연산자
#   - x < y : x가 y보다 작다
#   - x > y : x가 y보다 크다
#   - x == y : x와 y는 같다
#   - x != y : x와 y는 다르다
#   - x >= y : x가 y보다 크거나 같다
#   - x <= y : x가 y보다 작거나 같다

# and, or, not
#   - x or y : 둘중 하나만 참이어도 참
#   - x and y : 둘다 참이어야 참
#   - not x : x가 거짓이면 참
money = 2000
card = True
if money >= 3000 or card :
    print("택시를 타고 가라")
else :
    print("걸어가라")

# in, not in
#   - x in (리스트, 튜플, 문자열) : 리스트안에 값이 존재하면 참
#   - x not in (리스트, 튜플, 문자열) : 리스트안에 값이 존재하지 않으면 참
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

# 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어 가라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket :
    print("택시를 타고 가라")
else :
    print("걸어 가라")

# 주머니에 카드가 없다면 걸어 가고, 있다면 버스를 타고 가라
if 'card' not in pocket :
    print("걸어 가라")
else :
    print("버스를 타고 가라")


a = int(input("a를 입력하세요 : "))
b = int(input("b를 입력하세요 : "))
if a > b :
    print("a가 b보다 크다")
else :
    print("b가 a보다 크다")