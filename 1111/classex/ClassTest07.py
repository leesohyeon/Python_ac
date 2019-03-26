'''
제품의 가격과 수량을 넘겨주면,
 총 금액을 알려주는 프로그램을 만들어보세요

 class Payment:
    변수..
    메서드..
'''
# 1. 06.py 파일을 외워서, 스스로 작성해보기!
# 2. 할인율을 추가해서, 할인가격도 출력해보기!
class Payment:
    counter=0
    discount = 0.5
    def __init__(self,price,number):
        self.price=price
        self.number=number
        Payment.counter+=1

    def cal(self):
        self.tot=self.price*self.number
        self.dcpay=self.price - (self.price * Payment.discount)

    @classmethod      #할인율을 변경하는 메서드
    def update(cls,value):
        # 0<할인율<1
        # 만일 사용자가 위의 범위에서 벗어난 할인율을 적용하려 할때
        # 다시 입력받도록 하자
        while (0>value or value>=1):
            value = float(input("할인율을 다시 입력하세요"))
        cls.discount = value

    @staticmethod
    def message():
        print("어서오세요")
        print("할인행사중입니다")



    def showinfo(self):
        print("%s번째 제품입니다"%Payment.counter)
        print("정가 : %d"%self.price)
        print("정상가격 : %d"%self.tot)
        print("할인가격 : %d"%self.dcpay)


notebook = Payment(1000,5)
notebook.cal()
notebook.showinfo()
