import numpy as np

def gauss_elimination(A, b):
    """
    Solve the system of linear equations Ax = b using Gauss Elimination with partial pivoting.

    Parameters:
    - A: Coefficient matrix (n x n)
    - b: Right-hand side vector (n)

    Returns:
    - x: Solution vector
    """
    n = len(b)

    # Convert all elements to float64
    A = A.astype(np.float64)
    b = b.astype(np.float64)

    # Augmenting the coefficient matrix A with the column vector b
    augmented_matrix = np.column_stack((A, b))

    # Forward elimination with partial pivoting
    for i in range(n):
        # Partial pivoting: Find the row with the maximum absolute value in the current column
        max_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i
        augmented_matrix[[i, max_row], :] = augmented_matrix[[max_row, i], :]

        # Make the diagonal element 1
        pivot = augmented_matrix[i, i]
        augmented_matrix[i, :] /= pivot

        # Eliminate other elements in the current column
        for j in range(i + 1, n):
            factor = augmented_matrix[j, i]
            augmented_matrix[j, :] -= factor * augmented_matrix[i, :]

    # Backward substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:n], x[i+1:])

    return x

# Example usage and report

# Example 1:
A1 = np.array([[2, 1, -1],
               [-3, -1, 2],
               [-2, 1, 2]])
b1 = np.array([8, -11, -3])
solution1 = gauss_elimination(A1, b1)

# Example 2:
A2 = np.array([[4, -2, 1],
               [3, -1, 3],
               [2, 1, -2]])
b2 = np.array([4, 6, -3])
solution2 = gauss_elimination(A2, b2)

# Example 3:
A3 = np.array([[1, -2, 3],
               [4, -5, 6],
               [7, -8, 9]])
b3 = np.array([6, 15, 24])
solution3 = gauss_elimination(A3, b3)

# Display the results
print("Example 1 Solution:", solution1)
print("Example 2 Solution:", solution2)
print("Example 3 Solution:", solution3)
