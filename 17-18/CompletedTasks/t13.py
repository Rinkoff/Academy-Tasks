import turtle
import random

window = turtle.Screen()
t= turtle.Turtle()
colors = ["red", "blue", "green", "purple", "orange", "pink"]

t.left(45)
for _ in range(10):
        t.color(random.choice(colors))
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)




window.exitonclick()