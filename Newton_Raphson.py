def newton_raphson_method(func, func_derivative, x0, tol=1e-6, max_iter=100):
    """
    Newton-Raphson method to find the root of a function.

    Parameters:
    - func: The function for which the root is to be found.
    - func_derivative: The derivative of the function.
    - x0: Initial guess.
    - tol: Tolerance level for stopping criteria (default is 1e-6).
    - max_iter: Maximum number of iterations (default is 100).

    Returns:
    - root: The approximate root of the function.
    - iterations: The number of iterations performed.
    """
    x = x0
    iterations = 0

    while iterations < max_iter:
        x_new = x - func(x) / func_derivative(x)

        if abs(x_new - x) < tol:
            return x_new, iterations

        x = x_new
        iterations += 1

    raise ValueError("Maximum number of iterations reached. No convergence.")

# Example function and its derivative
def example_function(x):
    return x**2 - 4

def example_function_derivative(x):
    return 2 * x

# Initial guess
initial_guess = 1.0

# Run Newton-Raphson method for three different inputs
input_values = [initial_guess, -2.0, 3.0]

for input_value in input_values:
    root, iterations = newton_raphson_method(example_function, example_function_derivative, input_value)
    print(f"Root for input value {input_value}: {root} (found in {iterations} iterations)")
