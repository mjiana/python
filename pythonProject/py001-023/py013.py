# 조건문
# 반복문과 동일하게 :(콜론)과 들여쓰기를 사용한다.

# 기본
a = 3
if a == 3:
    print("OK")
# 입력받기
b = int(input("숫자를 1에서 5사이에서 입력하세요"))
if b == 4:
    print("Yes")
else:
    print("No")

# 12+23= 문제를 보여주고 정답 입력받기
# 맞으면 성공 틀리면 실패를 출력하는 프로그래밍 작성
a = int(input("12 + 23 = ?"))
if a == (12 + 23):
    print("성공")
else:
    print("실패")