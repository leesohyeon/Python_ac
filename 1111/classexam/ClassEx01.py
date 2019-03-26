# Exam01

class SayMyName:
    def __init__(self, myname):
        self.myname = myname

    def say(self):
        print("나의 이름은", self.myname, "입니다.")

# 정답
myname=SayMyName("이정우")

myname.say()

"""
콘솔 창에 아래 문장이 출력될 수 있도록 위의 코드를 작성해보세요.
나의 이름은 이정우 입니다.
"""