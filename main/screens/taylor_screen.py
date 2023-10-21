import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import latex, symbols, lambdify, exp, log
from services.taylor.methods import taylor
import matplotlib.pyplot as plt


class Taylor(ttk.Frame):
  def __init__(self, container, controller):
    super().__init__(container)

    self.controller = controller

    # Labels and Entries
    self.equation_label = ttk.Label(self, text="Ingresa la función:")
    self.equation_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    self.equation_entry = ttk.Entry(self)
    self.equation_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    self.initial_value_label = ttk.Label(self, text="Ingresa el valor inicial:")
    self.initial_value_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    self.initial_value_entry = ttk.Entry(self)
    self.initial_value_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    self.degree_label = ttk.Label(self, text="Ingresa el grado del polinomio:")
    self.degree_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    self.degree_entry = ttk.Entry(self)
    self.degree_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    self.solve_button = ttk.Button(self, text="Resolver", command=self.solve)
    self.solve_button.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    self.result_label = ttk.Label(self, text="Solución en LaTeX:")
    self.result_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

    # Configure weights
    self.columnconfigure(1, weight=1)  # Make the entry widgets expand horizontally
    self.rowconfigure(5, weight=1)     # Make the canvas expand vertically

    self.canvas = None

  def solve(self):
    f = self.equation_entry.get()
    x0 = float(self.initial_value_entry.get())
    n = int(self.degree_entry.get())
    symbols_in_equation = ' '.join(filter(str.isalpha, f))
    try:
        x, y, z, w, r, t = symbols('x y z w r t')
        equation = eval(f)
        solution = taylor(equation, x0, n)
        latex_solution = latex(solution)

        # Usar matplotlib para mostrar LaTeX
        fig, ax = plt.subplots(figsize=(5, 2))
        ax.text(0.5, 0.5, f"${latex_solution}$", size=20, ha="center", va="center")
        plt.axis("off")
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=5, column=0, columnspan=2, pady=10)

    except Exception as e:
        self.result_label.config(text=f"Error: {str(e)}")
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
