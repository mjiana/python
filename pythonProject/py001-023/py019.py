# 여러개 저장하는 데이터형
# 교재 72p
# list(), tuple() 수정불가, dictionary(), set()

# 리스트형의 여러가지 모습
# 리스트명 = [요소,요소,요소]
# 비어있는 리스트
a = []
print(a)
print(type(a))  # <class 'list'>
# 정수 요소
b = [1, 2, 3]
print(b)
print(type(b))
# 문자열 요소
c = ['life', 'is', 'too', 'short']
print(c)
print(type(c))
# 복합 요소
d = [1, 2, 'Art', 'is', 'long']
print(d)
print(type(d))
# 리스트 요소
e = [1, 2, 'Art', 'is', [1, 2, 3], ['life', 'is', 'too', 'short']]
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

# 요소값 바꾸기
e[4][1] = 100
print(e[4][1])  # 100
e[5][2] = "very"
print(e[5][2])   # very

# list 관련 함수
'''
lst.append(요소) 뒤에 추가
lst.sort() 정렬
lst.reverse() 역순
lst.index(요소) 위치
lst.insert(위치,값) 중간 삽입
lst.remove(요소) 요소 삭제
lst.pop() 맨 앞 위치 
lst.pop(index) 특정 위치
lst.count(요소) 요소 개수
lst.extend(리스트형 요소) 앞 리스트에 뒤의 리스트요소 연결 
'''