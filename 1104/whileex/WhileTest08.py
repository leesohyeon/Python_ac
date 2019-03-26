# Up / Down Game
"""
1. 컴퓨터로부터 임의의 수를 반환하도록 한다.  answer
2. 사용자로부터 숫자 한개를 입력받는다.       num
3. answer > num     => Up!
   answer < num     => Down!
   answer == num    => 정답!
4. 5번 기회를 모두 소진하면, 프로그램은 종료된다.
"""
import random
import time

print("=" * 25)
print("      Up / Down Game")
print("=" * 25)
print("준비 되었으면, 엔터를 누르세요!")
input("=>")
start = time.time()

answer = random.randint(1, 10)      # 컴퓨터가 발생시킬 난수
count = 0                           # 횟수

while True:

    num = int(input("정답을 입력하세요 : "))

    if answer > num:
        count += 1
        print("Up!")
    elif answer < num:
        count += 1
        print("Down")
    else:           # answer == num
        end = time.time()
        result = end - start
        print("=" * 40)
        print("정답입니다! 정답은 %d 이었습니다." % answer)
        print("걸린시간은 %.1f 였습니다." % result)
        print("=" * 40)
        break

    if count == 5:
        print("=" * 30)
        print("5번의 기회를 모두 사용하였습니다.")
        print("다음에 한번 더 도전해주세요")
        print("=" * 30)
        break
