import math
def calcCircle(raidus):
    # 원의 넓이
    area = math.pi * raidus * raidus
    # 원의 둘레
    circumstance = 2 * math.pi * raidus

    return (area, circumstance)

if __name__ == "__main__":
    radius = float(input("원의 반지름을 입력하세요 : "))
    (area, circumstance) = calcCircle(radius)
    print("원의 넓이 : ", area, "원의 둘레 : ", circumstance)