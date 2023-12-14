def regula_falsi(func, a, b, tol=1e-6, max_iter=100):
    """
    Regula Falsi method to find the root of a function.

    Parameters:
    - func: The function for which the root is to be found.
    - a, b: Initial bracketing values where f(a) and f(b) have opposite signs.
    - tol: Tolerance level for stopping criteria (default is 1e-6).
    - max_iter: Maximum number of iterations (default is 100).

    Returns:
    - root: The approximate root of the function.
    - iterations: The number of iterations performed.
    """
    if func(a) * func(b) > 0:
        raise ValueError("Initial values a and b do not bracket a root.")

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

initial_a = 0
initial_b = 2
tolerance = 1e-6

root, iterations = regula_falsi(example_function, initial_a, initial_b, tolerance)

print(f"Approximate root: {root}")
print(f"Iterations: {iterations}")