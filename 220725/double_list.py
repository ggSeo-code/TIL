
# 3행 5열의 2차원 리스트
double_list = [
                [1, 2, 3, 4, 5 ],
                [6, 7, 8, 9],
                [11,12,13,14,15]
              ]

print(double_list)
print(double_list[0])
print(double_list[1])
print(double_list[2])

print(id(double_list))
print(id(double_list[0]))
print(id(double_list[1]))
print(id(double_list[2]))

# 해당하는 리스트의 길이를 출력해보기
print(len(double_list))
print(len(double_list[0]))
print(len(double_list[1]))
print(len(double_list[2]))

# 2차원 리스트의 출력을 할려면 반드시 더블루프를 사용해야 된다.
for i in range(len(double_list)):
    for j in range(len(double_list[i])):
        print(double_list[i][j], end="\t")   # tab 만큼 띄운다.
    print()     # 줄바꿈

# 2차원 리스트는 정적인 것 보다 동적으로 생성하여 사용하는 경우가 많다.
# rows = int(input("원하는 행을 입력해주세요 : "))
# cols = int(input("원하는 열을 입력해주세요 : "))
# dbl_list = []
# 일반적인 2차원 리스트 동적생성 방법
# for row in range(rows):
#     dbl_list += [[0] * cols]
# 리스트 함축을 이용한 방법
# dbl_list = [ ([0] * cols) for row in range(rows)]
# print(dbl_list)

# 1차원 리스트에서는 list1[0]값이 바로 변수와 동일
# 2차원 리스트에서는 list2[1][1]값이 바로 변수와 동일
li1 = [1,2,3]
li1[0] = 10   # 1차원 리스트에 값을 저장하는 형태
print(li1)

li2 = [[1,2],[3,4]]
li2[0][1] = -7    # 2차원 리스트에 값을 저장하는 형태
print(li2)