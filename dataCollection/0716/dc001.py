# 강사님 파일명 data_col_001.py
# 교재 : 파이썬 웹크롤러만들기
# 참조 모듈이 없는 경우 :
# file – settings - Project:"project name" - python Interpreter - +버튼 - bs4 검색 - 선택 - Install Package - X - OK

# 데이터 수집하기 1
# from 모듈 import 함수 : 1개 참조
# from 모듈 import * : 여러개 참조
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")  # 실제 경로/파일
print(html.read())  # 소스코드가 나온다.

# 데이터 수집하기 2 : 매우 중요!!!!!
# BeautifulSoup : 데이터 분석-수집, DOM 구성에서 필요한 데이터 추출
from urllib.request import urlopen
from bs4 import BeautifulSoup  # 설치
html = urlopen("http://pythonscraping.com/pages/page1.html")  # 링크 접속
# BeautifulSoup을 이용해서 가져온 문서 분석하기
bsObj = BeautifulSoup(html, "html.parser")  # html 분석

# 직접 접근
# 인터넷 창을 열고 F12(개발자 도구)를 열어서 필요한 태그를 찾아본다.
print(bsObj.h1)  # 태그가 크롭되어 화면에 출력된다.
print(bsObj.title)

# 단계별 접근
print(bsObj.html.body.h1)

