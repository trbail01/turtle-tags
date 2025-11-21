import turtle
import random

# --- setup ---
screen = turtle.Screen()
screen.setup(800, 500)
screen.title("Turtle Tags: Code Your Initials in Python")
screen.bgcolor("white")  # Easy background for projection

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(6)
t.color("black")

# Quick commands you can try:
# t.forward(100)
# t.backward(50)
# t.left(90)
# t.right(90)
# t.penup()
# t.pendown()
# t.goto(x, y)
# t.color("red")
# t.pensize(8)

# --- example letter helpers ---
def draw_T(turtle_obj, x, y, size=100):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.setheading(0)
    turtle_obj.pendown()
    turtle_obj.forward(size)
    turtle_obj.backward(size / 2)
    turtle_obj.right(90)
    turtle_obj.forward(size * 1.2)

def draw_A(turtle_obj, x, y, size=100):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.setheading(60)
    turtle_obj.pendown()
    turtle_obj.forward(size)
    turtle_obj.right(120)
    turtle_obj.forward(size)
    # crossbar
    turtle_obj.backward(size / 2)
    turtle_obj.right(120)
    turtle_obj.forward(size / 2)

def draw_L(turtle_obj, x, y, size=100):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.setheading(270)
    turtle_obj.pendown()
    turtle_obj.forward(size)
    turtle_obj.left(90)
    turtle_obj.forward(size * 0.6)

# --- demo initials (you can change these to match your initials) ---
draw_T(t, -220, 120, 100)
draw_A(t,  -60,  20, 100)
draw_L(t,  120, 120, 100)

# --- confetti burst (fun finisher) ---
t.penup()
for _ in range(45):
    t.goto(random.randint(-350, 350), random.randint(-200, 200))
    t.pendown()
    t.pencolor(random.random(), random.random(), random.random())
    t.dot(random.randint(6, 16))
    t.penup()

# Click to close window (useful between rotations)
screen.exitonclick()
