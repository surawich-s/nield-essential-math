import tkinter as tk
from sympy import symbols, diff, sympify

class DerivativeCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Derivative Calculator")

        self.entry = tk.Entry(self.window, width=50)
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

        self.derivative_button = tk.Button(self.window, text="Calculate Derivative", command=self.calculate_derivative)
        self.derivative_button.grid(row=5, column=0, columnspan=4)

        self.x_value_label = tk.Label(self.window, text="Enter x value:")
        self.x_value_label.grid(row=6, column=0)

        self.x_value_entry = tk.Entry(self.window)
        self.x_value_entry.grid(row=6, column=1)

        self.solve_button = tk.Button(self.window, text="Solve Equation", command=self.solve_equation)
        self.solve_button.grid(row=6, column=2)

        self.solution_label = tk.Label(self.window, text="Solution:")
        self.solution_label.grid(row=7, column=0, columnspan=4)

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.window, text=button, width=5, command=lambda button=button: self.append_to_entry(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.window, text="(", width=5, command=lambda: self.append_to_entry("(")).grid(row=row_val, column=0)
        tk.Button(self.window, text=")", width=5, command=lambda: self.append_to_entry(")")).grid(row=row_val, column=1)
        tk.Button(self.window, text="^", width=5, command=lambda: self.append_to_entry("**")).grid(row=row_val, column=2)
        tk.Button(self.window, text="x", width=5, command=lambda: self.append_to_entry("x")).grid(row=row_val, column=3)
        tk.Button(self.window, text="C", width=5, command=self.clear_entry).grid(row=row_val+1, column=0, columnspan=4)

    def append_to_entry(self, value):
        self.entry.insert(tk.END, value)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def calculate_derivative(self):
        equation = self.entry.get()
        equation = self.insert_multiplication(equation)
        x = symbols('x')
        derivative = diff(sympify(equation), x)
        self.solution_label.config(text=f"Derivative: {derivative}")

    def solve_equation(self):
        equation = self.entry.get()
        equation = self.insert_multiplication(equation)
        x_value = float(self.x_value_entry.get())
        x = symbols('x')
        solution = sympify(equation).subs(x, x_value)
        self.solution_label.config(text=f"Solution: {solution}")

    def insert_multiplication(self, equation):
        i = 0
        while i < len(equation):
            if equation[i].isdigit() and i < len(equation) - 1 and equation[i+1] == 'x':
                equation = equation[:i+1] + '*' + equation[i+1:]
            i += 1
        return equation

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = DerivativeCalculator()
    calculator.run()
