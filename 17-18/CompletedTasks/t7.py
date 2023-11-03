import turtle

def draw_polygon(sides):
    window = turtle.Screen()
    t = turtle.Turtle()
    t.speed(10)

    angle = 360 / sides

    for _ in range(sides):
        t.forward(50)
        t.left(angle)

    window.exitonclick()


num_sides = int(input("Въведете брой на страните на многоъгълника: "))
draw_polygon(num_sides)
