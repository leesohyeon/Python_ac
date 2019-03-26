# 3일차 review 강사님 코드
#Exam01
'''
영희의 주민등록번호는 870612-2078321이다
영희의 주민등록번호를 870612 부분과
그 뒤의 2078321부분으로 나누어출력해보자
'''
pin = "876012-2078321"
print("영희의주민등록번호 나누기")
yyyymmdd = pin[:6]
num=pin[7:]
print(yyyymmdd)
print(num)
print()

#Exam02
'''
korea YT 라는 문자열을 koreaIT로 제대로 수정해보자
'''
print("korea YT 수정하기")
# 문자열을 값의 수정이 불가한 데이터이다. immutable

a="korea YT"
# a[6] = 'I'       #TypeError: 'str' object does not support item assignment
a = a[:6]+'I'+a[7]
print(a)
print()
#Exam03
'''
Hello world 라는 문자열을 Hello python으로 수정해보자
'''
a="Hello world"
print(a.replace("world","python")) #두가지 방법
print(a[:5]+" python")              #replace함수 사용 /  슬라이싱 사용
print()

#Exam04
'''
화씨온도(f)를 섭씨온도로 변환할 때에는 다음과 같은 공식을 사용한다
c = (f-32)/1.8
이 공식을 사용해 화씨온도 (f) 50일때의 온도를 계산해보자
'''
print("섭씨온도로 바꾸기")
f=50
c=(f-32)/1.8
print(c)
print()

#Exam05
'''
일주일이 몇분인지를 계산해보자
'''
print("일주일이 몇분인지")
minutesperhour=60
hourperday=24
dayperweek= 7
print((minutesperhour*hourperday)*dayperweek)
print()
#Exam06
"""
문자열의 연산을 이용하여 다음과 같이 출력해보자
===================
    My Program
===================    
"""
print('='*15)
print("   MY PROGRAM")
print('='*15)
print()

#Exam07
'''
다음(daum)의 주가가 8,900원이고
네이버(naver)의 주가가 751,000이라고 가정을 한다면,
어떤사람이 다음 주식 100주와 네이버 주식 20주를 가지고 있을때 
그사람이 갖고 있는 주식의 총액을 계산하는 프로그램을 작성해보자.
'''
daum=8900
naver=751000
total=daum*100+naver*20
print(total)