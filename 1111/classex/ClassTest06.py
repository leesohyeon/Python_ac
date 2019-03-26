'''
제품의 가격과 수량을 넘겨주면,
 총 금액을 알려주는 프로그램을 만들어보세요

 class Payment:
    변수..
    메서드..
'''
class Payment:
    counter=0
    def __init__(self,pay,number):
        self.pay=pay
        self.number=number
        Payment.counter +=1

    def cal(self):
        self.tot=self.pay*self.number

    def showinfo(self):
        print(Payment.counter,"번째 제품입니다.")
        print("정가 : %d"%self.pay)
        print("금액 : %d"%self.tot)

notebook=Payment(1000,5)
notebook.cal()
notebook.showinfo()
