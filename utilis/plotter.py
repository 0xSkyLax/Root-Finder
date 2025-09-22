import matplotlib.pyplot as plt
import numpy as np

try:
    import matlab.engine
    MATLAB_AVAILABLE = True
except ImportError:
    MATLAB_AVAILABLE = False

def evaluate_polynomial(coefficients, x):
    # Evaluate the polynomial at x.
    return np.polyval(coefficients, x)

def plot_with_matplotlib(coefficients, root=None):
    """Plot using matplotlib."""
    x_vals = np.linspace(-10, 10, 400)
    y_vals = evaluate_polynomial(coefficients, x_vals)

    plt.plot(x_vals, y_vals, label="Polynomial", color="blue")
    if root is not None:
        plt.scatter(root, 0, color="red", label=f"Root: {root:.5f}")
    
    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Polynomial and Root (matplotlib)")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_with_matlab(coefficients):
    # Plot using MATLAB (if available).
    if not MATLAB_AVAILABLE:
        print("MATLAB Engine for Python not installed.")
        return

    try:
        eng = matlab.engine.start_matlab()
        coeffs_matlab = matlab.double(coefficients)
        eng.workspace['p'] = coeffs_matlab
        eng.eval("fplot(@(x) polyval(p, x), [-10, 10]);", nargout=0)
        eng.eval("grid on; title('Polynomial (MATLAB)'); xlabel('x'); ylabel('f(x)')", nargout=0)
    except Exception as e:
        print("MATLAB plot failed:", e)


def plot_with_matplotlib(coefficients, root=None):
    # Plot the polynomial and the root if requested.
    # Define a range of x values for plotting
    x_vals = np.linspace(-10, 10, 400)
    y_vals = evaluate_polynomial(coefficients, x_vals)

    # Plot the polynomial curve
    plt.plot(x_vals, y_vals, label="Polynomial", color="blue")

    # Plot the root if it's provided
    if root is not None:
        plt.scatter(root, 0, color="red", label=f"Root: {root:.5f}")
    
    # Set graph labels
    plt.axhline(0, color="black",linewidth=1)
    plt.axvline(0, color="black",linewidth=1)
    # Sky was here 😑
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Polynomial and Root")
    plt.legend()

    # Show the plot
    plt.grid(True)
    plt.show()

def plot_polynomial(coefficients, root=None, mode="matplotlib"):
    # Plot based on selected mode.
    if mode == "matplotlib":
        plot_with_matplotlib(coefficients, root)
    elif mode == "matlab":
        plot_with_matlab(coefficients)
    else:
        print(f"Plotting using '{mode}' is not supported.")