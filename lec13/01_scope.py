import random

def some_fun() -> None:
    result = 10

def main() -> None:
    # print(result) # not in the main scope
    if random.randint(0, 1) == 0:
        result = "zero"
    else:
        result = "one"
    print(result) # in scope 

main()