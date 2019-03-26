class tv:
    brand=""
    channel = 0

    def __init__(self,b,c):
        # print("나 불럿니?")
        self.brand = b
        self.channel = c
    def showinfo(self):
        print("브랜드: %s"%self.brand)
        print("채  널: %d"%self.channel)

mytv=tv("LG",7)
# mytv.brand = "LG"
# mytv.channel = 7