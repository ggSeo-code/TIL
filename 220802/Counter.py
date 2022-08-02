# Counter 모듈은 시퀀스 자료형의 데이터의 값의 개수를 딕셔너리 형태로 반환해주는 자료구조
# 같은 값이 몇 개가 존재하는지 쉽게 알아보고자 할 때 사용하면 편리함
from collections import Counter
# 문자열을 가지고 리스트를 생성함.
text = list("high school")
print(text)
print(type(text))
# Counter 객체를 만드는데 인자값으로 리스트형을 취함.
count = Counter(text)
print(type(count))
print(count)
# 시퀀스 자료형에서 어떤 특수문자의 개수를 알고 싶을때도 사용 가능
print(count["h"])

print("--------------------------------")
# Counter() 객체를 만들 때, 값=개수 와 같은 형태로 입력도 가능
count = Counter(A=3, b=1, c=5, a=3)
print(count)
# elements() 는 Counter 로 주어진 값의 요소에 해당하는 값을 풀어서 반환
# 요소는 무작위적으로 반환하며 요소의 수가 1보다 작을 경우에는 elements() 는 이를 출력하지 않음.
# 대소문자를 구별하여 sorted() 정렬됨
print(sorted(count.elements()))

print("------------------------------")
# a = "가"
# b = "나"
# 값=개수 형태로 Counter() 객체를 만들 때는 문자열은 매개변수로 쓸 수 없다.
# 문자열 자체를 매개변수로 넣어주는 것은 아래와 같이 가능
count = Counter("가나다라가나다라")
print(count)
print(sorted(count.elements()))

print("------------------------------")
# 아래 문자열은 소문자로 다 바뀌고 단어별로 만들어진 리스트가 반환됨
text = "abcdedfg abcdedfg repeat count! you can do it nice to meet you. A Coun" \
       "telephone!!!!".lower().split()
print(text)
print(Counter(text))

print("------------------------------")
# 딕셔너리 형태로 Counter 객체를 생성하는 방법
count = Counter({"가":4, "나":3})
print(count)
print(list(count.elements()))