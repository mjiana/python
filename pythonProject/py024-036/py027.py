# 함수를 이용해서 거북이 조종하기
import turtle as t

def turn_right():
    t.setheading(0)  # 방향
    t.forward(10)
def turn_up():
    t.setheading(90)
    t.forward(10)
def turn_left():
    t.setheading(180)
    t.forward(10)
def turn_down():
    t.setheading(270)
    t.forward(10)
def blank():  # 초기화, 화면 지우기
    t.clear()


t.shape("turtle")
# t.shape 종류 : arrow turtle circle square triangle classic
t.speed(1)
# t.onkeypress(호출함수, 이벤트값)
# 상하좌우 초기화 5가지 기능
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape")

t.listen()  # 이벤트 적용 설정, 이벤트 발생 대기
t.mainloop()  # 계속 반복
