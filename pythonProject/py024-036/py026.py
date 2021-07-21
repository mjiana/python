# 함수정의하기
# 어떤 로직이나 알고리즘을 구현하는 코드를 반복실행할 수 있다.
'''
def 함수명([인자]):
    처리식
    [return 값]
'''
# 기본 함수
def hello():
    print("Hello python")

hello()
hello()

# 인자가 있는 함수
def hello2(name):
    print(name, "님 안녕하세요", sep='')

hello2("홍길동")
hello2("이순신")
hello2("유관순")

# return 함수
# 제곱함수 구현
def square(a):
    c = a*a
    return c
# return값 출력
print(square(2))
print(square(5))
print(square(7))
'''
4
25
49
'''

# 삼각형 넓이 구하는 함수 구현
def triangle(a,h):
    c = (a*h)/2
    return c
print(triangle(10, 5))
# 밑변 10, 높이 5, 삼각형의 넓이 25.0
