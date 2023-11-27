def to_int_list(num_str: str) -> list[int]:
    """
    Converts a string of comma-separate numbers into a list of ints.
    """
    int_list = num_str.split(",")
    for i in range(len(int_list)):
        int_list[i] = int(int_list[i])
    # can't do this, need write access
    # for num in int_list: 
    #     num = int(num)

        
    return int_list

def main() -> None:
    test_values = "1,2,3,4,5,6"
    int_list = to_int_list(test_values)
    for num in int_list:
        print(num, type(num))

main()