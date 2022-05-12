import turtle
wn = turtle.Screen()
wn.bgcolor("white")
alex = turtle.Turtle()
alex.pensize(4)
alex.shape("classic")
alex.stamp()
alex.speed(20)
alex.right(90)
alex.up()
alex.forward(100)
alex.stamp()
for _ in range(12):
        alex.goto(0, 0)
        alex.right(30)
        alex.up()
        alex.forward(100)
        alex.stamp()

tracy = turtle.Turtle()
tracy.shape("triangle")
tracy.pensize(2)
tracy.speed(20)
tracy.right(90)
tracy.up()
tracy.forward(90)
tracy.stamp()
for _ in range(12):
        tracy.goto(0, 0)
        tracy.right(30)
        tracy.up()
        tracy.forward(90)
        tracy.stamp()


import turtle

tanenbaum = turtle.Turtle()

tanenbaum.hideturtle()
tanenbaum.speed(20)

for i in range(350):
    tanenbaum.forward(i)
    tanenbaum.right(98)


wn.exitonclick()