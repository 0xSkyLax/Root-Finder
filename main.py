# Library Imports
import time
import numpy as np
import matplotlib.pyplot as plt

# Function imports from other files (Methods & other Utilities)
from methods.bisection import bisection_method
from methods.regula_falsi import false_position_method
from methods.newton_raphson import newton_raphson_method
from methods.secant import secant_method
from utilis.plotter import plot_polynomial
from utilis.logger import log_result

# Logo, Version & Author Information
def opening_screen():
    print("=" * 50)
    print("")
    print("██████╗░░█████╗░░█████╗░████████╗░░░░░░███████╗██╗███╗░░██╗██████╗░███████╗██████╗░")
    print("██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝░░░░░░██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗")
    print("██████╔╝██║░░██║██║░░██║░░░██║░░░█████╗█████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝")
    print("██╔══██╗██║░░██║██║░░██║░░░██║░░░╚════╝██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗")
    print("██║░░██║╚█████╔╝╚█████╔╝░░░██║░░░░░░░░░██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║")
    print("╚═╝░░╚═╝░╚════╝░░╚════╝░░░░╚═╝░░░░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝")
    print("")
    print("=" * 50)
    print("   Welcome to the ROOT-FINDER App!")
    print("     Version 0.1.3 Beta")
    print("         by Group 5")
    print("=" * 50)
    time.sleep(1)

# Takes User polynomial input
def get_polynomial():
    print("\nLet's define your polynomial.")

    # Ask for the order
    while True:
        try:
            order = int(input("Enter the order (degree) of the polynomial (e.g., 2 for quadratic): "))
            if order < 1:
                print("Polynomial must be at least of order 1.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Get coefficients
    print(f"\nEnter the coefficients for the polynomial of degree {order}.")
    print("Start from the highest degree term to the constant term.")

    coefficients = []
    for i in range(order, -1, -1):
        while True:
            try:
                coeff = float(input(f"Coefficient for x^{i}: "))
                coefficients.append(coeff)
                break
            except ValueError:
                print("Please enter a valid number.")

    coefficients = np.array(coefficients)
    print("\nYour polynomial is:")
    display_polynomial(coefficients)

    return coefficients

# Prints the polynomical
def display_polynomial(coefficients):
    poly_str = ""
    degree = len(coefficients) - 1
    for i, coeff in enumerate(coefficients):
        power = degree - i
        if coeff != 0:
            if coeff > 0 and i != 0:
                poly_str += " + "
            elif coeff < 0:
                # Sky was here 😑
                poly_str += " - " if i != 0 else "-"
            if abs(coeff) != 1 or power == 0:
                poly_str += f"{abs(coeff)}"
            if power > 0:
                poly_str += "x"
                if power > 1:
                    poly_str += f"^{power}"
    print(poly_str)

# Method Menu
def choose_method():
    print("\nChoose a root-finding method:")
    print("1. Bisection Method")
    print("2. Newton-Raphson Method")
    print("3. Secant Method")
    print("4. False Position Method (Regula Falsi)")

    methods = {
        "1": "bisection",
        "2": "newton-raphson",
        "3": "secant",
        "4": "false-position"
    }

    while True:
        choice = input("Enter the number corresponding to the method: ")
        if choice in methods:
            print(f"\nYou selected: {methods[choice].replace('-', ' ').title()}")
            return methods[choice]
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

# Set Tolerance and Max Iterations
def get_solver_settings():
    default_tol = 1e-5
    default_max_iter = 1000

    tol_input = input(f"Enter your desired tolerance or press Enter for default ({default_tol}): ").strip()
    iter_input = input(f"Enter the max number of iterations or press Enter for default ({default_max_iter}): ").strip()

    try:
        tolerance = float(tol_input) if tol_input else default_tol
    except ValueError:
        print("Invalid tolerance. Using default.")
        tolerance = default_tol

    try:
        max_iterations = int(iter_input) if iter_input else default_max_iter
    except ValueError:
        print("Invalid number of iterations. Using default.")
        max_iterations = default_max_iter

    return tolerance, max_iterations

# Required Guesses & Conditions for each Method
def get_initial_guesses(method):
    print("\nProvide initial guess(es) for the method.")

    if method in ["bisection", "false-position", "secant"]:
        # Two initial guesses needed
        while True:
            try:
                a = float(input("Enter first guess (a): "))
                b = float(input("Enter second guess (b): "))
                if a == b:
                    print("Guesses must be different. Try again.")
                    continue
                break
            except ValueError:
                print("Please enter valid numbers.")
        return (a, b)

    elif method == "newton-raphson":
        # Only one initial guess needed
        while True:
            try:
                x0 = float(input("Enter initial guess (x0): "))
                break
            except ValueError:
                print("Please enter a valid number.")
        return (x0,)

    else:
        raise ValueError("Invalid method selected.")

# Exits or restarts program
def exit_restart():
    while True:
        restart = input("\nWould you like to compute another root?\n(Press 'y' to continue or Enter to exit): ").strip().lower()
        if restart == 'y':
            print("\n\n\n\n")
            __main__()
            break
        elif restart == '':
            print('\nExiting Program...')
            time.sleep(1)
            break
        else:
            print("Invalid input. Please Press 'y' to contine or Enter to exit.")

# __main__ function to run
def __main__():
    opening_screen()
    coefficients = get_polynomial()
    method = choose_method()
    initial_guesses = get_initial_guesses(method)
    tolerance, max_iterations = get_solver_settings()

    # Choose the correct method to calculate the root based on user choice
    if method == "bisection":
        root, no_iter = bisection_method(coefficients, *initial_guesses, tolerance, max_iterations)
    elif method == "false-position":
        root, no_iter = false_position_method(coefficients, *initial_guesses, tolerance, max_iterations)
    elif method == "newton-raphson":
        root, no_iter = newton_raphson_method(coefficients, initial_guesses[0], tolerance, max_iterations)
    elif method == "secant":
        root, no_iter = secant_method(coefficients, *initial_guesses, tolerance, max_iterations)     

    print(f"Root found: {root:.6f} in {no_iter} iterations")

    # Ask user if they want to plot the graph
    print("How would you like to plot the polynomial? (press Enter to skip)")
    print("1. Plot with MATLAB")
    print("2. Plot with matplotlib")
    plot_choice = input("Select plot option: ").strip()

    if plot_choice == "1":
        plot_polynomial(coefficients, root, mode="matlab")
    elif plot_choice == "2":
        plot_polynomial(coefficients, root, mode="matplotlib")

    # Log result to file
    initial_conditions = initial_guesses  # Already in tuple form
    log_result(coefficients, method, initial_conditions, root, tolerance, max_iterations, no_iter)

    exit_restart()

__main__()