import numpy as np

def newton_forward_interpolation(x_values, y_values, x):
    """
    Newton's forward difference interpolation.

    Parameters:
    - x_values: List or array of x values of data points.
    - y_values: List or array of y values of data points.
    - x: The point at which to interpolate.

    Returns:
    - y: The interpolated value at point x.
    """
    n = len(x_values)
    forward_diff_table = np.zeros((n, n))

    # Fill in the first column with the y values
    forward_diff_table[:, 0] = y_values

    # Calculate forward differences
    for j in range(1, n):
        for i in range(n - j):
            forward_diff_table[i, j] = forward_diff_table[i + 1, j - 1] - forward_diff_table[i, j - 1]

    # Calculate interpolated value using Newton's formula
    y = forward_diff_table[0, 0]
    for j in range(1, n):
        term = forward_diff_table[0, j]
        for i in range(j):
            term *= (x - x_values[i])
            term /= (x_values[j] - x_values[i])
        y += term

    return y

# Example usage:
x_values = np.array([1, 2, 3, 4])
y_values = np.array([2, 1, 3, 6])

interpolation_point = 2.5
interpolated_value = newton_forward_interpolation(x_values, y_values, interpolation_point)

print(f"Interpolated value at x = {interpolation_point}: {interpolated_value}")
