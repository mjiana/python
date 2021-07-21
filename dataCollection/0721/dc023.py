# session, cookie 이용방법
# 로그인 후 페이지를 요청하는 방법
import requests
session = requests.Session()  # 생성자 호출, 세션 객체 생성
params = {"username": "any", "password": "password"}
# 링크는 열리는지 확인하고 사용하기
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)

# 로그인이 되었는지 쿠키 확인
print("Cookie is set to: ")
print(s.cookies.get_dict())
print("----------------------")
print("Going to profile page.....")

# 동일한 세션 상에서 다른 페이지 요청
s = session.get("http://pythonscraping.com/pages/cookies/profile.php")
print(s.text)


# 인증 이용하기 - 시스템 측면
import requests
# from requests.auth import AuthBase  # 미사용
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("ryan", "password")
r = requests.post("http://pythonscraping.com/pages/auth/login.php", auth=auth)
print(r.text)

# 방식 진화과정
# HTTPBasicAuth(요즘은 잘 사용하지 않음) ===> 쿠키(중요하지 않은 사이트) ===> 세션




