import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import latex, symbols, lambdify, exp, log
from services.taylor.methods import taylor
import matplotlib.pyplot as plt
from services.latex import render_latex


class Taylor(ttk.Frame):
  def __init__(self, container, controller):
    super().__init__(container)

    self.distance_y = 0


    self.controller = controller


    # Labels and Entries
    self.equation_label = ttk.Label(self, text="Ingresa la función:")
    self.equation_label.place(x=25, y=self.add(), anchor="w")


    self.equation_entry = ttk.Entry(self)
    self.equation_entry.place(x=25, y=self.add(), anchor="w")



    self.initial_value_label = ttk.Label(self, text="Ingresa el valor inicial:")
    self.initial_value_label.place(x=25, y=self.add(), anchor="w")



    self.initial_value_entry = ttk.Entry(self)
    self.initial_value_entry.place(x=25, y=self.add(), anchor="w")



    self.degree_label = ttk.Label(self, text="Ingresa el grado del polinomio:")
    self.degree_label.place(x=25, y=self.add(), anchor="w")



    self.degree_entry = ttk.Entry(self)
    self.degree_entry.place(x=25, y=self.add(), anchor="w")



    self.solve_button = ttk.Button(self, text="Resolver", command=self.solve)
    self.solve_button.place(x=25, y=self.add(), anchor="w")


    self.result_label = ttk.Label(self)
    self.result_label.place(x=25, y=self.add(180), anchor="w")


  def add(self,num = 30):
      self.distance_y+=num
      return self.distance_y

  def solve(self):
    f = self.equation_entry.get()
    x0 = float(self.initial_value_entry.get())
    n = int(self.degree_entry.get())

    try:
        x = symbols('x')
        equation = eval(f)
        solution = taylor(equation, x0, n)
        latex_solution = latex(solution)


        img = render_latex(latex_solution)
        self.result_label.config(image=img)


    except Exception as e:
        self.result_label.config(text=f"Error: {str(e)}")
