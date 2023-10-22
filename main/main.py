import tkinter as tk
from tkinter import ttk
from screens.screens import Menu, Screen2, Screen3
from screens.equations import a
from screens.taylor_screen import Taylor

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Mi Aplicación Tkinter")
        self.geometry("800x600")

        self.container = ttk.Frame(self)
        self.container.pack(expand=True, fill='both', padx=10, pady=10)

        self.frames = {}

        self.create_frames()

        self.create_menu() 

        self.show_frame("Taylor")
        
    def create_frames(self):
        for screen in (Menu, Screen2, Screen3,a,Taylor):
            frame = screen(self.container, self)
            self.frames[screen.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def create_menu(self):
        menu = tk.Menu(self)
        self.config(menu=menu)

        page_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Proyectos", menu=page_menu)

        page_menu.add_command(label="Menu", command=lambda: self.show_frame("Menu"))
        page_menu.add_command(label="Pantalla 2", command=lambda: self.show_frame("Screen2"))
        page_menu.add_command(label="Pantalla 3", command=lambda: self.show_frame("Screen3"))
        page_menu.add_command(label="Pantalla 4", command=lambda: self.show_frame("a"))
        page_menu.add_command(label="Taylor", command=lambda: self.show_frame("Taylor"))

if __name__ == "__main__":
    app = App()
    app.mainloop()