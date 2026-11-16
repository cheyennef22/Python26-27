#myfunctions

import turtle

bob = turtle.Turtle()
bob.speed(0) 

def polygon(sides, dist):
    angle = 360 / sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(dist)
        bob.left(angle)
    bob.end_fill()

def jump(x, y):
    bob.penup()
    bob.goto(x, y)
    bob.pendown()

def tree(x, y):
    jump(x, y)
    bob.width(5)
    bob.color("brown")
    polygon(4, 50)
    jump(-25 + x, 50 + y)
    bob.color("green")
    polygon(3, 100)

def sun(x, y):
    jump(x, y)
    bob.width(10)
    bob.color("yellow")
    for times in range(10):
        polygon(3, 20)
        bob.forward(30)
        bob.right(36)
    jump(16 + x, -75 + y)
    bob.width(20)
    bob.circle(30)

def sky():
    screen = turtle.Screen()
    screen.bgcolor("sky blue")

def cloud(x, y):
    jump(x, y)
    bob.color("white")
    for times in range(6):
        bob.begin_fill()
        bob.circle(30)
        bob.end_fill()
        bob.forward(20)

def dog(x, y):
    bob.width(1)
    bob.color("saddle brown")
    
    
    jump(x, y)
    polygon(4, 60)
    
    
    jump(x + 5, y - 30)
    polygon(4, 15)
    jump(x + 20, y - 30)
    polygon(4, 15) 
    jump(x + 40, y - 30)
    polygon(4, 15)
    
   
    jump(x + 40, y + 40)
    polygon(4, 30) 

   
    bob.color("dark brown")
    jump(x + 40, y + 55)
    polygon(3, 15)
    
    
    jump(x - 10, y + 50)
    bob.color("saddle brown")
    polygon(3, 15)


sky()
sun(180, 150)
cloud(-180, 120)


tree(-120, -200)
tree(-20, -200)


dog(80, -200)

