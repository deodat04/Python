import turtle
import math
c=["green","red","purple"]
t=turtle.pen()
turtle.bgcolor("black")
turtle.shape("turtle")
turtle.color("green")
turtle.speed(158000005)
for i in range (1200):
    turtle.pencolor(c[i%3])
    turtle.width(i/20+1)
    turtle.rt(120)
    turtle.fd(i)
    turtle.rt(144)
    turtle.fd(i)

    turtle.rt(144)