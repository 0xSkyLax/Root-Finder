import numpy as np


def evaluate_polynomial(coefficients, x):
    # Evaluate the polynomial at x.
    return np.polyval(coefficients, x)

def bisection_method(coefficients, a, b, tolerance=1e-5, max_iterations=1000):
    # Perform the Bisection method to find a root.
    if evaluate_polynomial(coefficients, a) * evaluate_polynomial(coefficients, b) >= 0:
        print("The function must have opposite signs at a and b. Bisection method cannot proceed.")
        return None

    iteration = 0
    while (b - a) / 2 > tolerance and iteration < max_iterations:
        c = (a + b) / 2
        # Sky was here 😑
        f_c = evaluate_polynomial(coefficients, c)

        if f_c == 0:
            # Found exact root
            return c
        elif evaluate_polynomial(coefficients, a) * f_c < 0:
            b = c
        else:
            a = c

        iteration += 1

    root = (a + b) / 2
    return root, iteration
