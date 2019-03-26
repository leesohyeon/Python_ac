while True:
    try:
        n=input("정수 : ")
        n=int(n)
        break
    except ValueError as e:
        print("정수가 아닙니다. 다시 입력하세요")
        print(e)
print("입력하신 정수 : %d"%n)