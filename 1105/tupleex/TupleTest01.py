#튜플

t1=()
print(t1)

t2=(1,)
print(t2)

# t3=1,2,3
t3=(1,2,3)
print(t3)

t4=(1,2,'a','b')
# t4[1]=100 #TypeError: 'tuple' object does not support item assignment
print(t4)

t5=(1,2,[3,4,5],6,7)
t5[2][0]=10
print(t5)