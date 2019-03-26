#변수는 오직 "대입연산자"를 통해서만
#값의 변경이 가능하다

num=10

print("변경 전 :",num)
print(num+1)    #11
print(num)      #10

num=num+1
print("변경 후 :",num)

x=10
y=5
tmp=0

#두 수를 바꿔보세요

tmp=x   #tmp=10
x=y     #x=5
y=tmp   #y=5
print("x :",x)
print("y :",y)

name="이소현"
address=" 서울시 용산구"

print("%s님은 %s에 삽니다"%(name,address))

"""
1.카멜표기법
    소문자로 시작하고, 두번째단어가 등장하면
    첫글자를 대문자로 작성한다
    ex)iPhone,myName
    
2.헝가리안 표기법
    접두사를 붙인다.
    strNum="100"
"""