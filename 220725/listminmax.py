# 일반적인 리스트 연산들 실습
# 최소값 최대값을 구하는 알고리즘

#내장함수이용
num = [ 1, 5, -9, 100 ]
print("최소값 : ", min(num))
print("최대값 : ", max(num))

# **최대최소 알고리즘 코드리뷰하면서 숙지할것
prices = [1000,3000,500,10000,20000,700]
# 먼저 prices[]에 있는 0번째 인덱스 값을 변수에 저장
lowPrice = prices[0]
# 이후, 루프를 돌면서 조건식으로 값이 작으면 해당하는 값을 lowPrice 변수에 재저장
for i in range(1, len(prices)):
    # 참이다 = prices[i]가 lowPrice 보다 작다라는 의미
    # 조건절에서 부등호를 수정을 하면 최대값을 구할 수도 있다.
    if prices[i] < lowPrice:
        lowPrice = prices[i]
print("가장 싼 가격 : ", lowPrice)
print("-------------------------")


words = ["dog","cat", "horse", "lion", "tiger", "elephant", "bi"]
word_han = ["안녕", "하이","가지마세요", "반갑습니다", "가세요", "오랜만입니다."]
# 문자열 리스트에서 min() 는 제일 첫 글자가 아스키코드 중 가장 작은 단어 반환
print("가장 짧은 단어 : ", min(words))
print("가장 짧은 단어 : ", max(words))
print("가장 짧은 단어 : ", min(word_han))
print("가장 짧은 단어 : ", max(word_han))

# 문자열에서 가장 짧은 문자열을 구하는 알고리즘 코드
shortest_word = words[0]
list_word = []
for i in range(1, len(words)):
    if len(words[i]) <= len(shortest_word):
        if len(words[i]) < len(shortest_word):
            list_word.clear()
            list_word.append(words[i])
        else:
            list_word.append(shortest_word)
            shortest_word = words[i]
            list_word.append(shortest_word)

print("가장 짧은 단어이거나 같은 단어들 : ", list_word)

for i in range(len(list_word)):
    print("가장 짧은 단어 : ", list_word[i])




