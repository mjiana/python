# 클래스 형태로 찾기 : 매우 중요!!!!!
from urllib.request import urlopen
from bs4 import BeautifulSoup

# urlopen()의 사이트가 정상작동하는지 확인 후 원하는 부분 찾고 작성하기


# 다수의 태그 추출 방법 : findAll("태그", {"속성": "값"})
# 1. 특정 태그의 속성과 값 찾기
html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
# span 태그 중 class 가 green 인 것 찾기
nameList = bsObj.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())

# 2. 특정 속성과 값 찾기
html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
# id 속성의 값이 text 일 때
nameList = bsObj.findAll(id="text")
for name in nameList:
    print(name.get_text())

# 3. 하위(자식)요소 찾기
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
# id 속성이 giftList 인 table 태그의 하위요소(자식 태그)
for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)

# 4. 형제(sibling) 요소들 찾기
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
# id 속성이 giftList 인 table 태그의 첫번째 tr 태그를 제외한 다른 tr 태그들
for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

# 5. 부모요소의 형제 요소 1개 찾기
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
# 경로가 ../img/gifts/img1.jpg 인 이미지 태그의 부모 태그 중 바로 이전의 형제 태그
print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

# 6. 정규식을 이용하여 검색
import re
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")
# images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
# img 태그 src 속성의 모든 내용
# images = bsObj.findAll("img", {"src": re.compile(".*")})
# 간단하게
images = bsObj.findAll("img", {"src": re.compile("/gifts/img.*")})

for image in images:  # img 태그 src 속성의 값 가져오기
    print(image["src"])

"""
# findAll("태그",{"속성":"값"})  # "../img/gifts/img*.jpg"
# . : 문자 하나(글자, 숫자, 기호, 공백)
# \ : 탈출문자, 순수문자로 치환
# a{2,3}b{2,3} : a가 두개나 세개이고 b가 두개나 세개로 연결되었다. aabbb aaabbb aabb aaabb
# [A-Z] : 알파벳 대문자
# [^A-Z] : A-Z 제외
# [A-Z]*[a-Z]*$ : * 0개 이상
# ?! : 포함하지 않는다
# ^문자 : 문자로 시작된다. []안과 밖의 위치에 따라 정반대의 의미를 갖는다
# 문자$ : 문자로 끝난다. 
"""

# 람다식 표현 = 축약표현
html = urlopen("http://www.pythonscraping.com/pages/page2.html")
bsObj = BeautifulSoup(html, "html.parser")
# 특정 태그의 속성이 2개인 것 찾기
tags = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
for t in tags:
    print(t)
