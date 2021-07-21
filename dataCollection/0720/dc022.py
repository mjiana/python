# requests 사용하고 파라미터 추가하기
import requests
from pip._internal import req

params = {"firstname": "Ryan", "lastname": "Michell"}
result = requests.post("https://pythonscraping.com/pages/files/processing.php",
                       data=params)
print(result.text)

# 파일 전송하기
import requests
# files = {"uploadFile": open("../files/Python-logo.png", "rb")}
files = {"uploadFile": open("./lrg_0.jpg", "rb")}
result = requests.post("http://pythonscraping.com/pages/processing2.php",
                       files=files)
print(result.text)  # 실제 업로드 불가능
# Sorry, there was an error uploading your file.


# 쿠키 다루기
import  requests
params = {"username": "Ryan", "password":  "password"}
result = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print("Cookie is set to :")
print(result.cookies.get_dict())
print("------------")
print("going to profile page....")

result = requests.post("http://pythonscraping.com/pages/cookies/profile.php",
                       cookies=result.cookies)
print(result.text)
