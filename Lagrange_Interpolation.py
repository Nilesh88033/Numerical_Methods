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

# Example usage and report

# Example 1:
x_values1 = np.array([1, 2, 3, 4])
y_values1 = np.array([2, 1, 3, 6])
interpolation_point1 = 2.5
interpolated_value1 = lagrange_interpolation(x_values1, y_values1, interpolation_point1)
print(f"Example 1 - Interpolated value at x = {interpolation_point1}: {interpolated_value1}")

# Example 2:
x_values2 = np.array([0, 1, 2, 3, 4])
y_values2 = np.array([0, 1, 8, 27, 64])
interpolation_point2 = 1.5
interpolated_value2 = lagrange_interpolation(x_values2, y_values2, interpolation_point2)
print(f"Example 2 - Interpolated value at x = {interpolation_point2}: {interpolated_value2}")

# Example 3:
x_values3 = np.array([-2, -1, 0, 1, 2])
y_values3 = np.array([4, 1, 0, 1, 4])
interpolation_point3 = 0.5
interpolated_value3 = lagrange_interpolation(x_values3, y_values3, interpolation_point3)
print(f"Example 3 - Interpolated value at x = {interpolation_point3}: {interpolated_value3}")
