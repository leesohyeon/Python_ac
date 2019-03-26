class  man:
    cnt=0
    # 생성자 매서드
    def __init__(self,name):
        self.name = name
        print("%s가 만들어지는 중..."%self.name)
        man.cnt +=1

        #die 매서드
    def die(self):
        print("%s가 죽었습니다.."%self.name)
        man.cnt -=1
        if man.cnt==0:
            print("%s는 마지막 생존자 였습니다"%self.name)
        else:
            print("아직 %d명의 생존자가 남아있다"%man.cnt)

ch1 = man("몬스터1")
ch2 = man("몬스터2")
ch3 = man("몬스터3")

ch3.die()