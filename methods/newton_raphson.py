import numpy as np


def evaluate_polynomial(coefficients, x):
    # Evaluate the polynomial at x.
    return np.polyval(coefficients, x)

def newton_raphson_method(coefficients, x0, tolerance=1e-5, max_iterations=1000):
    # Perform the Newton-Raphson method to find a root.
    derivative_coeffs = np.polyder(coefficients)

    iteration = 0
    while iteration < max_iterations:
        f_x0 = evaluate_polynomial(coefficients, x0)
        f_prime_x0 = evaluate_polynomial(derivative_coeffs, x0)

        if f_prime_x0 == 0:
            print("Derivative is zero. Newton-Raphson method fails.")
            return None

        x1 = x0 - f_x0 / f_prime_x0

        if abs(x1 - x0) < tolerance:
            return x1

        x0 = x1
        iteration += 1

    print("Maximum iterations reached. Method may not have converged.")
    return x0, iteration
# Sky was here 😑
