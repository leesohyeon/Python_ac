class Card:

    # 변수(속성,특징)
    width = 150         # 클래스 변수
    height = 250

    # shape = ""
    # number = 0

    def __init__(self, shape, number):
        self.shape = shape      # 인스턴스(객체) 변수
        self.number = number

c1 = Card("heart", 4)
c2 = Card("spade", 7)

# 클래스 변수 호출방법
# print(Card.width)
# print(Card.height)

# 객체(인스턴스) 변수 호출방법
# print(c1.shape)
# print(c1.number)

Card.width = 250
Card.height = 150
print(c1.width)
print(c2.width)
print(c1.height)
print(c2.height)

