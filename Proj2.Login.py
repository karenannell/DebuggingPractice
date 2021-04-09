#Project 2: Login System
#Create a login system that automatically generates a password for each user.

import turtle #wrong module

username1 = input("Enter your first name: ") #wrong placement
username2 = input("Enter your last name: ") #didnt specify first/last names
password_correct = username2+username1[0] #missing "username1"
password_attempt = input("Password: ")

def draw_smiley(): #don't need parameter
    t = turtle.Turtle()    
    t.penup()
    t.goto(-75,150)
    t.pendown()
    t.circle(10)

    t.penup()
    t.goto(75,150)
    t.pendown()
    t.circle(10)

    t.penup()
    t.goto(0,0)
    t.pendown()
    t.circle(100,90)

    t.penup()           
    t.setheading(180) 
    t.goto(0,0)
    t.pendown()
    t.circle(-100,90)

def draw_frown():
    turtle.forward(100) #missing frown code
    
if password_correct == password_attempt:
    draw_smiley() #missing ()
    
else:
    draw_frown() #missing ()

