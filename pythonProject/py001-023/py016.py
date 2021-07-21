# 게임
# 1에서 5사이의 난수를 발생시키고 하나의 값을 입력받는다.
# 난수와 입력받은 값이 일치하면 입력값의 3배를 돌려주고
# 일치하지 않으면 YOU LOSE라고 출력하기

import random as r
rnd = r.randint(1, 5)
num = int(input("숫자 1-5사이 입력"))
if rnd == num:
    print("YOU WIN!!")
    print("return", num*3)
else:
    print("YOU LOSE")
    print("rnd is", rnd)
