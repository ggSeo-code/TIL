# 함수를 만들어서 Queue 실습하기

# 큐에 저장하는 함수
def offer(data, n):   # data 는 저장할 장소(list), n 은 저장할 값
    data.append(n)

# 큐에서 삭제하는 함수
def poll(data):
    if len(data) > 0:
        return data.pop(0)
    return False

def offer_insert(data):
    for i in range(1, 5):
        offer(data, i)
        print("큐의 현재 상태 : ", queue)

def poll_delete(data):
    for i in range(1, 5):
        poll(data)
        print("큐의 현재 상태 : ", queue)

if __name__ == "__main__":
    queue = []
    offer_insert(queue)
    poll_delete(queue)


