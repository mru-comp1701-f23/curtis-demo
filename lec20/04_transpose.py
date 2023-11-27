def transpose(matrix: list[list]) -> list[list]:
    """
    Calculates and returns the transpose of a matrix
    """
    t = []
    for r in range(len(matrix)):
        row = []
        for c in range(len(matrix[r])):
            row.append(matrix[c][r])
        t.append(row)
    
    return t

def main() -> None:
    grid = [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]]
    t = transpose(grid)
    for row in t:
        print(row)

main()
