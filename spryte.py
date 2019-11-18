from JiangFunctions import*
turtle.colormode(255)
bob.width(10)
bob.speed(0)

x = -500
y = 400
jump(x,y)
for times in range(255):
    c = (35,times,75)
    bob.color(c)
    bob.forward(1500)
    jump(x,y-times*3)

turtle.goto(1,-100)
turtle.color("orange")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

#first mountain range
bob.begin_fill()
bob.color("grey")
bob.width(10)
jump(-500,-50)

bob.speed()

bob.left(40)
bob.forward(100)
bob.right(90)
bob.forward(200)
bob.left(100)
bob.forward(250)
bob.right(120)
bob.forward(300)
bob.left(120)
bob.forward(300)
bob.right(100)
bob.forward(200)
bob.left(110)
bob.forward(250)
bob.goto(1500,-500)
bob.end_fill()


bob.left(120)
bob.forward(300)
bob.right(100)
bob.forward(200)
bob.left(110)
bob.forward(250)
bob.goto(1500,-500)
bob.end_fill()

