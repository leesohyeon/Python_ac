#식별연산자
"""
is          :값이 같다면 참
is not      :값이 같지 않다면 참
"""

num1 = 10
num2 = 10
print(num1 is num2)     #True
print(num1 is not num2) #False

#멤버 연산자
"""
in      :멤버 안에 값이 있어야 참이다
not in  :멤버 안에 값이 없어야 참이다.
"""
nums = [1,2,3,4,5]    #리스트
           #1~5 = 멤버
print(1 in nums)
print(10 in nums)
print(7 not in nums)    #True



