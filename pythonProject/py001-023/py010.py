# 원 50개 반복 그리기
import turtle as t

t.bgcolor("black")  # 배경색
t.color("green")  # 선 색
t.speed(0)  # 0~10사이 속도. 0이 가장 빠르고, 범위 밖은 무조건 0

n = 50  # 반복횟수
for x in range(n):
    t.circle(80)
    # 원을 구별하기 위해 360/n 만큼 회전
    t.left(360/n)

# 외부변수 n 없이 내부 변수 x로 만들기
t.color("yellow")
# range()에 시작값을 주지 않으면 0부터 시작해서 오류가 발생한다.
for x in range(1, 51):
    t.circle(80)
    t.left(360/x)
# x의 숫자가 계속 변하므로 뒤죽박죽으로 생성된다.

# 선을 반복해서 그리는 프로그램
import turtle as t
angle = 89
t.bgcolor("black")
t.color("yellow")
t.speed(1)
for x in range(200):
    t.forward(x)  # 크기가 점점 늘어난다.
    t.left(angle)  # 겹치지 않게 회전
