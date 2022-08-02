from collections import defaultdict
# words 라는 set 을 받아서 길이를 키로 하고 값을 리스트 값으로 하는 딕셔너리 리턴하는 함수
def counterWords(words):
    grouper = defaultdict(set)
    print(grouper)
    for word in words:
        length = len(word)
        grouper[length].add(word)
    return grouper

if __name__ == "__main__":
    set1 = set()
    set1.add("한국")
    set1.add("미국")
    set1.add("우즈베키스탄")
    set1.add("사우디아라비아")
    set1.add("스페인")
    dic1 = counterWords(set1)
    print(dic1)