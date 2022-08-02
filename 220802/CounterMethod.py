from collections import Counter
# 문자열
count = Counter()
print(count)
count.update("안녕하세요.")
print(count)
# update() : Counter 의 값을 갱신하는 것을 의미
count.update({"안":3, "요":5, "가":3})
print(count)
print(list(count.elements()))

# most_common(n) : 입력된 값의 요소들 중에서 빈도수가 높은 순으로 상위 n개를 리스트 안에 튜플 형태로 반환하는 메서드
print("-------------------------------")
count = Counter("apple, orange, grape")
# 매개변수를 주지 않았을 때는 전체 문자열을 대상으로 값과 빈도수를 출력
print(count.most_common())
# 매개변수를 주었을 때는 전체 문자열을 대상으로 빈도수를 순서가 높은 순 으로 n 개만큼 출력
print(count.most_common(5))

# substract() : 단어 그대로 요소의 값을 빼는 것을 의미
# 요소가 없는 경우에는 음수의 값을 출력
print("-------------------------------")
c1 = Counter("반갑습니다.안녕하세요.")
c2 = Counter("반갑다.친구야")
c1.subtract(c2)
print(c1)

print("-------------------------------")
# Counter() 는 산술/집합 연산이 가능
# 덧셈
c1 = Counter(["a","b","c","d","a"])
c2 = Counter("apple")
print(c1)
print(c2)
print(c1 + c2)
# 연산자로 뺄셈을 하면 음수의 값은 출력하지 않음(substract 와 차이점)
print("-------------------------------")
c1 = Counter(["a","b","c","d","a"])
c2 = Counter("apple")
print(c1)
print(c2)
print(c1 - c2)

print("-------------------------------")
# Counter 모듈의 교집합 및 합집합의 출력하는 기능
c1 = Counter("abcdefg")
c2 = Counter("abcd가나다라")
# 교집합을 하고자 할 때는 & 연산자를 사용
print("교집합 :", c1 & c2)
# 합집합을 하고자 할 때는 | 연산자를 사용
print("합집합 :",c1 | c2)

# 덧셈과 뺄셈만 Counter 모듈은 허용하지만, *, /, % 연산자는 지원하지 않는다
print("-------------------------------")
c1 = Counter([1,2,3,4,5])
c2 = Counter([2,3,4,5,6])
print(c1)
print(c2)
# print(c1 % c2)
# print(c1 * c2)
# print(c1 / c2)

