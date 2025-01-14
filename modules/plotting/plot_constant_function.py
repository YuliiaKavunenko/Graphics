import sympy, numpy
from ..main_elements import *
plots = []

# функція для побудови функцій-констант / function for constructing constant functions
def plot_constant_function(a, color):
    # створення значень x в діапазоні від -10 до 10 / creating x values in the range from -10 to 10
    x_vals = numpy.linspace(-10, 10, 400)
    # створення значень y, які дорівнюють a для кожного значення x / creating y values equal to a for each x value
    y_vals = [a] * len(x_vals)
    # побудова графіка константної функції / plotting the constant function
    plot_const, = ax.plot(x_vals, y_vals, label=f'y = {a}', color=color)
    plots.append(plot_const)  # додавання графіка до списку / adding the plot to the list
    # додаємо легенду / adding the legend
    ax.legend()
    legend = ax.legend()
    for text in legend.get_texts():
        text.set_color('red')  # встановлюємо червоний колір тексту легенди / setting the legend text color to red
    canvas.draw()  # перерисовуємо холст / redrawing the canvas