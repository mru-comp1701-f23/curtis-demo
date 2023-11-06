def int_to_binary(number: int) -> str:
    """
    Convert the number into binary, returning the result
    as a string.
    """
    # initialize accumulator
    result = ""

    while number > 0:
        if number % 2 == 1:
            bit = "1"
        else:
            bit = "0"

        # accumulate bits
        result = bit + result # string concatenation
        number = number // 2

    return result

def main() -> None:
    num = int(input("Enter a number to convert to binary: "))
    print(f"{num} in binary is {int_to_binary(num)}")

main()