import tkinter as tk


class RootWindow:

    def __init__(self, title, geo):
        self._tk = tk.Tk()
        self._tk.title(title)
        self._tk.geometry(geo)

    def start(self):
        self._tk.mainloop()
