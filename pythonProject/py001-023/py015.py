# 난수 함수
import random

# 1에서 50 사이에서 난수 출력
rnd = random.randint(1, 50)
print(rnd)
rnd = random.randint(1, 50)
print(rnd)
rnd = random.randint(1, 50)
print(rnd)

# 마음대로 기어다니는 거북이 만들기
import random as r
import turtle as t

t.shape("turtle")
t.speed(2)
for x in range(500):
    a = r.randint(1, 360)
    b = r.randint(1, 100)
    t.setheading(a)
    t.forward(b)
