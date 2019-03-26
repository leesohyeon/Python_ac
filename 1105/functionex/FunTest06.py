def sum(num1,num2):     #num은 마치 리스트 자료형처럼 적용된다
    return num1+num2

result = sum(10,20)
print("두수의 합=",result)

def sum(*num):
    tot=0
    for i in num:
       tot+=i
    return tot
r1=sum(10,20,30)
r2=sum(1,2,3,4,5,6,7,8,9,10)
print(r1)
print(r2)

def calc(res,*num):
    if res == "덧셈":
        tot=0
        for i in num:
            tot += i
    elif res == "곱셈":
        tot=1
        for i in num:
            tot *= i
    return tot
r1=calc("덧셈",1,10)
r2=calc("곱셈",1,2,4,9)
print(r1)
print(r2)

