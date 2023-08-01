 ## 함수
def addNumber(num):
    if num == 1:
        return 1
    return num + addNumber(num-1)


def factorial(num):
    if num ==1:
        return 1
    return num * factorial(num-1)


def countDown(n):
    if n == 0:
        return print('발사!')
    else:
        print(n)
        countDown(n-1)


def printStar(n):
    if n == 1:
        return print(n * "*")
    print((n-1) * '*')
    return printStar(n-1)


def gugu(dan, num):

    for i in range(2,10):
        dan = i
        for k in range(1,10):
            num = k

    print(f"### {dan} 단###")
    print(f"{dan}X{num} =", dan * num)

## 메인
print(addNumber(10))
print(factorial(5))
print(countDown(5))
print(printStar(10))
print(gugu())