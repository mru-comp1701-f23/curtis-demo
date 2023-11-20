def to_sarcastic(original: str) -> str:
    """
    Converts a string to sarcastic
    """
    length = len(original)
    sarcastic = ""
    for c in range(length):
        if c % 2 == 0:
            sarcastic += original[c].upper()
        else:
            sarcastic += original[c]
    
    return sarcastic

def main() -> None:
    text = input("What do you want to make sarcastic? ")
    print(to_sarcastic(text))

main()