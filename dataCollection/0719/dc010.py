# scrapy 스크레피
# 교재 97p 하단

# 실행방법
# 0. 실행할 파일의 폴더 잘 확인하기
#   C:\Users\poimk\PycharmProjects\data_collection\0719>
# 1. Terminal 탭에서 scrapy startproject wikiSpider 명령을 실행하면 아래처럼 폴더가 생성된다.
#  * 콘솔창에서 실행해도 결과값이 나오지 않는다.
# 1-1. 폴더 구조 확인방법 : tree wikiSpider
# C:\USERS\POIMK\PYCHARMPROJECTS\DATA_COLLECTION\WIKISPIDER
# └─wikiSpider
#    └─spiders

#. 2. 소스 작성
import scrapy


class ArticleSpider(scrapy.Spider):
    name = "article"

    def start_requests(self):  # 내장함수
        urls = ["http://en.wikipedia.org/wiki/Python_%28programming.language%29",
                "https://en.wikipedia.org/wiki/Functional_programming",
                "https://en.wikipedia.org/wiki/Monty_Python"]
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        url = response.url
        title = response.css("h1:text").extract_first()
        print("url is {}".format(url))
        print("title is {}".format(title))

# 3. 터미널 실행명령 : scrapy runspider 모듈명
# 위치 : C:\Users\poimk\PycharmProjects\data_collection\0719>
# 명령어 : scrapy runspider dc010.py

