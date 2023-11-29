def read_valid_courses(filename: str) -> list[str]:
    """
    Reads the list of valid courses
    """
    f = open(filename, "r")
    courses = []
    for line in f:
        courses.append(line.strip())
    
    f.close()
    return courses

def get_comp_courses() -> list[str]:
    """
    Repeatedly prompt the user to enter a course.
    If it's a valid course, adds to the list.
    """
    valid = read_valid_courses("data/comp_courses.txt")
    prompt = "Enter a course, or press Enter to finish: "
    course = input(prompt)

    user_list = []
    while course != "":
        course = course.upper()
        if course in valid:
            user_list.append(course)
        else:
            print("Sorry, that's not a valid course")
        course = input(prompt)

    return user_list

def main() -> None:
    # print(read_valid_courses("data/comp_courses.txt"))
    user_courses = get_comp_courses()
    print(user_courses)

main()