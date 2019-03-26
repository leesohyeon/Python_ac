"""
이름 그리고 국어, 영어, 수학 3개의 점수를 입력받아
총점과 평균을 구하기
"""
name=input("이름을 입력하세요 : ")
kor=int(input("국어점수 : "))
Eng = int(input("영어점수 : "))
math = int(input("수학점수 : "))

print(name+"님의 성적입니다")
print("국어 : ",kor)
print("영어 : ",Eng)
print("수학 : ",math)
print("총점 : ",(kor+Eng+math))
print("평균 : ",((kor+Eng+math)/3))

#---------------------------------

name=input("이름을 입력하세요 : ")
kor=int(input("국어점수 : "))
Eng = int(input("영어점수 : "))
math = int(input("수학점수 : "))
total=kor+Eng+math
avg = total/3

print(name+"님의 성적입니다")
print("국어 : ",kor)
print("영어 : ",Eng)
print("수학 : ",math)
print("%s님의 총점은 %d점이고 평균은 %d점입니다 "%(name,total,avg))