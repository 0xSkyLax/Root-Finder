import os
from datetime import datetime

# Prepares a readable polynomial
def polynomial_to_string(coefficients):
    terms = []
    degree = len(coefficients) - 1

    for i, coef in enumerate(coefficients):
        power = degree - i
        if coef == 0:
            continue
        coef_str = f"{abs(coef)}" if abs(coef) != 1 or power == 0 else ""
        sign = "-" if coef < 0 else "+" if terms else ""
        if power > 1:
            terms.append(f"{sign} {coef_str}x^{power}")
        elif power == 1:
            terms.append(f"{sign} {coef_str}x")
        else:
            terms.append(f"{sign} {coef_str}")
    return " ".join(terms).strip()


def log_result(coefficients, method, initial_conditions, root, tolerance, max_iterations, no_iter):
    # Ensures that output directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    log_file = os.path.join(output_dir, "results_log.txt")

    poly_str = polynomial_to_string(coefficients)
    # Sky was here 😑
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Builds log entry
    log_entry = f"""
===========================
Timestamp: {timestamp}
Method: {method}
Polynomial: f(x) = {poly_str}
Initial Conditions: {initial_conditions}
Tolerance: {tolerance}
Max Iterations: {max_iterations}
Resulting Root: {root}
No. of Iterations taken: {no_iter}
===========================\n"""

    # Appends the log file
    with open(log_file, "a") as f:
        f.write(log_entry)
