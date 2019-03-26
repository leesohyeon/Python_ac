'''
***코리아은행 ATM***
1.잔액조회
2.현금인출
3.계좌이체
4.종료

잔액 : 10,000원
비밀번호 = 1234

num = 번호입력
1)3번을 제외하고 실습!
2)1번 완료 후 3번을 추가
3)비밀번호 3회이상 오류 입력시 , "가까운 은생지점을 방문해주세요"
----------------------------------
4)초기시작시 비밀번호 설정 위한 질문
    비밀번호 3회 오류 입력시 비밀번호 초기화
    재실행시 비밀번호 설정
'''

money=10000
pw=""
account = "01041954927"
error=3
while True:
    print('''
    ***코리아은행 ATM***
       1.잔액조회
       2.현금인출
       3.계좌이체
       4.종료
    ''')
    pw=input("비밀번호를 설정해주세요 :")
    num = int(input("원하는 서비스를 선택해주세요 : "))
    if num==1:
        pw = int(input("서비스를 이용하려면 비밀번호를 입력해주세요 : "))
        if pw==pw:
            print("잔액은 ",money,"원 입니다")
        else:
            if error>0:
                print("비밀번호를 확인해주세요")
                error -= 1
            elif error==0:
                print("비밀번호 입력횟수를 초과했습니다. 첫 화면으로 돌아갑니다")

    elif num==2:
        pw = int(input("서비스를 이용하려면 비밀번호를 입력해주세요 : "))
        if pw==pw:
            withdrawal= int(input("얼마를 출금하시겠습니까? :"))

            if withdrawal <= money:
                print("출금가능. %d원이 출금되었습니다"%withdrawal)
                money-=withdrawal

            elif withdrawal>money:
                print("잔액이 부족합니다")


        else:
            if error > 0:
                print("비밀번호를 확인해주세요")
                error -= 1
            elif error == 0:
                print("비밀번호 입력횟수를 초과했습니다. 첫 화면으로 돌아갑니다")

    elif num==3:
         pw = int(input("서비스를 이용하려면 비밀번호를 입력해주세요 : "))
         if pw==pw:
            send=input("계좌를 입력해주세요 : ")
            if send == account:
                 deposit=int(input("얼마를 이체하시겠습니까? : "))
                 if deposit <= money:
                     print("이체가능. %d원이 이체되었습니다" %deposit)
                     money -= deposit

                 elif deposit > money:
                     print("잔액이 부족합니다")

            elif send != account:
                print("계좌번호가 다릅니다. 계좌번호를 확인해주세요")
         else:
             if error > 0:
                print("비밀번호를 확인해주세요")
                error -= 1
             elif error == 0:
                print("비밀번호 입력횟수를 초과했습니다. 첫 화면으로 돌아갑니다")

    elif num==4:
        print("서비스를 종료합니다")
        break