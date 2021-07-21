# 도메인을 지정하고 내부 경로를 수집하는 방법
from urllib.request import urlopen  # 필수
from bs4 import BeautifulSoup  # 필수
import datetime
import random
import re

random.seed(datetime.datetime.now())  # 가능하면 중복된 난수가 발생하지않도록 처리


def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    # id 속성이 bodyContent 인 div 태그 안에서 /wiki/로 시작하고 :이 없고 문자 하나 이상으로 끝나는 a태그
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


# 처음 여는 사이트 : https://en.wikipedia.org/wiki/Kevin_Bacon
links = getLinks("/wiki/Kevin_Bacon")  # 처음 링크 수 계산
while len(links) > 0:
    # 임의의 링크 하나 선택
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)  # 새로운 문서 내 링크 수 계산
