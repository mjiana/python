# 특정 사이트 내부의 링크된 모든 페이지
# 교재 69p
from urllib.parse import urlparse
from urllib.request import urlopen  # 필수
from bs4 import BeautifulSoup  # 필수
import datetime
import random
import re

pages = set()
random.seed(datetime.datetime.now())  # 중복방지


# 페이지에서 발견된 내부 링크를 목록으로 수집
def getInternalLinks(bsObj, includeUrl):
    includeUrl = "{}://{}".format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []  # list
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):  # /xx
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internalLinks:
                if link.attrs["href"].startswith("/"):
                    internalLinks.append(includeUrl+link.attrs["href"])
                else:
                    internalLinks.append(link.attrs["href"])
    return internalLinks


# 외부 사이트 링크 수집
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # http로 시작하거나 www로 시작
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in externalLinks:
                externalLinks.append(link.attrs["href"])
    return externalLinks


# 데이터 전처리
def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")  # http://제거 후 / 자르기
    return addressParts


# 임의의 외부 링크 얻어오기
def getRandomExtenalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    # externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)

    if len(externalLinks) == 0:
        print("외부링크가 없습니다.")
        domain = "{}://{}".format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bsObj, domain)
        return getRandomExtenalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:  #
        return externalLinks[random.randint(0, len(externalLinks)-1)]


def followExternalOnly(startingSite):
    # externalLink = getRandomExtenalLink(startingSite) 교재에서는 이렇게 나왔지만 오류 발생
    externalLink = getRandomExtenalLink("http://oreilly.com")
    print("임의의 외부 링크는 ", externalLink)
    followExternalOnly(externalLink)
    # 재귀, 임의로 선정된 외부사이트를 시작페이지로 설정
    # 재귀로 반복되면 또 다른 임의의 사이트를 시작페이지로 설정

# 최초의 시작
followExternalOnly("http://oreilly.com")
