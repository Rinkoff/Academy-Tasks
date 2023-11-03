import turtle

window = turtle.Screen()
t = turtle.Turtle()

t.color("red")
t.pensize(3)
t.begin_fill()

t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)

t.end_fill()
window.exitonclick()