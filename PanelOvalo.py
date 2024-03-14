import tkinter as tk
from tkinter import ttk

class PanelOvalo(tk.Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.diametro = 10
        self.create_oval(10, 10, self.diametro, self.diametro, fill='yellow')

    def establecer_diametro(self, nuevo_diametro):
        self.diametro = max(nuevo_diametro, 10)
        self.delete("all")
        self.create_oval(10, 10, self.diametro, self.diametro, fill='yellow')

class MarcoSlider(tk.Tk):
    def __init__(self):
        super().__init__()

        self.mi_panel = PanelOvalo(self, width=200, height=200)
        self.mi_panel.pack(pady=10)

        self.diametro_slider = ttk.Scale(
            self, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
            command=self.actualizar_diametro
        )
        self.diametro_slider.set(10)
        self.diametro_slider.pack(pady=10)

    def actualizar_diametro(self, valor):
        nuevo_diametro = int(float(valor))
        self.mi_panel.establecer_diametro(nuevo_diametro)

if __name__ == "__main__":
    app = MarcoSlider()
    app.title("Demostracion de Slider en Python")
    app.geometry("220x270")
    app.mainloop()
