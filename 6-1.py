## 함수

## 변수
stack = [None, None, None, None, None]
top = -1


## 메인

#Push()
top += 1
stack[top] = '커피'

top += 1
stack[top] = '녹차'

top += 1
stack[top] = '꿀물'

print('바닥 :', stack)

# Pop()
data = stack[top]
stack[top] = None
top -= 1
print('pop ->', data)

data = stack[top]
stack[top] = None
top -= 1
print('pop ->', data)

data = stack[top]
stack[top] = None
top -= 1
print('pop ->', data)
print('바닥 :',stack) # push의 반대 순으로 출력되어 나옴