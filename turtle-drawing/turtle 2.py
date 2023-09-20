
import turtle
colors = ['red', 'red' ,'red', 'red' , 'purple','purple', 'purple' , 'purple' ,'blue' , 'blue', 'green' , 'green', 'red' ,'orange',  'yellow' , 'black', 'black', 'black', 'black' , 'green', 'green', 'blue', 'orange']
#changing colours for turtle
t1 = turtle.Pen()
turtle.bgcolor('red')
#putting background colour to red
for x in range(360):
    t1.pencolor(colors[x%22])
    #changing pen colour according to colours in the list
    t1.width(x//1800 + 12)
    #change the width of turtle
    t1.forward(x)
    #forwarding turtle
    t1.left(89)
    #turning tutrtle in given degree
loadWindow = turtle.Screen()
#loading screen
turtle.speed(290)
#changes the speed of turtle
 
for i in range(100):
    turtle.circle(8*i)
    turtle.circle(-5*i)
    turtle.left(i)
    #making circles


t2 = turtle.Pen()
turtle.bgcolor('red')
# turtle background colour change to red colour
for x in range(360):
    t2.pencolor(colors[x%22])
    #change turtle colour
    t2.width(x//1800 + 10)
    #change turtle width
    t2.forward(x)
    #make turtle go forward
    t2.left(89)
    #turn turle 
loadWindow = turtle.Screen()
#load turtle screen
turtle.speed(120)
#turtle speed checking
 
for i in range(100):
    turtle.circle(8*i)
    turtle.circle(-7*i)
    turtle.left(i)
    #make turtle circle designs
   
 
turtle.exitonclick()
# make turtle screen exit when click

