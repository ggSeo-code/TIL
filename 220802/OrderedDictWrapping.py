# 일반 딕셔너리를 정렬을 하여 OrderedDict 로 포장하기
dic = {}
dic["z"] = 100
dic["a"] = 200
dic["e"] = 300
dic["d"] = 400
dic["e"] = 500
dic["h"] = 500
dic["j"] = 500
dic["h"] = 500
dic["1"] = 500
dic["3"] = 500
dic["m"] = 500
print(dic)
# 키, 값으로 정렬 해보기
li1 = (sorted(dic.keys()))
li2 = (sorted(dic.values()))
print(li1)
print(li2)
print(dic["3"])

from collections import OrderedDict

# 넘어오는 t의 값은 딕셔너리의 요소 -> 0 인덱스가 키값이 됨
def sort_by_key(t):
    return t[0]

dic1 = {}
dic1["z"] = 500   # z : 100
dic1["a"] = -10
dic1["e"] = 300
dic1["d"] = 400
# 일반 딕셔너리의 내용을 sorted() 를 이용하여 정렬을 하면 키를 기준으로 정렬된 리스트가 리턴.
# OrderedDict() 로 포장(wrapping) 기존의 딕셔너리나 리스트의 순서를 지키면서 딕셔너리의 형태로 관리를 할 수가 있다.
for k, v in OrderedDict(sorted(dic1.items(), key=sort_by_key)).items():
    print(k, v)

# li3 =sorted(dic1.items(), key=sort_by_key)
# print(li3)

# 딕셔너리의 동등성 비교
# 동등성은 논리적 동등이라는 것을 의미한다.논리적 동등이란은 주소는 다르지만 요소들의 값이 순서가 비록 틀리더라도 논리적 동등으로 바라보는 시점이다.
# 일반적인 딕셔너리의 동등성 비교
dic1 = {"가":1, "나":2, "다":3 }
dic2 = {"가":1, "다":3, "나":2 }
print(id(dic1))
print(id(dic2))
print(dic1 == dic2)
print("-------------------------")
from collections import OrderedDict
# OrderedDict 는 두 개의 OrderedDict 를 비교할 때 해당하는 값들의 순서와 해당하는 키와 값이 같아야지만 동등하게 바라본다.
# 일반적인 딕셔너리보다 좀 더 디테일하게 비교하는 것이 OrderedDict 의 특징이다.
ordered_dic1 = OrderedDict({"가":1, "나":2, "다":3 })
ordered_dic2 = OrderedDict({"가":1, "다":3, "나":2 })
ordered_dic3 = OrderedDict({"가":1, "나":2, "다":3 })
print(id(ordered_dic1))
print(id(ordered_dic2))
print(ordered_dic1 == ordered_dic2)
print(ordered_dic1 == ordered_dic3)

# 결론
# 첫 번째는 OrderedDict 모듈은 딕셔너리의 순서대로 저장하지 않는 방식을 순서대로 저장하는 방식으로 개선되었다.
# (파이썬 버전이 3.6 이후로는 저장과 출력이 OrderedDict 와 동일하게 작동을 하고 있지만 2.x 버전에서는 문제점이 발생한 것을 보았다.)
# 두 번째는 딕셔너리의 동등성 비교에서 일반적인 딕셔너리는 순서를 유지하지 않아도 해당 키와 값이 동등하다면 True 를 리턴하지만,
# OrderedDict 에서는 순서, 키와 값이 무조건 같아야 True 를 리턴하는 좀 더 강한 동등성 비교로 개선되었다.
# OrderedDict 를 사용을 하면 정확한 데이터의 순서나 값을 유지하는데 일반 딕셔너리에 비해서는 엄청 좋은 면이 존재한다.
# 딕셔너리보다는 OrderedDict 모듈을 이용하는 것이 효율적일 수 있음







