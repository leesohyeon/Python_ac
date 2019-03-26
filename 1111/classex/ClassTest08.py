# 상속

class Parent:

    parentVar = 100

    def say(self):
        print("말하기")

class Child(Parent):
    pass

hgd = Child()
print(hgd.parentVar)
hgd.say()

