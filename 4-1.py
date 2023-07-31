## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

## 변수

## 메인
node1 = Node()
node1.data = '다현'

node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5


print(node1.data, end=' ')
print(node2.data, end=' ')
print(node3.data, end=' ')
print(node4.data, end=' ')
print(node5.data, end=' ')

print("")

print(node1.data, end=' ')
print(node1.link.data, end=' ')
print(node1.link.link.data, end=' ')
print(node1.link.link.link.data, end=' ')
print(node1.link.link.link.link.data, end=' ')

## 노드 삽입
# newNode = Node()
# newNode.data = '제욱'
# newNode.link = node2.link
# node2.link = newNode

## 노드 삭제
node2.link = node3.link # 쯔위의 링크 : 사나 -> node2의 링크에 대입
del(node3)

print("")
current = node1
print(current.data, end=' ')
while (current.link != None) : 노드의 링크가 없을 때 까지 출력
    current = current.link
    print(current.data, end=' ')



# print("")
# print(node1.data, end=' ')
# print(node1.link.data, end=' ')
# print(node1.link.link.data, end=' ')
# print(node1.link.link.link.data, end=' ')
# print(node1.link.link.link.link.data, end=' ')
# print(node1.link.link.link.link.link.data, end=' ')

