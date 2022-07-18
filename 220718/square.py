# 정수를 사용자로부터 입력받아서 제곱한 값을 반환하는 함수

from calc import *

# 함수 호출
num = int(input("제곱하고 싶은 정수를 입력하세요 : "))
print("제곱하기 전 : ", num)
print("제곱한 후 : ", square(num))
