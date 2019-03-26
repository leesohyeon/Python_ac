# Exam02

class Meeting:

    # 정답
    def name(self,name):
        self.name=name
        print("%s님 어서오세요!"%name)

    def talk(self):
        print("%s 님과 대화 중입니다..." % self.name)

f1 = Meeting("이병재")
f2 = Meeting("박영호")
f1.talk()
f2.talk()

"""
이병재님 어서오세요!
박영호님 어서오세요!
이병재 님과 대화 중입니다.
박영호 님과 대화 중입니다.
"""


