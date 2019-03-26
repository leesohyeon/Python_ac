# grid관리자
from tkinter import*

# 4.이벤트
def fun1() :
    print("one 버튼 눌렀다")
def fun2() :
    print("two 버튼 눌렀다")
def fun3() :
    print("three 버튼 눌렀다")


#1.컨테이너 생성
win = Tk()

# 2.컴포넌트 생성
b1=Button(win,text="one",command=fun1)
b2=Button(win,text="two",command=fun2)
b3=Button(win,text="three",command=fun3)
b4=Button(win,text="종료",command=win.quit())


# 3.배치 관리자
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=1,column=0,columnspan=3)

win.mainloop()