# 스크레핑 함정 탈출하기
# 사람인 척, 정식 브라우저인 척 하기

# 1. 헤더 수정
import requests
from bs4 import BeautifulSoup
session = requests.Session()
# 인터넷에서 긁어오기 F12-Network-Name-오른쪽 하단
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/92.0.4515.107 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,"
                     "application/xml;q=0.9,image/avif,image/webp,"
                     "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
url = "https://whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"
# 위 링크를 누르면
# https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending
# 로 이동한다.
req = session.get(url, headers=headers)
bs = BeautifulSoup(req.text, "html.parser")
print(bs.find("table", {"class": "table-striped"}).get_text)

