## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()


def insertNode(findData, insertData):
    global memory, head, current, pre
    # Case1 : head 앞에 데이터 삽입하는 경우
    if (head.data == findData):
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    # Case2 : 중간 노드 앞에 삽입
    current = head
    while (current.link != None):
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    # Case3 : 없는 노드 앞에 삽입(==추가)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return


def deleteNode(deleteData):
    global memory, head, current, pre
    # Case1 : head 삭제
    if (head.data == deleteData):
        current = head
        head = head.link
        del (current)
        return
    # Case2 : 중간 노드 삭제
    current = head
    while (current.link != None):
        pre = current
        current = current.link
        if (current.data == deleteData):
            pre.link = current.link
            return
    # Case3 : 삭제 할 노드가 없음
    return


def findNode(findData):
    global memory, head, current, pre
    current = head
    if (current == findData) :
        return current
    while (current.link != None):
        current = current.link
        if (current.data == findData):
            return current
    return Node()

## 변수
memory = []

# head : 첫번째 변수
head, current, pre = None, None, None
data_array = ['다현', '정연', '쯔위', '사나', '지효'] # 실제 사용 데이터 모음


## 메인
node = Node()
node.data = data_array[0] # '다현'을 head로 지정(첫 번째 노드)
head = node #
memory.append(node)

for i in data_array[1:]: # ['정연', '쯔위' ...]
    pre = node # '다현'을 pre에 대입
    node = Node()
    node.data = i
    pre.link = node # '다현'의 링크 : node
    memory.append(node) # 메모리 리스트에 추가

printNodes(head)


## 노드 삽입
## 1) 맨 앞 노드에 삽입
# insertNode('다현', '화사') # 다현 앞에 화사노드 삽입
# printNodes(head)

## 2) 중간 노드에 삽입
# insertNode('사나', '솔라')
# printNodes(head)


## 3) 찾는 노드가 없는경우
# insertNode('욱', '솔라')
# printNodes(head)


## 노드 삭제
## 1) 맨 앞 노드 삭제
# deleteNode('다현')
# printNodes(head)

## 2) 중간 노드 삭제
# deleteNode('쯔위')
# printNodes(head)

## 3) 삭제 할 노드가 없음
# deleteNode('제욱')
# printNodes(head)

## 노드 찾기
fNode = findNode('사나')
print(fNode.data, '뮤비가 나옵니다. ~~ 쿵짝쿵짝')