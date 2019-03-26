print(10)
print(3.14)
print("문자")

print("Python" +"class")
#print("숫자와 연결할래~" + 10) #TypeError: must be str, not int

#문자와 숫자를 연결할때에는
#콤마(,)를 구분자로 연결한다.
print("문자",10)

#문자열 포맷팅(format)
"""
1.구조
    print("%포맷팅문자" % 값)
    print("%포맷팅문자1,%포맷팅문자2" % (값1,값2))
    *2개 이상의 값을 사용할 때에는 괄호로 반드시 묶어줘야 한다!!!

2.포맷팅문자
    정수          : %d (decimal)
    실수          : %f (float)
    문자 하나     : %c (character)
    문자 여러개   : %s (string)
"""
print("나이는 %d세 입니다" %25)
print("키는 %.2fcm입니다" %188.18)
print("혈액형은 %c형 입니다" %'B')
print("국적은 %s입니다" %"대한민국")

print("국어 점수는 %d점이고, 학점은 %c입니다." % (100,'A'))