# 클래스와 함수를 이용한 사칙연산 계산기 만들기
# 내일(07.16) 리포트
'''
스토리
1. 숫자 연산자 숫자 순서로 입력받는다.
2. 선택된 연산자에 따라 함수를 실행한다.
2-1. 나눗셈에서 분모가 0인 경우 예외처리
3. 값을 출력한다.
* 실행과 처리로 구분하면 편리
* 주기능(가감승제)을 먼저 구현하고 부기능(예외처리)을 나중에 구현하면 편리
'''


class Calculator:
    # 클래스 변수
    def __init__(self):  # self는 인자가 아니다.
        # 전역변수
        self.result = 0

    def add(self, num1, num2=None):
        if num2 is None:
            self.result += num2  # 인자가 한개면 기존값에 누적
        else:
            self.result = num1 + num2  # 인자가 두개면 더하여 반환
        return self.result

    def sub(self, num1, num2):
        self.result = num1 - num2
        return self.result

    def mul(self, num1, num2):
        self.result = num1 * num2
        return self.result

    def div(self, num1, num2):
        try:
            self.result = num1 / num2
            return self.result
        except ZeroDivisionError:
            print("[경고] 0으로 나눌 수 없습니다.")


# 인스턴스화
cal = Calculator()

try:
    # 변수 선언 및 데이터 입력
    result = 0
    print("사칙연산 계산기 입니다.")
    n1 = int(input("첫번째 숫자를 넣어주세요 >"))
    str = input("+ - * / 중 하나를 입력해주세요 >")
    n2 = int(input("두번째 숫자를 넣어주세요 >"))
    list = ["+", "-", "*", "/"]

    # 명령 분석
    if str == "+":
        result = cal.add(n1, n2)
    if str == "-":
        result = cal.sub(n1, n2)
    if str == "*":
        result = cal.mul(n1, n2)
    if str == "/":
        result = cal.div(n1, n2)

    # 결과 출력
    if str in list:

        print("결과 :", n1, str, n2, "=", result)
    else:
        print("[경고] 연산자는 + - * / 중 하나를 입력해주세요")
except ZeroDivisionError:
    print("[경고] 0으로 나눌 수 없습니다.")
except ValueError:
    print("[경고] 연산자 이외에는 숫자만 입력 가능합니다.")
except IndexError as e:
    print("[경고] 오류가 발생했습니다.")
    print(e)
