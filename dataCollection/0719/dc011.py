# 미디어 페이지 수집
import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "download"
baseUrl = "http://pythonscraping.com"


def getAbsoluteURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://"+source[11:]  # http://www. == 11자, www 제거
    elif source.startswith("http://"):
        url = source
    elif source.startswith("https://"):
        url = source
    elif source.startswith("www."):
        url = source[4]
        url = "http://"+source
    else:
        url = baseUrl+"/"+source

    if baseUrl not in url or ".js" in url:
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace("www.", "")  # www. 제거
    path = path.replace(baseUrl, "")
    path = downloadDirectory+path  # 로컬경로로 변경
    directory = os.path.dirname(path)  # 저장경로 설정
    # 저장폴더 생성
    if not os.path.exists(directory):
        os.makedirs(directory)  # 이미 생성된 폴더일 경우 오류 발생, 중간경로 자동생성
    return path


html = urlopen("http://pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
downloadList = bsObj.findAll(src=True)  # 무엇을 다운로드 할지 지정

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)
        # 실제 저장
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
