import turtle

def draw_square(x,y):
    for _ in range(4):
        t.forward(x)
        t.right(y)


window = turtle.Screen()
t = turtle.Turtle()

draw_square(100,90)
t.penup()
t.goto(150,0)
t.pendown()
draw_square(100,90)




window.exitonclick()


