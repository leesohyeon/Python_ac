import turtle as t
import random

screen = t.Screen()

image1 = "front.gif"
image2 = "back.gif"

screen.addshape(image1)
screen.addshape(image2)

coin = random.randint(0, 1)        # 0 또는 1을 랜덤하게 생성
#print(coin)
t1 = t.Turtle("turtle")

if coin == 0:
    t1.shape(image1)
    t1.stamp()
else:
    t1.shape(image2)
    t1.stamp()

t.exitonclick()










