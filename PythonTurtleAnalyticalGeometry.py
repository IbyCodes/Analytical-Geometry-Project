
# All work done by Mohammad Ibrahim Khan


import turtle # both modules needed
import math

#SETTING UP TURTLE

WIDTHWINDOW = 800
HEIGHTWINDOW = 600

MIDDLEX = WIDTHWINDOW/2
MIDDLEY = HEIGHTWINDOW/2

pen = turtle.Turtle()
screen = turtle.Screen()
screen.setup(WIDTHWINDOW,HEIGHTWINDOW, 0, 0)
screen.setworldcoordinates(0,0, WIDTHWINDOW, HEIGHTWINDOW)
pen.hideturtle()

FONTSIZE = 25
FONT = ("Arial", FONTSIZE, "normal")


# DRAWING THE AXIS (in black)
pen.up()
pen.goto(MIDDLEX-HEIGHTWINDOW, MIDDLEY)
pen.down()
pen.goto(MIDDLEX+HEIGHTWINDOW, MIDDLEY)
pen.up()
pen.goto(MIDDLEX, MIDDLEY-MIDDLEY)
pen.down()
pen.goto(MIDDLEX, MIDDLEY+MIDDLEY)
pen.up()


# PROMPTING THE USER FOR ALL OF THE INPUTS NEEDED FOR THE PROGRAM (7 IN TOTAL)

print("You will be asked for some values of a circle you would like to draw.")
print("You will then be asked for some inputs for the start and end of a line.")
print("The amount of intersections between the circle and the line coordinates you input will be calculated and shown to you.")

xc = int(input("What is the x coordinate of the centre of your circle?: "))
yc = int(input("What is the y coordinate of the centre of your circle?: "))
r = float(input("What is the radius of your circle?: "))


print("Thank you. Now some information about the line you would like to draw.")

x1 = int(input("What is the starting x coordinate of your line?: "))
y1 = int(input("What is the starting y coordinate of your line?: "))
x2 = int(input("What is the ending x coordinate of your line?: "))
y2 = int(input("What is the ending y coordinate of your line?: "))
print("Drawing...")


# determining a, b, and c

a = (x2-x1)**2+(y2-y1)**2
b = 2*((x1-xc)*(x2-x1)+(y1-yc)*(y2-y1))
c = (x1-xc)**2+(y1-yc)**2-(r**2)



def calcAlpha(): # this function will calculate alpha values if called upon

    global intersections
    alpha1 = ((-b)+math.sqrt(b**2-4*(a*c)))/(2*a)
    alpha2 = ((-b)-math.sqrt(b**2-4*(a*c)))/(2*a)

    if alpha1>1:
        intersections = intersections-1

    if alpha2>1:
        intersections = intersections-1

    if alpha1<0:
        intersections = intersections-1

    if alpha2<0:
        intersections = intersections-1



#determining the number of intersections

intersections = 0


if (b**2)-4*(a*c) < 0:
    intersections = 0
    # DONT CALCULATE ALPHA if discriminant less than zero, so we won't call calcAlpha

elif (b**2)-4*(a*c) == 0:
    intersections = 1
    calcAlpha()

elif (b**2)-4*(a*c) > 0:
    intersections = 2
    calcAlpha()

else:
    print("Invalid input.")



# DRAWING THE LINE

pen.color("blue") # changing the colour to blue when drawing the line
pen.goto(x1,y1)
pen.down() # NOW it will start drawing the line
pen.goto(x2,y2)  # note that we haven't lifted the pointer yet, so it'll draw to this point
pen.up()

# DRAWING THE CIRCLE
pen.color("red") # changing the colour to red when drawing the circle
pen.goto(xc,yc-r)
pen.down()
pen.circle(r)
pen.up()

# Writing on the screen the amount of intersections
pen.color("Dark Green")
pen.goto(MIDDLEX-150,MIDDLEY)
if intersections == 0:
    pen.write("You have 0 intersections!", font=FONT)
    print("You have 0 intersections!")
elif intersections == 1:
    pen.write("You have 1 intersection!", font =FONT)
    print("You have 1 intersection!")
elif intersections == 2:
    pen.write("You have 2 intersections!",font =FONT)
    print("You have 2 intersections!")
print ("Done drawing!")

turtle.done() # NEED to keep the window open after the process is finished in the turtle window

