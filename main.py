from turtle import Turtle,Screen

t1=Turtle()
screen=Screen()

def move_farwards():
    t1.forward(10)

def move_backwards():
    t1.backward(10)


screen.listen()
screen.onkey(move_farwards,key='w')
screen.onkey(move_backwards,key='s')

screen.exitonclick()