import mod1

print(mod1.add(3, 4))
print(mod1.sub(4, 2))



import mod2
print(mod2.PI)

a = mod2.Math()
print(a.solv(2))

print(mod2.add(mod2.PI, 4.4))


for i in range(5, 0, -1):
    print("*" * i)


for i in range(0, 9):
    for j in range(0, 10):
        if i < 5:
            if j < 4 - i or j > 4 + i:
                print(" ", end="")
            else:
                print("*", end="")
        else :

            if j < i - 4 or j > 12 - i:
                print(" ", end="")
            else:
                print("*", end="")

    print("")


for i in range(10):
    print("*" * i, end="")
    print(" " * (10 - i), end="")
    print("*" * (10 - i), end="")
    print("")
for i in range(10):
    print(" " * (10 - i), end="")
    print("*" * i, end="")
    print(" " * i, end="")
    print("*" * (10 - i), end="")
    print("")

for i in range(20):
    if i < 10:
        for j in range(20):
            if j < (i + 1) :
                print("*", end="")
            elif j <= 10:
                print(" ", end="")
            elif j < 21 - i:
                print("*", end="")
        print("")
    else :
        for j in range(20):
            if j < 19 - i :
                print(" ", end="")
            elif j < 10:
                print("*", end="")
            elif j <= i :
                print(" ", end="")
            else :
                print("*", end="")
        print("")
