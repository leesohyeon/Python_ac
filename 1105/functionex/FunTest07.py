# 파라미터 초기값 설정하기

def showInfo(name,age,gender="남성"):
    print("이름은 %s입니다"%name)
    print("나이는 %d입니다"%age)
    print("%s입니다"%gender)

showInfo("홍길동",15)
print()
showInfo("하늬",10,"여성")