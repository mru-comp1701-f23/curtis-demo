import turtle

def square(turtie: turtle.Turtle, side: float) -> None:
    """Draws a square with side length side"""
    turtie.forward(side)
    turtie.left(90) 
    turtie.forward(side) 
    turtie.left(90) 
    turtie.forward(side)
    turtie.left(90)
    turtie.forward(side)
    turtie.left(90)
    

def main() -> None:
    bob = turtle.Turtle() # my turtle is named Bob

    # repeatedly draw a square in increments of 60 degrees
    # until a circle is completed
    # Statements? LCV? Initialization? Update?

    # turtle.done keeps the window active
    turtle.done()

main()
