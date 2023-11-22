def capitalize(names: list[str]) -> None:
    """
    Converts each name in the list to capital case.
    """
    # or the for loop version
    # for pos in range(len(names)):

    pos = 0
    while pos < len(names):
        names[pos] = names[pos].title()
        pos += 1
        # first_last = names[pos].split()
        # if len(first_last) < 2:
        #     names[pos] = first_last[0].capitalize()
        # else:
        #     names[pos] = (first_last[0].capitalize() + ' ' 
        #                   + first_last[1].capitalize())
    
def main() -> None:
    some_names = ["cali", "salvador", "someone else"]
    capitalize(some_names)
    print(some_names)
    
main()
