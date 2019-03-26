# ex01

a=20 #전역변수

def test(num):
    num=10  #지역변수

print(a)
# print(num)

# ex02
def func(b):
    b=b+1
    print(b)

func(30)

# ex03
a=10

def func(num):
    num+=1
    return num

a=func(a)
print(a)

# ex04
b=100
def func():
    global b
    b=b+1
func()
print("전역변수 :",b)






