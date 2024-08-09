def get_matrix_dimensions(prompt):
    rows = int(input(f"{prompt} rows: "))
    cols = int(input(f"{prompt} columns: "))
    return rows, cols

def get_matrix_values(rows, cols, prompt):
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = int(input(f"{prompt} row {i+1}, column {j+1}: "))
    return matrix

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions to be added")
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def print_matrix(matrix):
    max_width = max(len(str(x)) for row in matrix for x in row)
    for row in matrix:
        print(" ".join(f"{x:>{max_width}}" for x in row))

def main():
    rows1, cols1 = get_matrix_dimensions("Enter number of rows and columns for matrix 1:")
    matrix1 = get_matrix_values(rows1, cols1, "Enter value for matrix 1")

    rows2, cols2 = get_matrix_dimensions("Enter number of rows and columns for matrix 2:")
    matrix2 = get_matrix_values(rows2, cols2, "Enter value for matrix 2")

    try:
        result = add_matrices(matrix1, matrix2)
        print("Result:")
        print_matrix(result)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()