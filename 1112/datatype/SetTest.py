# 집합(set)

s1 = set([1, 2, 3, 4, 5, 6, 7])
s2 = set([3, 6, 8, 9])

# 교집합 : &
print(s1 & s2)
print(s1.intersection(s2))

# 합집합 : |
print(s1 | s2)
print(s1.union(s2))

# 차집합 : -
print(s1 - s2)
print(s1.difference(s2))

# 추가하기 : add()
s3 = set([1, 2, 3])
s3.add(4)
print(s3)

# 삭제하기 : remove()
s3.remove(4)
print(s3)
