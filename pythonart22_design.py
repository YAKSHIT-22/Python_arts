import turtle
t = turtle.Turtle()
turtle.Screen().bgcolor("green")
def circles(color, radius):
    # Set the fill
    t.fillcolor(color)
    # Start filling the color
    t.begin_fill()
    # Draw a circle
    t.circle(radius)
    # Ending the filling of the color
    t.end_fill()
# Draw first ear
t.up()
t.setpos(-35, 95)
t.down
circles('black', 15)
# Draw second ear
t.up()
t.setpos(35, 95)
t.down()
circles('black', 15)
#....... Draw face ......#
t.up()
t.setpos(0, 35)
t.down()
circles('white', 40)
#-------Draw eyes black-------#
# Draw first eye
t.up()
t.setpos(-18, 75)
t.down
circles('black', 8)
# Draw second eye
t.up()
t.setpos(18, 75)
t.down()
circles('black', 8)
#-------Draw eyes white-------#
# Draw first eye
t.up()
t.setpos(-18, 77)
t.down()
circles('white', 4)
# Draw second eye
t.up()
t.setpos(18, 77)
t.down()
circles('white', 4)
#-------Draw nose-------#
t.up()
t.setpos(0, 55)
t.down
circles('black', 5)
#-------Draw mouth-------#
t.setpos(0, 55)
t.down()
t.right(90)
t.circle(5, 180)
t.up()
t.setpos(0, 55)
t.down()
t.left(360)
t.circle(5, -180)
t.hideturtle()