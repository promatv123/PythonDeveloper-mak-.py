import turtle

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("lightblue")
screen.title("Пейзаж")

t = turtle.Turtle()
t.speed(5)
t.width(3)

t.penup()
t.goto(0, 10)
t.pendown()
t.color("green")
t.begin_fill()
t.setheading(100)
for _ in range(3):
    t.forward(100)
    t.left(180)
t.end_fill()


t.hideturtle()
screen.exitonclick()