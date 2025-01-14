import matplotlib.pyplot as plot
# імпортуємо модуль для відображення графіків у вікні Tkinter / Importing module for displaying graphs in the Tkinter window
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from .windows import main
# створення фігури і осей ох, оу / creating the figure and axes ox, oy
fig, ax = plot.subplots(figsize=(6, 6), facecolor='white')
# Створення холста на головному вікні для розміщення побудови графіків / creating the canvas on the main window for displaying the graphs
canvas = FigureCanvasTkAgg(figure = fig, master = main)