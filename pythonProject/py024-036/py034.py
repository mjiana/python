# 타이핑 게임 만들기
import random
import time

# 단어리스트
"""
w = ["cat", "dog", "fox", "monkey", "mouse"
     , "panda", "frog", "snake", "wolf", "python", "anaconda"
     , "Cat", "Dog", "Fox", "Monkey", "Mouse"
     , "Panda", "Frog", "Snake", "Wolf", "Python", "Anaconda"
     , "고양이", "개", "여우", "원숭이", "쥐"
     , "판다", "개구리", "뱀", "늑대", "파이썬", "아나콘다"
     , "나비"
     ]
"""
word_file = "py034_words.txt"  # 인터넷 다운로드 파일
w = open(word_file).read().splitlines()
n = 1  # 문제 번호
print("타자게임입니다. 준비되면 엔터를 치세요")
input()  # 엔터를 칠때까지 대기상태
start = time.time()
q = random.choice(w)  # 단어 리스트 중 하나 선택
s = 0  # 정답 개수
while n <= 10:
    print("-문제:", n)
    print(q)  # 문제 출력
    x = input()  # 입력
    if q == x.strip():  # x의 양쪽 공백 제거
        print("통과")
        n += 1
        s += 1
        q = random.choice(w)
    else:
        print("재도전")
        q = random.choice(w)

w.close()
end = time.time()
et = end - start  # 소요시간
et = format(et, ".2f")  # 미관상 소수점 2자리까지만 표현
print("결과======================")
print("맞힌 개수:", s, "개")
print("소요 시간 :", et, "초")
