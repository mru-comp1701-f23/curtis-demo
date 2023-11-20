def list_of_squares(n: int) -> list[int]:
    """
    Builds a list containing squares of numbers from 1 to n.
    """
    squares = []
    for num in range(1, n + 1):
        squares.append(num ** 2)
    return squares

def main() -> None:
    squares_to_12 = list_of_squares(12)
    print(squares_to_12)

main()