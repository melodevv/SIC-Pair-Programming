import turtle
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']
aiden = turtle.Turtle()
turtle.bgcolor('black')

t = turtle.Pen()
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x//100+1)
    t.forward(x)
    t.left(80)
    t.speed(5)
