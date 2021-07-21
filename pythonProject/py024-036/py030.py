# 예외처리
# 교재 222

# 단일 예외
try:
    4/0
except ZeroDivisionError as e:
    print(e)
# 다중 예외
try:
    a = [1, 2]
    print(a[2])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없다")
except IndexError:
    print("인덱스 범위 초과")
