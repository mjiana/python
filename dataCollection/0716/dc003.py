# 예외처리
from urllib.request import urlopen
from urllib.error import HTTPError  # 예외처리용
from bs4 import BeautifulSoup
# import sys


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None

    try:
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None

    return title


title = getTitle("http://pythonscraping.com/pages/page1.html")
if title is None:
    print("title 태그를 찾을 수 없습니다.")
else:
    print(title)
