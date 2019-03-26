#조건1) 사용자가 1~5이외의 수를입력하면 잘못입력했어요~
# 조건2) 영수증 출력

menu = """
***코리아 카페***
1.사슴의 눈물 :7000원
2.참새의 아침식사 : 5000원
3.안돼요 공주님 : 6000원
4.검은물 : 2000원
5.종료
"""
num=0
total=0
while num!= 5:  #num이 5가 아닐때까지 반복하라!
    print(menu)
    num = int(input("메뉴를 선택하세요 :"))

    if num==1:
        print("사슴의 눈물")
        total += 7000
    elif num==2:
        print("참새의 아침식사")
        total += 5000
    elif num==3:
        print("안돼요 공주님")
        total += 6000
    elif(num==4):
        print("검은물")
        total += 2000

    if num>5:
        print("잘못 입력하셨습니다 1~5사이의 수만 입력해주세요")

print("총금액은 ",total,"원입니다")
