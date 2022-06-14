from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=600)

is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which color do you bet on?")

colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink"]
all_turtles = []

for turtle_index in range(len(colors)):
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-350, y=-150 + turtle_index * 50)
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(1, 15))
        if turtle.xcor() > 370:
            winning_turtle = turtle.pencolor()
            is_race_on = False
            if winning_turtle == user_bet:
                print("You won!" + " " + winning_turtle + " " + "is the color of the winning turtle.")
            else:
                print("You lost!" + " " + winning_turtle + " " + "is the color of the winning turtle.")

screen.mainloop()