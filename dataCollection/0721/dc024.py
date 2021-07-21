# selenium을 이용한 웹 스크랩핑
# 웹사이트 검증용 툴이지만 스크래핑용으로도 활용 가능
# 교재 218p
"""
1. 셀레니움 설치
2-1. 크롬 드라이버 설치
https://chromedriver.storage.googleapis.com/index.html?path=92.0.4515.43/
    * 자신의 크롬 버전과 앞 두자리가 동일한 버전으로 다운로드 해야한다.
    * 압축을 풀고 chromedriver 폴더 생성 후 chromedriver.exe 를 붙여넣는다.
    ==> 폴더 경로 주의하기
2-2. phantomjs 드라이버 설치
https://phantomjs.org/download.html
    * 압축을 풀고 phantomjs 폴더 생성 후 phantomjs.exe 를 붙여넣는다.
    ==> 폴더 경로 주의하기
"""

# 1) 크롬드라이버
# selenium 패키지 webdriver 모듈
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(executable_path="chromedriver/chromedriver.exe",
                          chrome_options=options)
url = "http://pythonscraping.com/pages/javascript/ajaxDemo.html"
driver.get(url)
time.sleep(3)  # 3초 후에 진행 => 요청 완료 대기 # 매우 중요한 문구
print(driver.find_element_by_id("content").text)  # 셀레니움 선택자
driver.close()

# 2) phantomjs 드라이버
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.PhantomJS(executable_path="phantomjs/phantomjs.exe")
url = "http://pythonscraping.com/pages/javascript/ajaxDemo.html"
driver.get(url)
time.sleep(3)  # 3초 후에 진행 => 요청 완료 대기 # 매우 중요한 문구
print(driver.find_element_by_id("content").text)  # 셀레니움 선택자
driver.close()

