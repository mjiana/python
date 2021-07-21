# 외부정보를 가져와서 db에 저장하기
# 교재 135~137p, 교재와는 조금 다름

# mysql 실행시키기
from urllib.request import urlopen  # 필수
from bs4 import BeautifulSoup  # 필수
import re  # 정규식
import datetime  # 시간
import random  # 난수
import pymysql  # MySQL

# DB 연결
conn = pymysql.connect(host="127.0.0.1", port=3306, user="jspuser", password="1234", db="jspdb", charset="UTF8")
# 인터넷 검색 시 국내외 대부분의 사이트는 UTF8 사용
cur = conn.cursor()
random.seed(datetime.datetime.now())  # 난수 중복 가능성 낮춤

"""
create table pages(
    title varchar(100),
    content varchar(300)
) engine=myisam, default charset=utf8;
"""


# 함수부
def store(title, content):
    cur.execute("insert into pages (title, content) values( \"%s\", \"%s\" )", (title, content))
    # cur.execute( "SQL", %s에 입력할 변수)
    cur.connection.commit()  # 나중에 필요성 테스트


def getLinks(articleUrl):
    html = urlopen("http://wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    title = bsObj.find("h1").get_text().strip()  # 타이틀을 가져와서 변수에 저장
    # mw-content-text 라는 id를 가진 div를 찾아 그 안의 p 태그의 내용 가져오기
    content = bsObj.find("div", {"id": "mw-content-text"}).find("p").get_text().strip()
    # 사이트에 위 태그들이 있는지 확인하기

    store(title, content)  # DB 저장함수 호출
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    # 시작이 /wiki/로 시작하고 :을 제외한 문자하나 이상이 온 뒤 끝


# 실행부
links = getLinks("/wiki/Kevin_Bacon")  # 처음 검색 위치
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        print(newArticle)  # 새로운 경로 확인용 출력
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()

# desc pages;
# select count(1) from pages;
# select title from pages;
# select content from pages;
