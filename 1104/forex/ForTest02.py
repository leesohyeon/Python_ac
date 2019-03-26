"""
총 5명의 학생이 시험을 보았는데,
시험점수가 60점 이상이면 합격이고,
60점 미만이면 불합격이다.
합격인지 불합격인지 그 결과를 알려주자!
"""
scores = [90, 50, 60, 44, 80]
count=0
# 1) for i in 리스트
# for i in scores:
#     if i>=60:
#         print("합격")
#     else:
#         print("불합격")
for i in scores:
    if i>=60:
        count+=1
        print("합격")
    else:
        count+=1
        print("불합격")
print()
# 2) for i in range()
for i in range(5):
    if scores[i]>=60:
        print("합격")
    else:
        print("불합격")




