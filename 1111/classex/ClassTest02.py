# Tv 클래스
"""
1. 변수
    1) 브랜드
    2) 색상
    3) 채널

2. 메서드
    1) channelUp()      : 채널 1증가
    2) channelDown()    : 채널 1감소
    3) remote(num)
        num == 1    드라마 채널
        num == 2    영화 채널
        num == 3    음악 채널
        num == 4    교육 채널
"""
class TV:
    brand=""
    color=""
    channel=0

    def channelUp(self):
        TV.channel+=1

    def channelDown(self):
        TV.channel-=1

    def remote(self,num):
       if num==1:
           print("드라마채널")
       elif num==2:
           print("영화채널")
       elif num==3:
           print("음악채널")
       elif num==4:
           print("교육채널")

    def showinfo(self):
        print("브랜드 : %s"%self.brand)
        print("색상 : %s"%self.color)
        print("채널 : %d"%self.channel)
tv=TV()
tv.brand="SAMSUNG"
tv.color="black"
tv.channel=1
tv.channelUp()
tv.channelUp()

tv.showinfo()
tv.remote()