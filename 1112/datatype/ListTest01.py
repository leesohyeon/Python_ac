#딕셔너리(dictionary)

dic = {"축구":"박지성","야구":"강민호","체조":"손연재"}
print(dic["축구"])
print(dic["야구"])
print(dic["체조"])

lst = ['a','b','c']
print(lst[0])
print(lst[1])
print(lst[2])

# 딕셔너리 관련함수

# 키와 밸류가 없는 빈 딕셔너리 생성하기 : dict()
a = dict()
print(a)

# 키값만 반환해주는 함수 : key()
b={"HP":"010-1234-5678","AGE":20,"NAME":"홍길동"}
keylst=b.keys()
print(keylst)

for i in keylst:
    print(i)

# value 값만 반환해주는 함수 : values()
valueLst=b.values()
print(valueLst)

# key와 value 한쌍으로 얻는 함수 : items()
item = b.items()
print(item)

# key값을 이용해서 value 값 얻어오기:get()
name = b.get("NAME")
print(name)
print(b.get("gender")) #NONE
b.get("gender","없음") #없음
# 딕셔너리 내에 키 값이 없을 경우, 에러발생!
# print(b["gender"]) # KeyError 에러

# key: value 한쌍 모두 삭제하기 : clear()
# b.clear()
# print(b)  # {}

# 딕셔너리 내에 해당 키가 존재하는지 알아보기 :in
result = "gender" in b
print(result)   #false

