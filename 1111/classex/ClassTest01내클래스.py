'''
person 클래스
1.변수 :속성, 특징
    이름 (name)
    나이 (age)
    성별 (gender)
    혈액형 (blood)
    주민번호 (jumin)

2.매서드(변수) : 기능
    말하다
    걷다
    먹는다
'''

class mirim:
    # 변수
    grade=0
    ban=0
    totmember=0
    teacher=""
    banjang=""
    # 메서드(함수)
    def say(self):
        print(self.teacher+"선생님네 반")
        print()

    def showinfo(self):
        print("%d학년"%self.grade,end="")
        print("%d반"%self.ban)
        print("반 총 인원 : %d"%self.totmember)
        print("담임선생님 : %s선생님"%self.teacher)
        print("반장 : %s"%self.banjang)

lsh=mirim()
lsh.grade=1
lsh.ban=6
lsh.totmember=20
lsh.teacher="김영철"
lsh.banjang="임소영"

lsh.say()
lsh.showinfo()

