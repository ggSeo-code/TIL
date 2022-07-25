# 리스트 복사하기
# 얕은 복사(shallow copy) : 주소값을 공유하는 개념, 원본 리스트에 영향을 끼치는 복사 방법, 엄밀히 얘기하면 진정한 복사가 아니다.

scores = [10,20,30,40,50]
refer = scores     # scores 의 주소값을 refer 변수에게 복사
print("scores 의 주소값 : ", id(scores))
print("refer 의 주소값 : ", id(refer))
refer[0] = 100
refer.append(-70)
refer.insert(1, -100)
print("scores 의 주소값 : ", id(scores))
print("refer 의 주소값 : ", id(refer))

print("scores 의 요소값 : ", scores)
print("refer 의 요소값 : ", refer)

