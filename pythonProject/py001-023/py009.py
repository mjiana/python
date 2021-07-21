# turtle를 이용해 보라색을 칠한 오각형 그리기
# begin_fill() 색상을 칠한 ~반복문~ end_fill()

import turtle as t

t.color("purple")  # 색상 지정
t.begin_fill()  # 색상의 범위 시작
n = 5  # n각형 도형
for x in range(n):
    t.forward(100)
    t.left(360/n)
t.end_fill()  # 색상의 범위 종료