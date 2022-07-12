# 사용자로부터 참석하는 인원의 수를 받아 해당하는 인원의 수에 따라
# 치킨은 인원당 1마리, 맥주는 인원당 2병, 케익은 인원 4개를 출력

# input()함수는 사용자로부터 입력->'문자열형태'
# 문자열을 숫자로 변환-> int()함수
number = int(input("참석자 수를 입력하세요 : "))
print(type(number))
chickens = number
beers = number * 2
cakes = number * 4
print("치킨의 수 : ", chickens)
print("맥주의 수 : ", beers)
print("케익의 수 : ", cakes)
