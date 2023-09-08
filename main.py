from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
turtle_race=False
user=screen.textinput(title="Make Your Bet",prompt="Which turtle will win the Race? Enter the color")

colors=["purple","yellow","red","blue","orange"]
y_position=[-80,-40,0,40,80]
all_turtle=[]

for i in range(0,5):
    race=Turtle(shape="turtle")
    race.color(colors[i])
    race.penup()
    race.goto(x=-230,y=y_position[i])
    all_turtle.append(race)

if user in colors:
    turtle_race=True

while turtle_race:

    for each_turtle in  all_turtle:
        if each_turtle.xcor() >= 230:
            winner=each_turtle.pencolor()
            turtle_race=False
            if user == each_turtle.pencolor() :
                print(f'You won the race ,Winner is {winner} color Turtle')
            else:
                print(f'You lost the Winner is {winner} color Turtle')
 
        move=random.randint(1,10)
        each_turtle.forward(move)


screen.exitonclick()