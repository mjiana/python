#
from urllib.request import urlopen  # 필수
from bs4 import BeautifulSoup  # 필수
import re  # 정규식
import datetime  # 시간
import random  # 난수
import pymysql  # MySQL

# DB 연결
conn = pymysql.connect(host="127.0.0.1", port=3306, user="jspuser",
                       password="1234", db="jspdb", charset="UTF8")
# 인터넷 검색 시 국내외 대부분의 사이트는 UTF8 사용
cur = conn.cursor()
random.seed(datetime.datetime.now())  # 난수 중복 가능성 낮춤


def pageScraped(url):
    cur.execute("select * from pages where url=%s", url)
    if cur.rowcount == 0:  # 테이블에 찾는 url이 없다면
        return False
    page = cur.fetchone()
    cur.execute("select * from links where fromPageId=%s", (int(page[0])))
    if cur.rowcount == 0:  #
        return False
    return True


def insertPageIfNotExists(url):
    cur.execute("select * from pages where url=%s", url)
    if cur.rowcount == 0:  # 테이블에 찾는 url이 없다면
        cur.execute("insert into pages (url) values (%s)", url)
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]


def insertLink(fromPageId, toPageId):
    cur.execute("select * from links where fromPageId=%s and toPageId=%s",
                (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:  #
        cur.execute("insert into links (fromPageId, toPageId) values (%s, %s)",
                    (int(fromPageId), int(toPageId)))
        conn.commit()


def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return
    pageId = insertPageIfNotExists(pageUrl)  # 함수 호출
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if not pageScraped(link.attrs["href"]):
            newPage = link.attrs["href"]
            print(newPage)
            getLinks(newPage, recursionLevel+1)  # 재귀
        else:
            print("Skipping: ", str(link.attrs["href"]), "found on ", pageUrl)


# 실행부
getLinks("/wiki/Kevin_Bacon", 0)

cur.close()
conn.close()

"""
drop table pages;

create table pages(
    id int not null auto_increment,
    url varchar(300) not null,
    created timestamp default CURRENT_TIMESTAMP,
    primary key(id)
) engine=myisam, default charset=utf8;

create table links(
    id int not null auto_increment,
    fromPageId int,
    toPageId int,
    created timestamp default CURRENT_TIMESTAMP,
    primary key(id)
) engine=myisam, default charset=utf8;

desc pages;
desc links;
"""
