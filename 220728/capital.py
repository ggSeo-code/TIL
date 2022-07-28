
# 문자열을 입력하시오 : North Atlantic Treaty Organization
# 머리문자열 : NATO
#------------------------------------------------------------------
def main():
    string = input("문자열을 입력하시오 : ")
    acronym = ""
    # 입력받은 문자열을 대문자로 바꾼 후, 문자열을 분리
    for word in string.upper().split():
        acronym += word[0]

    print("머리문자열 : " + acronym)

if __name__ == "__main__":
    main()