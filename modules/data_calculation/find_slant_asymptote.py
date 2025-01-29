import sympy, numpy
from ..main_elements import canvas, ax

# Функція для знаходження і побудови похилої асимптоти / Function to find and plot the slant asymptote
def find_and_plot_slant_asymptote(expr, x_symbol, label_widget = None):
    
    try:
        # Визначаємо k як границю f(x)/x при x -> ±∞ / Determine k as the limit of f(x)/x as x -> ±∞
        k = sympy.limit(expr / x_symbol, x_symbol, sympy.oo)

        # Перевіряємо, чи k є числом / Check if k is a number
        if not k.is_real:  # Якщо k не є числом / If k is not a number
            if label_widget:
                label_widget.configure(text="11) Похила асимптота: не існує")  # Оновлюємо текст лейблу / Update the label text
            return

        # Визначаємо b як границю f(x) - kx при x -> ±∞ / Determine b as the limit of f(x) - kx as x -> ±∞
        b = sympy.limit(expr - k * x_symbol, x_symbol, sympy.oo)

        # Перевіряємо, чи b є числом / Check if b is a number
        if not b.is_real:  # Якщо b не є числом / If b is not a number
            if label_widget:
                label_widget.configure(text="11) Похила асимптота: не існує")  # Оновлюємо текст лейблу / Update the label text
            return

        # Формуємо рівняння асимптоти / Form the equation of the asymptote
        asymptote_expr = k * x_symbol + b
        asymptote_func = sympy.lambdify(x_symbol, asymptote_expr, 'numpy')

        # Будуємо асимптоту / Plot the asymptote
        x_vals = numpy.linspace(-100, 100, 4000)  # Генеруємо значення x від -10 до 10 / Generate x values from -10 to 10
        y_vals = asymptote_func(x_vals)  # Обчислюємо значення y для асимптоти / Compute the y values for the asymptote

        ax.plot(x_vals, y_vals, linestyle='--', color='brown', label=f"y = {k:.2f}x + {b:.2f}")  # Додаємо асимптоту на графік / Add the asymptote to the graph

        # Додаємо текст рівняння в лейбл / Add the equation text to the label
        if label_widget:
            label_widget.configure(text=f"11) Похила асимптота: y = {k:.2f}x + {b:.2f}")  # Оновлюємо текст лейблу / Update the label text

        # Оновлюємо легенду / Update the legend
        ax.legend()  # Додаємо легенду до графіка / Add the legend to the graph
        canvas.draw()  # Оновлюємо графік / Update the canvas

    except Exception as e:
        print(f"Помилка: {e}")  # Виведення повідомлення про помилку / Print the error message
        if label_widget:
            label_widget.configure(text="11) Похилої асимптоти не існує")  # Оновлюємо текст лейблу при помилці / Update the label text on error