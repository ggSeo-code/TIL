# 자료구조_(통곡의 벽)천천히 이해하면서 할 것 
# 자료구조란? 데이터의 특징을 고려하여 데이터를 저장하는 방법
# 자료구조의 특징 : 최대한 메모리를 효율적으로 저장 및 반환하는 방법으로, 데이터를 관리하는 것, 대용량일수록 빨리 저장하고 빨리 검색하고,
# 메모리를 최대한 효율적으로 사용하면 유저들에게 실행결과를 빨리 돌려주는 방법

# 스택(stack) : 택시기사님의 동전통, LIFO(Last In First Out)
# 데이터를 저장하는 것을 push, 데이터를 추출할 때 pop 이라고 한다.
stack_data = []
# 스택에 값을 push 하고 있다.
stack_data.append(10)
stack_data.append(20)
stack_data.append(30)
stack_data.append(40)
stack_data.append(50)
print(stack_data)
# 스택에서 추출할 때는 pop()메서드를 사용
# pop() 메서드는 스택에서 마지막으로 들어온 데이터를 삭제하면서 삭제된 데이터를 반환한다.
print(stack_data.pop())
print(stack_data.pop())
print(stack_data)

# 입력받은 텍스트를 역순으로 추출하는 프로그램
word = input("문자열을 입력해주세요 : ")
# list()메서드를 사용하여 문자열을 리스트로 변환하고 있다.
word_list = list(word)
print(word_list)

result = []
# _ 라는 기호는 파이썬에서 상당히 많이 사용되는 기호인데, for 문을 루핑시킬 때, 루프 변수에 값을 사용하지 않을때, _ 로 할당받는 것이다.
for _ in range(len(word_list)):
    # 사용자에게서 입력 받은 문자 리스트의 마지막 부분부터 result[] 에 담고 있다.
    result.append(word_list.pop())
print(result)
