from turtle import Turtle,Screen

t1=Turtle()
screen=Screen()

def move_farwards():
    t1.forward(10)

def move_backwards():
    t1.backward(10)

def move_clockwise():
    t1.right(10)
def move_anti_clockwise():
    t1.left(10)
def clear_screen():
    t1.clear()
    t1.reset()


screen.listen()
screen.onkey(move_farwards,key='w')
screen.onkey(move_backwards,key='s')
screen.onkey(move_clockwise,key='d')
screen.onkey(move_anti_clockwise,key='a')
screen.onkey(clear_screen,key='c')

screen.exitonclick()