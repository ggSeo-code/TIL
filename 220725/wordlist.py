# 문자열에 대한 리스트 함축

# 문자열의 첫 번째 문자만 가지는 리스트를 생성
list1 = ["KOREA","대한민국","서울특별시","한라산","END"]
first_word = [word[0] for word in list1]
print("단어의 첫 문자 : ", first_word)

# 문자열의 마지막 번째 문자만 가지는 리스트를 생성
list1 = ["KOREA","대한민국","서울특별시","한라산","END"]
first_word = [word[len(word)-1] for word in list1]
print("단어의 끝 문자 : ", first_word)

# 문자열의 길이만 가지는 리스트를 생성
list1 = ["KOREA","대한민국","서울특별시","한라산","END"]
first_word = [len(word) for word in list1]
print("단어의 길이 : ", first_word)

# 상호곱(Cross Product)
colors = ["흰색", "브라운색", "검정색"]
cars = ["그랜져", "소나타", "스파크", "아반떼", "봉고"]
colors_cars = [ x+"-"+y for x in colors
                        for y in cars  ]
print("색상과 차종 : ", colors_cars)


