#리스트 관련 함수들

#1.요소 추가하기 : append()
lst=[1,2,3]
lst.append(4)   #리스트의 맨 마지막에 요소를 추가한다.
print(lst)

#2.리스트 확장 : extend()
lstA=[1,2,3]
lstB=[4,5,6]
lstA.extend(lstB)
print(lstA) #lstA 를 확장 함

# 3.리스트의 요소 삽입 : insert(a,b)
#                         a번째 위치에 b요소를 삽입
lst =[1,2,3]
lst.insert(0,4)
print(lst)

# 4.리스트 제거
lst = [1,2,3,4,5,6]
# lst = []
print(lst)
# =====OR======
lst.remove(3)       #3제거
print(lst)
#=====OR=====
# del(lst)
# print(lst)      #NameError: name 'lst' is not defined

# 5.정렬 : sort()
a=[1,4,2,3]
a.sort()
print(a)

# 6.리스트 뒤집기 : reverse()
a=['a','c','b']
a.reverse()  #바꾸는게 아니라 아얘 순서를 거꾸로 함
print(a)

pocket = ["paper","cellphone","money"]

if "money" in pocket:
    # print("택시타고 가")
    pass
else:
    print("걸어가")