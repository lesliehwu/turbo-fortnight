import turtle

def drawPolygon(t,sideLength,numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

def draw_balls(my_turtle,size,x,y):
    my_turtle.penup()
    my_turtle.goto(x,y)
    my_turtle.pendown()
    my_turtle.circle(size)

def draw_shaft(my_turtle,height,width,x,y):
    my_turtle.penup()
    my_turtle.goto(x,y)
    my_turtle.pendown()
    my_turtle.left(90)
    my_turtle.forward(height)
    my_turtle.right(90)
    my_turtle.forward(width)
    my_turtle.right(90)
    my_turtle.forward(height)
    my_turtle.right(90)
    my_turtle.forward(width)

def draw_head(my_turtle,length,x,y):
    my_turtle.penup()
    my_turtle.goto(x,y)
    my_turtle.pendown()
    my_turtle.right(120)
    my_turtle.forward(length)
    my_turtle.right(120)
    my_turtle.forward(length)

turt = turtle.Screen()
crush = turtle.Turtle()

draw_balls(crush,20,25,0)
draw_balls(crush,20,-15,0)
draw_shaft(crush,150,40,-15,40)
draw_head(crush,40,-15,190)


turt.exitonclick()
