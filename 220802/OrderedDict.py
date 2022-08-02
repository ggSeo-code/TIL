# OrderedDict 모듈: 이름 그대로 순서를 가지는 딕셔너리 객체이다.
# (원래, 딕셔너리는 순서를 보장하지 않는 객체)
# 일반적인 딕셔너리는 순서를 보장하지 않는게 원래의 딕셔너리 -> 딕셔너리는 인덱스가 없기 때문이다.
# 파이썬 버전이 3.6 이상일 경우 일반 딕셔너리가 입력된 순서대로 정확하게 출력, but 파이썬 버전이 2.x 에서는 순서가 중구난방으로 나온다(파이썬 튜터로 확인 가능)
dic = {}
dic["a"] = 100
dic["b"] = 200
dic["c"] = 300
dic["d"] = 400
dic["e"] = 500
dic["f"] = 500
dic["g"] = 500
dic["h"] = 500
dic["i"] = 500
dic["j"] = 500
dic["k"] = 500

for k, v in dic.items():
    print(k, v)

print("------------------------")
# OrderedDict 는 딕셔너리의 순서, 동등성 비교를 개선한 모듈이다.
from collections import OrderedDict

dic = OrderedDict()
dic["a"] = 100
dic["b"] = 200
dic["c"] = 300
dic["d"] = 400
dic["e"] = 500
dic["f"] = 500
dic["g"] = 500
dic["h"] = 500
dic["i"] = 500
dic["j"] = 500
dic["k"] = 500

for k, v in dic.items():
    print(k, v)
