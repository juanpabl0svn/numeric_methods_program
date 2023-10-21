import tkinter as tk
from tkinter import ttk
from sympy import latex, symbols,lambdify
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class a(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.controller = controller

        self.equation_label = ttk.Label(self, text="Ingresa la funcion:")
        self.equation_label.pack(pady=10)

        self.equation_entry = ttk.Entry(self)
        self.equation_entry.pack(pady=5)

        self.lower_interval_label = ttk.Label(self, text="Ingresa el intervalos inferior (A):")
        self.lower_interval_label.pack(pady=10)

        self.lower_interval_entry = ttk.Entry(self)
        self.lower_interval_entry.pack(pady=5)

        self.upper_interval_label = ttk.Label(self, text="Ingresa el intervalo superior (B):")
        self.upper_interval_label.pack(pady=10)

        self.upper_interval_entry = ttk.Entry(self)
        self.upper_interval_entry.pack(pady=5)

        self.solve_button = ttk.Button(self, text="Resolver", command=self.solve_equation)
        self.solve_button.pack(pady=10)

        self.result_label = ttk.Label(self, text="Solución en LaTeX:")
        self.result_label.pack(pady=10)

        self.canvas = None

    def solve_equation(self):
        equation_str = self.equation_entry.get()
        A = self.lower_interval_entry.getint()
        B = self.upper_interval_entry.getint()
        symbols_in_equation = ' '.join(filter(str.isalpha, equation_str))
        try:
            x,y,z,w,r,t = symbols('x y z w r t')
            equation = eval(equation_str)
            equation_lambda = lambdify(symbols(symbols_in_equation[0]),equation)
            table,solution = biseccion(equation_lambda,A,B)
            latex_solution = latex(solution)  # Considerando que hay una única solución

            # Usar matplotlib para mostrar LaTeX
            fig, ax = plt.subplots(figsize=(5, 2))
            ax.text(0.5, 0.5, f"${latex_solution}$", size=20, ha="center", va="center")
            plt.axis("off")
            if self.canvas:
                self.canvas.get_tk_widget().destroy()

            self.canvas = FigureCanvasTkAgg(fig, master=self)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(pady=10)

        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")
            if self.canvas:
                self.canvas.get_tk_widget().destroy()



