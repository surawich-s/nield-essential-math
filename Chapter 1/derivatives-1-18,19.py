from sympy import *
# Declare 'x' to SymPy
x = symbols('x')
# Now just use Python syntax to declare function
f = (3*x**2 + 2*x - 5) / (x**2 - 4*x + 3)
# Calculate the derivative of the function
dx_f = diff(f)

print(dx_f)

# Simplify the derivative expression
simplified_dx_f = simplify(dx_f)
print("Simplified derivative:")
print(simplified_dx_f)

# def f(x):
#     return 3*x**2+1
# def dx_f(x):
#     return 6*x

# slope_at_2 = dx_f(3)
# print(slope_at_2)

# dx_f_callable = lambdify(x, dx_f)
# result2 = dx_f_callable(2) 

# print(result2)