# 문자열 비교
# == 등치 연산자로 비교합니다.

first = "홍길동"
second = "이순신"
third = "홍길동"
four = "홍"
five = "대"

if first == second:
    print("문자열 일치")
else:
    print("문자열 불일치")
if first == third:
    print("문자열 일치")

# 부분일치
if four in first:
    print("문자열 부분 일치")
else:
    print("문자열 불일치")

# 부분일치
if five in first:
    print("문자열 부분 일치")
else:
    print("문자열 불일치")
