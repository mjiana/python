# 자동문제 출제 채점하기
import  random as r
a = r.randint(1, 30)
b = r.randint(1, 30)

# 문제 출제
print("아래 연산결과는 ?")
print(a, "+", b, "=")

# 정답 입력
x = input()

# 채점
if int(x) == (a+b):
    print("정답")
else:
    print("실패")

# 다섯번을 실행하여 총점을 출력하는 프로그램으로 변경
# 1회당 20점
import  random as r
total = 0
print("연산결과를 구하시오")
for i in range(1, 6):
    # 문제
    a = r.randint(1, 30)
    b = r.randint(1, 30)
    print(i, ". ", a, "+", b, "=", sep='')
    # 정답
    x = input()
    # 채점
    if int(x) == (a + b):
        print("정답")
        total += 20
    else:
        print("실패")
print("점수 :", total, "/ 100")
