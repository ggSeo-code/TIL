# 단어에서 마침표를 제거하고 소문자로 만드는 함수.
def process(word):
    out_str = ""
    for ch in word:
        if ch.isalpha():     # 영문자라면....
            out_str += ch
    return out_str.lower()   # 단어를 소문자로 리턴해준다.

if __name__ == "__main__":
    words = set()     # 비어있는 세트를 만든다.
    f_name = input("입력 파일 이름 : ")
    file = open(f_name, mode="r")   # 파일을 열고 읽기 모드로 설정함.

    # 파일의 모든 줄에 대해서 반복한다.
    for line in file:
        lineWords = line.split()      # 한 라인을 읽어와서 단어(토큰)별로 분리하고 있다.
        for word in lineWords:
            words.add(process(word))           # 단어를 세트에 추가한다.

    print("사용된 단어의 개수 : ", len(words))
    print(words)
    file.close()