def lines_without_first(filename: str) -> list[str]:
    fobj = open(filename, "r")
    first = fobj.readline() # read the first line
    rest = []
    for line in fobj:
        rest.append(line)
    fobj.close()
    return rest

def main() -> None:
    all_but_first = lines_without_first("lec21/01_read_file.py")
    print(all_but_first)

main()