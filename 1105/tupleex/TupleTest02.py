#튜플의 요소 추출하기

t1 = (1,2,'a','b')
print(t1[0])
print(t1[1: ])
print(t1[:3])       #맨 처음부터 3미만까지

#튜플함수

#1.요소를 모두 더하는 함수 :sum()

tup = (1,2,3,4,5)
print(sum(tup))

# 2.튜플의 최대 최소값구하는 함수 :  max(), min()
print("최대값 :",max(tup))
print("최소값 :",min(tup))

# 3.요소의 개수를 모두 세는 함수 : count(요소)
print(tup.count(1))

# 4.요소의 인덱스 번호르 구하는 함수 : index(요소)
print(tup.index(4))






