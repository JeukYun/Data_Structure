# 스택이 꽉 찼을때 스택에 추가하는 경우 overflow 발생
# 스택이 비어있을 때 스택에서 빼는 경우 underflow 발생
# -> 방지해야함.

## 함수
def isStackFUll():
    global SIZE, stack, top
    if (top >= SIZE -1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if isStackFUll(): # 스택이 꽉 찬경우 더이상 push X
        print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data


def isStackEmpty():
    global SIZE, stack, top
    if (top <= -1):
        return True
    else:
        return False


def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print("스택이 비었습니다.")
        return
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data


def peek():
    global SIZE, stack, top
    if isStackEmpty():
        print("스택이 비었습니다.")
        return
    return stack[top]


    ## 변수
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

## 메인

##push
push('커피')
push('녹차')
# push('꿀물')
# push('콜라')
# push('환타')
# print('바닥 :', stack)
#
# push('밀키스') # -> 스택이 꽉 찼습니다.

## pop, peek
retData = pop()
print('팝 ->', retData)
print('다음 예정 :', peek())
retData = pop()
print('팝 ->', retData)
retData = pop()
print('팝 ->', retData)
print('바닥 :', stack)


