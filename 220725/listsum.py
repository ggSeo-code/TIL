
# 행의 합계를 구하는 실습
double_list = [
                [1, 2, 3, 4, 5 ],
                [6, 7, 8, 9],
                [11,12,13,14,15]
              ]
# 원하는 행의 합계를 구하는 방법
hap = 0
for i in range(len(double_list[0])):
    hap += double_list[0][i]
print("double_list[0] 행의 합계", hap)

# 전체 2차원 리스트의 합계를 구하는 방법
hap = 0
for i in range(len(double_list)):
    for j in range(len(double_list[i])):
        hap += double_list[i][j]
print("double_list 전체의 합계", hap)