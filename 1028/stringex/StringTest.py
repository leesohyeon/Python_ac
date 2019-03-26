# 1. 문자열의 길이 구하기 : len()

# ctrl + shift + f10
str = "hahaha"
print("문자열의 길이 =", len(str))

# 2.문자 개수 세기 : count()
str = "hihihihihihihihihihihihihihihi"
print("h의 개수 =", str.count('h'))

# 3.위치 알려주기 : find()
str = "Korea IT Academy"
print("첫 문자 a의 위치 =", str.find('a'))
# 찾는 문자나 문자열이 존재하지 않으면, -1을 반환
print(str.find('z'))        # -1

# 4.위치 알려주기 : index()
print(str.index('o'))
# 찾는 문자나 문자열이 존재하지 않으면, 에러 발생
# print(str.index('z'))

# 5.문자열 삽입 : join()
str = '~'
print(str.join("Okay"))     # O~k~a~y

# 6.소문자를 대문자로 바꾸기 : upper()
str = "apple tree"
print(str.upper())

# 7.대문자를 소문자로 바꾸기 : lower()
print(str.lower())

# 8.양쪽 공백 지우기 : strip()
str = "      python        "
print(str.strip())

# 9.문자열 바꾸기 : replace()
# replace("바뀌게 될 문자열", "바꿀 문자열")
str = "Life is too short."
print(str.replace("Life", "Your leg"))  # Your leg is too short.

# 10.문자열 나누기 : split()
str = "Korea:Academy"
print(str.split(':'))  # ['Korea', 'Academy']

































