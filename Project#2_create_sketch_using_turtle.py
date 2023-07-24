from sketchpy import canvas
import turtle
obj=canvas.sketch_from_image("C:\\Users\\HP\\pradip1.jpg")
t=turtle.Turtle()
t.penup()
t.goto(-60,-290)
t.pendown()
t.pencolor("#ff6600")
t.write("Happy Birthday", align="center", font=("arial",50,"bold"))
obj.draw()
t.hideturtle()
turtle.done()