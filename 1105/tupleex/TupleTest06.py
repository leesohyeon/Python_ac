# 타자연습게임

import random
import time

print("==========================")
print("        타자연습          ")
print(" Enter를 누르면 게임 시작 ")
print("==========================")

input(":")

question = ["python","C","Java","JSP","Android"]
start=time.time()

count = 1
random.shuffle(question)        #문제 섞기

while True:
    print("문제",count)
    print(question[0])
    answer=input("=>")

    if question[0]==answer:
        print("통과!")
        question.pop(0)
        count += 1
        random.shuffle(question)
    else:
        print("오타! 다시도전!")
        # question(빈공간) =>True
        #not False       => True
    if not question:
        end= time.time()
        result = end-start
        print("=====================================")
        print("  모든 문제를 정확하게 맞히셨습니다  ")
        print("    걸린 시간은 총 %.1f초 입니다     "%result)
        print("=====================================")




