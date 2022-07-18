# 사용자로부터 정수를 입력받아서 소수를 판별하는 함수
# 소수면 True, 소수가 아니면 False
# 1과 자기자신과 나누어지는 수를 소수라고 한다.
def is_prime(num):
    for i in range(2, num):
        temp = True
        if (num%i) == 0:
            temp = False
        else:
            temp = True
        return temp

prime = int(input("정수를 입력하세요 : "))

# 함수 호출
print(is_prime(prime))

