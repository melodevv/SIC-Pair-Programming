import turtle
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']
aiden = turtle.Turtle()
turtle.bgcolor('black')

t = turtle.Pen()
t.color('white')
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x//100+1)
    t.forward(x)
    t.left(80)
    t.speed(50)
t.penup()
for x in range(36):
    t.forward(250)
    t.pendown()
    t.circle(5)
    t.penup()
    t.backward(250)
    t.right(10)
    t.pencolor(colors[x % 6])

