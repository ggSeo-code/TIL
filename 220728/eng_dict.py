# 영한 사전 만들기
# 공백 딕셔너리 생성하고 여기에 영어단어를 키로 하고 설명을 값으로 저장

eng_dict = dict()     # 빈 딕셔너리 생성

# 빈 딕셔너리에 데이터를 추가하기
eng_dict["one"] = "하나, 일"
eng_dict["two"] = "둘, 이"
eng_dict["three"] = "셋, 삼"
eng_dict["four"] = "넷, 사"
eng_dict["five"] = "다섯, 오"

while True:
    word = input("단어를 입력하시오(종료를 하시려면 '종료'라고 입력하세요 : ")
    # 무한루프를 빠져나가는 코드
    if word == "종료":
        print("프로그램을 종료합니다.")
        break
    # 입력한 단어가 있는지 확인
    if word in eng_dict:
        print(eng_dict.get(word))   # 딕셔너리에 해당하는 단어가 존재하면 출력
    else:
        print("해당하는 단어가 없습니다.")

