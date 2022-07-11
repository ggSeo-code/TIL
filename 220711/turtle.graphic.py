import turtle
##거북이가 그려주는 이것 저것
t = turtle.Pen()
##캔버스 커서 거북이 모양으로
t.shape("turtle")
t.pencolor("blue")

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)



##캔버스 안 꺼지게
turtle.exitonclick()
