"""
성별(남자:1, 여자:0)과 나이를 입력받아서
남자, 여자
성인, 미성년을 구분(18세이상 성인)하는 프로그램을 작성해보자!

18세 이상 : 성인
18세 미만 : 미성년자

숫자1 : 남자
숫자0 : 여자

=> 당신은 여자 성인입니다.
"""

gender = int(input("성별을 입력하세요(남자:1, 여자:0) : "))
age = int(input("나이를 입력하세요 : "))

msgGender = ""
msgAge = ""

if gender == 1:
    msgGender = "남성"
else:
    msgGender = "여성"

if age >= 18:
    msgAge = "성년"
else:
    msgAge = "미성년자"

print("당신은 " + msgGender + " 이고, " + msgAge + " 입니다.")



















