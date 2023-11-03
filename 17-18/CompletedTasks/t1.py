import turtle

window = turtle.Screen()

t = turtle.Turtle()

for _ in range(2):
    t.forward(50)
    t.right(90)
    t.forward(20)
    t.right(90)


window.exitonclick()