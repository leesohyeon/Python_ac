# 1)파라미터o 리턴값o
def sum(num1,num2):
    return num1+num2

result=sum(10,5)
print(result)

# 2)파라미터o 리턴값x
def sum(num1,num2):
    print("%d와 %d의 합은 %d입니다"%(num1,num2,num1+num2))
sum(10,5)

# 3)파라미터x 리턴값o
def sayHello():
    return "sayHello"
result=sayHello()
print(result)

# 4)파라미터x 리턴값x
def sayHi():
    print("hi")
sayHi()