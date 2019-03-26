#커피자판기 만들기
'''
커피는 10잔만 존재한다
while문을 통해 무한반복하다가
커피 10잔이 다 떨어지면 반복을 종료하자!

1.input함수를 통해 커ㅣ값을 입력받는다(커피값 300원)
2.200원 이상 입력하게 되면 거스름돈을 출력해준다
3.300원 이하를 받게 되면 돈이 부족하다고 출력해준다
4.300을 입력하게 되면 커피 나왔습니다 라고출력하준다
'''
coffee=3

while True:
    money=int(input("돈을 넣어주세요 :"))
    if money==300:
        money-300
        print("커피 나왔습니다!")
        coffee-=1

    elif money>300:
        coffee -= 1
        print("커피 나왔습니다 ~ 거스름돈은 %d원 입니다"%(money- 300))
    else:
        print("돈이 부족합니다..")
        print("300원을 넣어주세요~")

    if not coffee:      #coffee == 0 (false) ==>중요☆
        print("커피가 다 떨어졌어요~ 판매를 중단합니다.")
        break