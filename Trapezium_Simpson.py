import numpy as np

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

# Example usage and report

# Example 1:
def example_function1(x):
    return x**2

a1 = 0
b1 = 1
n1 = 4

# Example using Trapezium Rule
result_trapezium1 = trapezium_rule(example_function1, a1, b1, n1)
print(f"Example 1 - Approximate integral using Trapezium Rule: {result_trapezium1}")

# Example using Simpson's 1/3rd Rule
result_simpsons1 = simpsons_one_third_rule(example_function1, a1, b1, n1)
print(f"Example 1 - Approximate integral using Simpson's 1/3rd Rule: {result_simpsons1}")

# Example 2:
def example_function2(x):
    return np.sin(x)

a2 = 0
b2 = np.pi / 2
n2 = 4

# Example using Trapezium Rule
result_trapezium2 = trapezium_rule(example_function2, a2, b2, n2)
print(f"Example 2 - Approximate integral using Trapezium Rule: {result_trapezium2}")

# Example using Simpson's 1/3rd Rule
result_simpsons2 = simpsons_one_third_rule(example_function2, a2, b2, n2)
print(f"Example 2 - Approximate integral using Simpson's 1/3rd Rule: {result_simpsons2}")

# Example 3:
def example_function3(x):
    return np.exp(-x)

a3 = 0
b3 = 1
n3 = 4

# Example using Trapezium Rule
result_trapezium3 = trapezium_rule(example_function3, a3, b3, n3)
print(f"Example 3 - Approximate integral using Trapezium Rule: {result_trapezium3}")

# Example using Simpson's 1/3rd Rule
result_simpsons3 = simpsons_one_third_rule(example_function3, a3, b3, n3)
print(f"Example 3 - Approximate integral using Simpson's 1/3rd Rule: {result_simpsons3}")
