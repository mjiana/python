# 데이터 정리 : 지저분한 코드 삭제하기
# n-gram : 텍스트나 연설 내용 중에서 연속되게 나타나는 n개의 단어
# => 쉽게 표현하면 끝말잇기
# 2-gram :  [ '대나무', '무지개' ] [ '무지개', '하늘소' ]  [ '하늘소', '소나무' ]

# n-gram 만들기
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict


def cleaninput(input):
    # 줄바꿈을 스페이스로 변환
    input = re.sub("\n+", " ", input)  # sub(타켓, 바꿈, 문자열) + : 반복
    # 숫자는 empty
    input = re.sub("\[[0-9]*\]", "", input)
    # 공란 1개로
    input = re.sub(" +", " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleaninput = []
    input = input.split(" ")
    for item in input:
        item = item.strip(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        if len(item) > 1 or item.lower() == "a" or item.lower() == "i":  # 관사
            cleaninput.append(item)
    return cleaninput


def getNgrams(input, n):
    input = cleaninput(input)  # 지저분한 문자 제거
    output = dict()
    for i in range(len(input) - n + 1):
        newNgram = " ".join(input[i:i + n])
        if newNgram in output:
            output[newNgram] += 1  # 빈도
        else:
            output[newNgram] = 1
    return output


# 실행1 접속
html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
ngrams = getNgrams(content, 2)  # 묶은 순서는 상관없음, 1로 설정할 경우 워드카운트가 된다.
# print(ngrams)


# 실행2 데이터 빈도 기준 정렬, 역순 출력
html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
print(ngrams)
