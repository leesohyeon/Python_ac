#input() 함수 :사용자로부터 입력받기
#파이썬 2.7버전의 경우 raw_input()

name = input("이름을 입력하세요 : ")
print("입력하신 이름은 " + name+"입니다.")

#외부로 부터 입력받는 데이터는 "문자"타입입니다
#때문에 이를 정수타입으로 "형변화"시켜야한다.
num1 = input("정수1을 입력하세요 : ")
num2 = input("정수2를 입력하세요 : ")
print("두 수의 합 : ", (num1+num2)) #"10" + "20" = 1020

#복제 : ctrl + d
#이동 : alt + shift + 방향키(위,아래)

#case1
num1=int(num1)
num2=int(num2)
print("두 수의 합 : ", (num1+num2)) #"10" + "20" = 1020

#case2
x=int(input("정수1입력: "))
y=int(input("정수2입력: "))
print("두 수의 합 : ", (x+y)) #"10" + "20" = 1020
