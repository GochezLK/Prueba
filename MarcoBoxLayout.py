import tkinter as tk
from tkinter import ttk

class MarcoBoxLayout(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Demostración de BoxLayout")
        self.geometry("400x300")

        tab_control = ttk.Notebook(self)

        horizontal1 = tk.Frame(tab_control)
        for cuenta in range(3):
            tk.Button(horizontal1, text=f"Boton {cuenta}").pack(side=tk.LEFT)

        vertical1 = tk.Frame(tab_control)
        for cuenta in range(3):
            tk.Label(vertical1, text="").pack()
            tk.Button(vertical1, text=f"Boton {cuenta}").pack()

        horizontal2 = tk.Frame(tab_control)
        for cuenta in range(3):
            tk.Label(horizontal2, text="").pack(side=tk.LEFT)
            tk.Button(horizontal2, text=f"Boton {cuenta}").pack(side=tk.LEFT)

        vertical2 = tk.Frame(tab_control)
        for cuenta in range(3):
            tk.Frame(vertical2, height=8, width=12).pack()
            tk.Button(vertical2, text=f"Boton {cuenta}").pack()

        panel = tk.Frame(tab_control)
        for cuenta in range(3):
            tk.Label(panel, text="").pack()
            tk.Button(panel, text=f"Boton {cuenta}").pack()

        tab_control.add(horizontal1, text="Cuadro horizontal")
        tab_control.add(vertical1, text="Cuadro vertical con montantes")
        tab_control.add(horizontal2, text="Cuadro horizontal con pegamento")
        tab_control.add(vertical2, text="Cuadro vertical con áreas rígidas")
        tab_control.add(panel, text="Cuadro vertical con pegamento")

        tab_control.pack(expand=1, fill="both")

if __name__ == "__main__":
    app = MarcoBoxLayout()
    app.mainloop()
