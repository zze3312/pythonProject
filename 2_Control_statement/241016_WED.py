# 반복문 : 해당 조건이 참이면 수행할 문장이 계속 실행됨
#  - while 조건문 :
#         실행할 문장1
#         실행할 문장2
#         실행할 문장3
#         ...

treeHit = 0
while treeHit < 10 :
    treeHit = treeHit + 1
    print(f"나무를 {treeHit}번 찍었습니다")
    if treeHit == 10 :
        print("나무 넘어갑니다.")


prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number : """
number = 0

while number != 4 :
    print(prompt, end="")
    number = int(input())

# 0~9
num = 0
while num < 10 :
    print(num)
    num = num + 1

# 10~1
num = 10
while num > 0 :
    print(num)
    num = num - 1

coffee = 10
money = 300
while money :
    print("돈을 받았으니 커피를 줍니다")
    coffee = coffee - 1
    print(f"남은 커피의 양은 {coffee}개 입니다")
    if coffee == 0 :
        print("커피가 다 떨어졌습니다. 판매를 중지합니다")
        break

num = 1
numSum = 0
while num < 11 :
    numSum = numSum + num
    num = num + 1
print(f"합계 : {numSum}")

# 1- 10까지의 짝수의 합
num = 1
numSum = 0
while num < 11 :
    if num % 2 == 0 :
        numSum = numSum + num
    num = num + 1
print(f"합계 : {numSum}")

# 1 - 100까지의 짝수, 홀수의 합
evenSum = 0
oddSum = 0
num = 1
while num <= 100 :
    if num % 2 == 1 :
        oddSum = oddSum + num
    else :
        evenSum = evenSum + num
    num = num + 1
print(f"홀수의 합 : {oddSum}")
print(f"짝수의 합 : {evenSum}")

# 1 - 100까지의 3으로 나누어 떨어지는 수
treeSum = 0
num = 1
while num <= 100 :
    if num % 3 == 0 :
        treeSum = treeSum + num
    num = num + 1

# 1 - 100 까지의 수중에 3 또는 5로 나누어 떨어지는 수 를 출력
num = 1
while num <= 100 :
    if num % 3 == 0 or num % 5 == 0 :
        print(num)
    num = num + 1

num = 1
star = "*"
while num < 6 :
    print(star * num)
    num = num + 1

num = 5
while num > 0 :
    print(star * num)
    num = num - 1

coffee = 10
while True :
    money = int(input("돈을 넣어주세요 : "))
    if money == 300 :
        print("커피를 줍니다")
        coffee = coffee - 1
    elif money > 300 :
        print(f"거스름돈 {money - 300}을 주고 커피를 줍니다.")
        coffee = coffee - 1
    else :
        print("돈을 다시 돌려 주고 커피를 주지 않습니다.")
        print(f"남은 커피의 양은 {coffee}개 입니다")
    if coffee == 0 :
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# continue : 반복문의 처음으로 돌아감
a = 0
while a < 10 :
    a = a + 1
    if a % 2 == 0 : continue
    print(a)


# 문제 1
input_num = int(input("정수 : "))
cnt = 0
sum = 0
while cnt < input_num :
    cnt = cnt + 1
    sum = sum + cnt
print(sum)


# 문제 2
cnt = 0
sum = 0

while cnt < 100 :
    cnt = cnt + 1
    if cnt % 3 == 0 :
        sum = sum + cnt
print(sum)


# 문제 3
i = 0
result = 0
n1 = int(input("정수 : "))
n2 = int(input("정수 : "))

while i < n1 :
    i = i + 1
    if n1 % i == 0 and n2 % i == 0 :
        print(i, end=" ")
print("")


# 문제 4
i = 0
cnt = 0
i_list = list()

n = int(input("정수 : "))
while i < n :
    i = i + 1
    if n % i == 0 :
        i_list.append(i)
        print(f"{i}", end=" ")
        cnt = cnt + 1
print(f": {cnt}")


# 문제 5
n1 = int(input("정수 : "))
n2 = int(input("정수 : "))

i = n1
while i > 0 :
    if n1 % i == 0 and n2 % i == 0 :
        print(i)
        break
    i = i - 1


# 문제 6
i = 0
num = 0
sum = 0
while i < 100 :
    i = i + 1
    if i % 2 == 0 :
        num = i * (-1)
    else :
        num = i
    sum = sum + num
print(sum)


# 문제 7
i = 0
max = 0
n_list = list()

while i < 5 :
    input_num = int(input("정수 : "))
    n_list.append(input_num)
    i = i + 1

i = 0
while i < 5 :
    if max < n_list[i] :
        max = n_list[i]
    i = i + 1
print(f"최댓값 : {max}")