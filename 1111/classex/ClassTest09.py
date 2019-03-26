# 오버라이딩(overriding)
# ~을 기각하다, ~을 무시하다

"""
사람              # 부모
- 이름
- 나이
- 사랑()

학생(사람):
- 학번
근로자(사람):
- 급여
"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def love(self):
        print("사랑해~")

class Student(Person):
    def __init__(self,name,age,id):
        self.id=id
    def love(self):
        print("우정해~")

class Employee(Person):
    def __init__(self,name,age,salary):
        self.salary=salary
    def love(self):
        print("뫵뫵해~")

stu =Student("홍길동",15,1234)
stu.love()
cyj = Employee("최여정",20,4567)
cyj.love()