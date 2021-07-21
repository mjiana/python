# 데이터 정리 : 지저분한 코드 삭제하기

# n-gram 만들기
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getNgrams(input, n):
    input = input.split(" ")  # 스페이스(공백) 기준 자르기
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output


# 접속
html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
ngrams = getNgrams(content, 2)  # 2개씩 묶어주기, 묶은 순서는 상관없음
print(ngrams)
