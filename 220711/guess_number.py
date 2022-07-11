print("숫자게임 시작합니다.")
number = 62
# input() 사용자로부터 값을 입력
exact_num = input("1에서 100사이의 숫자를 추측해보세요.")
print(exact_num)
# int() 문자열(input) -> 숫자
guess = int(exact_num)

if guess == number :
    print("맞았습니다")
else :
    print("틀렸습니다")

print("게임이 종료되었습니다.")