from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
tim.shape("circle")

def move_forward():
    tim.pencolor("black")
    tim.forward(10)
    tim.write("F")

def move_backward():
    tim.pencolor("black")
    tim.backward(10)
    tim.write("B")

def move_counter_clockwise():
    tim.pencolor("black")
    tim.right(10)
    tim.forward(10)
    tim.write("R")

def move_clockwise():
    tim.pencolor("black")
    tim.left(10)
    tim.forward(10)
    tim.write("L")

def _move_turtle_home():
    tim.pencolor("white")
    tim.home()



screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=_move_turtle_home)
screen.exitonclick()