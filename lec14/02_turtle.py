import turtle

def square(turtie: turtle.Turtle, side: float) -> None:
    """Draws a square with side length side"""
    n = 0 # LCV initialization
    while n < 4: # Loop condition
        turtie.forward(side)
        turtie.left(90) 
        n += 1 # LCV update

def main() -> None:
    bob = turtle.Turtle() # my turtle is named Bob
    degrees = 0 # LCV initialization
    increment = 60
    while degrees < 360: # Loop condition
        square(bob, 100)
        bob.left(increment)
        degrees += increment # LCV update

    # turtle.done keeps the window active
    turtle.done()

main()
