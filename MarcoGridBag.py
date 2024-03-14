import tkinter as tk
from tkinter import ttk

class MarcoGridBag(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("GridBagLayout")
        self.config(bg="white")  # Color de fondo blanco

        self.columnconfigure(0, weight=1)  # Columna 0 expandible
        self.columnconfigure(1, weight=1)  # Columna 1 expandible
        self.columnconfigure(2, weight=1)  # Columna 2 expandible
        self.columnconfigure(3, weight=1)  # Columna 3 expandible

        self.rowconfigure(0, weight=1)  # Fila 0 expandible
        self.rowconfigure(1, weight=1)  # Fila 1 expandible
        self.rowconfigure(2, weight=1)  # Fila 2 expandible
        self.rowconfigure(3, weight=1)  # Fila 3 expandible

        areaTexto1 = tk.Text(self, height=5, width=10)
        areaTexto1.insert(tk.END, "AreaTexto1")

        areaTexto2 = tk.Text(self, height=2, width=2)
        areaTexto2.insert(tk.END, "AreaTexto2")

        nombres = ["Hierro", "Acero", "Bronce"]
        cuadroComb = ttk.Combobox(self, values=nombres)

        campoTexto = tk.Entry(self, text="CampoTexto")

        boton1 = tk.Button(self, text="Boton 1")
        boton2 = tk.Button(self, text="Boton 2")
        boton3 = tk.Button(self, text="Boton 3")

        self.agregarComponente(areaTexto1, 0, 0, 1, 3)
        self.agregarComponente(boton1, 0, 1, 2, 1)
        self.agregarComponente(cuadroComb, 2, 1, 2, 1)
        self.agregarComponente(boton2, 1, 1, 1, 1)
        self.agregarComponente(boton3, 1, 2, 1, 1)
        self.agregarComponente(campoTexto, 3, 0, 2, 1)
        self.agregarComponente(areaTexto2, 3, 2, 1, 1)

    def agregarComponente(self, componente, fila, columna, anchura, altura):
        componente.grid(row=fila, column=columna, columnspan=anchura, rowspan=altura, sticky="nsew")

if __name__ == "__main__":
    app = MarcoGridBag()
    app.mainloop()
