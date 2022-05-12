import turtle
import time
import random
import math

wn = turtle.Screen()
wn.bgcolor('black')


color_list = ['red','green','orange','purple','yellow','blue']
turtle_list = []
for i in range(5):
	wr = turtle.Turtle()
	wr.shape('turtle')
	wr.setheading(90)
	wr.setposition(-200+(i*100),-200)
	wr.color(color_list[i])
	wr.pensize(5)
	turtle_list.append(wr)
for i in range(0,2):
	for j in range(0,8):	
		line = turtle.Turtle()
		line.color('white')
		line.penup()
		line.shape('square')
		if i ==0 :
			line.setposition(-250+((70*j)),250-(30*i))
		else:
			line.setposition(-215+((70*j)),250-(30*i))	

def res():
	wn.clear()
	wn.bgcolor('black')
	msg.write('Game Over',False,align = 'center',font = ('Arial',25))
	time.sleep(3)
	flag = 0		
		
msg = turtle.Turtle()
msg.color('white')
msg.hideturtle()
msg.penup()

while True:

	for j in turtle_list:
		speed = random.randint(10,20)
		y  = j.ycor()+speed
		x  = j.xcor()
		j.goto(x,y)
	
		distance = j.ycor()
		x = j.xcor()
		winner = (x/100)-1
		if (distance>210):
			res()
line.mainloop()
