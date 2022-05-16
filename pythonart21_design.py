#Import turtle
import turtle

#Setting the turtle object
pen=turtle.Turtle()
pen.speed(1)
#Setting the headposition  of turtle at angle 270 degree
pen.setheading(270)
pen.begin_fill()
#draws the penguin body
pen.circle(50,180)
pen.forward(80)
pen.circle(50,180)
pen.forward(80)
pen.end_fill()

#Belly of penguin
pen.fillcolor("white")
pen.goto(10,0)
pen.begin_fill()
pen.circle(40)
pen.end_fill()

#Eyes of penguin
pen.setheading(0)
pen.goto(30,80)
pen.begin_fill()
pen.circle(20)
pen.end_fill()
pen.goto(70,80)
pen.begin_fill()
pen.circle(20)
pen.end_fill()

# Eye  dot of penguins eye
pen.shape("circle")
pen.fillcolor("black")
pen.penup()
pen.goto(30,100)
pen.stamp()
pen.goto(70,100)
pen.stamp()


#Nose of penguin

pen.shape("triangle")
pen.fillcolor("orange")

pen.goto(50,70)
pen.setheading(270)
pen.stamp()

#Hands of penguin
pen.fillcolor("black")
pen.pencolor("white")
pen.setheading(180)
pen.goto(0,50)
pen.stamp()
pen.setheading(0)
pen.goto(100,50)
pen.stamp()


#legs of penguin
pen.shape("square")
pen.fillcolor("orange")
pen.goto(35,-50)
pen.stamp()
pen.goto(65,-50)
pen.stamp()
turtle.done()
