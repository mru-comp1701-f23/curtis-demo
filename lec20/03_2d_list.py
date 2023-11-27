def to_int_list(num_str: str) -> list[int]:
    """
    Converts a string of comma-separate numbers into a list of ints.
    """
    int_list = num_str.split(",")
    for i in range(len(int_list)):
        int_list[i] = int(int_list[i])
    
    return int_list

def create_2d_list() -> list[list[int]]:
    """
    Repeatedly prompts for a row to add to list.
    """
    grid = []
    prompt = "Enter a row of comma-separated numbers (Enter to stop): "
    row = input(prompt)
    while row != "":
        grid.append(to_int_list(row))
        row = input(prompt)
    
    return grid

def main() -> None:
    grid = create_2d_list()
    # print(grid)
    for row in grid:
        print(row)

main() 