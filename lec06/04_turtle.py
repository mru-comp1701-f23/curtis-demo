import turtle
bob = turtle.Turtle() # my turtle is named Bob

bob.forward(100) # bob goes forward 100 units
bob.left(90) # bob turns left 90 degrees
bob.forward(200) # bob goes forward 200 units
bob.left(90) # bob turns left 90 degrees
bob.forward(100) # bob goes forward 100 units
bob.left(90) # bob turns left 90 degrees
bob.forward(200) # bob goes forward 200 units

units = int(input("How far should bob go now? "))
bob.forward(units)

# turtle.done keeps the window active
turtle.done()