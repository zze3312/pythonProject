# 변수 : 변화하는 데이터
# 상수 : 변하지 않는 데이터
# 선언 : 사용하려는 변수를 정의
# 대입 : 변수에 데이터를 삽입
# 초기화 : 데이터 기본값으로 초기화

student1 = "A"
student2 = "B"
student3 = "C"
student4 = "D"
student5 = "E"

s1_korea = 90
s2_korea = 80
s3_korea = 70
s4_korea = 60
s5_korea = 50

student_cnt = 5
student_kor_sum = s1_korea + s2_korea + s3_korea + s4_korea + s5_korea
student_kor_avg = student_kor_sum / student_cnt

print(student_kor_avg)

# 문자열 슬라이싱(slicing) : 문자열을 자른다
# 교재 58p
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
# 교재 59p
c = a[0:4]
# b, c 결과는 같지만 c처럼 사용하기
print(b)
print(c)

# 연습
phone_number = ("010-6634-3312")
num_mid = phone_number[4:8]
num_last = phone_number[9:13]
print(num_mid)
print(num_last)

# 문자열 > 정수형 변환 함수 : int()
num_sum = int(num_mid) + int(num_last)
print(num_sum)

# 앞숫자 생략시 0, 뒤숫자 생략시 마지막 번호
num_last2 = phone_number[9:]
print(num_last2)

# 교재 60p
a_slice = a[19:]
print(a_slice)
a_slice2 = a[:]
print(a_slice2)
a_slice3 = a[:-7]
print(a_slice3)
a_slice4 = a[-6:]
print(a_slice4)

# 교재 61p
data = "20230331Rainy"
year = data[0:4]
mon = data[4:6]
day = data[6:8]
weather = data[8:]

print(year + "년 " + mon + "월 " + day + "일 날씨 : " + weather )

# 대입을 통한 수정도 가능
# 교재 62p
a = "Pithon"
# a[1] = 'y' (오류)
b = a[:1] + 'y' + a[2:]
print(b)

# 문자열 포매팅
#  - %s : 문자열
#  - %c : 문자1개
#  - %d : 정수
#  - %f : 부동소수
#  - %o : 8진수
#  - %x : 16진수
#  - %% : Literal %(문자 %자체)
print("데이터 : %s" %data)
print("정수형 숫자 : %d" % 3)
print("실수형 숫자 : %f" % 3.14)

#여러개 대입시 괄호로 묶음
print("오늘은 %s년 %s월 %s일 날씨는 %s 입니다" %(year, mon, day, weather))

# 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
# 교재 65p
err_percent = 90
print("Error is %d%%." %err_percent)

# 포맷코드와 숫자 함께 사용
# 1. 정렬
# 교재 66p
print("%10s" % "hi")
print("%10s jane." % "hi") # 오른쪽 정렬
print("%-10s jane." % "hi") # 왼쪽 정렬

# 2. 소수점
# 교재 67p
print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234)

# 3. format 함수를 사용한 포매팅
# 교재 67~70
print("I eat {0} appels." .format(3))
print("I eat {0} appels." .format("five"))
number = 3
print("I eat {0} appels." .format(number))
day = "three"
print("I ate {0} appels. So I was sick for {1} days." .format(number, day))
print("I ate {number} apples. So I was sick for {day} days." .format(number=10, day=3))
print("I ate {0} apples. So I was sick for {day} days." .format(10, day=3))
print("{0:<10}" .format("hi")) # 왼쪽 정렬
print("{0:>10}" .format("hi")) # 오른쪽 정렬
print("{0:^10}" .format("hi")) # 가운데 정렬
print(f'{"hi":=^10}') # 가운데 정렬하고 =로 공백 채우기
print(f'{"hi":!<10}') # 왼쪽 정렬하고 !로 공백 채우기

# 연습
subject = ["이름", "국어", "영어", "수학", "파이썬", "평균"]
subject_cnt = 4

student1 = {"name" : "김연수", "kor" : 90, "eng" : 95, "math" : 89, "python" : 85}
student1_sum = student1["kor"] + student1["eng"] + student1["math"] + student1["python"]
student1_avg = student1_sum / subject_cnt
student1["avg"] = student1_avg

student2 = {"name" : "김기태", "kor" : 80, "eng" : 85, "math" : 88, "python" : 84}
student2_sum = student2["kor"] + student2["eng"] + student2["math"] + student2["python"]
student2_avg = student2_sum / subject_cnt
student2["avg"] = student2_avg

student3 = {"name" : "박세진", "kor" : 75, "eng" : 75, "math" : 87, "python" : 78}
student3_sum = student3["kor"] + student3["eng"] + student3["math"] + student3["python"]
student3_avg = student3_sum / subject_cnt
student3["avg"] = student3_avg

student4 = {"name" : "이소윤", "kor" : 85, "eng" : 85, "math" : 86, "python" : 77}
student4_sum = student4["kor"] + student4["eng"] + student4["math"] + student4["python"]
student4_avg = student4_sum / subject_cnt
student4["avg"] = student4_avg

