# defaultdict 모듈은 딕셔너리의 요소를 생성할 때, 키에 기본 값을 지정하는 방법

# 일반적인 딕셔너리를 생성하고 키의 값으로 값을 알아낼 수 있다.
dic = dict()
print(dic)
# 비어진 딕셔너리에 "a"라는 키는 없다는 오류가 발생한다.
# print(dic["a"])
print(dic.get("a"))

from collections import defaultdict
dic = defaultdict(lambda : 0)   # lambda 를 이용하여 0을 리턴하게 만듬
print(dic["a"])
print(dic["b"])
print(dic[100])
print(dic)

print("----------------------------")
dic.clear()
dic = defaultdict(int)     
dic["a"] += 100           
print(dic["a"])
print(dic["b"])
print(dic[100])
print(dic)


print("----------------------------")
dic.clear()
dic = defaultdict(float)    
print(dic["a"])
print(dic["b"])
print(dic[100])
print(dic)

print("----------------------------")
dic.clear()
dic = defaultdict(str)    
print(dic["a"])
print(dic["b"])
print(dic[100])
print(dic)