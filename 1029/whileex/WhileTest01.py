#while 문

# 10번찍어 안넘어가는 나무 없다!
# 라는 속담을 코드로 구현해보자!

treehit = 0

while treehit<10:
    treehit += 1    #treehit = treehit+1
    print("나무를 %d번 찍었습니다" %treehit)

    if treehit ==10:
        print("나무 넘어갑니다~")