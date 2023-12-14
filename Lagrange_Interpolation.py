import numpy as np

def lagrange_interpolation(x_values, y_values, x):
    """
    Lagrange interpolation method.

    Parameters:
    - x_values: List or array of x values of data points.
    - y_values: List or array of y values of data points.
    - x: The point at which to interpolate.

    Returns:
    - y: The interpolated value at point x.
    """
    n = len(x_values)
    y = 0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
        y += term

    return y

# Example usage:
x_values = np.array([1, 2, 3, 4])
y_values = np.array([2, 1, 3, 6])

interpolation_point = 2.5
interpolated_value = lagrange_interpolation(x_values, y_values, interpolation_point)

print(f"Interpolated value at x = {interpolation_point}: {interpolated_value}")
