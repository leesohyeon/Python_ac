# 주민등록번호를 입력받아서, (ex. 870612-2087421)
# 남성인지 여성인지 판단하는 프로그램을 만들어보자!

# 1, 3 == 남성
# 2, 4 == 여성

print("Hello"[0])

jumin = input("주민등록 번호를 입력하세요 : ")

gender = jumin[7]

if gender == '1' or gender == '3':
    print("남자")
elif gender == '2' or gender == '4':
    print("여자")








