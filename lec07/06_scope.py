def say_hello(word: str) -> None:
    print(f"Hello, {word}")

def main() -> None:
    name = input("Enter your name: ")
    say_hello(name)

main()