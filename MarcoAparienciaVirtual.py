import tkinter as tk
from tkinter import ttk

class MarcoAparienciaVisual(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Demo de apariencia visual")

        self.cadenas = ["Metal", "Motif", "Windows"]
        self.apariencias = ttk.Combobox(self, values=self.cadenas)
        self.apariencias.set("Metal")
        self.apariencias.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        self.opcion = [ttk.Radiobutton(self, text=cadena) for cadena in self.cadenas]
        self.grupo = tk.StringVar()

        for i, opcion in enumerate(self.opcion):
            opcion["variable"] = self.grupo
            opcion["value"] = str(i)
            opcion.grid(row=1, column=i, sticky="ew")

        self.etiqueta = ttk.Label(self, text="Esta es una apariencia visual metálica", anchor="center")
        self.etiqueta.grid(row=2, column=0, columnspan=len(self.cadenas), pady=5)

        self.boton = ttk.Button(self, text="JButton")
        self.boton.grid(row=3, column=0, columnspan=len(self.cadenas), pady=5)

        self.apariencias.bind("<<ComboboxSelected>>", self.cambiar_apariencia_visual)
        self.grupo.trace_add("write", self.cambiar_apariencia_radiobutton)

        self.cambiar_apariencia_visual()

    def cambiar_apariencia_visual(self, event=None):
        valor = self.cadenas.index(self.apariencias.get())
        self.grupo.set(str(valor))
        self.cambiar_apariencia_radiobutton()

    def cambiar_apariencia_radiobutton(self, *args):
        valor = int(self.grupo.get())
        self.etiqueta["text"] = f"Esta es una apariencia visual {self.cadenas[valor]}"

if __name__ == "__main__":
    app = MarcoAparienciaVisual()
    app.mainloop()
