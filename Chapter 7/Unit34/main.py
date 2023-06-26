import turtle
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']
aiden = turtle.Turtle()
turtle.bgcolor('black')

t = turtle.Pen()
t.color('white')
for x in range(320):
    t.pencolor(colors[x % 6])
    t.width(x//100+1)
    t.forward(x)
    t.left(80)
    t.speed(50)
t.pendown()
t.penup()
for i in range(36):
    aiden.forward(280)
    aiden.pendown()
    aiden.color(colors[i % 6])
    aiden.circle(5)
    aiden.penup()
    aiden.backward(280)
    aiden.right(10)

