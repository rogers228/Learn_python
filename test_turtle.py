import turtle

paper = None
myTurtle = None

def myinit():
    global paper
    paper = turtle.Screen()
    paper.setup(500, 400)
    global myTurtle
    myTurtle = turtle.Turtle()

def test1():
    myTurtle.forward(150)
    myTurtle.left(90)
    myTurtle.forward(75)

    # Exit
    paper.exitonclick()

if __name__ == '__main__':
    myinit()
    test1()