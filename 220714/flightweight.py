# 항공사에서 짐을 부칠 때, 20kg이 넘어가면 20,000원의 추가비용 20Kg 미만이면 수수료 0.
# 사용자로부터 짐의 무게를 입력을 받고 사용자가 지불해야하는 금액이 얼마인지 계산


weight = float(input("짐의 무게를 입력하세요 : "))

if weight > 20:
    print("짐의 무게가 20kg을 넘었기 때문에 추가비용 20,000원 내셔야 합니다.")
else:
    print("짐에 대한 수수료가 없습니다.")
    
print("감사합니다.고객님")