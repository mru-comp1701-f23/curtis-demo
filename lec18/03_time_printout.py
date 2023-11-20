def print_all_times() -> None:
    """
    Prints all the times from 0 to 24 hrs in 1 s increments.
    """
    for hours in range(24):
        for mins in range(60):
            for secs in range(60):
                print(f"{hours}:{mins}:{secs}")
    

def print_all_times_while() -> None:
    """
    Prints all the times from 0 to 24 hrs in 1 s increments.
    """
    hours = 0
    while hours < 24:
        mins = 0
        while mins < 60:
            secs = 0
            while secs < 60:
                print(f"{hours}:{mins}:{secs}")
                secs += 1
            mins += 1
        hours += 1


def main() -> None:
    # print_all_times()
    print_all_times_while()

main()