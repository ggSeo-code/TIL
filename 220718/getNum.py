# 두 개의 정수를 입력받아서 두 수 중에서 더 큰 수를 찾아서 큰 수를 리턴하는 함수

# 함수의 목록이 정의되어 있는 모듈을 import 할 때는 항상 개발코드의 상위에 위치할 수 있도록 해야 한다.
from calc import *

num1 = int(input("첫 번째 숫자 : "))
num2 = int(input("두 번째 숫자 : "))
value = get_max(num1, num2)
print(num1,"과 ",num2,"의 값 중에 큰 값은 ", get_max(num1, num2))
print(num1,"과 ",num2,"의 값 중에 큰 값은 ", value)


# 두 개의 정수를 입력받아서 두 수 중에서 더 작은 수를 찾아서 작은 수를 리턴하는 함수
num1 = int(input("첫 번째 숫자 : "))
num2 = int(input("두 번째 숫자 : "))
value = get_min(num1, num2)
print(num1,"과 ",num2,"의 값 중에 작은 값은 ", get_min(num1, num2))
print(num1,"과 ",num2,"의 값 중에 작은 값은 ", value)

# 거듭제곱을 구하는 코드
num1 = int(input("거듭 제곱 대상 숫자 : "))
num2 = int(input("거듭 제곱 횟수 숫자 : "))
value = power(num1, num2)
print(num1,"의 ",num2,"거듭제곱 값은 ", power(num1, num2))

