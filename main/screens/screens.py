import tkinter as tk
from tkinter import ttk

class Screen1(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.controller = controller

        label = ttk.Label(self, text="Pantalla 1")
        label.pack(padx=10, pady=10)

        button = ttk.Button(self, text="Ir a la Pantalla 2", command=self.go_to_screen2)
        button.pack(padx=10, pady=10)

    def go_to_screen2(self):
        self.controller.show_frame("Screen2")

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
        self.controller.show_frame("Screen1")
