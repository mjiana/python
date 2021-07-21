# 1에서 10까지 출력하기

for x in range(10):  # 0 ~ 9
    print(x)
print("end")

for x in range(1, 10):  # 1 ~ 9
    print(x)
print("end")

for x in range(1, 11):  # 1 ~ 10
    print(x)
print("end")

# 1에서 10까지 합 구하기
sum = 0
for x in range(1, 11):
    sum = sum+x  # sum += x 도 가능
print(sum)
