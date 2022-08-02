from collections import defaultdict

def counterWords(words):
    grouper = defaultdict(list)
    print(grouper)
    for word in words:

        length = len(word)
        grouper[length].append(word)
    return grouper
    
if __name__ == "__main__":
    li1 = ["감자", "귤", "사과", "배", "오징어", "꼼장어", "불가사리"]
    dic1 = counterWords(li1)
    print(dic1)
    print(dic1[2])