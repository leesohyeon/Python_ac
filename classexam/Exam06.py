class Discount:
    def __init__(self, product):
        if product == "Clothing":
            self.dc = 0.6
        elif product == "Cap":
            self.dc = 0.7
        else:
            self.dc = 0.8

class Clothing(Discount):
    def __init__(self, count):
        #정답 : 바로 아래 2줄 작성하기
        #
        #
        print("옷 가격 :", int(50000 * self.count*self.dc))

class Cap(Discount):
    def __init__(self, count):
        #정답 : 바로 아래 2줄 작성하기
        #
        #
        print("모자 가격 :", int(10000 * self.count*self.dc))

class Other(Discount):
    def __init__(self, count):
        # 정답 : 바로 아래 2줄 작성하기
        #
        #
        print("기타 가격 :", int(20000 * self.count * self.dc))

Clothing(2)
Cap(2)
Other(2)

"""
옷 가격 : 60000
모자 가격 : 14000
기타 가격 : 32000
"""









