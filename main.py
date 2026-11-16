from myfunctions import *

bob.speed(0)
bob.hideturtle()

sky()

cloud(-200, 200)
cloud(0, 250)
cloud(150, 180)

for times in range(2):
    tree(-250 + times * 100, -200)

sun(350, 360)

turtle.done()

