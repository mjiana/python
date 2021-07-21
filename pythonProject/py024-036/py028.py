# 클래스
'''
class 클래스명:
    def 함수명:
        처리식
    def 함수명:
        처리식
'''
# 클래스 정의
class Calculator:
    # 클래스 변수
    def __init__(self):  # 생성자, 주의) self는 인자가 아니다.
        # 전역변수
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


# 인스턴스화
# 지역변수
cal1 = Calculator()
print(id(cal1))  # 2333689889888
result = cal1.add(50)  # 메서드 호출
print(result)  # 50

cal2 = Calculator()
print(id(cal2))  # 2333689889264
result2 = cal2.add(50)  # 메서드 호출
print(result2)  # 50
