# 함수를 이용하여 딕셔너리를 초기화 하는 코드

from collections import defaultdict
# 일반 딕셔너리 함수를 이용하여 초기화 방법
def countLetters(word):
    counter = {}
    for letter in word:
        # 넘어온 문자열의 값을 하나가 키가 되고 그 키의 기본값으로 0을 설정함.
        if letter not in counter:
            counter[letter] = 0
    return counter

# setdefault() 메서드를 이용한 초기화 방법
def countLetters_setdefalut(word):
    counter = {}
    for letter in word:
        # 위의 countLetters() 보다 조건절 사라졌지만 루프를 돌 때마다, setdefault() 를 계속 호출하므로 효율적이지 못한 코드임.
        counter.setdefault(letter, 0)
    return counter

# defaultdict 모듈을 직접 이용하는 방법
def countLetters_defalutdict(word):
    # 이 함수에서는 defaultdict() 만 한 번 호출이 일어난다.
    counter = defaultdict(lambda : 0)
    for letter in word:
        counter[letter] += 1
    return counter


if __name__ == "__main__":
    dic = countLetters("가나다라마")
    print(dic.items())
    print("---------------------------------")
    dic = countLetters_setdefalut("가나다라마")
    print(dic.items())
    print("---------------------------------")
    dic = countLetters_defalutdict("가나다라마")
    print(dic.items())



