# You are given a table with rows and columns. Each cell is colored with white or black. Considering the shapes created by black cells, what is the maximum border of these shapes? Border of a shape means the maximum number of consecutive black cells in any row or column without any white cell in between.
#
# A shape is a set of connected cells. Two cells are connected if they share an edge. Note that no shape has a hole in it.
#
# Input format
#
# The first line contains denoting the number of test cases.
# The first line of each test case contains integers denoting the number of rows and columns of the matrix. Here, '#' represents a black cell and '.' represents a white cell.
# Each of the next lines contains integers.
# Output format
#
# Print the maximum border of the shapes.

def max_border(rows, cols, matrix):
    max_border = 0

    # Function to explore the shape starting from a given cell
    def explore_shape(row, col):
        nonlocal max_border
        border = 1
        # Explore up
        for r in range(row - 1, -1, -1):
            if matrix[r][col] == '#':
                border += 1
            else:
                break
        # Explore down
        for r in range(row + 1, rows):
            if matrix[r][col] == '#':
                border += 1
            else:
                break
        # Explore left
        for c in range(col - 1, -1, -1):
            if matrix[row][c] == '#':
                border += 1
            else:
                break
        # Explore right
        for c in range(col + 1, cols):
            if matrix[row][c] == '#':
                border += 1
            else:
                break

        # Update max_border if needed
        max_border = max(max_border, border)

    # Iterate through the matrix to find black cells and explore their shapes
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '#':
                explore_shape(i, j)

    return max_border


# Input
num_cases = int(input())
for _ in range(num_cases):
    rows, cols = map(int, input().split())
    matrix = [input().strip() for _ in range(rows)]
    result = max_border(rows, cols, matrix)
    print(result)
