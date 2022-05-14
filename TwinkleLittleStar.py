import turtle
import random
import time

turtle.color("yellow")
turtle.hideturtle()
turtle.tracer(0)
if turtle.bgcolor()== 'white':
    turtle.bgcolor("black")
def drawstar():
    turtle.begin_fill()
    for i in range(5):
     turtle.forward(100)
     turtle.right(144)
    turtle.end_fill()
    turtle.update()

colorlist=["red","blue","green","yellow","orange","purple","black"]
for i in range(100):
    turtle.clear()
    turtle.color(random.choice(colorlist))
    turtle.penup()
    turtle.goto(random.randint(-100,100), random.randint(-100,100))
    turtle.goto(random.randint(-50, 50), random.randint(-50, 50))
    turtle.pendown()
    drawstar()
    time.sleep(0.5)
turtle.done()
