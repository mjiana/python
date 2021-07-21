# 숫자 추측하기
# 스무고개 방식
import random as r

n = r.randint(1, 100)
cnt = 1
while True:  # 무한루프, break 필수
    x = input("1에서 100 사이의 정수입니다.")
    print(cnt, "회 시도")
    num = int(x)

    if n == num:
        print("정답입니다.")
        break
    if n < num:
        print("입력값 보다 작습니다.")
    if n > num:
        print("입력값 보다 큽니다.")
    cnt += 1
