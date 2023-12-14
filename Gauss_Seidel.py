import numpy as np

def gauss_seidel(A, b, initial_guess=None, tol=1e-6, max_iter=100):
    n = len(b)
    
    if initial_guess is None:
        initial_guess = np.zeros(n)
    
    x = initial_guess.copy()
    iteration = 0
    
    while iteration < max_iter:
        x_old = x.copy()
        
        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = (b[i] - sigma) / A[i, i]
        
        if np.linalg.norm(x - x_old, np.inf) < tol:
            return x, iteration + 1  # Return the solution and the number of iterations
        
        iteration += 1
    
    raise ValueError("Maximum number of iterations reached. No convergence.")

# Example usage and report

# Example 1:
A1 = np.array([[4, -1, 0, 0],
               [-1, 4, -1, 0],
               [0, -1, 4, -1],
               [0, 0, -1, 3]])
b1 = np.array([15, 10, 10, 10])
initial_guess1 = np.zeros(len(b1))

solution1, iterations1 = gauss_seidel(A1, b1, initial_guess1)
print("\n""Example 1 Solution:", solution1)
print("Example 1 Number of iterations:", iterations1,"\n")

# Example 2:
A2 = np.array([[3, -1, 0],
               [-1, 3, -1],
               [0, -1, 3]])
b2 = np.array([11, 10, 10])
initial_guess2 = np.zeros(len(b2))

solution2, iterations2 = gauss_seidel(A2, b2, initial_guess2)
print("Example 2 Solution:", solution2)
print("Example 2 Number of iterations:", iterations2,"\n")

# Example 3:
A3 = np.array([[4, -2, 1],
               [1, 4, -2],
               [1, 1, 3]])
b3 = np.array([5, 4, 6])
initial_guess3 = np.zeros(len(b3))

solution3, iterations3 = gauss_seidel(A3, b3, initial_guess3)
print("Example 3 Solution:", solution3)
print("Example 3 Number of iterations:", iterations3,"\n")
