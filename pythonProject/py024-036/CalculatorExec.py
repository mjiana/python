# Calculator 실행파일
# py029

# 계산기 실행 파일 CalculatorExec.py
# 모듈
import Calculator
# 인스턴스화 : 모듈.생성자()
cal = Calculator.Calculator()

# 예외 처리
try:
    result = 0  # 계산 결과 저장
    print("사칙연산 계산기 입니다.")  # 안내문구
    # 입력값
    n1 = int(input("첫번째 숫자를 넣어주세요 >"))
    str = input("+ - * / 중 하나를 입력해주세요 >")
    n2 = int(input("두번째 숫자를 넣어주세요 >"))
    list = ["+", "-", "*", "/"]  # 사칙연산 리스트

    # 입력받은 연산자가 리스트 중 하나에 해당이 된다면
    if str in list:
        if str == "+":  # 연산자가 +로 입력되었다면
            result = cal.add(n1, n2)  # 덧셈함수 실행
        if str == "-":  # 연산자가 -로 입력되었다면
            result = cal.sub(n1, n2)  # 뺄셈함수 실행
        if str == "*":  # 연산자가 *로 입력되었다면
            result = cal.mul(n1, n2)  # 곱셈함수 실행
        if str == "/":  # 연산자가 /로 입력되었다면
            result = cal.div(n1, n2)  # 나눗셈함수 실행
        # 결과 출력
        print("결과 :", n1, str, n2, "=", result)
    else:  # 연산자가 아닌 값을 입력한 경우
        print("[경고] 연산자는 + - * / 중 하나를 입력해주세요")
except ZeroDivisionError:  # 나눗셈에서 분모가 0인 경우
    print("[경고] 0으로 나눌 수 없습니다.")
except ValueError:  # 숫자 입력값에 숫자를 넣지 않을 경우
    print("[경고] 연산자 이외에는 숫자만 입력 가능합니다.")

