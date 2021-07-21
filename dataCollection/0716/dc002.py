# 구문 분석기의 여러 종류
# 참조 모듈이 없는 경우 :
# file – settings - Project:"project name" - python Interpreter - +버튼 - bs4 검색 - 선택 - Install Package - X - OK

from urllib.request import urlopen
from bs4 import BeautifulSoup
# lxml과 html5lib는 import를 하지 않아도 작동한다.

# html.parser : html 분석
html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.h1)  # <h1>An Interesting Title</h1>

# lxml : 짝이 맞지 않는 태그를 보수할 수 있다.
bsObj = BeautifulSoup(html.read(), "lxml")  # 설치
print(bsObj.h1)  # None
bsObj = BeautifulSoup(html.read(), "lxml")  # 설치
print(bsObj.html.body.h1)  # None

# html5lib : 짝이 맞지 않는 태그를 보수할 수 있다. lxml과 거의 동일
bsObj = BeautifulSoup(html.read(), "html5lib")  # 설치
print(bsObj.h1)  # None
# 예제없음