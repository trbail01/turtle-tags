import turtle
import random
from letters import draw_T, draw_A, draw_L

screen = turtle.Screen()
screen.setup(800, 500)
screen.title("Turtle Tags Demo")
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(6)
t.color("black")

draw_T(t, -220, 120, 100)
draw_A(t,  -60,  20, 100)
draw_L(t,  120, 120, 100)

# Confetti
t.penup()
for _ in range(45):
    t.goto(random.randint(-350, 350), random.randint(-200, 200))
    t.pendown()
    t.pencolor(random.random(), random.random(), random.random())
    t.dot(random.randint(6, 16))
    t.penup()

screen.exitonclick()
