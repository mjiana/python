# py033.py
# 모듈일 때는 파일명을 최상단에 적어두기
# 모듈 참조와 실행

def add(a, b):
    return a+b
def sub(a, b):
    return a-b


# 참조될 때 실행되지 않으려면 아래 조건문을 추가한다.
if __name__ == "__main__" :
    print(add(10, 20))
    print(sub(30, 20))

# 하단 Terminal 탭
"""
dir *.py
# py033.py 파일 확인
python py033.py  # 실행 명령
# 실행 결과
python
import py033  # import만 했을뿐인데 실행결과가 출력 된다
# 참조될 때 실행되지 않으려면 조건문(if __name__ == "__main__" :)을 추가한다.
import py033  # 결과가 출력되지 않는다.
# Ctrl+Z를 누르면 phthon 종료, 디렉토리로 나온다.
"""
