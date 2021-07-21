# 사이트 전체 크롤링
from urllib.request import urlopen  # 필수
from bs4 import BeautifulSoup  # 필수
import re

pages = set()  # set == 집합


def getLinks(pageUrl):
    global pages  # 전역변수 선언
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs["href"])
    except AttributeError:
        print("찾는 페이지가 없습니다")

    # a 태그의 href 속성에서 /wiki/로 시작될 동안 반복
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        # link 의 속성에 href 가 있다면
        if "href" in link.attrs:
            # 해당 페이지가 전역변수에 있는지 확인, 없을 경우 동작
            if link.attrs["href"] not in pages:
                newPage = link.attrs["href"]  # href에 연결된 페이지 저장
                print("--------------\n"+newPage)
                pages.add(newPage)  # 전역변수에 등록
                getLinks(newPage)  # 페이지 검색


getLinks("")  # 지정된 웹사이트 루트부터 검색
