import turtle

window = turtle.Screen()
window.bgcolor('black')
galatic = turtle.Turtle()
galatic.speed(20)
galatic.color('white')

rotate=int(180)

def Circles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4

def drawCircles(t,size,repeat):
  for i in range (repeat):
    Circles(t,size)
    t.right(360/repeat)

drawCircles(galatic,150,10)

t1 = turtle.Turtle()
t1.speed(20)
t1.color('yellow')

rotate=int(90)

def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10

def drawCircles(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)
drawCircles(t1,130,10)
t2= turtle.Turtle()
t2.speed(20)
t2.color('blue')

rotate=int(80)

def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5

def drawCircles(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)

drawCircles(t2,110,10)
t3 = turtle.Turtle()
t3.speed(20)
t3.color('red')

rotate=int(90)

def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19

def drawCircles(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)

drawCircles(t3,80,10)
t4= turtle.Turtle()
t4.speed(20)
t4.color('green')

rotate=int(90)

def Circles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20

def drawCircles(t,size,repeat):
    for i in range (repeat):
        Circles(t,size)
        t.right(360/repeat)

drawCircles(t4,40,10)

turtle.done()
