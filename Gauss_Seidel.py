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

# Example usage:
A = np.array([[4, -1, 0, 0],
              [-1, 4, -1, 0],
              [0, -1, 4, -1],
              [0, 0, -1, 3]])

b = np.array([15, 10, 10, 10])

initial_guess = np.zeros(len(b))

solution, iterations = gauss_seidel(A, b, initial_guess)
print("Solution using Gauss-Seidel method:", solution)
print("Number of iterations:", iterations)
