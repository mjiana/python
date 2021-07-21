# 파일 처리하기
# f = open("경로/파일", "mode") mode : w 쓰기, r 읽기, a 추가
# f.close() 파일 닫기

# 파일에 데이터 쓰기
f = open("/myFile.txt", "w")
for i in range(1, 11):  # 1~10
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()
# terminal
"""
python py036.py
dir
# myFile.txt 확인
# 해당 폴더로 이동 후 파일 내용 확인하기
"""

# 파일 한줄씩 읽기
f = open("/myFile.txt", "r")
while True:
    line = f.readline()  # 한줄 읽기
    if not line:
        break
    print(line)
f.close()

# 파일 여러줄 읽기
f = open("/myFile.txt", "r")
lines = f.readlines()  # 여러줄 읽기
for line in lines:
    print(line)
f.close()

# 문서 전체 읽기
f = open("/myFile.txt", "r")
lines = f.read()  # 전체 읽기
print(lines)
f.close()

# 내용 추가하기
f = open("/myFile.txt", "a")
for i in range(11, 21):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)
f.close()