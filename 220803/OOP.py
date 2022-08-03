# 객체지향 프로그래밍(OOP: Object Oriented Programming)
# 현실 세계에 있는 어떠한 사물을 코드로 표현하는 방법
# 클래스 용어 : 사물을 묘사하는 것이고 예를 들면 설계도, 붕어빵틀이다.
# 클래스 요소 : 멤버변수(필드, 속성), 멤버메서드(기능), 생성자(필수)
# Car 클래스 설계하기
class Car :
    # Car 클래스의 필드
    color = ""
    speed = 0



    def __init__(self):
        self.color = ""
        self.speed = 0
        print("기본생성자")
    # def __init__(self, color, speed):
    #     self.color = color
    #     self.speed = speed
    #     print("매개변수 생성자")
    # Car 클래스의 기능을 담당하는 메소드
    # 속도 높이는 메소드
    def upSpeed(self, speed):
        # self 는 자바에서 this 와 동일하며 자기 자신의 주소를 가지고 있는 인자다.인스턴스를 생성해야 비로소 self 는 활성화 된다.
        if speed < 0:    # 음수를 입력방지하기 위한 코드
            print("속도는 음수일수가 없습니다. 뒤로 갈까요?")
            return
        self.speed = speed

    # 속도 감소하는 메소드
    def downSpeed(self, speed):
        if speed < 0:    # 음수를 입력방지하기 위한 코드
            print("속도는 음수일수가 없습니다. 뒤로 갈까요?")
            return
        self.speed = speed

    # 멤버변수(필드)의 값을 출력해주는 메소드 추가
    def printFields(self, myCar):
        print("%s의 색상 : %s, 속도(감속,증속) : %dKm" % (myCar, self.color, self.speed))

if __name__ == "__main__":
    # Car 클래스의 인스턴스를 생성하여 사용하기
    myCar1 = Car()
    myCar2 = Car()
    myCar3 = Car()
    # 아래와 같이 주소를 찍어보면 각각 인스턴스는 독립적인 공간을 지니고 있다.
    print("myCar1의 주소 : ", id(myCar1))
    print("myCar2의 주소 : ", id(myCar2))
    print("myCar3의 주소 : ", id(myCar3))
    print("-----------------------------")
    print("myCar1의 타입 : ", type(myCar1))
    print("myCar2의 타입 : ", type(myCar2))
    print("myCar3의 타입 : ", type(myCar3))

    myCar1.color = "파랑색"
    myCar1.upSpeed(50)
    myCar1.printFields("myCar1")

    myCar2.color = "노랑색"
    myCar2.upSpeed(100)
    myCar2.printFields("myCar2")

    myCar3.color = "빨강색"
    myCar3.upSpeed(-100)
    myCar3.downSpeed(100)
    myCar3.printFields("myCar3")

    # 클래스를 설계하고 사용하는 루틴
    # 1. 클래스를 설계(정의)
    # 2. 인스턴스 생성하기
    # 3. 필드나 메소드를 호출하여 원하는 프로그램을 만들기