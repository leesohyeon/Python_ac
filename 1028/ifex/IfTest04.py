"""
사용자로부터 정수를 입력받아
정수의 부호에 따라 거북이를 움직여보자!
양수(100, 100)
0(100, 0)
음수(100, -100)
"""
import turtle as t

t.shape("turtle")

t.up()
t.goto(100, 100)
t.write("거북이가 여기로 오면, '양수' 입니다.")

t.goto(100, 0)
t.write("거북이가 여기로 오면, '0' 입니다.")

t.goto(100, -100)
t.write("거북이가 여기로 오면, '음수' 입니다.")

t.goto(0, 0)
t.down()

num = int(input("숫자를 입력하세요 : "))

if num > 0:
    t.goto(100, 100)
if num == 0:
    t.goto(100, 0)
if num < 0:
    t.goto(100, -100)

t.exitonclick()


























