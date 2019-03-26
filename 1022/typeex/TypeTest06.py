#문자열 슬라이싱

a = "Korea Academy"

#Korea
print(a[0:4])   #0 <= a < 4
print(a[0:5])
print(a[:5])

#Academy
print(a[6:13])
print(a[6:])

#실습
import datetime
today = datetime.date.today()
print(today)    #2017-10-22

print(type(today))  #<class 'datetime.date'>

#문자열로 타입을 변경하자
today = str(today)
print(type(today))  #<class 'str'>

#2017년 10월 22일
print(today[:4]+"년 ",end="")
print(today[5:7]+"월 ",end="")
print(today[8:]+"일")

year = today[:4]
month = today[5:7]
day = today[8:]
print("%s년 %s월 %s일"%(year,month,day))