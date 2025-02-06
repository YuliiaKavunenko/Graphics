import sympy
import matplotlib.pyplot as plt

'''
    Функція знаходить і будує горизонтальні асимптоти для заданої функції.
'''

def plot_horizontal_asymptotes(expr, color='orange', linestyle='--'):
    from ..main_elements import canvas

    # Символ змінної x / Symbol for the variable x
    x = sympy.symbols('x')

    # Ліміти при x -> +∞ / Limit as x -> +∞
    lim_pos_inf = sympy.limit(expr, x, sympy.oo)
    # Ліміти при x -> -∞ / Limit as x -> -∞
    lim_neg_inf = sympy.limit(expr, x, -sympy.oo)

    # Побудова горизонтальної асимптоти при x -> +∞, якщо вона існує
    # Plot horizontal asymptote as x -> +∞ if it exists
    if lim_pos_inf.is_real:
        plt.axhline(float(lim_pos_inf), color = color, linestyle = linestyle, linewidth = 2,label = f"Асимптота при x → +∞: y = {lim_pos_inf}")

    # Побудова горизонтальної асимптоти при x -> -∞, якщо вона існує
    # Plot horizontal asymptote as x -> -∞ if it exists
    if lim_neg_inf.is_real:
        plt.axhline(float(lim_neg_inf), color = color, linestyle = linestyle, linewidth = 2, label = f"Асимптота при x → -∞: y = {lim_neg_inf}")

    canvas.draw()
