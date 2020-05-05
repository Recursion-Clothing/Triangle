# Check out Recursion Clothing @ recursion.uk

import turtle

triangle_size = 600
triangle_iterations = 3


class Triangle:
    def __init__(self, plane, size, max_depth):
        max_depth -= 1
        plane.forward(size)
        plane.left(120)
        plane.forward(size)
        plane.left(120)
        plane.forward(size)
        plane.left(120)
        plane.forward(size / 2)
        plane.left(120)
        plane.forward(size / 2)
        plane.right(120)
        if max_depth > 0:
            self.__init__(plane, size / 2, max_depth)
        plane.forward(size / 2)
        plane.right(120)
        if max_depth > 0:
            self.__init__(plane, size / 2, max_depth)
        plane.forward(size / 2)
        plane.right(60)
        plane.forward(size / 2)
        plane.left(180)
        if max_depth > 0:
            self.__init__(plane, size / 2, max_depth)


t = turtle.Turtle()
t.speed(10)
t.pensize(2)
t.penup()
t.setx(-(triangle_size/2))
t.sety(-(triangle_size/2))
t.pendown()
t.speed(100)
triangle = Triangle(t, triangle_size, triangle_iterations)
t.hideturtle()
turtle.Screen().mainloop()

