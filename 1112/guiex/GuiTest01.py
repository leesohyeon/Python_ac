from tkinter import*

# 1.컨테이너 생성
win = Tk()

# 2.컴포넌트 생성(버튼)
b1=Button(win,text="one")
b2=Button(win,text="two")

# 3.배치 관리자
b1.pack()
b2.pack()

win.mainloop()
