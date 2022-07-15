# 문자열의 중앙에 있는 문자를 추출
# ex. "weekday"-> "k"출력
# but, 짝수 개 중앙-> 2개의 문자를 출력 ex. "monday" -> "nd"

str_1 = input("문자열을 입력하세요 : ")
length = len(str_1)  # 문자열의 길이
# 문자열의 길이/2 나머지 1 = 홀수
if (length % 2) == 1:
    ch = str_1[length//2]
    print("중앙에 있는 한 글자는 ", ch)
else:   # 짝수
    ch1 = str_1[length//2 - 1]
    ch2 = str_1[length//2]
    print("중앙에 있는 두 글자는 ", ch1, ch2)


