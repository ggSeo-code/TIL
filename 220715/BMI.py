# 몸무게와 키를 입력받고 BMI 가 20.0이상이고 25미만이면 '표준'
# 키를 입력받고 100.0으로 나누고 공식에 대입
# BMI = 몸무게 / (키 * 키)

height = float(input("키(cm)를 입력 : "))
weight = float(input("몸무게(kg)를 입력 : "))
# 복합대입 연산자
height /= 100.0  # height = height / 100.0 와 동일
bmi = weight / (height * height)
print("bmi 값 :", bmi)

if(bmi >= 20.0) and (bmi < 25.0):
    print("표준입니다.")
else:
    print("체중 관리가 필요합니다.")

