# ****문제
# 회문: 앞으로 읽으나 뒤로 읽으나 동일한 문장을 의미한다.
# ex. "mom","civic","dad" 등이 회문의 예이다.

# --------------------------------------------------------
def main():
    string = input("문자열을 입력하세요 : ")
    string = string.replace(" ", "")

    if check(string) == True:
        print(string + "은 회문입니다.")
    else:
        print(string + "은 회문이 아닙니다.")

def check(s):
    # 단어의 처음 인덱스와 마지막 인덱스를 저장하는 코드
    low = 0
    high = len(s)-1
    while True:
        # 회문이라면
        if low > high:
            return True

        s1 = s[low]
        s2 = s[high]
        print(s1, s2)
        # 회문아님
        if s1 != s2:
            return False
        # 인덱스 증가 비교항목 변경
        low += 1
        high -= 1

if __name__ == "__main__":
    main()

