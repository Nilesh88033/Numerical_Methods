import numpy as np

def gauss_jordan_elimination(A, b):
    """
    Gauss-Jordan elimination method to solve a system of linear equations.

    Parameters:
    - A: Coefficient matrix.
    - b: Right-hand side vector.

    Returns:
    - solution: The solution vector.
    """
    augmented_matrix = np.hstack((A, b.reshape(-1, 1)))
    n = len(b)

    for pivot_row in range(n):
        # Partial pivoting: Find the row with the maximum absolute value in the current column
        max_row = np.argmax(np.abs(augmented_matrix[pivot_row:, pivot_row])) + pivot_row

        # Swap rows to move the maximum absolute value to the pivot position
        augmented_matrix[[pivot_row, max_row], :] = augmented_matrix[[max_row, pivot_row], :]

        # Check if the pivot is zero
        if np.abs(augmented_matrix[pivot_row, pivot_row]) < 1e-10:
            raise ValueError("The matrix is singular, and the system may have no unique solution.")

        # Make the diagonal element 1
        augmented_matrix[pivot_row, :] = augmented_matrix[pivot_row, :] / augmented_matrix[pivot_row, pivot_row]

        # Eliminate other elements in the current column
        for row in range(n):
            if row != pivot_row:
                factor = augmented_matrix[row, pivot_row]
                augmented_matrix[row, :] = augmented_matrix[row, :] - factor * augmented_matrix[pivot_row, :]

    # Extract the solution vector
    solution = augmented_matrix[:, -1]

    return solution

# Example usage and report

# Example 1:
A1 = np.array([[2, 1, -1],
               [-3, -1, 2],
               [-2, 1, 2]])
b1 = np.array([8, -11, -3])
try:
    solution1 = gauss_jordan_elimination(A1, b1)
    print("Example 1 Solution:", solution1)
except ValueError as e:
    print(f"Example 1 Error: {e}")

# Example 2:
A2 = np.array([[4, -2, 1],
               [3, -1, 3],
               [2, 1, -2]])
b2 = np.array([4, 6, -3])
try:
    solution2 = gauss_jordan_elimination(A2, b2)
    print("Example 2 Solution:", solution2)
except ValueError as e:
    print(f"Example 2 Error: {e}")

# Example 3:
A3 = np.array([[1, -2, 3],
               [4, -5, 6],
               [7, -8, 9]])
b3 = np.array([6, 15, 24])
try:
    solution3 = gauss_jordan_elimination(A3, b3)
    print("Example 3 Solution:", solution3)
except ValueError as e:
    print(f"Example 3 Error: {e}")
