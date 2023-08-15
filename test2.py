import turtle

print("wellcom")
feeling = input("How do you feel=")
if feeling == "sad" :
    smiles = turtle.Turtle()

    smiles.penup()
    smiles.goto(-105,155)
    smiles.pendown()
    smiles.goto(-45,115)

    smiles.penup()
    smiles.goto(-75,75)
    smiles.pendown()
    smiles.circle(10)

    smiles.penup()
    smiles.goto(105,155)
    smiles.pendown()
    smiles.goto(45,115)

    smiles.penup()
    smiles.goto(75,75)
    smiles.pendown()
    smiles.circle(10)

    smiles.penup()
    smiles.goto(0,25)
    smiles.pendown()
    smiles.circle(-100,80)

    smiles.penup()
    smiles.setheading(180)
    smiles.goto(0,25)
    smiles.pendown()
    smiles.circle(100,80)

    print()

if feeling == "happy" :
    print()

        
    # Python program to draw smile
    # face emoji using turtle

    # turtle object
    pen = turtle.Turtle()
    
    # function for creation of eye
    def eye(col, rad):
        pen.down()
        pen.fillcolor(col)
        pen.begin_fill()
        pen.circle(rad)
        pen.end_fill()
        pen.up()
    
    
    # draw face
    pen.fillcolor('yellow')
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()
    pen.up()
    
    # draw eyes
    pen.goto(-40, 120)
    eye('white', 15)
    pen.goto(-37, 125)
    eye('black', 5)
    pen.goto(40, 120)
    eye('white', 15)
    pen.goto(40, 125)
    eye('black', 5)
    
    # draw nose
    pen.goto(0, 75)
    eye('black', 8)
    
    # draw mouth
    pen.goto(-40, 85)
    pen.down()
    pen.right(90)
    pen.circle(40, 180)
    pen.up()
    
    # draw tongue
    pen.goto(-10, 45)
    pen.down()
    pen.right(180)
    pen.fillcolor('red')
    pen.begin_fill()
    pen.circle(10, 180)
    pen.end_fill()
    pen.hideturtle()
else:
    print()
 
    t = turtle.Turtle()  
    t.forward(150) # moving the turtle Forward by 150 units  
    t.left(90) #Turning the turtle by 90 degrees  
    t.forward(150)  
    t.left(90)  
    t.forward(150)  
    t.left(90)  
    t.forward(150)  
    t.left(90)  
