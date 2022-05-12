import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("#ffb6c1")
c = [
    "yellow","red","pink","cyan","green","blue","white","grey","purple"
    ]
for i in range(100):
    for j in range(2):
        t.speed(0)
        t.pensize(2)
        t.circle( i * 2)
    t.lt(10)
    t.pencolor(c[i % 5])
turtle.done()
