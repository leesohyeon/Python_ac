"""

"""
def check(id, pw):

    accounts = [
        ("kildong", "qwer1234"),
        ("dangoon", "garlic"),
        ("harrypotter", "malfoy"),
    ]
    for (dbid,dbpw) in accounts:
        if dbid == id:
            if dbpw==pw:
                return 1
            else:
                return 0
    return -1
"""
    id와 pw를 전달받아서 그 결과를 정수형으로 반환하는 check함수 만들기!
    1. id가 존재하지 않을 경우   : return -1
    2. id는 존재O, pw가 틀린경우 : return 0
    3. id와 pw 모두 일치할 경우  : return 1
"""

def login():
    myid = input("ID : ")
    mypw = input("PW : ")
    num = check(myid,mypw)
       # num은 -1, 0, 1

    if num==-1:
        print("존재하지 않는 id입니다.")
    elif num==0:
        print("비밀번호가 틀립니다.")
    elif num==1:
        print("환영합니다. %s님"%myid)
    """
    1. num이 -1이면,     "존재하지 않는 id입니다."
    2. num이 0이면,      "비밀번호가 틀립니다."
    3. num이 1이면,      "환영합니다. id님"
    """
login()


















