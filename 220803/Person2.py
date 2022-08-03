from Person import *

if __name__ == "__main__":
    # 기본 생성자 호출
    # 기본 생성자는 호출되면 무조건 똑같은 초기값을 지니고 메모리에 생성된다.
    # 그리고 그 값을 변경하려면 직접 setter() 나 인스턴스명.필드 = 값 을 대입을 하여 변경하여야 하는 단점이 있다.
    person1 = Person()
    person1.__str__()
    print("--------------")
    person2 = Person()
    person2.__str__()
    print("--------------")
    print("person1.name : ", person1.getName())
    person1.setName("김길동")
    person1.age = 50
    print("person1.name : ", person1.getName())
    # age 라는 필드는 __ 붙지 않았기에 public 성질을 지니고 있어서 외부에서도 바로 접근이 가능하다.
    print("person1.address : ", person1.getAddress())
    print("person1.age : ", person1.age)


    # 같은 필드의 값을 가지고 있지만 서로 다른 인스턴스이다.
    # print("person1의 주소 :", id(person1))
    # print("person2의 주소 :", id(person2))