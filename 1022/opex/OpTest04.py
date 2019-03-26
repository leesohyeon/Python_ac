'''
화폐매수 구하기

은행에서 손님이예그을 현금으로 인출하려 한다.
금액에 대한 최소 화폐매수를 알려주는 프로그램을 만들어보자!

예)65,700원
오만원     : 1장
만원      : 1장
오천원     :1장
천원      :0장
오백원     :1개
백원      :2개
'''
won = int(input("금액을 입력해주세요 : "))
omanwon = won // 50000
print("오만원권 : ",omanwon,"장")
won-=omanwon*50000

manwon = won // 10000
print("만원권 : ",manwon,"장")
won-=manwon*10000

ochunwon = won // 5000
print("오천원권 : ",ochunwon,"장")
won-=ochunwon*5000

chunwon = won // 1000
print("천원권 : ",chunwon,"장")
won-=chunwon*1000

obaekwon = won // 500
print("오백원 : ",obaekwon,"개")
won-=obaekwon*500

baekwon = won // 100
print("백원 : ",baekwon,"개")