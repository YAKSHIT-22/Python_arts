import turtle
import math


turtle.Screen().bgcolor('black')

Johny = turtle.Turtle()
Johny.speed(0)
Johny.color('white')
Steve = turtle.Turtle()
Steve.speed(0)
Steve.color('yellow')
Barry = turtle.Turtle()
Barry.speed(0)
Barry.color('blue')
Terry = turtle.Turtle()
Terry.speed(0)
Terry.color('orange')
Will = turtle.Turtle()
Will.speed(0)
Will.color('pink')
Nich = turtle.Turtle()
Nich.speed(0)
Nich.color('red')


minus = int(5)
print ("Click on results now")

while True:

 def drawCircles(t,size):
     for i in range(10):
         t.circle(size)
         size=size- minus+62
 def drawSpecial(t,size,repeat):
   for i in range (repeat):
     drawCircles(t,size)
     t.right(360/repeat)
 drawSpecial(Johny,100,10)

 def drawCircles(t,size):
     for i in range(4):
         t.circle(size)
         size=size - minus -3
 def drawSpecial(t,size,repeat):
     for i in range (repeat):
         drawCircles(t,size)
         t.right(360/repeat)
 drawSpecial(Steve,100,10)

 def drawCircles(t,size):
     for i in range(4):
         t.circle(size)
         size=size- minus
 def drawSpecial(t,size,repeat):
     for i in range (repeat):
         drawCircles(t,size)
         t.right(360/repeat)
 drawSpecial(Barry,100,10)

 def drawCircles(t,size):
     for i in range(4):
         t.circle(size)
         size=size- minus + 2
 def drawSpecial(t,size,repeat):
     for i in range (repeat):
         drawCircles(t,size)
         t.right(360/repeat)
 drawSpecial(Terry,100,10)

 
 def drawCircles(t,size):
     for i in range(4):
         t.circle(size)
         size=size-minus*3
 def drawSpecial(t,size,repeat):
     for i in range (repeat):
         drawCircles(t,size)
         t.right(360/repeat)
 drawSpecial(Will,100,10)

 def drawCircles(t,size):
     for i in range(4):
         t.circle(size)
         size=size-minus-45
 
 def drawSpecial(t,size,repeat):
     for i in range (repeat):
         drawCircles(t,size)
         t.right(360/repeat)
         drawSpecial(Nich,100,10)