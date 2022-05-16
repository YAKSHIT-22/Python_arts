
from turtle import *

speed(1)
width(4)

bgcolor('black')

color('blue')

begin_fill()

penup()


goto(-50,60)
pendown()
# going to right top
goto (100,100)
# going to right bottom
goto (100,-100)
# going to left bottom
goto(-50,-60)
# going to starting point
goto(-50,60)

end_fill()

penup()

color('black')

width(10)


goto(-50,0)
pendown()

goto(100, 0)

penup()


goto (25,80)
pendown()

goto(25,-80)

done()