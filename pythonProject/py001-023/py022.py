# 집합 자료형 set { }
# 집합 : 합집합, 교집합, 차집합 ...
# 특징 : 중복 불허, 순서 필요없음

# list를 set으로
sd = set([1, 2, 3, 4, 5])
print(sd)  # {1, 2, 3, 4, 5}
type(sd)  # set

# 문자열을 set으로
sd2 = set('abcde')
print(sd2)  # {'a', 'c', 'b', 'd', 'e'}
type(sd2)  # set

# data
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 합집합 : 중복 불허
print(s1 | s2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 교집합
print(s1 & s2)  # {4, 5, 6}
print(s1.intersection(s2))  # {4, 5, 6}

# 차집합
print(s1 - s2)  # {1, 2, 3}
print(s1.difference(s2))  # {1, 2, 3}
print(s2 - s1)  # {8, 9, 7}
print(s2.difference(s1))  # {8, 9, 7}

# 집합 요소 1개 추가
s1.add(10)
print(s1)  # {1, 2, 3, 4, 5, 6, 10}

# 집합 요소 여러 개 추가
s2.update([11, 22, 33])
print(s2)  # {33, 4, 5, 6, 7, 8, 9, 11, 22}

# 특정 값 지우기
s2.remove(33)
print(s2)  # {4, 5, 6, 7, 8, 9, 11, 22}

