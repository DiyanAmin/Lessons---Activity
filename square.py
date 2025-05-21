#Drawing a square
import turtle
turtle.Screen().setup(500,500)
turtle.Screen().bgcolor('purple')
start=turtle.Turtle()
a = 0
while a<4:
    start.forward(100)
    start.right(90)
    a+=1
turtle.done()