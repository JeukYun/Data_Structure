## 원형 큐 ##
# (rear + 1) % SIZE >> 코드로 원형큐를 만들 수 있음.
# 특징 : 마지막 한칸은 사용되지 않는다.
# -> 마지막 칸까지 사용하는 경우 front == rear인 경우 꽉 찬것과 텅 빈것이 똑같이 인식됨(isQueueEmpty)

## 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear + 1) % SIZE == front: # rear가 SIZE를 넘어가면 다시 0부터 증가하도록 함
        return True
    else :
        return False


def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data


def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print("큐가 비었습니다.")
    else:
        front = (front + 1) % SIZE
        data = queue[front]
        queue[front] = None
        return data


def peek() :
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐가 비었습니다.')
        return
    return queue[(front+1) % SIZE]




## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0


## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
print('출구<--',queue,'<--입구')


retData = deQueue()
print('식사 손님 :', retData)
retData = deQueue()
print('식사 손님 :', retData)
print('출구<--',queue,'<--입구')

enQueue('제욱')
print('출구<--',queue,'<--입구')

enQueue('길동')
print('출구<--',queue,'<--입구')

