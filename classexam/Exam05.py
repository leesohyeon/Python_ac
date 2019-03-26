# Exam05

class Animal:

    #정답
    #
    #
    def talk(self):
        return "없음"

class Cat(Animal):

    def talk(self):
        return "야옹"

class Dog(Animal):
    #정답
    #
    #

animals = [ Cat("하얀 고양이"),
            Cat("검은 고양이"),
            Dog("강아지")]

for i in animals:
    print(i.name + ": " + i.talk())

"""
하얀 고양이: 야옹
검은 고양이: 야옹
강아지: 멍멍
"""






