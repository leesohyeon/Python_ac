'''
Exam01
[1,3,5,4,2]라는 리스크를 [5,4,3,2,1]로 만들어 보자!
'''
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)
print()

'''
Exam02
아래의 리스트에서 
"korea",3,8 을 각각 출력해보자
'''
a=["korea",["IT",[1,3,5,7,9]],["EVEN",[0,2,4,6,8]]]
print(a[0])
print(a[1][1][1])
print(a[2][1][4])
print()

#Exam03
print("==================")
print("      파이썬      ")
print("==================")
subject=["자료형","제어문","입출력","클래스"]
level = [3,1,5,7]
#subject와 level을 이용하여
# 이후 아래의 결과가 출력되도록 완성해보자.
'''
==================
      파이썬
==================
자료형★
제어문★★★
입출력★★★★★
클래스★★★★★★★
'''
level.sort()
print(subject[0]+("★"*level[0]))
print(subject[1]+("★"*level[1]))
print(subject[2]+("★"*level[2]))
print(subject[3]+("★"*level[3]))
print()

#Exam04
a = ["Life","is","too","short"]
print(a[0]+" " +a[1]+" " +a[2]+" " +a[3])
