# Function to check if placing a queen is safe
def is_safe(board, row, col, N):
    # Check if there's another queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper left diagonal (moving upwards)
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the upper right diagonal (moving upwards)
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True  # If no queens are attacking, it's safe

# Function to solve the N-Queens problem
def solve_nqueens(board, row, N):
    # If all queens are placed (reached the end), we're done
    if row >= N:
        return True

    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen
            board[row][col] = 1

            # Recur to place the rest of the queens
            if solve_nqueens(board, row + 1, N):
                return True

            # If placing the queen doesn't lead to a solution, backtrack (remove the queen)
            board[row][col] = 0

    return False  # If no place is safe in this row, return False

# Function to print the board with queens
def print_solution(board, N):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))

# Function to start solving the N-Queens problem
def nqueens(N):
    # Create an empty N x N chessboard (all zeros)
    board = [[0] * N for _ in range(N)]

    # Try to solve the problem, starting from the first row
    if solve_nqueens(board, 0, N):
        print_solution(board, N)  # Print the solution if it exists
    else:
        print("No solution exists")  # Print if no solution is found

# Ask the user for input (the size of the board)
N = int(input("Enter the value of N: "))
nqueens(N)





