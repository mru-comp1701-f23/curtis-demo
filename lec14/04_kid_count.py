count = 0
print("Welcome to kid count! Enter the count, -1 to stop")
# LCV initialization - priming read
kids = int(input("How many trick or treaters did you get? "))
num_inputs = 1
while kids != -1: # while sentinel isn't reached
    count += kids
    running_avg = count / num_inputs 
    print(f"The running average is {running_avg}")

    num_inputs += 1
    kids = int(input("How many kids? ")) # LCV update (internal read)

print(f"Wow, you had {count} trick or treaters!")