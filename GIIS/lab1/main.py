import tkinter as tk
from tkinter import messagebox

class GraphicalEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Графический редактор")
        
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        self.toolbar = tk.Frame(self.root)
        self.toolbar.pack()

        self.line_type = tk.StringVar()
        self.line_type.set("Окружность")

        self.line_menu = tk.OptionMenu(self.toolbar, self.line_type, "Окружность", "Эллипс", "Гипербола", "Парабола")
        self.line_menu.pack(side=tk.LEFT)

        self.draw_button = tk.Button(self.toolbar, text="Построить", command=self.draw_line)
        self.draw_button.pack(side=tk.LEFT)

        self.debug_mode = tk.BooleanVar()
        self.debug_checkbox = tk.Checkbutton(self.toolbar, text="Отладочный режим", variable=self.debug_mode)
        self.debug_checkbox.pack(side=tk.LEFT)

    def draw_line(self):
        line_type = self.line_type.get()
        if line_type == "Окружность":
            self.canvas.create_oval(100, 100, 300, 300)
        elif line_type == "Эллипс":
            self.canvas.create_oval(100, 100, 300, 200)
        elif line_type == "Гипербола":
            self.canvas.create_line(100, 100, 300, 300)
            self.canvas.create_line(100, 300, 300, 100)
        elif line_type == "Парабола":
            self.canvas.create_line(100, 300, 200, 200, 300, 300)

        if self.debug_mode.get():
            self.show_debug_info()

    def show_debug_info(self):
        debug_window = tk.Toplevel(self.root)
        debug_window.title("Отладочный режим")

        debug_canvas = tk.Canvas(debug_window, width=800, height=600)
        debug_canvas.pack()

        # Ваш код для отображения пошагового решения на дискретной сетке

root = tk.Tk()
app = GraphicalEditor(root)
root.mainloop()