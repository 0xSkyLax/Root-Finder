# Root Finder 🔢

A numerical methods project for finding the roots of single-variable polynomials.  
Implements **Bisection, Newton–Raphson, Regula Falsi, and Secant** methods.

---

## ✨ Features
- **Multiple algorithms**:  
  - Bisection  
  - Newton–Raphson  
  - Regula Falsi  
  - Secant  
- **Dual plotting support**:  
  - Uses the **MATLAB Engine for Python** (if installed).  
  - Falls back to **NumPy + Matplotlib** if MATLAB is not available.  
- **Result logging**: Each run is logged in `output/results_log.txt`.  
- **Easy setup**: Includes `install_dependencies.bat` for quick dependency installation.  

---

## 🛠 Requirements
- Python **3.9+**  
- [MATLAB Engine for Python](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html) (optional, only required for MATLAB-based plotting)  
- NumPy  
- Matplotlib  

🔗 See [MATLAB-Python compatibility requirements](https://www.mathworks.com/support/requirements/python-compatibility.html) for supported versions.  

---

## 🚀 Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/root-finder.git
cd root-finder
```

Install dependencies with the provided script:
```bash
install_dependencies.bat
```
Or manually:
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage
Run the program:
Double Click to Run or;
```bash
python root_finder.py
```

You will be prompted to:

1. Enter a polynomial function.
2. Choose a root-finding method.
3. View the results and (optionally) plots.

Results are automatically saved in:
```bash
output/results_log.txt
```

---

## 📊 Example
```text
===========================
Timestamp: 20XX-XX-XX XX:XX:XX
Method: bisection
Polynomial: f(x) = x^3 - 6.0x^2 + 11.0x - 6.0
Initial Conditions: (1.5, 0.5)
Tolerance: 1e-05
Max Iterations: 1000
Resulting Root: 1.0
===========================
```
If MATLAB is installed and linked, plots can use MATLAB. Otherwise, NumPy + Matplotlib will be used.
