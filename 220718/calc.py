# 제곱을 계산하여 반환하는 함수
def square(num):
    # temp = num * num
    return (num * num)      # 반환값 처리

# 두 수 중에서 큰 값을 반환하는 함수
def get_max(x, y):
    # return 문은 최소화하는게 좋은 코드이다.
    temp = 0
    if x > y:
        temp = x
    else:
        temp = y
    return temp

# 두 수 중에서 작은 값을 반환하는 함수
def get_min(x, y):
    # return 문은 최소화하는게 좋은 코드이다.
    temp = 0
    if x > y:
        temp = y
    else:
        temp = x
    return temp

# 거듭제곱 구하여 해당하는 값을 반환하는 함수
def power(x, y):
    result = 1
    for i in range(y):
        result *= x
    return  result