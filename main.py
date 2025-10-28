import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(width=800, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# Y positions for the 6 turtles (one entry per color)
y_positions = [-90, -54, -18, 18, 54, 90]
# X start positions for the turtles (all start at the same x, but kept as a list for flexibility)
x_positions = [-370] * len(colors)
# All turtles
all_turtles = []

# Validate that the positions arrays match the number of turtles
if len(y_positions) != len(colors):
    raise ValueError(f"y_positions must have the same length as colors ({len(colors)}), got {len(y_positions)}")
if len(x_positions) != len(colors):
    raise ValueError(f"x_positions must have the same length as colors ({len(colors)}), got {len(x_positions)}")

for turtle_index in range(len(colors)):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=x_positions[turtle_index], y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 380:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You win! {winning_color} wins!')
            else:
                print(f'You lose! {winning_color} wins!')

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()