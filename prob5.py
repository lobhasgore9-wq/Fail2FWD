def spiralOrder(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)  
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())  
        if matrix:
            result += matrix.pop()[::-1]  
        if matrix and matrix[0]:
            for row in reversed(matrix):
                result.append(row.pop(0))  
    return result
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
print("Enter the matrix row by row (space-separated):")
matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    if len(row) != n:
        print("Invalid row length. Please enter exactly", n, "numbers.")
        exit()
    matrix.append(row)
print("Spiral Order:", spiralOrder(matrix))


