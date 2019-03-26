#양수, 음수의 개수를 출력해보세요
lst = [1,-10,40,50,-40]
plus=0
minus=0
for i in lst:
    if i<0:
        minus+=1
    elif i>0:
        plus+=1
print("양수는 %d개 , 음수는 %d개 입니다"%(plus,minus))
print()
'''
1단계 :  철수가 은행에 500원 입금
그리고 은행은 하루에 이자 1원씩
5일후 잔액은?

2단계 :  원금과 예치일 수를 입력받아 처리

3단계 : 2단계 + 이자 매일 1씩 증가
'''

money=int(input("원금을 입력하세요 : "))
day=int(input("예치일 수를 입력하세요 : "))
won=0
won=money
day1=0
for i in range(day):
    money+=i+1  #+1뒤에안해주면 0,1,2,3,4 순으로
print("입금한 금액은 %d원 이고 %d일간 맡겨서 총 %d원이 되었습니다"%(won,day,money))

