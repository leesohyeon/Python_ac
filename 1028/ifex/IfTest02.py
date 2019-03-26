score = int(input("점수를 입력하세요 : "))

msg = ""

if score >= 60:
    # 점수가 60점 이상일 때
    # print("합격입니다.")
    msg = "합격"
else:
    # 점수가 60점 미만일 때
    # print("불합격입니다.")
    msg = "불합격"

print("귀하의 점수는 %d점으로 %s입니다." % (score, msg))

# Quiz1
# 정수 한개를 입력받아, 그 수가 짝수인지 홀수인지 판단해보자!
num = int(input("정수 한개를 입력하세요 : "))

msg = ""

if num % 2 == 0:
    msg = "짝수"
else:
    msg = "홀수"

print("입력하신 숫자 %d(은)는 %s 입니다." % (num, msg))

# Quiz2
"""
id = "koreaIT"
pw = "1234"

사용자로부터 아이디와 패스워를 입력받아,

아이디와 패스워드 일치,   koreaIT님 로그인 되었습니다.
아이디와 패스워드 불일치, 아이디와 패스워를 확인해주세요.
"""
# 강사님과 함께..
dbId = "koreaIT"
dbPw = "1234"

myId = input("아이디를 입력하세요 : ")
myPw = input("패스워드를 입력하세요 : ")

if dbId == myId and dbPw == myPw:
    print("%s님 로그인 되었습니다." % myId)
else:
    print("아이디와 패스워드를 확인해주세요.")

















