import turtle

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

def draw_E(turtle_obj, x, y, size=100):
    turtle_obj.penup()
    turtle_obj.goto(x, y)
    turtle_obj.setheading(0)
    turtle_obj.pendown()
    for i in range(3):
        turtle_obj.forward(size * 0.6)
        turtle_obj.backward(size * 0.6)
        if i < 2:
            turtle_obj.right(90)
            turtle_obj.forward(size / 2)
            turtle_obj.left(90)
