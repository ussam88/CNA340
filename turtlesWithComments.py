import turtle										##import the turtle module
import random										##import the random module

wn = turtle.Screen()								##create a screen & label the screen
wn.bgcolor('lightblue')
wn.title("Turtle Race")

andyTotalDistance=0
lanceTotalDistance=0

lance = turtle.Turtle()								##(create two turtles...
andy = turtle.Turtle()								## named : lance, and Andy	......)
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()
lance.up()
andy.goto(-100, 20)										##(move the turtles to their starting points
lance.goto(-100, -20)									## to get race is about to start)

start = turtle.Turtle()  # OPTIONAL						##create a third turtle object called start that will be used to display the winner of the game
start.hideturtle()										##hide the third turtle object until the game is over for aesthetic purposes

for i in range(150):									##iterate through the loop to run the forward method on both turtles 150 times

    andyDistance = random.randrange(1, 5)				##Indent to begin the loop & make a random distance for andy to move & move andy forward and use the andyDistance variable to determine the amount to move forward by.
    lanceDistance = random.randrange(1, 5)				##make a random distance for lance to move
    andy.forward(andyDistance)							##move andy forward and use the andyDistance variable to determine the amount to move forward by.
    lance.forward(lanceDistance)
    andyTotalDistance = andyTotalDistance + andyDistance
    lanceTotalDistance = lanceTotalDistance + lanceDistance


for eachInt in range(150):								##De-indent to end the loop						##(this section is to determine the winner of the game and be used to print who the winner is. It calculates total distance for lance and for andy.
    if andyTotalDistance > lanceTotalDistance:			##Indent to begin the loop 						##use a cascading set of conditions to determine the winner.
        start.write("Andy is the winner!", move=False, align="center", font=("Arial", 25, "normal"))
    elif lanceTotalDistance > andyTotalDistance:														##use a cascading set of conditions to determine the winner.##...
        start.write("Lance is the winner!", move=False, align="center", font=("Arial", 25, "normal"))

wn.exitonclick()										##De-indent to end the loop & exit on click of the window