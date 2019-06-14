# set 생성
s = set()
print(s, type(s))

s = {1, 2, 3}
print(s, type(s))

# 기본연산
print(len(s))
print(2 in s)
print(10 not in s)

nums = [1, 2, 3, 2, 2, 4, 5, 5, 6]
s = set(nums)
nums = list(s)
print(s)

#
# 객체함수
#

s.add(7)
print(s)

s.add(2)
print(s)

s.discard(2)
print(s)

s.remove(3)
print(s)

s.discard(3)
print(s)

# 존재하지 않는 객체 삭제시 예외 발생
# s.remove(2)

s.update({2, 7, 8})
print(s)

s.clear()
print(s)

# 수학 집합 관련 객체함수
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {10, 20, 30}

s3 = s1.union(s2)
print(s3)

s4 = s1.intersection(s2)
print(s4)

s3 = s1.difference(s2)
print(s3)

s3 = s1.symmetric_difference(s2)
print(s3)

print(s1.issuperset(s4))
print(s4.issuperset(s1))
print(s4.issubset(s1))
