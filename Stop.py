import turtle
turtle.hideturtle()
sides = 8
turtle.color("red")

def drawOct(x ,y,size):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(sides):
        turtle.forward(size)
        turtle.right(360 / sides)
    turtle.end_fill()


drawOct(0,0,100)
turtle.color("white")
drawOct(6,-12,90)
turtle.color("red")
drawOct(10,-25,80)
turtle.color("white")
turtle.penup()
turtle.goto(50,-145)
turtle.write("STOP", align="center", font=("Ariel", 40, "bold"))
turtle.done()