print("{0:^60}" .format("성적표"))
print("-" * 60)
print(f"{subject[0]:<10}{subject[1]:<9}{subject[2]:<9}{subject[3]:<9}{subject[4]:<9}{subject[5]:<9}")
print("-" * 60)
print(f"{student1["name"]:<10}{student1["kor"]:<10}{student1["eng"]:<10}{student1["math"]:<10}{student1["python"]:<10}{student1["avg"]:<10}")
print(f"{student2["name"]:<10}{student2["kor"]:<10}{student2["eng"]:<10}{student2["math"]:<10}{student2["python"]:<10}{student2["avg"]:<10}")
print(f"{student3["name"]:<10}{student3["kor"]:<10}{student3["eng"]:<10}{student3["math"]:<10}{student3["python"]:<10}{student3["avg"]:<10}")
print(f"{student4["name"]:<10}{student4["kor"]:<10}{student4["eng"]:<10}{student4["math"]:<10}{student4["python"]:<10}{student4["avg"]:<10}")
print("-" * 60)

# 문자열 관련 함수
#  - count() : 문자 개수
#  - find() : 문자의 위치
#  - index() : 문자의 위치
#  - join() : 문자열 삽입
# 교재 74p
join_str = ",".join("abcd")
print(join_str)
join_str2 = ",".join(['a', 'b', 'c', 'd'])
print(join_str2)
#  - upper() : 소문자 > 대문자
#  - lower() : 대문자 > 소문자
#  - lstrip() : 왼쪽 공백 지우기
#  - rstrip() : 오른쪽 공백 지우기
#  - strip() : 양쪽 공백 지우기
#  - replace() : 문자열 바꾸기
#  - split() : 문자열 나누기

# 리스트형
#  - 리스트명 = [요소1, 요소2, 요소3, ...]
#  - 빈 리스트 만들때 : 리스트명 = list()
# 교재 79p
list_a = [1, 2, 3, ['a', 'b', 'c']]
print(list_a[0])
print(list_a[-1])
print(list_a[3])

# 교재 80p
list_b = [1, 2, ['a', 'b', ['Life', 'is']]]
print(list_b[2][2][0])

# 리스트의 슬라이싱 : 문자열의 슬라이싱과 사용방법은 같으나 마지막 요소 출력여부가 다름
# 교재 81p
slice_list = [1, 2, 3, 4, 5]
print(slice_list[0:2])
print(slice_list[2:])
print(slice_list[:3])

# 중첩된 리스트에서의 슬라이싱
# 교재 81p
slice_list2 = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(slice_list2[2:5])
print(slice_list2[3][:2])

# 리스트의 연산
# 교재 82~83p
lst_a = [1, 2, 3]
lst_b = [4, 5, 6]
lst_c = ['4', '5', '6']
print(lst_a + lst_b)
print(lst_a + lst_c)
# print(lst_a[0] + lst_c[0]) : 숫자 + 문자열이라 오류
print(lst_a[0] + int(lst_c[0])) # 숫자 + 숫자 더하기 연산
print(str(lst_a[0]) + lst_c[0]) # 문자열 + 문자열 연결 연산

# 리스트의 반복
print(lst_a * 3)

# 리스트의 길이
print(len(lst_a))

# 리스트의 값 수정하기
# 교재 83p
lst_c = [1, 2, 3]
lst_c[2] = 4
print(lst_c)

# 리스트 관련 함수
#  - del() : 요소 삭제 함수
# 교재 84p
del lst_c[1]
print(lst_c)

lst_d = [1, 2, 3, 4, 5]
del lst_d[2:]
print(lst_d)

#  - append() : 요소 추가 함수
# 교재 85p
lst_e = [1, 2, 3]
lst_e.append(4)
print(lst_e)

#  - sort() : 요소 정렬
# 교재 85p
lst_f = [1, 4, 3, 2]
lst_f.sort()
print(lst_f)

#  - reverse() : 리스트 뒤집기
# 교재 85p
lst_g = ['a', 'c', 'b']
lst_g.reverse()
print(lst_g)

#  - index() : 인덱스 반환
# 교재 86p
lst_h = [1, 2, 3, 4, 5]
print(lst_h.index(3))

#  - insert() : 리스트에 요소 삽입
# 교재 86p
lst_i = [1, 2, 3]
lst_i.insert(0, 4)
lst_i.insert(3, 5)
print(lst_i)

#  - remove() : 특정 요소 제거
# 교재 87p
lst_j = [1, 2, 3, 1, 2, 3]
lst_j.remove(3) # 제일먼저 나오는 3 1개만 지움
print(lst_j)

#  - pop() : 리스트의 요소 끄집어 내기(마지막 요소 제거)
# 교재 87p
lst_k = [1, 2, 3, 4]
lst_k.pop()
print(lst_k)
lst_k.pop(1)
print(lst_k)

#  - count() : 리스트에 포함된 요소의 개수 세기
# 교재 88p
lst_l = [1, 2, 3, 1]
print(lst_l.count(1))

#  - extend() : 리스트의 확장
# 교재 88p
lst_m = [1, 2, 3]
lst_m.extend([4, 5])
print(lst_m)
lst_n = [6, 7]
lst_m.extend(lst_n)
print(lst_m)

# 튜플 자료형(tuple)
#  - 리스트와 거의 비슷
#  - 리스트는 요솟값의 생성, 삭제, 수정이 가능하지만 튜플은 불가
#  - 하나의 요소를 가질 때는 마지막에 ,를 꼭 붙여준다

