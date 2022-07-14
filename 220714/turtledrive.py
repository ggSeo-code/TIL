# 사용자에게 명령어를 입력받아서 터틀그래픽 제어

import turtle
# 펜의 기능을 t라는 변수에 저장
t = turtle.Pen()
# 반복문 무한루프로 if 구문을 이용하여 방향을 제어하는 코드
# **무한루프 -> 반드시 루프를 탈출하는 코드가 반드시 있어야 함
while True:
    direction = input("왼쪽=left, 오른쪽=right, 종료=quit 입력 : ")
    # break 무한루프 탈출
    if direction == "quit":
        print("종료되었습니다.")
        break
    # 사용자가 left 를 입력했을때
    if direction == "left":
        print("left 를 입력하셨습니다.")
        t.left(60)
        t.forward(50)
    # 사용자가 right 를 입력했을때
    if direction == "right":
        print("right 를 입력하셨습니다.")
        t.right(60)
        t.forward(50)

# **안꺼지게= 클릭해야 꺼짐
turtle.exitonclick()



