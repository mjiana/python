# Calculator.py
# py029
# 교재 207
"""
별도의 파일로 빼내는 것을 모듈이라고 한다.
클래스의 형태를 이루지 않고 함수들만 정의해도 가능하다.
참조하는 곳에서는 반드시 import 모듈명(파일명)을 사용하고,
인스턴스화를 시킬때는 모듈명.생성자명()으로 사용한다.
"""
# 계산기 처리 파일 Calculator.py
# 클래스 정의
class Calculator:
    # 생성자, self는 인자가 아니다.
    def __init__(self):  
        # 전역변수
        self.result = 0
   
    # 덧셈 함수
    def add(self, num1, num2):
        self.result = num1 + num2
        return self.result
    
    # 뺄셈 함수
    def sub(self, num1, num2):
        self.result = num1 - num2
        return self.result
    
    # 곱셈 함수
    def mul(self, num1, num2):
        self.result = num1 * num2
        return self.result

    # 나눗셈 함수
    def div(self, num1, num2):
        self.result = num1 / num2
        return self.result
