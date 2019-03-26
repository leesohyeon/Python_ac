#논리 연산자
'''

1)x or y     :x와 y둘중에 하나만 참이면 참이다
2)x and y    :x와 y모두 참이어야 참이다
3) not x    :x가 거짓이면 참이다

진리표
x   y   or (논리합)
T   T   T
T   F   T
F   T   T
F   F   F
---------------
x   y   and (논리곱)
T   T   T
T   F   F
F   T   F
F   F   F
---------------
x       not (논리부정)
T       F
F       T

'''

a,b,c,d=10,9,8,7

print(a<b and c>d)  #False and True = False
print(a>b and c>d)  #True and True =True

print(a<b or c<d)   #False and False = False
print(a>b or c<d)   #True and False = True

print(not(a<b or c<d))  #not(False and False) = True
print(not(a>b or c<d))  #not(True and False) = False