# 사용자로부터 두 개의 정수를 입력받아서 둘 중에서 큰 수를 출력하는 프로그램

x = int(input("첫 번째 정수 : "))
y = int(input("두 번째 정수 : "))
maximum = 0
if x > y:
    maximum = x
else:
    maximum = y

print("둘 중에 큰 수 : ", maximum)
