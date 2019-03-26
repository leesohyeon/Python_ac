# 정수한개를 입력받아
# 그 수가 양수, 0, 음수인지 판단해보자!

num = int(input("정수를 입력하세요 : "))

if num > 0:
    print("양수입니다.")
elif num == 0:
    print("0입니다.")
elif num < 0:
    print("음수입니다.")
