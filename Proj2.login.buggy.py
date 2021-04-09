#Project 2: Login System
#Create a login system that automatically generates a password for each user.
#AnnellK
#PageA

import turtle

username1 = input("Enter your first name: ")
username2 = input("Enter your last name: ")
password_correct = username2+username1[0]
password_attempt = input("Password: ")


def draw_smiley():
    t = turtle.Turtle()    
    t.penup()
    t.goto(-75,150)
    t.pendown()
    t.circle(10)     #eye one

    t.penup()
    t.goto(75,150)
    t.pendown()
    t.circle(10)     #eye two

    t.penup()
    t.goto(0,0)
    t.pendown()
    t.circle(100,90)   #right smile

    t.penup()           
    t.setheading(180) # <-- look West
    t.goto(0,0)
    t.pendown()
    t.circle(-100,90)

def draw_frown():
    turtle.forward(100)
    #Draw a sad face
    
if password_correct == password_attempt:
    draw_smiley()
    
else:
    draw_frown()

#There are bugs in this code! I've found: 8
