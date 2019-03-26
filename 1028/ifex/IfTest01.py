score = int(input("점수를 입력하세요 : "))

# ctrl + shift + enter
# case1)
# if score >= 60:
#     print("합격입니다.")
#     print("축하합니다.")

# case2)
res = int(score / 60)
# 0 ~ 59점       =>  0 (False)
# 60 ~ 100점     =>  1 (True)

if res:
    # res가 1이면 True
    print("합격입니다.")
    print("축하합니다.")







