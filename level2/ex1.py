def keyword(**data): #딕셔너리 데이터 받기
    print(data)

keyword(id=1,username="ssar")

n1 = 1

def var_test():
    global n1
    n1=2

var_test()
print(n1)