def to_pig(word: str) -> str:
    """
    Converts a word to pig latin by moving
    the first letter to the end and adding "ay"
    """
    return word[1:] + word[0] + "ay"

def main() -> None:
    word = input("What word would you like to convert? ")
    pig = to_pig(word)
    print(f"{word} in pig latin is {pig}!")

main()