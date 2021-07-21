# 파이썬도 객체지향 언어이므로 상속 개념이 있다.
# 외부클래스나 패키지 참조도 가능
# import turtle as t
# tutle 패키지를 참조하고 t라고 부릅니다.
# 블럭단위 실행을 위해 import 중복 입력

# 삼각형 그리기
import turtle as t
t.forward(100) # 진행 길이
t.left(120) # 각도(외각)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
# 전체 실행하면 코드가 완료된 후 창이 사라진다.
# 한줄씩 실행해야 사라지지 않는다.

# 사각형 만들기
import turtle as t
t.forward(200) # 진행 길이
t.left(90) # 각도(외각)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)

# 원 만들기 : 반지름이 50인 원
import turtle as t
t.circle(50)
