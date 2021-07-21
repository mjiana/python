# 거북이 그림 2
# 블럭단위 실행을 위해 import 중복 입력

# 선에 색상이 있는 삼각형 그리기
import turtle as t
t.color("red") # 선의 색상
t.forward(100) # 진행 길이
t.left(120) # 각도(외각)
t.color("orange") 
t.forward(100)
t.left(120)
t.color("blue")
t.forward(100)


# 두께가 있는 사각형 그리기
import turtle as t
t.color("red") # 선의 색상
t.pensize(5) # 두께
t.forward(200) # 진행 길이
t.left(90) # 각도(외각)
t.color("orange")
t.pensize(15)
t.forward(200)
t.left(90)
t.color("blue")
t.pensize(5)
t.forward(200)
t.left(90)
t.color("green")
t.pensize(15)
t.forward(200)

# 두께가 있는 원 그리기
import turtle as t
t.color("red") # 선의 색상
t.pensize(5) # 두께
t.circle(100)