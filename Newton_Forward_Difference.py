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

# Example usage and report

# Example 1:
x_values1 = np.array([1, 2, 3, 4])
y_values1 = np.array([2, 1, 3, 6])
interpolation_point1 = 2.5
interpolated_value1 = newton_forward_interpolation(x_values1, y_values1, interpolation_point1)
print(f"Example 1 - Interpolated value at x = {interpolation_point1}: {interpolated_value1}")

# Example 2:
x_values2 = np.array([0, 1, 2, 3, 4])
y_values2 = np.array([0, 1, 8, 27, 64])
interpolation_point2 = 1.5
interpolated_value2 = newton_forward_interpolation(x_values2, y_values2, interpolation_point2)
print(f"Example 2 - Interpolated value at x = {interpolation_point2}: {interpolated_value2}")

# Example 3:
x_values3 = np.array([-2, -1, 0, 1, 2])
y_values3 = np.array([4, 1, 0, 1, 4])
interpolation_point3 = 0.5
interpolated_value3 = newton_forward_interpolation(x_values3, y_values3, interpolation_point3)
print(f"Example 3 - Interpolated value at x = {interpolation_point3}: {interpolated_value3}")
