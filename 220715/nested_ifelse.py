# 중첩(nested) if ~ else 구문 실습

appleQuality = input("사과의 상태를 입력하시오(좋음, 나쁨) : ")

if appleQuality == "좋음":
    applePrice = int(input("사과 1개당 가격을 입력하세요 : "))
    if applePrice < 1000:   # 중첩 if 구문
        print("10개를 산다.")
    else:
        print("5개를 산다")
else:
    print("사과를 사지 않는다.")


