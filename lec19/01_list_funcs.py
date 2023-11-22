def modify_me(a: list) -> None:
    a[0] = 0

def dont_modify(a: list) -> None:
    a = [1, 2, 3]

def main() -> None:
    b = [1, 2, 3]
    print(b)
    modify_me(b)
    print(b)
    dont_modify(b)
    print(b)

main()