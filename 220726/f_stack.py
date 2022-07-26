# 함수를 만들어서 스택 사용하는 실습
def push(data, n):   # data : 스택 리스트(장소), n : 추가할 값
    data.append(n)

def pop(data):       # data : 스택 리스트(장소)
    # 유효성 검사(스택에 데이터가 없으면 에러 발생)
    if len(data) > 0:
        return data.pop()
    return False

def push_data(stack):
    for i in range(1, 5):
        push(stack, i)
        print("현재 스택 상태 : ", stack)

def pop_data(stack):
    for i in range(1, 6):
        pop(stack)
        if i >= 5:
            print("스택이 비었습니다.")
            return
        print("현재 스택 상태 : ", stack)

if __name__ == "__main__":    # 프로그램의 시작점
    stack = []
    push_data(stack)
    pop_data(stack)


