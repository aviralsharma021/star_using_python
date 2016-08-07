import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("fuck off")

avi = turtle.Turtle()
avi.shape("turtle")
avi.color("blue")
avi.speed(2)

def draww_star(avi):
    avi.left(36)
    for i in range(5):
        avi.forward(100)
        avi.left(144)

for i in range(5):
    draww_star(avi)
    avi.penup()
    avi.forward(150)
    avi.right(108)
    avi.pendown()


wn.mainloop()
