# 여러개 저장하는 데이터형

# dictionary() {key:value}쌍으로 저장되는 구조
# 중괄호 사용

student = {"no": 11, "name": "Hong Gil", "phone": "010-0000-0000"}
print(type(student))  # <class 'dict'>
print(student["no"])  # 11
print(student["name"])  # Hong Gil
print(student["phone"])  # 010-0000-0000

student["no"] = 123
print(student["no"])  # 재 초기화 가능
print(student[0])  # 인덱스 사용 불가

# 요소 추가
student['address'] = "종로구"
print(student)
# {'no': 123, 'name': 'Hong Gil', 'phone': '010-0000-0000', 'address': '종로구'}

# 요소 삭제, 없는 키를 찾으면 오류 발생
del student['address']
print(student)
# {'no': 123, 'name': 'Hong Gil', 'phone': '010-0000-0000'}

# 키를 이용해서 리스트로 만들기
stkey = student.keys()
print(stkey)  # dict_keys(['no', 'name', 'phone'])
for k in student.keys(): # 리스트가 되면 반복문을 쉽게 할 수 있다.
    print(k)
'''
no
name
phone
'''
# 리스트로 형변환
keylist = list(student.keys())
type(keylist)  # list
print(keylist)  # ['no', 'name', 'phone']

# value값으로 리스트 만들기
print(student)
vallist = student.values()
print(vallist)  # dict_values([123, 'Hong Gil', '010-0000-0000'])
type(vallist)  # dict_values
# 리스트로 형변환
vlist = list(vallist)
print(vlist)  # [123, 'Hong Gil', '010-0000-0000']
type(vlist)  # list

# k:v 둘 다 얻기
st_items = student.items()
print(st_items)
# dict_items([('no', 123), ('name', 'Hong Gil'), ('phone', '010-0000-0000')])
# k를 이용한 v 얻기
print(student.get("no"))  # 123
print(student.get("name"))  # Hong Gil
print(student.get("phone"))  # 010-0000-0000

# 요소 k:v 모두 지우기
student.clear()
print(student)  # {}

# get(키, 디폴트 값)
# 찾는 값이 없으면 디폴트 값이 출력된다.
student = {"no": 111, "name": "Hong Gil", "phone": "010-0000-0000"}
student.get("no")  # 111
student.get("no2")  #
student.get("no2", "값 없음")  # '값 없음'


# 특정키가 있는지 확인
print('no' in student)  # True
print('no2' in student)  # False