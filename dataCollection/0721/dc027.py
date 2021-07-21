# 허니팟 피하기
# 검색(크롤링 )하기 전에 이 모듈로 먼저 테스트하고 정확한 위치의 폼값만을 입력해야한다.
# 교재 290p
"""
실제 유저에게는 보이지 않고 bot(봇)에게만 보인다.
# 숨겨진 필드 : hidden
# 화면 비표시 : display:none
# 화면 이동 : right:50000px
위 항목들에 값을 넣거나 클릭하게 되면 함정에 걸린것이다.
"""
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(executable_path="chromedriver/chromedriver.exe",
                          chrome_options=options)
driver.get("http://pythonscraping.com/pages/itsatrap.html")
driver.implicitly_wait(4)

links = driver.find_elements_by_tag_name("a")  # 결과 중 a태그 찾기
for link in links:
    if not link.is_displayed():
        print("링크 {}는 함정입니다.".format(link.get_attribute("href")))

fields = driver.find_elements_by_tag_name("input")
for field in fields:
    if not field.is_displayed():
        print("{}는 값 입력이 불가능합니다.".format(field.get_attribute("name")))

# 교재 끝
# 교재 18챕터는 꼭 읽어보기
