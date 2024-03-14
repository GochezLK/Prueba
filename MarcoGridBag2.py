import tkinter as tk
from tkinter import ttk

class MarcoGridBag2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GridBagLayout")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        metales = ["Cobre", "Aluminio", "Plata"]
        cuadro_comb = ttk.Combobox(self, values=metales)
        cuadro_comb.set(metales[0])

        campo_texto = tk.Entry(self, text="CampoTexto")

        fuentes = ["Serif", "Monospaced"]
        lista = tk.Listbox(self)
        for fuente in fuentes:
            lista.insert(tk.END, fuente)

        nombres = ["cero", "uno", "dos", "tres", "cuatro"]
        botones = [tk.Button(self, text=nombre) for nombre in nombres]

        self.agregar_componente(campo_texto, 0, 0, 2)
        self.agregar_componente(botones[0], 1, 0, 1)
        self.agregar_componente(botones[1], 1, 1, 1)
        self.agregar_componente(botones[2], 1, 2, 1)
        self.agregar_componente(cuadro_comb, 2, 0, 3)
        self.agregar_componente(botones[3], 3, 0, 1)
        self.agregar_componente(botones[4], 3, 1, 1)
        self.agregar_componente(lista, 3, 2, 1)

    def agregar_componente(self, componente, fila, columna, columna_span):
        componente.grid(row=fila, column=columna, columnspan=columna_span, sticky='nsew')

if __name__ == "__main__":
    app = MarcoGridBag2()
    app.mainloop()
