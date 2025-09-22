import numpy as np
# Sky was here 😑

def evaluate_polynomial(coefficients, x):
    #Evaluate the polynomial at x.
    return np.polyval(coefficients, x)

def secant_method(coefficients, x0, x1, tolerance=1e-5, max_iterations=1000):
    # Perform the Secant method to find a root.
    iteration = 0

    while iteration < max_iterations:
        f_x0 = evaluate_polynomial(coefficients, x0)
        f_x1 = evaluate_polynomial(coefficients, x1)

        if (f_x1 - f_x0) == 0:
            print("Division by zero detected in Secant method.")
            return None

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        if abs(x2 - x1) < tolerance:
            return x2

        x0, x1 = x1, x2
        iteration += 1

    print("Maximum iterations reached. Method may not have converged.")
    return x1, iteration
