# 여러개 저장하는 데이터형

# tuple() 튜플형의 여러가지 모습
# 튜플명 = (요소,요소,요소)
# 대괄호 []가 아닌 소괄호 () 사용
# 튜플과 리스트는 매우 유사하지만 재초기화가 불가능한 점이 다르다.

# 비어있는 리스트
a = ()
print(a)
print(type(a))  # <class 'tuple'>
# 정수 요소
b = (1, 2, 3)
print(b)
print(type(b))
# 문자열 요소
c = ('life', 'is', 'too', 'short')
print(c)
print(type(c))
# 복합 요소
d = (1, 2, 'Art', 'is', 'long')
print(d)
print(type(d))
# 리스트 요소
e = (1, 2, 'Art', 'is', (1, 2, 3), ('life', 'is', 'too', 'short'))
print(e)
print(type(e))
print(len(e))
for x in range(len(e)):
    print(e[x])
'''
1
2
Art
is
[1, 2, 3]
['life', 'is', 'too', 'short']
'''
print(e[4][1])  # 2
print(e[5][2])  # too

# tuple()은 요소값 바꾸기 불가능
e[4][1] = 100
print(e[4][1])  # 2
e[5][2] = "very"
print(e[5][2])   # too

