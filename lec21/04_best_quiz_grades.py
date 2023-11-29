def read_quizzes(filename: str) -> list[list[float]]:
    """
    Reads a multi-column spreadsheet of quiz grades.
    """
    f = open(filename, "r")
    header = f.readline() # ignore the header line
    quizzes = []
    for line in f:
        # something like "10.2,4.5"
        grades = line.split(",") # yields ["10.2", "4.5\n"]
        for i in range(len(grades)):
            try:
                grades[i] = float(grades[i]) # [10.2, 4.5]
            except ValueError:
                print("Unexpected value", grades[i])
                grades[i] = 0 # assume that bad value = 0

        quizzes.append(grades)
    
    f.close()
    return quizzes

def get_best_quiz(grades: list[list[float]]) -> list[float]:
    """
    Returns the best quiz grade for each student.
    """
    best = []
    for row in grades:
        best.append(max(row))
    
    return best

def write_best_quiz(filename: str, grades: list[float]) -> None:
    """
    Writes the best quiz grade to a new file specified
    by filename.
    """
    f = open(filename, "w")
    f.write("Best quiz grade\n")
    for grade in grades:
        # grade is now a single float
        f.write(f"{grade:.1f}\n")
    f.close()

def main() -> None:
    all_quizzes = read_quizzes("data/quiz_grades.csv")
    best_quiz = get_best_quiz(all_quizzes)
    write_best_quiz("data/best_quiz.csv", best_quiz)

main()