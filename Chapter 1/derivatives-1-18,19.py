from sympy import *
# Declare 'x' to SymPy
x = symbols('x')
# Now just use Python syntax to declare function
f = 3*x**2+1
# Calculate the derivative of the function
dx_f = diff(f)

print(dx_f)

def f(x):
    return 3*x**2+1
def dx_f(x):
    return 6*x

slope_at_2 = dx_f(3)
print(slope_at_2)