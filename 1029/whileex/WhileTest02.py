#네이버 웹툰 : 계룡선녀전

menu = """
***코리아 카페***
1.사슴의 눈물 :7000원
2.참새의 아침식사 : 5000원
3.안돼요 공주님 : 6000원
4.검은물 : 2000원
5.종료
"""
num=0
while num!= 5:  #num이 5가 아닐때까지 반복하라!
    print(menu)
    num = int(input("메뉴를 선택하세요 :"))

    if num==1:
        print("사슴의 눈물")
    elif num==2:
        print("참새의 아침식사")
    elif num==3:
        print("안돼요 공주님")
    elif(num==4):
        print("검은물")