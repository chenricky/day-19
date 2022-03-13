from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
colours = ["red", "blue", "green", "yellow"]
tim.color("black")
tim.shape("circle")


def move_forward():
    # tim.pencolor("black")
    tim.color(random.choice(colours))
    tim.forward(10)
    tim.write("F")

def move_backward():
    # tim.pencolor("black")
    tim.color(random.choice(colours))
    tim.backward(10)
    tim.write("B")

def move_counter_clockwise():
    # tim.pencolor("black")
    tim.color(random.choice(colours))
    tim.right(10)
    tim.forward(10)
    tim.write("R")

def move_clockwise():
    # tim.pencolor("black")
    tim.color(random.choice(colours))
    tim.left(10)
    tim.forward(10)
    tim.write("L")

def _move_turtle_home():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=_move_turtle_home)
screen.exitonclick()