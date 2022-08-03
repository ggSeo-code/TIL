# Monitor 클래스를 이용한 실습
from Monitor import *

if __name__ == "__main__":
    # 매개변수가 있는 생성자를 호출하는 방법
    monitor1 = Monitor("LG", 32, 300000, "흰색")
    monitor1.__str__()

    print("-------------------------------")
    # 아래와 같이 setter() 를 통하여 기존에 생성자로 생성했던 값을 변경하고 있다.
    monitor1.setCompany("삼성")
    monitor1.setInch(27)
    monitor1.setPrice(150000)
    monitor1.setColor("검정색")
    monitor1.__str__()





