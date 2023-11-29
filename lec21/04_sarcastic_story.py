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
    in_file = open("data/story.txt", "r") # read mode
    story = in_file.read()
    in_file.close()

    sarcastic_story = to_sarcastic(story)

    out_file = open("data/sarcastic_story.txt", "w") # write mode
    out_file.write(sarcastic_story)
    out_file.close()

main()