def false_position_method(func, a, b, tol=1e-6, max_iter=100):
    """
    False Position (Regula Falsi) method to find the root of a function.

    Parameters:
    - func: The function for which the root is to be found.
    - a, b: Initial bracketing interval.
    - tol: Tolerance level for stopping criteria (default is 1e-6).
    - max_iter: Maximum number of iterations (default is 100).

    Returns:
    - root: The approximate root of the function.
    - iterations: The number of iterations performed.
    """
    iterations = 0

    while iterations < max_iter:
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))

        if abs(func(c)) < tol:
            return c, iterations

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iterations += 1

    raise ValueError("Maximum number of iterations reached. No convergence.")

# Example usage:
def example_function(x):
    return x**3 - 6*x**2 + 11*x - 6

initial_interval_a = 1.5
initial_interval_b = 3.0
tolerance = 1e-6

root, iterations = false_position_method(example_function, initial_interval_a, initial_interval_b, tolerance)

print(f"Approximate root: {root}")
print(f"Iterations: {iterations}")
