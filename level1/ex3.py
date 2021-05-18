# 1.리스트
list1 = [1,2,3,4]
list2 = [5,6,7,8]

print(list[2])
print('='*50)

list3 = list1 + list2
print(list3)

# 3 스칼라
#[1,3,4] 숫자의 방향이 있는 것을 벡터라고 함 (수직수평상관X)

# 2차원 matrix, 3치원 tensor
list4 = [
    list1,
    list2
] # 더하기 중요함 2차원 배열

print(list4)

list1.append(10)

print(list1)

list5 = [list1, 11]
print(list5)

del list1[0]
print(list1)

list1.remove(2)

print(list1)

list6 = list(range(10))
print(list6)

list7 = list(range(1,12)) # 마지막 인덱스 직전까지
print(list7)

# 2.튜플 - 리스트 같음. 데이터 변경이 불가능함
tuple1 = (1,2,3)
print(tuple1)

tuple2 = (4,5,6)
print(tuple2)

tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = (tuple1, tuple2)
print(tuple4)

# 3.딕셔너리