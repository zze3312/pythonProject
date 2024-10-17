# for : 반복문의 문장구조가 한눈에 잘 보임
#
# for 변수 in 리스트(또는 튜플, 문자열) :
#     수행할 문장 1
#     수행할 문장 2
#     수행할 문장 3
#     ...

test_list = ['one', 'two', 'three']
for i in test_list :
    print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a :
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks :
    number = number + 1
    if mark >= 60 :
        print(f"{number}번 학생은 합격입니다")
    else :
        print(f"{number}번 학생은 불합격입니다")

sum = 0
cnt = 0

for mark in marks :
    sum += mark
    cnt += 1
avg = sum / cnt
print (f"합 : {sum}")
print (f"평균 : {avg}")

find_num = 67
cnt = 0
min = marks[0]
max = 0
for mark in marks :
    cnt += 1
    if mark == find_num :
       print(f"{mark}는 {cnt}번 입니다")

for mark in marks :
    if min > mark :
        min = mark
    if max < mark :
        max = mark
print(f"{max}")
print(f"{min}")

cnt = 0
for mark in marks :
    cnt += 1
    if mark < 60 :
        continue
    print(f"{cnt}번 학생은 합격입니다")

# range() : 원하는 범위의 숫자를 담은 객체를 만듦
# range((시작_숫자), 끝_숫자, (증감식))
# 끝숫자 바로 앞 숫자까지 만들어짐 (시작숫자 이상 끝숫자 미만)
# range(개수) > range(0, 개수)

for i in range(10) :
    print(i + 1)

for i in range(1, 11) :
    print(i)

add = 0
for i in range(1, 11) :
    add = add + i
print(add)

for i in range(10, 0, -1) :
    print(i)

for number in range(len(marks)) :
    if marks[number] < 60 :
        continue
    print(f"{number + 1}번 학생은 합격입니다")

sum = 0
for i in range(100) :
    sum = sum + i + 1

print(sum)

for i in range(1, 6) :
    print("*" * i)

for i in range(6, 0, -1) :
    print("*" * i)

for i in range(2, 10) :
    for j in range(1, 10) :
        print(f" {i} x {j} = {i * j} ", end=" ")
    print("")

print("")


for i in range(1, 10) :
    for j in range(2, 10) :
        print(f" {j} x {i} = {i * j} ", end=" ")
    print("")

li_score = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]]

for i in range(len(li_score)) :
    for j in range(len(li_score[i])) :
        print(li_score[i][j], end = " ")
    print("")

for li in li_score :
    for i in li :
        print(i, end = " ")
    print("")

# 리스트 컴프리헨션
#  - [표현식 for 항목 in 반복 가능한 객체 if 조건문]
a = [1, 2, 3, 4]
result = list()
for i in a :
    result.append(i * 3)
print(result)

result2 = [i * 3 for i in a]
print(result2)

result3 = [i * 3 for i in a if i % 2 == 0]
print(result3)

result4 = [x * y for x in range(2, 10)
                 for y in range(1, 10)]
print(result4)


# 되새김 문제 1 : need
a = "Life is too short, you need python"
if "wife" in a : print("wife")
elif "python" in a and "you" not in a : print("python")
elif "shirt" not in a : print("shirt")
elif "need" in a : print("need")
else : print("none")

# 답 : shirt > shirt가 없기 때문에 출력됨
# 문제를 제대로 읽자

# 되새김 문제 2 : i % 3 == 0
result = 0
i = 1
while i <= 1000 :
    if i % 3 == 0 :
        result += i
    i += 1
print(result)

# 되새김 문제 3 : i > 5, "*" * i
i = 0
while True :
    i += 1
    if i > 5 : break
    print("*" * i)

# 되새김 문제 4 : range(1, 101)
for i in range(1, 101) :
    print(i)

# 되새김 문제 5 : score, total / len(A)
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A :
    total += score
average = total / len(A)
print(average)

# 되새김 문제 6 : [n * 2 for n in numbers if n % 2 == 1]
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers :
    if n % 2 == 1 :
        result.append(n * 2)
print(result)

result2 = [n * 2 for n in numbers if n % 2 == 1]
print(result2)

# 문제 1
a1 = [i for i in range(1, 11)]
print(a1)
print("")

# 문제 2
a2 = [i * 10 for i in range(1, 11)]
#print(a2)
for i in range(10, 0, -1) :
    print(a2[i-1], end=" ")
print("")
print("")

# 문제 3
temp = 0
a3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(5) :
    temp = a3[i]
    a3[i] = a3[9 - i]
    a3[9 - i] = temp
print(a3)
print("")

# 문제 4
a4_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a4_2 = list()
for i in range(len(a4_1)) :
    idx = len(a4_1) - i - 1
    a4_2.append(a4_1[idx])
print(a4_2)
print("")

# 문제 5
a5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp = a5[0]
for i in range(10) :
    idx = i + 1
    if idx < 10 :
        a5[i] = a5[i + 1]
    else :
        a5[i] = temp
print(a5)
print("")

# 문제 6
for i in range(10) :
    print(f"{i + 1} 약수 : ", end="")
    for j in range(i + 1) :
        if (i + 1) % (j + 1) == 0 :
            print(f"{j + 1}", end=" ")
    print("")
print("")

# 문제 7_1
for i in range(5) :
    print(f"{i + 1}" * (i + 1))
print("")

# 문제 7_2
for i in range(5) :
    num = 0
    for j in range(5 - i, 0, -1) :
        num = num + 1
        print(num, end="")
    print("")
print("")

# 문제 7_3
for i in range(5) :
    num = 5 - i
    for j in range(5 - i, 0, -1) :
        print(num, end="")
        num = num - 1
    print("")
print("")

# 문제 8
input_num = int(input("정수 : "))
cnt = 0
for i in range(input_num) :
    if input_num % (i + 1) == 0 :
        cnt = cnt + 1

if cnt == 2 : print(f"{input_num} : 소수임")
else : print(f"{input_num} : 소수아님")
print("")

# 문제 9
for i in range(2, 101) :
    cnt = 0
    for j in range(i):
        if i % (j + 1) == 0:
            cnt = cnt + 1
    if cnt == 2 : print(i, end=" ")
print("")

# 문제 10(선택)
input_num2 = int(input("자연수 : "))
temp = 0
a_10 = [i for i in range(2, input_num2 + 1)]
a_10_2 = [] # 소수인수 담기

# 입력한 숫자까지 소수인 수 찾기
for i in a_10 :
    chk = True
    for j in range(2, i + 1) :
        if i % j == 0 and i != j :
            chk = False
            break
        else :
            temp = j
    if chk :
        a_10_2.append(temp)
print(a_10_2)
