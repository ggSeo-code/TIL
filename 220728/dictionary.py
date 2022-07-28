# 딕셔너리(dictionary) : 사전과 매우 유사하다. 사전에는 단어와 단어의 설명이 저장되어 있다.
# 파이썬에서는 키(key)와 값(value)의 쌍을 저장할 수 있는 객체를 딕셔너리라고 한다.

# 딕셔너리 생성방법은 { } "키:값" 같은 형태로 요소를 넣어주면 된다.
dic1 = {1:"사과", 2:"토마토", 3:"오렌지"}
print(dic1)
# 딕셔너리의 키값은 변경 불가능한 객체이어야 한다.문자열이나 숫자를 권장
# 아래와 같이 키값을 리스트로 주면 TypeError 가 발생
# dic2 = {[1]:"사과", 2:"토마토", 3:"오렌지"}

# 딕셔너리의 키값의 자료형은 혼합되어도 된다.(권장하지 않음)
dic2 = {1:"사과", "2":"토마토", (3,):"오렌지"}
print(dic2)

# 공백 딕셔너리
dic3 = {}
print(dic3)
# set 객체도 역시 {}사용하기 때문에 혼돈이 있을수가 있다. 하여 set 을 생성할\
# 때는 내장함수인 set()사용해야 한다.
set1 = set()
print(set1)

# 딕셔너리 항목 추출하는 방법
dic4 = {1:"사과", 2:"토마토", 3:"오렌지"}
# 첫 번째 방법: []안에 키값
print("dic4[2]키의 값은 : ", dic4[2])
# 두 번째 방법: get()
print("dic4[1]키의 값은 : ", dic4.get(1))
# 만약에 키가 딕셔너리에 존재하지 않으면 KeyError 가 발생
# print("dic4[5]키의 값은 : ", dic4.get(5))   # 리턴값이 None
# print("dic4[5]키의 값은 : ", dic4[5])       # 에러 발생

# 키가 딕셔너리에 없으면 디폴트 값을 사용하는 방법
a = dic4.get(5, "파인애플")
print(a)

# 키가 딕셔너리에 존재하는지 알아보는 방법
print(1 in dic4)
print(5 not in dic4)

print("-------------------------------------")
# 딕셔너리 항목 추가하는 방법, 딕셔너리는 변경 가능한 객체
# 값을 추가,삭제를 해도 동일한 주소값을 가지고 있다.
dic5 = {1:"사과", 2:"토마토", 3:"오렌지"}
print("요소추가 전 주소 : ", id(dic5))
dic5[4] = "파인애플"
print("요소추가 후 주소 : ", id(dic5))

print("-------------------------------------")
# 딕셔너리의 항목을 삭제하는 방법
# pop()를 이용하여 키를 주면 키에 해당하는 항목 삭제가 이루어진다.
dic6 = {1:"사과", 2:"토마토", 3:"오렌지"}
a = dic6.pop(2)
print(a)
print(dic6)
# 또 다른 삭제방법은 del 키워드를 이용한다.
dic7 = {1:"사과", 2:"토마토", 3:"오렌지"}
del dic7[1]
print(dic7)

# 딕셔너리의 모든 항목을 삭제 : clear()
a = dic7.clear()
print(a)
print(dic7)