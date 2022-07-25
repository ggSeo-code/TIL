
list1 = [4, 8, 9, -1, 10]
# 리스트 객체에서 제공해주는 sort()를 이용하여 정렬하는 방법
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

# 선택 정렬 알고리즘
# 주어진 리스트 중에서 일단 최솟값을 찾는다.
# 그 최솟값을 맨 앞에 위치한 값과 교환한다.
# 맨 처음 위치를 뺀 나머지 리스트를 위와 똑같은 방법으로 루핑하면서 최종적으로 정렬이 이루어진다.
# **선택 정렬은 제자리 정렬이기 때문에 더블루프를 사용해야 한다.
def selectionSort(li):
    cnt = 0
    for i in range(len(li)-1):
        min_idx = i
        for j in range(i+1, len(li)):
            if li[min_idx] > li[j]:
                min_idx = j

        if min_idx != i:   
            print(li[min_idx], li[i], "을 교환합니다.")
            li[i], li[min_idx] = li[min_idx], li[i]
            cnt += 1

    print(cnt, "만큼 교환이 이루어졌습니다.")
    return li

# 버블 정렬 알고리즘 인접한 두 원소를 검사하여 정렬하는 방법
# 장점 정확도 높다.
# 단점 데이터가 많아지면 질수록 속도가 떨어진다.
def bubble_sort(li):
    list_length = len(li)   # 길이가 10
    for i in range(list_length-1):
        for j in range(list_length-i-1):
            # 4, 6, 1, 10
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                #print(i, j, j+1, li)
        print(i, j, j + 1, li)

if __name__ == "__main__":
    li = [4,6,1,10,7,-7,-100,15,30,15]
    selectionSort(li)
    print(li)
    print("----------------------")
    li1 = [4, 6, 1, 10]
    bubble_sort(li1)
    print(li1)

    rows = 3
    cols = 15
    s = []

    for row in range(rows):
        s += [[0] * cols]
    print("s =", s)

    rows = 3
    cols = 15
    s = [([0] * cols) for row in range(rows)]  # 리스트 함축
    print("s =", s)

    s = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    # 행과 열의 개수를 구한다.
    rows = len(s)
    cols = len(s[0])
    for r in range(rows):
        for c in range(cols):
            print(s[r][c], end="\t")
        print()

    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]
    print(x)

