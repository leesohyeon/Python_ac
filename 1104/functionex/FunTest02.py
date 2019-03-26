'''
입려받은 숫자가 홀수이면 홀수 반환
짝수이면 짝수반환
'''
def hol(num):
    if num%2==0:
        result="짝수"
    elif num%2==1:
        result="홀수"
    return result
num=int(input("숫자 하나를 입력해주세요 : "))
msg=print(num)
print(msg)