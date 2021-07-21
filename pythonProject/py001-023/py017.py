# 반복문 while

# 1에서 10까지 출력
x = 1
while x <= 10:
    print(x)
    x += 1  # x++ 불가

# 1에서 100까지의 합 출력
x = 1
sum = 0
while x <= 100:
    print(x)
    sum += x
    x += 1
print(sum)