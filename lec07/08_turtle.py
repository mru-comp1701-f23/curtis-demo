import turtle

def square(turtie: turtle.Turtle, side: float) -> None:    
    turtie.forward(side)
    turtie.left(90) 
    turtie.forward(side) 
    turtie.left(90) 
    turtie.forward(side)
    turtie.left(90)
    turtie.forward(side)

def move(turtie: turtle.Turtle, dir: float, dist: float) -> None:
    turtie.right(dir)
    turtle.penup()
    turtie.forward(dist)
    turtle.pendown()

def main() -> None:
    bob = turtle.Turtle() # my turtle is named Bob
    square(bob, 100)
    move(bob, 30, 10)
    square(bob, 150)
    move(bob, 30, 10)
    square(bob, 200)
    # turtle.done keeps the window active
    turtle.done()

main()
