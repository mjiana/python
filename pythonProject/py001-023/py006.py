# 반복문
# 파이썬은 블럭 범위{ }가 없는 대신 :(콜론)과 들여쓰기를 사용한다.
# 들여쓰기가 되어 있다면 반복 실행된다.

# range(10) : 0에서 9까지의 10개 범위
print(range(10))

# for 변수 in 범위:
for x in range(10):  # : 잊지말기
    print("Hello", x)  # 엔터치면 자동 들여쓰기
    print("end!")
print("final end!")  # 반복문 영향 없음

for x in range(3):
    print("첫째")
    print("둘째")
print("셋째")
