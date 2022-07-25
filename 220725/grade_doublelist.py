# 성적 처리 프로그램(2차원 리스트)

# score = [
#          [100, 100, 100], [20, 20, 20],[30, 30, 30],
#          [40, 40, 40],[50, 50, 50]
#         ]
# 출력결과
# 번호	    국어	    영어	    수학   총점     평균
# -------------------------------------------------
#   1	    100	    100	    100	    300	    100.00
#   2	    20	    20	    20	    60	    20.00
#   3	    30	    30	    30	    90	    30.00
#   4	    40  	40	    40	    120	    40.00
#   5	    50	    50	    50	    150	    50.00
# -------------------------------------------------
# 총점	    240	    240	    240	    720	    48.00

# 문제 풀이
score = [ [100, 100, 100], [20, 20, 20],[30, 30, 30],
          [40, 40, 40],[50, 50, 50] ]
# 과목별 총점을 저장할 변수
korTotal = 0
engTotal = 0
mathTotal = 0

# 전체 합계와 평균을 저장하기 위한 변수
totalSum = 0
avg = 0.0
# 출력 상단부
print("번호     국어   영어   수학     총점     평균")
print("----------------------------------------------")

for i in range(len(score)):
    sum = 0    # 개인별 총점
    average = 0.0   # 개인별 평균

    korTotal += score[i][0]   # 국어 점수 누적
    engTotal += score[i][1]   # 영어 점수 누적
    mathTotal += score[i][2]  # 수학 점수 누적

    # 번호를 출력하는 부분
    print("%3d" % (i+1), end="\t")

    for j in range(len(score[i])):
        sum += score[i][j]   # 개인별 총점
        print("\t%d" % score[i][j], end="\t")
    
    totalSum += sum    # 총합
    average = sum / len(score[i])   # 개인별 평균
    avg += average   # 전체 평균
    print("\t%d\t\t%.2f" % (sum, average))

avg /= len(score)
print("----------------------------------------------")
print("총점\t%d\t\t%d\t\t%d\t\t%d\t\t%.2f" % (korTotal, engTotal, mathTotal, totalSum, avg))

    