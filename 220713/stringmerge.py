# 문자열의 연결
# + 연산자는 문자열 사이에 들어가면 문자열을 연결해주는 역할을 한다.
first_name = " Eun Hyuk"
last_name = "Shin"
name = last_name + first_name
print(name)

# "Person" = 문자열이고, 100= int 타입이다.하여 타입 불일치 = 연결에러
# temp = "Person" + 100
# print(temp)

# 숫자 100을 str()를 이용하여 문자열로 변환, 타입 일치시킨다
# 문자열+문자열
temp = "Person" + str(100)
print(temp)

temp = "Person" + str(100.188)
print(temp)

# 문자열을 숫자로 변환
# 정수일때는 int()
price = int("123456")
print(type(price))
print(price)
# 실수일때는 float()
price = float("123456.187")
print(type(price))
print(price)

# 문자열의 반복
# 문자열에서 * 연산자를 사용하면 그만큼 반복됨
arrow = "->" * 10
print(arrow)

arrow = "->"
print(arrow * 10)

# %s(형식 지정자)
# %s는 문자열이나 숫자값을 변수에 대입, 자주 변경이 있을 경우 사용
# %s에 정수를 대입
price = 1000
print("가격 : %s" % price)
# %s에 문자열을 대입
time = "13:49"
print("현재 시간 : %s" % time)
# %s를 2개 이상을 사용하고자 할 때는 해당하는 %s의 개수 만큼 소괄호로 묶어서 형식 지정자에 대입
temp = "현재 시간은 %s 시 %s 분 %s 초입니다."
print(temp % (10, 38, 12))
