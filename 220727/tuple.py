

data_list = [(90,80),(85,75),(90,100)]
for i, scores in enumerate(data_list):
    hap = 0
    for score in scores:
        hap += score
    print("%d번 학생의 총점은 %d이고, 평균은 %0.1f입니다." % (i+1, hap, hap/2.0))
