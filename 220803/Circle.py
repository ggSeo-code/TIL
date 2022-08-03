
import math
class Circle:
    __radius = 0

    # 생성자
    def __init__(self, radius):
        self.__radius = radius

    # getter(), setter()제공
    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius = radius

    # 원의 넓이 구하는 메소드
    def calcArea(self):
        area = math.pi * self.__radius * self.__radius
        return area

    # 원의 둘레 구하는 메소드
    def calcCircum(self):
        value = 2 * math.pi * self.__radius
        return value

if __name__ == "__main__":
    circle = Circle(10)
    print("원의 반지름 : ", circle.getRadius())
    print("원의 넓이 : ", round(circle.calcArea(),2))
    print("원의 둘레 : ", round(circle.calcCircum(),2))

