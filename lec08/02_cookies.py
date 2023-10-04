def eat_cookie(cookies: int) -> int:
    cookies = cookies - 1
    return cookies

def main() -> None:
    og_cookies = 3
    print(og_cookies, eat_cookie(og_cookies))

main()