
   
import turtle

t = turtle.Turtle()
S = turtle.Screen()

S.bgcolor("black")
t.speed(0)
color = ("yellow","red","pink","cyan","green","blue","white","grey","purple")

for i in range(200):
    t.pencolor(color[i%6])
    t.circle(190-i/2,90)
    t.lt(90)
    t.circle(190-i/3,90)
    t.lt(60)
S.exitonclick()