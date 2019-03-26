'''
문제 )
        반복문을 통해 numbers의 리스트요소를 3으로 나눠보자
        이때 0이라는 요소를 3으로 나누려 하면, 에러가 발생할 것이다.
        try-except를 통해 예외처리를 해보자!
'''

numbers=[0.2,2.5,0,10]

for i in numbers:
    try:
        print(3/i)
    except ZeroDivisionError:
        print("연산할 수 없음")