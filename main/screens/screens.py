import tkinter as tk
from tkinter import ttk

class Menu(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.controller = controller

        self.label = ttk.Label(self,text='Bienvenido a este programa por el cual pordras recorrer todos los temas visto en la clase de metodos nuemricos, aqui podras usar unicametne las variables (x,y,z,w), puedes usar exp() y log(), solo ve al programa deseado en el menu desplegable que ves arriba (Proyectos)')
        self.label.pack(side='top', padx=10, pady=10)



class Screen2(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.controller = controller

        label = ttk.Label(self, text="Pantalla 2")
        label.pack(padx=10, pady=10)

        button = ttk.Button(self, text="Ir a la Pantalla 3", command=self.go_to_screen3)
        button.pack(padx=10, pady=10)

    def go_to_screen3(self):
        self.controller.show_frame("Screen3")

class Screen3(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.controller = controller

        label = ttk.Label(self, text="Pantalla 3")
        label.pack(padx=10, pady=10)

        button = ttk.Button(self, text="Ir a la Pantalla 1", command=self.go_to_screen1)
        button.pack(padx=10, pady=10)

    def go_to_screen1(self):
        self.controller.show_frame("Menu")
