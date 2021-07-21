# 자료형 정리

# 숫자형 : 정수, 실수, 8진수, 16진수
a = 0o175 # 8진수
print(a) # 125
b = 0x4f # 16진수
print(b) # 79

# 연산
# % 나머지 // 몫
print(45/4)  # 나누기 11/25
print(45%4)  # 나머지 1
print(45//4)  # 몫 11

# 한 줄 주석
'''
여러 줄 
주석
'''

# 문자열 반복
hi = "Hi"
print(hi*4)  # HiHiHiHi

# 문자열 인덱싱
str = "HELLO"
print(str[0])  # H
print(str[1])  # E
print(str[2])  # L
print(str[3])  # L
print(str[4])  # O
print("---------------")
# 0은 -를 넣어도 0이기에 의미 없음
print(str[-1])  # O  # 뒤에서 첫글자
print(str[-2])  # L  
print(str[-3])  # L  
print(str[-4])  # E  # 앞에서 두번째 글자
print(str[-5])  # H #
print("---------------")

# 슬라이싱
str = "HELLO"
# 0번지부터 3-1번지까지 == (0,1,2) == HEL
print(str[0:3])
# [시작:끝]
str2 = "20210714Hotday"
date = str2[:8]  # 시작은 상관없이 8-1(7)까지
print(date)
weather = str2[8:]  # 8부터 끝까지
print(weather)

# 문자열 포맷
print("I eat %d apples" % 3)  # 정수
print("I eat %s apples" % "five")  # 문자열
cnt = 3
str = "GILDONG"
print("%s eat %d apples" % (str, cnt))  # 혼합 사용 가능

# 포맷 종류
# %s, %d, %c, %f, %o, %x, %%

# 문자열 관련 함수
'''
len(str) 문자열 길이
str.count("n") 문자열에서 문자열 n의 개수
str.find(s) 위치, 없으면 -1
str.index(s) 위치, 없으면 오류 발생
str.upper() 대문자
str.lower() 소문자
str.lstrip() 왼쪽 공백제거
str.rstrip() 오른쪽 공백 제거
str.strip() 양쪽 공백 제거
str.replace("구","신") 문자열 대체
str.split() 분리

",".join('abcd') ,로 연결
'''
print(",".join('abcd'))  # a,b,c,d
str = "aaaabbbbabaabccc"
print(len(str))  # 문자열 길이
print(str.count("c"))  # c의 개수
