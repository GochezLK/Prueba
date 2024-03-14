import tkinter as tk
from tkinter import ttk

class MarcoJTabbedPane(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Demo de JTabbedPane")
        self.geometry("400x300")

        panel_fichas = ttk.Notebook(self)

        etiqueta1 = tk.Label(panel_fichas, text="panel uno", justify=tk.CENTER)
        panel1 = tk.Frame(panel_fichas)
        panel1.pack(fill=tk.BOTH, expand=True)
        etiqueta1.pack(in_=panel1)
        panel_fichas.add(panel1, text="Ficha uno")

        etiqueta2 = tk.Label(panel_fichas, text="panel dos", justify=tk.CENTER)
        panel2 = tk.Frame(panel_fichas, background="yellow")
        panel2.pack(fill=tk.BOTH, expand=True)
        etiqueta2.pack(in_=panel2)
        panel_fichas.add(panel2, text="Ficha dos")

        etiqueta3 = tk.Label(panel_fichas, text="panel tres")
        panel3 = tk.Frame(panel_fichas)
        panel3.pack(fill=tk.BOTH, expand=True)
        tk.Button(panel3, text="Norte").pack(side=tk.TOP)
        tk.Button(panel3, text="Oeste").pack(side=tk.LEFT)
        tk.Button(panel3, text="Este").pack(side=tk.RIGHT)
        tk.Button(panel3, text="Sur").pack(side=tk.BOTTOM)
        etiqueta3.pack(in_=panel3)
        panel_fichas.add(panel3, text="Ficha tres")

        panel_fichas.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = MarcoJTabbedPane()
    app.mainloop()
