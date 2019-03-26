# 사용자 정의 예외
# raise 키워드를 통해 프로그래머가
# 일부로 예외상황을 만들 수 있다.

def errMake():
    num = int(input(("1~5사이의 정수를 입력하세요 : ")))

    if num < 1 or num>5:
        raise           #에러를 발생시키는 키워드
    else:
        print("입력한 정수는  %d"%num)

    try:
        errMake()
    except:
        print("예외가 발생했어요!")