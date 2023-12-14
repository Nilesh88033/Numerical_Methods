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
def example_function(x):
    return x**2

x_value = 2.0

# Example using Newton's Forward Difference Method
derivative_forward = numerical_diff_forward(example_function, x_value)
print(f"Numerical derivative at x = {x_value} using Newton's Forward Difference Method: {derivative_forward}")

# Example using Newton's Backward Difference Method
derivative_backward = numerical_diff_backward(example_function, x_value)
print(f"Numerical derivative at x = {x_value} using Newton's Backward Difference Method: {derivative_backward}")
