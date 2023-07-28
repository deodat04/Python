import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(10)
col =['yellow','blue','white','green','red','black','brown','gold','violet']
c=0
#users
for i in range(50):
    t.forward(i*10)
    t.right(144)
    t.color(col[c])
    if c==8:
        c=0
    else:
        c+=1
