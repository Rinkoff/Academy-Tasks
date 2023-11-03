import turtle

window = turtle.Screen()

t = turtle.Turtle()

t.right(66)

for _ in range(2):
    t.forward(100)
    t.right(45)
    t.forward(100)
    t.right(135)

window.exitonclick()