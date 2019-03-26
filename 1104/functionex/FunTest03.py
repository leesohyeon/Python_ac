'''
아이디 패스워드 전달받아
둘다 일치시 1리턴
아이디만 일치ㅣ 0리턴
아이디 불일치 -1리턴
'''
# result=0
# id=input("아이디를 입력해주세요 :")
# pw=input("패스워드를 입력해주세요 :")
# def id(dbid,dbpw):
#     if id==dbid and pw==dbpw:
#         result = 1
#     elif id==dbid and pw!=dbpw:
#         result = 0
#     elif id!=dbid:
#         result = -1
# num=id("thgus","1234")
# print(result)
dbid="thgus"
dbpw="1234"
def check(id,pw):
    if id==dbid:
        if pw==dbpw:
            result=1
        else:
            result=0
    else:
        result = -1
    return result
def login():
    myid=input("ID : ")
    mypw=input("PW : ")
    num=check(myid,mypw)
    if num==1:
        print("%s님 환영합니다"%dbid)
    elif num==0:
        print("비밀번호를 확인해주세요")
    elif num==-1:
        print("존재하지 않는 ID입니다")

login()
