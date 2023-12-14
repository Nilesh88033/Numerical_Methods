def newton_raphson(func, deriv_func, x0, tol=1e-6, max_iter=100):
    """
    Newton-Raphson method to find the root of a function.

    Parameters:
    - func: The function for which the root is to be found.
    - deriv_func: The derivative of the function.
    - x0: Initial guess for the root.
    - tol: Tolerance level for stopping criteria (default is 1e-6).
    - max_iter: Maximum number of iterations (default is 100).

    Returns:
    - root: The approximate root of the function.
    - iterations: The number of iterations performed.
    """
    iterations = 0
    x = x0

    while iterations < max_iter:
        f_x = func(x)
        f_prime_x = deriv_func(x)

        if abs(f_x) < tol:
            return x, iterations

        x = x - f_x / f_prime_x

        iterations += 1

    raise ValueError("Maximum number of iterations reached. No convergence.")

# Example usage:
def example_function(x):
    return x**3 - 6*x**2 + 11*x - 6

def derivative_example_function(x):
    return 3*x**2 - 12*x + 11

initial_guess = 1.5
tolerance = 1e-6

root, iterations = newton_raphson(example_function, derivative_example_function, initial_guess, tolerance)

print(f"Approximate root: {root}")
print(f"Iterations: {iterations}")
