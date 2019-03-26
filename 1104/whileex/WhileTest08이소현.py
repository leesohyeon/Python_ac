'''
up& down

1.컴퓨터로부터 임의의 수 하나를 입력받기
2.사용자로 부터 숫자 한개 입력
3. answer > num   => up
   answer < num    => down
   answer == num   =>정답
4. 5번의 기회모두 소진시 종료
'''
import random
answer=random.randint(1,10)
play=5
while True:
    num= int(input("숫자 하나를 입력해주세요"))
    if play>0:
        if num<answer:
            print("UP!!")
            print()
            play -= 1
        elif num>answer:
            print("DOWN!!")
            print()
            play -= 1
        elif num==answer:
             print("정답입니다!")
             print()
             play -= 1
             break
    elif play == 0:
        print("기회를 모두 소진하였습니다")
        break