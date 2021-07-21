# csv 파일로 저장하기
import csv
csvFile = open("./0719/test.csv", "w+", newline="")

try:
    writer = csv.writer(csvFile)
    writer.writerow(("number", "number plus 2", "number times 2"))  # 줄단위 작성
    for i in range(10):  # 0~9
        writer.writerow((i, i+2, i*2))  # 인자값을 하나로 표시하기 위해 () 처리
finally:
    csvFile.close()
# 실행 후 프로젝트를 새로고침하면 .csv 파일이 생성되어있다.


# 특정사이트에서 테이블을 읽어서 csv로 저장하기
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")
table = bsObj.findAll("table", {"class": "wikitable"})[0]  # 대상이 존재하는지 확인
rows = table.findAll("tr")
csvFile = open("./0719/mytable.csv", "wt", newline="", encoding="UTF-8")
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(["td", "th"]):  # td or th
            csvRow.append(cell.get_text())  # csv에 추가
            writer.writerow(csvRow)  # 파일객체에 작성
finally:
    csvFile.close()  # 자원반납
