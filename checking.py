from tkinter import CENTER
from turtle import *
from random import *

getscreen().bgcolor("#88B04B")
title("Bugs Race")
register_shape("ant.gif")
register_shape("cockroach.gif")
register_shape("beetle.gif")
register_shape("ladybug.gif")

speed(0)
color("#B2D2A4")
penup()
setposition(0,250)
pendown()
write("WELCOME TO THE RACE", align=CENTER, font=("Arial",20,"bold"))

speed(0)
color("white")
penup()
setposition(-600,-300)
pendown()
pensize(4)
for i in range(2):
    forward(1200)
    left(90)
    forward(600)
    left(90)
hideturtle()

penup()
setpos(-350,140)

for sp in range(15):
    speed(0)
    write(sp)
    right(90)
    forward(15)
    pendown()
    forward(250)
    penup()
    backward(265)
    left(90)
    forward(50)

#print(pos())

beetle = Turtle()
beetle.shape("beetle.gif")
beetle.speed(0)
beetle.penup()
beetle.setpos(-350,100)

ant = Turtle()
ant.shape("ant.gif")
ant.speed(0)
ant.penup()
ant.setpos(-350,40)

roach = Turtle()
roach.shape("cockroach.gif")
roach.speed(0)
roach.penup()
roach.setpos(-350,-20)

ladybug = Turtle()
ladybug.shape("ladybug.gif")
ladybug.speed(0)
ladybug.penup()
ladybug.setpos(-350,-80)


dice=[1,2,3,4,5,6]
for i in range(20):
    if beetle.pos() < (400,100):
        beetle_turn=input("Press Enter to roll the dice for Beetle ")
        dice_outcome=choice(dice)
        print("Beetle can move ", dice_outcome, " steps forward")
        beetle.fd(50*dice_outcome)
        if beetle.pos() >= (400,100):
            print("Beetle wins")
            break
        

    if ant.pos() <(400,40):
        ant_turn=input("Press Enter to roll the dice for Ant ")
        dice_outcome=choice(dice)
        print("Ant can move ", dice_outcome, " steps forward")
        ant.fd(50*dice_outcome)
        if ant.pos() >= (400,40):
            print("Ant wins")
            break
        

    if roach.pos() < (400,-20):
        roach_turn=input("Press Enter to roll the dice for Cockroach ")
        dice_outcome=choice(dice)
        print("Cockroach can move ", dice_outcome, " steps forward")
        roach.fd(50*dice_outcome)
        if roach.pos() >= (400,-20):
            print("Cockroack wins")
            break

    if ladybug.pos() < (400,-80):
        ladybug_turn=input("Press Enter to roll the dice for Ladybug ")
        dice_outcome=choice(dice)
        print("Ladybug can move ", dice_outcome, " steps forward")
        ladybug.fd(50*dice_outcome)
        if ladybug.pos() >= (400,-80):
            print("Ladybug wins")
            break
        

done()
