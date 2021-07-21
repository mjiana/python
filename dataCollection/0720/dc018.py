# 수집대상이 웹문서가 아닌경우

# docx 문서 읽어오기
# lxml 패키지 설치
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)  # 바이트 객체로 만들어서
document = ZipFile(wordFile)  # 압축을 해제하면 xml 형태로 표시
xml_content = document.read("word/document.xml")  # 해제된 xml 읽기
# print(xml_content.decode("utf-8"))  # 결과가 한줄에 모두 출력된다.

# BeautifulSoup
wordObj = BeautifulSoup(xml_content.decode("utf-8"), "lxml-xml")  # xml방식 파싱
textStrings = wordObj.findAll("w:t")
# xml => html 출력
for t in textStrings:
    closeTag = ""
    try:
        style = t.previousSibling.find("w:t")
        if style is not None and style["w:val"] == "Title":
            print("<h1>")
            closeTag = "</h1>"
    except AttributeError:
        pass
    print(t.text)
    print(closeTag)

