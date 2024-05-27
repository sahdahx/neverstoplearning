import turtle

# Creating a turtle object(pen) 
pen = turtle.Turtle()


# Defining a method to draw curve
def curve():
    for i in range(200):
        # Defining step by step curve motion
        pen.right(1)
        pen.forward(1)

    # Defining method to draw a full heart


def heart():
    # Set the fill color to red
    pen.fillcolor('red')

    # Start filling the color 
    pen.begin_fill()

    # Draw the left line 
    pen.left(140)
    pen.forward(113)

    # Draw the left curve 
    curve()
    pen.left(120)

    # Draw the right curve 
    curve()

    # Draw the right line 
    pen.forward(112)

    # Ending the filling of the color 
    pen.end_fill()


# Defining method to write text
def txt():
    # Move turtle to air
    pen.up()

    # Move turtle to a given position 
    pen.setpos(-68, 95)

    # Move the turtle to the ground 
    pen.down()

    # Set the text color to lightgreen 
    pen.color('blue')

    # Write the specified text in  
    # specified font style and size 
    pen.write("Sahda", font=(
        "Verdana", 12, "bold"))


# Draw a heart 
heart()

# Write text 
txt()

# To hide turtle 
win = turtle.Screen()
win.bgcolor("white")

tess = turtle.Turtle()

tess.speed(0)
tess.color("red")             
tess.pensize(5)                 
offSet=30

def doNextEvent(x,y):

    global offSet
    global win
    tess.forward(20)
    tess.left(1+offSet)
    offSet=offSet-2
    if(offSet<1):
        win.exitonclick()


win.onclick(doNextEvent)
win.listen()
win.mainloop()