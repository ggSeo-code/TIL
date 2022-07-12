Money = 5000
candyPrice = 120
# 최대로 살 수 있는 사탕의 개수
# /를 하나로 넣으면 실수, //적용하면 정수로 결과값이 나온다.
numCandies = Money // candyPrice
print("최대로 살 수 있는 사탕의 개수 : ", numCandies)

# 거스름돈
change = Money % candyPrice
print("최대로 살 수 있는 사탕을 구입하고 남은 돈 : ", change)

