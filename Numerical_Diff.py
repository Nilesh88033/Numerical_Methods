import numpy as np

def numerical_diff_forward(f, x, h=1e-5):
    """
    Numerical differentiation using Newton's forward difference method.

    Parameters:
    - f: The function for which to calculate the derivative.
    - x: The point at which to calculate the derivative.
    - h: Step size (default is 1e-5).

    Returns:
    - derivative: The numerical derivative of the function at point x.
    """
    return (f(x + h) - f(x)) / h

def numerical_diff_backward(f, x, h=1e-5):
    """
    Numerical differentiation using Newton's backward difference method.

    Parameters:
    - f: The function for which to calculate the derivative.
    - x: The point at which to calculate the derivative.
    - h: Step size (default is 1e-5).

    Returns:
    - derivative: The numerical derivative of the function at point x.
    """
    return (f(x) - f(x - h)) / h

# Example usage:
# Example usage and report

# Example 1:
def example_function1(x):
    return x**2

x_value1 = 2.0

# Example using Newton's Forward Difference Method
derivative_forward1 = numerical_diff_forward(example_function1, x_value1)
print(f"Example 1 - Numerical derivative at x = {x_value1} using Newton's Forward Difference Method: {derivative_forward1}")

# Example using Newton's Backward Difference Method
derivative_backward1 = numerical_diff_backward(example_function1, x_value1)
print(f"Example 1 - Numerical derivative at x = {x_value1} using Newton's Backward Difference Method: {derivative_backward1}")

# Example 2:
def example_function2(x):
    return np.sin(x)

x_value2 = np.pi / 4

# Example using Newton's Forward Difference Method
derivative_forward2 = numerical_diff_forward(example_function2, x_value2)
print(f"Example 2 - Numerical derivative at x = {x_value2} using Newton's Forward Difference Method: {derivative_forward2}")

# Example using Newton's Backward Difference Method
derivative_backward2 = numerical_diff_backward(example_function2, x_value2)
print(f"Example 2 - Numerical derivative at x = {x_value2} using Newton's Backward Difference Method: {derivative_backward2}")

# Example 3:
def example_function3(x):
    return np.exp(x)

x_value3 = 1.0

# Example using Newton's Forward Difference Method
derivative_forward3 = numerical_diff_forward(example_function3, x_value3)
print(f"Example 3 - Numerical derivative at x = {x_value3} using Newton's Forward Difference Method: {derivative_forward3}")

# Example using Newton's Backward Difference Method
derivative_backward3 = numerical_diff_backward(example_function3, x_value3)
print(f"Example 3 - Numerical derivative at x = {x_value3} using Newton's Backward Difference Method: {derivative_backward3}")

