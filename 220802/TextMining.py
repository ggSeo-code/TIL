# 텍스트 마이닝 기법
def file_read(text):
    # f_name = open("D:\TIL\220802\\lee.txt", mode="r", encoding="UTF-8")
    f_name = open("D:\TIL\220802\\lee.txt", mode="r", encoding="UTF-8")
    for line in f_name:
        words = line.strip().split()
        for word in words:
            if len(word) >= 2:
                text.append(word)
    print(text)

if __name__ == "__main__":
    from collections import defaultdict
    from collections import OrderedDict
    text = []
    file_read(text)
    word_count = defaultdict(lambda : 0)   # 값을 0으로 초기화
    # text 에 담긴 단어들의 빈도수를 증가시키는 부분
    for word in text:
        word_count[word] += 1
    for i, v in OrderedDict(sorted(word_count.items(), key=lambda t:t[1], reverse=True)).items():
        if v >= 2:
            print(i, v)