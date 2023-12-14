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
        # Make the diagonal element 1
        pivot_value = augmented_matrix[pivot_row, pivot_row]
        augmented_matrix[pivot_row, :] = augmented_matrix[pivot_row, :] / float(pivot_value)

        # Eliminate other elements in the current column
        for row in range(n):
            if row != pivot_row:
                factor = augmented_matrix[row, pivot_row]
                augmented_matrix[row, :] = augmented_matrix[row, :] - factor * augmented_matrix[pivot_row, :]

    # Extract the solution vector
    solution = augmented_matrix[:, -1]

    return solution

# Example usage:
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])

b = np.array([8, -11, -3])

solution = gauss_jordan_elimination(A, b)
print("Approximate solution using Gauss-Jordan Elimination:", solution)
