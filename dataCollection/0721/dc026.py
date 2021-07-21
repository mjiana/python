# 스크레핑 함정 탈출하기
# 사람인 척, 정식 브라우저인 척 하기
# 교재 284p

# 쿠키 다루기, 수집하기
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(executable_path="chromedriver/chromedriver.exe",
                          chrome_options=options)

driver.get("http://pythonscraping.com")
driver.implicitly_wait(10)  # 최대 n초간 대기, 응답이 완료되면 바로 다음 진행
# 비교 : time.sleep(4) - 응답이 완료되도 무조건 4초간 대기
print(driver.get_cookies())


# 쿠키 읽기, 삭제, 추가
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(executable_path="chromedriver/chromedriver.exe",
                          chrome_options=options)
driver.get("http://pythonscraping.com")
driver.implicitly_wait(10)  # 최대 n초간 대기, 응답이 완료되면 바로 다음 진행
# 비교 : time.sleep(4) - 응답이 완료되도 무조건 4초간 대기
saveCookies = driver.get_cookies()
print("쿠키 저장")
print(saveCookies)
print("\n----------------------\n")
driver2 = webdriver.Chrome(executable_path="chromedriver/chromedriver.exe",
                           chrome_options=options)
driver2.get("http://pythonscraping.com")
driver2.delete_all_cookies()  # 자신의 모든 쿠키 삭제
print("쿠키 삭제 확인")
print(driver2.get_cookies())
for cookie in saveCookies:
    driver2.add_cookie(cookie)  # 쿠키 추가(복사)
driver2.get("http://pythonscraping.com")
driver2.implicitly_wait(10)
print("두번째 쿠키들 :")
print(driver2.get_cookies())  # 복사 확인
print("\n----------------------\n")
