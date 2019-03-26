# ValueError
# ZeroDivisionError

try:
    x= float(input("숫자를 입력하세요 : "))
    result= 3/x
    print("결과 :",result)
# except ValueError:
#     #문자를 입력했을때
#     print("숫자를 입력하셔야 해요~")
# except ZeroDivisionError:
#     #0으로 나누려 할때
#     print("0으로 나눌 수 없어요")

except Exception:
    print("모든 예외 처리해준대~")
finally:
    print("예외발생 여부와 무관하게 무조건 실행할 코드를 여기에 넣어~")