import turtle
import random
import math

#Set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.bgpic("giphy.png")
wn.tracer(3)


#Draw border
mypen = turtle.Turtle()
mypen.color("white")
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for i in range(4):
    mypen.forward(600)
    mypen.left(90)

mypen.hideturtle()


#Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

#Create score
score = 0

#create multiple goal
maxGoals = 6
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color('red')
    goals[count].shape('circle')
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300,300),random.randint(-300,300))


#Set speed variable
speed = 1

#Define functions
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def decreasespeed():
    global speed
    speed -= 1

def isCollision(t1,t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False

#Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")
turtle.onkey(decreasespeed,"Down")


while True:
    player.forward(speed)

    #Boundary checking
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(100)

    if player.ycor() > 300 or player.ycor() < -300:
        player.right(100)

    #move the goal
    for count in range(maxGoals):
        goals[count].forward(0.5)

    # Boundary checking(goal)
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(100)

        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(100)

     # collision checking
        if isCollision(player, goals[count]):
            goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goals[count].right(random.randint(0, 360))
            score += 1
            #draw score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring = "Score: %s"%score
            mypen.write(scorestring, False, align="left", font=("Arial",14,"normal"))
