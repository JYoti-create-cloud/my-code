import turtle
f=turtle.Turtle()
wn=turtle.Screen()
wn.title("FLAG OF NEPAL")
wn.bgcolor("black")
f.setheading(-90)
f.color("black")
f.pensize(2)
f.begin_fill()
f.color("red")

f.up()

f.goto(0,-100)
f.down()
f.goto(0,155)
f.up()
f.goto(0,145)
f.down()
f.left(55)
f.forward(200)
f.right(150)
f.forward(100)
f.right(220)
f.forward(150)
f.right(135)
f.forward(170)
f.end_fill()
f.up()


f.goto(0,155)
f.color("blue")
f.begin_fill()
f.color("blue")
f.left(145)
f.down()
f.forward(230)
f.right(145)
f.forward(100)
f.left(138)
f.forward(150)
f.right(138)
f.forward(200)
f.right(90)
f.forward(8)
f.right(90)
f.forward(170)
f.left(134)
f.forward(150)
f.right(137.2)
f.forward(99)
f.left(149.5)
f.forward(200)
f.right(50)

f.forward(11)
f.end_fill()
f.color("white")
f.up()
f.goto(33,-11)
f.down()
f.begin_fill()
f.color('white')
f.circle(-15)
f.end_fill()
f.up()
f.goto(30,70)
f.begin_fill()
f.color('white')
f.right(180)
f.down()

f.circle(15,180)
f.left(180)
f.circle(-10,100)
f.forward(6)
f.up()
f.goto(30,70)
f.left(90)
f.down()
f.circle(10,100)
f.forward(2)
f.end_fill()



f.hideturtle()











wn.mainloop()