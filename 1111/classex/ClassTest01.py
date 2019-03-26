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

class person:
    # 변수
    name=""
    age=0
    gender=""
    blood=""
    jumin=0
    # 메서드(함수)
    def say(self):
        print(self.name+"이 말합니다")

    def __init__(self,n,a,g,b,j):
        self.name=n
        self.age=a
        self.gender=g
        self.blood=b
        self.jumin=j

    def showinfo(self):
        print("이름 : %s"%self.name)
        print("나이 : %d"%self.age)
        print("성별 : %s"%self.gender)
        print("혈액형 : %s"%self.blood)
        print("주민번호 : %d"%self.jumin)

lsh=person("홍길동",20,"남자","B",1234)
# lsh.name="이소현"
# lsh.age=17
# lsh.gender="여자"
# lsh.blood="B"
# lsh.jumin= 10702

lsh.say()
lsh.showinfo()

