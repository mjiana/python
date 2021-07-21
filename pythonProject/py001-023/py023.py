# bool 자료형
# 첫글자 대문자 주의
a = True
b = False
type(a)  # bool

print(1 == 1)  # True
print(2 > 1)  # True
print(2.5 > 11.5)  # False
bool(())  # False, 요소 값이 있다면 True
bool([])  # False, 요소 값이 있다면 True
bool({})  # False, 요소 값이 있다면 True
bool(0)  # False
bool(1)  # True
bool(2)  # True
bool('')  # False
bool(' ')  # True

if ():  # False
    print("True")
else:
    print("False")

if []:  # False
    print("True")
else:
    print("False")

if {}:  # False
    print("True")
else:
    print("False")

#
a = [1, 2, 3, 4]
while a:  # a가 참인 동안 : 모든 요소를 다 꺼낼 때까지
    print(a.pop())  # 마지막 요소 꺼내기
'''
4
3
2
1
'''

