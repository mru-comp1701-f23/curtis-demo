def average(num1: float, num2: float) -> None:
    avg = (num1 + num2) / 2
    print(f"The average of {num1} and {num2} is {avg}")

def main() -> None:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    # names don't matter, but order does!
    average(num2, num1)
    average(2 * num1, 3 * num2)

main()