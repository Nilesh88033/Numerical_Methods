def trapezium_rule(f, a, b, n):
    """
    Numerical integration using the Trapezium rule.

    Parameters:
    - f: The integrand function.
    - a: The lower limit of integration.
    - b: The upper limit of integration.
    - n: The number of subintervals.

    Returns:
    - integral: The approximate integral value.
    """
    h = (b - a) / n
    x_values = [a + i * h for i in range(n + 1)]
    y_values = [f(x) for x in x_values]
    
    integral = h * (0.5 * y_values[0] + sum(y_values[1:-1]) + 0.5 * y_values[-1])
    
    return integral

def simpsons_one_third_rule(f, a, b, n):
    """
    Numerical integration using Simpson's 1/3rd rule.

    Parameters:
    - f: The integrand function.
    - a: The lower limit of integration.
    - b: The upper limit of integration.
    - n: The number of subintervals (should be even).

    Returns:
    - integral: The approximate integral value.
    """
    h = (b - a) / n
    x_values = [a + i * h for i in range(n + 1)]
    y_values = [f(x) for x in x_values]

    integral = (h / 3) * (y_values[0] + 4 * sum(y_values[1::2]) + 2 * sum(y_values[2:n-1:2]) + y_values[-1])

    return integral

# Example usage:
def example_function(x):
    return x**2

a = 0
b = 1
n = 4

# Example using Trapezium Rule
result_trapezium = trapezium_rule(example_function, a, b, n)
print(f"Approximate integral using Trapezium Rule: {result_trapezium}")

# Example using Simpson's 1/3rd Rule
result_simpsons = simpsons_one_third_rule(example_function, a, b, n)
print(f"Approximate integral using Simpson's 1/3rd Rule: {result_simpsons}")
