# 자동 판매기를 시뮬레이션하는 프로그램을 작성
# 사용자는 1000원권 지폐와 500원, 100원짜리 동전을 사용할 수가 있다. 물건값을 사용자로부터 입력을 받아서
# 1000권 지폐, 500원짜리 동전, 100원짜리 동전의 개수를 입력하면 거스름돈을 계산
# 하여서 동전으로 반환화는 프로그램을 만들어보자.

itemPrice = int(input("물건값을 입력하세요 : "))
bills_1000 = int(input("1000원 지폐 개수 입력 : "))
coin_500 = int(input("500원 동전 개수 입력 : "))
coin_100 = int(input("100원 동전 개수 입력 : "))

# 거스름돈 구하기
nod_money = ((bills_1000 * 1000) + (coin_500 * 500) + (coin_100 * 100)) - itemPrice
print("거스름 돈 : ", nod_money)
# 거스름돈(500원 동전 개수)를 계산
nCoin500 = nod_money // 500
nod_money = nod_money % 500   # 500원으로 나눈 나머지값

# 거스름돈(100원 동전 개수)를 계산
nCoin100 = nod_money // 100
nod_money = nod_money % 100   # 100원으로 나눈 나머지값

# 거스름돈(50원 동전 개수)를 계산
nCoin50 = nod_money // 50
nod_money = nod_money % 50   # 50원으로 나눈 나머지값

# 거스름돈(10원 동전 개수)를 계산
nCoin10 = nod_money // 10
nod_money = nod_money % 10   # 10원으로 나눈 나머지값

# 거스름돈(1원 동전 개수)를 계산
nCoin1 = nod_money

print("500원 개수 : ", nCoin500, ", 100원 개수 : ", nCoin100, ", 50원 개수 : ", nCoin50,
      ", 10원 개수 : ", nCoin10, ", 1원 개수 : ", nCoin1)




