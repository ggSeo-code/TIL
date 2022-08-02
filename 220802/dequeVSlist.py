# deque 와 list 의 성능 테스트 비교
from collections import deque
import time     # 성능테스트를 하기 위해서 time 모듈을 가지고 옴

# 저장 성능 테스트
# 아무런 요소가 없는 deque 를 생성함
deque_test = deque()
start = time.time()     # 시작 시간을 저장(second 단위)

for i in range(1000000):
    deque_test.insert(1,"x")

end = time.time()
print("deque append 시간 : ", end - start)

# 빈 리스트를 생성
list = list()
start = time.time()     # 시작 시간을 저장(second 단위)
for i in range(1000000):
    list.insert(1,"x")
end = time.time()
print("list append 시간 : ", end - start)

print("--------------------------------")
# 추출 기능 테스트
# start = time.time()     # 시작 시간을 저장(second 단위)
# for i in range(100000000):
#     deque_test.pop()
# end = time.time()
# print("deque pop 시간 : ", end - start)
#
# start = time.time()     # 시작 시간을 저장(second 단위)
# for i in range(100000000):
#     list.pop()
# end = time.time()
# print("list pop 시간 : ", end - start)

# start = time.time()     # 시작 시간을 저장(second 단위)
# for i in range(10000000):
#     deque_test.popleft()
# end = time.time()
# print("deque popleft() 시간 : ", end - start)
#
# start = time.time()     # 시작 시간을 저장(second 단위)
# for i in range(10000000):
#     list.pop(0)
# end = time.time()
# print("list pop(0) 시간 : ", end - start)

# 결론
# list, deque 중 데이터를 추가를 할 때는 deque 가 훨씬 좋은 성능을 발휘함, 대용량일수록 더욱더 많은 차이가 있음,
# 중간에 삽입하는 기능 역시 deque 가 훨씬 빠르다.
# 추출할 때도 deque 가 list 보다 훨씬 빠른 성능을 보인다.
# 데이터용량이 클수록 deque 사용을 고려해 봐야한다.