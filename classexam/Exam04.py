# Exam04

class FirstClass:

    def setData(self, value):
        self.data = value

    def display(self):
        print(self.data)

class SecondClass(FirstClass):

    #정답
    #
    #

z = SecondClass()
z.setData(42)
z.display()

"""
현재의 value = "42"가 출력될 수 있도록 코드를 완성해보세요.
"""