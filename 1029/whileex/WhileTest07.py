#보조제어문
'''
break       :반복문 종료
continue    :반복문을 빠져나가지 않고
             다시 맨 처음(조건문)으로 돌아가게 된다

    1~10까지의홀수를 출력해보세요!
'''

num=0

while num<10:
    num+=1
    if num%2==1:
        print(num)

# continue문을 활용해서 다시 구현해보자!

num=0

while num<10:
    num+=1
    if num%2==0:
        continue
    else:
        print(num)