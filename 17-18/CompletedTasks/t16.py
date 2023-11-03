import turtle

def draw_square(x,y):
    for _ in range(4):
        t.forward(x)
        t.right(y)


window = turtle.Screen()
t = turtle.Turtle()

t.speed(20)

t.color("grey")
t.begin_fill()
draw_square(200,90)
t.end_fill()

t.left(45)
t.color("red")
t.begin_fill()
t.forward(140)
t.right(90)
t.forward(140)
t.end_fill()

t.penup()
t.goto(30,-20)
t.pendown()
t.left(45)

t.color("white")
t.begin_fill()
draw_square(50,90)


t.penup()
t.goto(125,-20)
t.pendown()
draw_square(50,90)

t.end_fill()

t.penup()
t.goto(80,-120)
t.pendown()

t.color("brown")
t.begin_fill()
for _ in range(2):
    t.forward(40)
    t.right(90)
    t.forward(80)
    t.right(90)
t.end_fill()


t.penup()
t.goto(-200,90)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(90)
t.end_fill()



t.penup()
t.goto(-200,-70)
t.pendown()
t.color("brown")
t.begin_fill()
for _ in range(2):
    t.forward(20)
    t.right(90)
    t.forward(130)
    t.right(90)
t.end_fill()

t.penup()
t.goto(-190,-70)
t.pendown()
t.color("green")
t.begin_fill()
t.circle(50)
t.end_fill()

t.hideturtle()

window.exitonclick()