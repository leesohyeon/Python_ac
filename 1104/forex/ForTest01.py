#for문

lst = [1,2,3,4,5]
line="--------------------"
for i in lst:
    # print(i)
    print(i,".Hello")

print(line)

# range(num) : 0부터 num 미만까지
for i in range(10):
    print(i , end="")
print("\n"+line)

# range(num1,num2) : num1 부터 num2까지
for i in range(1,10):
    print(i , end="")
print("\n"+line)

#range(num1,num2,num3):
for i in range(1,10,2): # 1부터 10미만까지 2씩 증가해!
    print(i , end="")
print("\n" + line)

    #QUIZ
    # 1부터10까지의 합 구하기
sum=0
for i in range(1, 11): #1부터 11미만까지
   sum += i
print("1부터 10까지의 합 =",sum)