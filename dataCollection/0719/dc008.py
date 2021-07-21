# 트위터 검색하기
# 패키지 > 모듈 > 클래스 or 함수
# 트위터 사이트 가입 후 API 사용 동의 및 등록해야 사용가능하다.
# "Access Token", "Access Token Secret", "Consumer Key", "Consumer Secret" 등 발급 필요
"""
from twitter import Twitter, OAuth
t = Twitter(auth=OAuth("Access Token", "Access Token Secret", "Consumer Key", "Consumer Secret"))
pythonTweets = t.search.tweets(q="#python")  # 찾을 해쉬태드
print(pythonTweets)
"""