# 거북이 대포게임 만들기
import turtle as t
import random as r

t.shape("turtle")

def turn_up(): # 상향 버튼을 눌렀을 때
    t.left(2)  # 거북이가 왼쪽으로 2도 돌아간다.
def turn_down(): # 하향 버튼을 눌렀을 때
    t.right(2)  # 거북이가 오른쪽으로 2도 돌아간다.
def fire():  # 대포 발사
    ang = t.heading()  # 현재 거북이가 바라보는 각도 저장
    while t.ycor() > 0 :  # 거북이의 y축 각도가 땅 위에 있는 동안
        t.forward(15)  # 이동
        t.right(5)  # 오른쪽으로 5도 회전
    d = t.distance(target, 0)
    t.sety(r.randint(10, 100))
    if d < 25:
        t.color("blue")
        t.write("Good", False, "center", ("", 15))
    else:
        t.color("red")
        t.write("Bad", False, "center", ("", 15))
    t.color("black")
    t.goto(-200, 10)
    t.setheading(ang)


# 땅 그리기
# x y 축은 화면의 정중앙을 0,0으로 본다
t.goto(-300, 0)
t.down()
t.goto(300, 0)  # x 300 y 0 이동

target = r.randint(50, 150)
t.pensize(5)
t.color("green")
t.up()
t.goto(target-25, 2)
t.down()
t.goto(target+25, 2)

# 거북이 색상을 검정으로 두고 처음 발사지로 되돌린다.
t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)

# event
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")

t.listen()
t.mainloop()
