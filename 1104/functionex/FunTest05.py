#사칙연산 수행 프로그램[2단계]
def cal(num1,num2):
    print("덧셈       : %d" % (num1 + num2))
    print("뺄셈       : %d" % (num1 - num2))
    print("곱셈       : %d" % (num1 * num2))

def calc(num1,num2):
    if num2 != 0:
        cal(num1,num2)
        print("나눗셈      : %.1f" % (num1 / num2))
    elif num2==0:
        cal(num1, num2)
        print("0으로 나눌 수 없습니다")
num1=int(input("정수1 입력 : "))
num2=int(input("정수2 입력 : "))

calc(num1,num2)
