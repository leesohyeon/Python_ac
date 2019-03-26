# 구구단 출력
# #  1) 2단만
# for i in range(1,10):
#     print("2 * %d = %d"%(i,2*i))
# print()
# #단수 입력받아 출력
#
# gugudan=int(input("단수를 입력해주세요 : "))
# for i in range(1,gugudan+1):
#     for j in range(1,10):
#         print("%d * %d = %d"%(i,j,i*j))
#
# #강사님 코드
# gugudan=int(input("단수를 입력해주세요 : "))
# for j in range(1,10):
#         print("%d * %d = %d"%(gugudan,j,i*j))
# print()

#2중for 문 이용해 구구단 출력
for i in range(2,10):
    print()
    print("***%d단***"%i)
    for j in range(1,10):
        print("%d * %d = %d"%(i,j,i*j))