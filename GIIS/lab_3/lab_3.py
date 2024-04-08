
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CurveEditor:
    def __init__(self, root):
        self.control_points = []
        self.curve_points = []
        self.method = None
        
        self.root = root
        self.root.title("Curve Editor")
        
        self.canvas = None
        self.figure = plt.figure()
        
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        self.curves_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Curves", menu=self.curves_menu)
        self.curves_menu.add_command(label="Hermite", command=self.set_method_hermite)
        self.curves_menu.add_command(label="Bezier", command=self.set_method_bezier)
        self.curves_menu.add_command(label="B-spline", command=self.set_method_bspline)
        
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(side=tk.TOP)
        
        self.add_button = tk.Button(self.control_frame, text="Add Control Point", command=self.add_control_point)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.delete_button = tk.Button(self.control_frame, text="Delete Control Point", command=self.delete_control_point)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.edit_button = tk.Button(self.control_frame, text="Edit Control Point", command=self.edit_control_point)
        self.edit_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.plot_button = tk.Button(self.control_frame, text="Plot Curve", command=self.plot_curve)
        self.plot_button.pack(side=tk.LEFT, padx=5, pady=5)
        
    def set_method_hermite(self):
        self.method = "Hermite"
        
    def set_method_bezier(self):
        self.method = "Bezier"
        
    def set_method_bspline(self):
        self.method = "BSpline"
        
    def add_control_point(self):
        x = float(self.x_entry.get())
        y = float(self.y_entry.get())
        self.control_points.append((x, y))
        
    def delete_control_point(self):
        index = self.control_listbox.curselection()[0]
        del self.control_points[index]
        self.control_listbox.delete(index)
        
    def edit_control_point(self):
        index = self.control_listbox.curselection()[0]
        x = float(self.x_entry.get())
        y = float(self.y_entry.get())
        self.control_points[index] = (x, y)
        self.control_listbox.delete(index)
        self.control_listbox.insert(index, f"({x}, {y})")
        
    def compute_curve(self):
        if self.method == "Hermite":
            self.curve_points = self.compute_hermite_curve()
        elif self.method == "Bezier":
            self.curve_points = self.compute_bezier_curve()
        elif self.method == "BSpline":
            self.curve_points = self.compute_bspline_curve()
        
    def compute_hermite_curve(self):
        # Implement Hermite curve computation
        pass
    
    def compute_bezier_curve(self):
        # Implement Bezier curve computation
        pass
    
    def compute_bspline_curve(self):
        # Implement B-spline curve computation
        pass
    
    def plot_curve(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.scatter(*zip(*self.control_points), color='red', label='Control Points')
        ax.plot(*zip(*self.curve_points), color='blue', label='Curve')
        ax.legend()
        
        if self.canvas:
            self.canvas.get_tk_widget().pack_forget()
        
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.canvas.draw()
        
        self.compute_curve()
 

    def run(self):
        self.x_label = tk.Label(self.control_frame, text="X:")
        self.x_label.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.x_entry = tk.Entry(self.control_frame)
        self.x_entry.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.y_label = tk.Label(self.control_frame, text="Y:")
        self.y_label.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.y_entry = tk.Entry(self.control_frame)
        self.y_entry.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.control_listbox = tk.Listbox(self.root)
        self.control_listbox.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.root.mainloop()

# Example usage
root = tk.Tk()
editor = CurveEditor(root)
editor.run()