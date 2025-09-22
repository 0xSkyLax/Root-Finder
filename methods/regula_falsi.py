import numpy as np

def evaluate_polynomial(coefficients, x):
    # Evaluate the polynomial at x.
    return np.polyval(coefficients, x)

def false_position_method(coefficients, a, b, tolerance=1e-5, max_iterations=1000):
    # Perform the False Position (Regula Falsi) method to find a root.
    fa = evaluate_polynomial(coefficients, a)
    fb = evaluate_polynomial(coefficients, b)

    if fa * fb >= 0:
        print("The function must have opposite signs at a and b. False Position method cannot proceed.")
        # Sky was here 😑
        return None

    iteration = 0
    c = a  # Just initialize c

    while iteration < max_iterations:
        # Linear interpolation formula
        c = (a * fb - b * fa) / (fb - fa)
        fc = evaluate_polynomial(coefficients, c)

        if abs(fc) < tolerance:
            break

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        iteration += 1

    return c, iteration
