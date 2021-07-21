# 1. text 문서 읽어오기
from urllib.request import urlopen
# 링크는 무조건 열리는지 확인 ctrl+링크 클릭
textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
print(textPage.read()) # 한줄로 길게 나온다.
# 실행 시 맨 앞에 출력되는 b = byte code


# 2. 텍스트형식 인코딩하기 : 러시아어
from urllib.request import urlopen
textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(str(textPage.read(), "UTF-8"))


# 3. 텍스트형식 인코딩하기 : BeautifulSoup & 파이선 3.x 이용
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
# decode
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")
print(content)


# 4. csv 파일 읽어오기 : 중요!!!!!!!!!!!
from urllib.request import urlopen
from io import StringIO
import csv
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv")
data = data.read().decode("ascii", "ignore")
dataFile = StringIO(data)  # 파일을 객체처럼 취급한다.
csvReader = csv.reader(dataFile)  # 파이썬 리스트 처럼 다룰 수 있어서 편리하다.
for row in csvReader:
    # print("앨범", row[0], "은", str(row[1]), "년에 출판되었습니다.")
    print(row)
# 출력 결과 : ["Monty Python's Cotractual Obligation Album", '1980']


# 5. csv 파일을 읽어서 dictionary 처럼 취급하기
from urllib.request import urlopen
from io import StringIO
import csv
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv")
data = data.read().decode("ascii", "ignore")
dataFile = StringIO(data)  # 파일을 객체처럼 취급한다.
dicReader = csv.DictReader(dataFile)  # 파이썬 딕셔너리처럼 다룬다.
print(dicReader.fieldnames)  # key
for row in dicReader:
    print(row)
# 출력 결과 : {'Name': 'Monty Python Sings Again', 'Year': '2014'}
