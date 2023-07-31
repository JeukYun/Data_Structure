## 함수
def add_data(friend):
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = friend

def insert_data(position, friend):
    # 1단계 빈칸 추가
    katok.append(None)
    # 2단계 마지막 칸부터 삽입칸 까지 한 칸씩 뒤로 이동
    klen = len(katok) # len(katok) : 7
    for i in range(klen-1, position, -1): # 마지막 ~ position 까지 -1 뒤로
        katok[i] = katok[i-1]
        katok[i-1] = None
    # 3단계 position 자리에 친구 입력
    katok[position] = friend

def delete_data(position):
    # 1단계 데이터 지우기
    katok[position] = None
    # 2단계 한칸식 앞으로 당기기
    klen = len(katok)
    for i in range(position + 1, klen, 1):
        katok[i-1] = katok[i] # 지효
        katok[i] = None
    # 3단계 마지막 칸 제거
    del(katok[klen-1])


## 변수
katok = []


## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')

print(katok)

add_data('모모')
print(katok)


insert_data(3,'미나')
print(katok)

delete_data(4)
print(katok)