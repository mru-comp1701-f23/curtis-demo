def cookies_per(num_cookies: int, friends: int) -> int:
    """
    Divides the cookies evenly amongst friends,
    Returns number of cookies per person.
    """
    num_cookies_per_friend = 0
    # check for zero must be first
    if friends > 0 and num_cookies // friends > 0:
        num_cookies_per_friend = num_cookies // friends
    
    return num_cookies_per_friend

def main() -> None:
    # test values
    print(f"4 friends, 3 cookies: {cookies_per(3, 4)}")
    print(f"0 friends, 3 cookies: {cookies_per(3, 0)}")
    print(f"5 friends, 22 cookies: {cookies_per(22, 5)}")
    

main()
