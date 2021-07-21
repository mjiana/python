# 상속 개념 정리
# 생성자에 인자가 있는 경우

class Person:
    total_count = 0  # 클래스 변수

    def __init__(self, name, age):  # 생성자
        self.name = name  # 멤버 변수
        self.age = age
        Person.total_count += 1  # 클래스변수 호출

    def introduce(self):
        print(f"제 이름은 {self.name}이고, 나이는 {self.age}세 입니다.")
        # f 누락 주의


p1 = Person("이순신", 45)
p1.introduce()
print(Person.total_count)  # 클래스 변수 출력


# 상속
class Student(Person):  # Person을 상속받은 Student
    def __init__(self, name, age):
        super().__init__(name, age)  # 상위 클래스 생성자 호출

    def print_name(self):
        print(f"제 이름은 {self.name}입니다.")  # 상속받은 자원 사용

    def print_age(self):
        print(f"제 나이는 {self.age}입니다.")  # 상속받은 자원 사용


s1 = Student("유관순", 19)
s1.print_name()
s1.print_age()
