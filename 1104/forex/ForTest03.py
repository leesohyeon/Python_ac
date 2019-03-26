'''
for문 이용 ,  총점 평균 구하기
평균은 소수점 이하 한자리까지
'''

scores=[70,60,55,75,95,90,80,80,85,90]
tot=0
avg=0.0
for i in range(10):
    tot+=scores[i]
avg = tot/len(scores)
print("총점 :",tot)
print("평균 :",avg)