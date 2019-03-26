import turtle as t
import random
random.randint(1,5)
import time

t.bgcolor("#FFEAEA")

t1=t.Turtle()
t1.shape("turtle")
t1.speed(0)
t1.up()
t1.goto(-300,200)
t1.color("#F15F5F")
t1.write("1번 거북이",False,"left",("",15,"bold"))

t2=t.Turtle()
t2.shape("turtle")
t2.speed(0)
t2.up()
t2.goto(-300,100)
t2.color("#F29661")
t2.write("2번 거북이",False,"left",("",15,"bold"))

t3=t.Turtle()
t3.shape("turtle")
t3.speed(0)
t3.up()
t3.goto(-300,0)
t3.color("#F2CB61")
t3.write("3번 거북이",False,"left",("",15,"bold"))

t4=t.Turtle()
t4.shape("turtle")
t4.speed(0)
t4.up()
t4.goto(-300,-100)
t4.color("#47C83E")
t4.write("4번 거북이",False,"left",("",15,"bold"))

t5=t.Turtle()
t5.shape("turtle")
t5.speed(0)
t5.up()
t5.goto(-300,-200)
t5.color("#A566FF")
t5.write("5번 거북이",False,"left",("",15,"bold"))

line= t.Turtle()
line.pensize(3)
line.up()
line.goto(300,-300)
line.down()
line.goto(300,300)
line.write("골인지점",False,"center",("",20,"bold"))
line.ht()#거북이 숨기기

time.sleep(2)

for i in range(100):
    a= random.randint(0,25)
    t1.forward(a)

    b = random.randint(0, 25)
    t2.forward(b)

    c = random.randint(0, 25)
    t3.forward(c)

    d = random.randint(0, 25)
    t4.forward(d)

    e = random.randint(0, 25)
    t5.forward(e)

t.exitonclick()
