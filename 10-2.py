## 함수
import random

def findMinIndex(ary):
    minIndx = 0
    for i in range(1,len(ary)):
        if ary[minIndx] > ary[i]:
            minIndx = i
    return minIndx


## 변수
before = [random.randint(30,190) for _ in range(8)]
after = []


## 메인
print('정렬 전 -->', before)

for i in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del before[minPos]

print('정렬 후 -->', after)