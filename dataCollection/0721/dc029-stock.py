# 주가정보 수집 프로그램 만들기
# 레포트 주제
import csv
import codecs
import urllib
import datetime
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
with codecs.open("ezfulldata.csv", "w", "euc-kr") as fp:
    writer = csv.writer(fp, delimiter=",", quotechar='"')
    writer.writerow(["date", "final_price", "normal_price", "high_price", "low_price", "trade_cnt"])

stockItem = "005930"  # 삼성전자 주가 035810에서 005930으로 변경
url = "http://finance.naver.com/item/sise_day.nhn?code="+stockItem
session = requests.session()
html = urlopen(url)
source = BeautifulSoup(html.read(), "html.parser")
maxPage = source.find_all("table", align="center")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/92.0.4515.107 Safari/537.36",
           "Accept": "*/*"}

for page in range(1, 10):
    url = "http://finance.naver.com/item/sise_day.nhn?code="+stockItem+"&page="+str(page)
    req = session.get(url, headers=headers)
    source = BeautifulSoup(req.text, "html.parser")
    srlists = source.find_all("tr")
    isCheckNone = None

    if (page % 1) == 0:
        time.sleep(3)  # 일정시간이 지난 후 3초 간격으로 휴식
    for i in range(1, len(srlists)-1):
        if srlists[i].span != isCheckNone:
            srlists[i].td.text
            print(
                srlists[i].find_all("td", align="center")[0].text.replace(",", "")
                , srlists[i].find_all("td", class_="num")[0].text.replace(",", "")
                , srlists[i].find_all("td", class_="num")[2].text.replace(",", "")
                , srlists[i].find_all("td", class_="num")[3].text.replace(",", "")
                , srlists[i].find_all("td", class_="num")[4].text.replace(",", "")
                , srlists[i].find_all("td", class_="num")[5].text.replace(",", "")
            )
            with codecs.open("ezfulldata.csv", "a", "euc_kr") as fp:
                writer = csv.writer(fp, delimiter=",", quotechar='"')
                writer.writerow([
                    srlists[i].find_all("td", align="center")[0].text.replace(",", "")
                    , srlists[i].find_all("td", class_="num")[0].text.replace(",", "")
                    , srlists[i].find_all("td", class_="num")[2].text.replace(",", "")
                    , srlists[i].find_all("td", class_="num")[3].text.replace(",", "")
                    , srlists[i].find_all("td", class_="num")[4].text.replace(",", "")
                    , srlists[i].find_all("td", class_="num")[5].text.replace(",", "")
                ])
