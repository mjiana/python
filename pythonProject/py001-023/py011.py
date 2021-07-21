# 외부변수를 받아 출력하기
name = input("너의 이름은?")
print("안녕", name, "님")

# 두개의 값을 입력받아 덧셈 후 출력
a = input("숫자 1")  # 20
b = input("숫자 2")  # 5
print("덧셈결과", a+b)  # 205, 문자열로 인식
print("덧셈결과", int(a+b))  # 205, 문자열로 인식
print("덧셈결과", int(a)+int(b))  # 25, 형변환이 필요하다.

# 출력 시 , 공백 제거방법
print("a", "aa")  # a aa
print("a", "aa", sep='')  # aaa

# 다섯개의 숫자를 입력받아서 총합을 구하는 프로그램 작성
n = 5
sum = 0
for x in range(n):
    print(x+1, "번 숫자", sep='')
    num = input()
    sum = sum + int(num)
print(sum)