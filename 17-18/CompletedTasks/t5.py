import turtle

window = turtle.Screen()

t = turtle.Turtle()

for _ in range(6):
    t.forward(100)  
    t.left(60)


window.exitonclick()