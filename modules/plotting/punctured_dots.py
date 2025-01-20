import sympy
from ..main_elements import *
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, limit, oo, sympify

# Функція для знаходження і побудови асимптот та виколотих точок / Function for finding and plotting asymptotes and punctured points
def punctured_dots(function):
    x = sympy.symbols('x')  # Оголошення символічної змінної x / Declaring symbolic variable x

    # Отримуємо область визначення функції / Getting the domain of the function
    domain = sympy.calculus.util.continuous_domain(function, x, sympy.S.Reals)

    # Перевіряємо, чи є розриви в області визначення (об'єднання інтервалів) / Checking for discontinuities in the domain (union of intervals)
    punctured_points = []  # Список для збереження виколотих точок / List to store punctured points

    if isinstance(domain, sympy.Union):  # Якщо область визначення є об'єднанням інтервалів / If the domain is a union of intervals
        for interval in domain.args:  # Проходимо по кожному інтервалу / Iterating over each interval
            if isinstance(interval, sympy.Interval):  # Якщо це інтервал / If it is an interval
                # Якщо інтервал не включає кінцеву точку (виколота точка) / If the interval does not include an endpoint (punctured point)
                if interval.left_open:
                    punctured_points.append(interval.start)  # Ліва точка інтервалу є виколотою / Left endpoint is punctured
                if interval.right_open:
                    punctured_points.append(interval.end)  # Права точка інтервалу є виколотою / Right endpoint is punctured

    # Будуємо вертикальні пунктирні лінії для виколотих точок і кружечки без заливки / Plot vertical dashed lines for punctured points and circles without fill
    for point in punctured_points:
        if point.is_finite:  # Перевіряємо, чи точка є скінченною / Check if the point is finite
            ax.axvline(x=point, color='black', linestyle='--', linewidth=2)  # Вертикальна лінія / Vertical line

            y_value = float(function.subs(x, float(point) + 0.01))  # Обчислення значення функції поблизу виколотої точки / Compute the function value near the punctured point

            # Округлення для підпису / Rounding for label

            point_rounded = round(point)  # Округлення координати x / Rounding x coordinate
            y_value_rounded = round(y_value)  # Округлення значення y / Rounding y value

            ax.scatter(point, y_value, facecolors='none', edgecolors='black', s = 40)  # Кружечок без заливки / Circle without fill
            ax.annotate(f'({point_rounded}, {y_value_rounded})',
                        (point, y_value),
                        textcoords="offset points",
                        xytext=(10, 10),
                        ha='center')  # Додавання підпису до виколотої точки / Adding a label to the punctured point
    canvas.draw()  # Оновлення графіка / Updating the canvas


def plot_function_with_asymptotes(func_str, x_range=(-10, 10), num_points=1000):
    """
    Построение графика функции с горизонтальными асимптотами, если они существуют.
    
    :param func_str: Строка с математической функцией, например "x / (x + 1)".
    :param x_range: Диапазон значений по оси X (tuple).
    :param num_points: Количество точек для построения графика.
    """
    # Объявляем переменную x для sympy
    x = symbols('x')
    
    # Преобразуем строку в sympy-выражение
    func = sympify(func_str)
    
    # Проверяем горизонтальные асимптоты
    left_limit = limit(func, x, -oo)
    right_limit = limit(func, x, oo)
    
    # Генерируем данные для построения графика функции
    x_vals = np.linspace(x_range[0], x_range[1], num_points)
    y_vals = [float(func.subs(x, val)) if func.subs(x, val).is_real else np.nan for val in x_vals]
    
    # Построение графика функции
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {func_str}', color='blue')
    
    # Добавляем горизонтальные асимптоты, если они существуют
    if left_limit.is_finite:
        plt.axhline(y=float(left_limit), color='brown', linestyle='--', label=f'Asymptote y = {left_limit}')
    if right_limit.is_finite and right_limit != left_limit:
        plt.axhline(y=float(right_limit), color='brown', linestyle='--', label=f'Asymptote y = {right_limit}')
    
    # Настройки графика
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.title('Function with Horizontal Asymptotes')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()
    plt.show()

# plot_function_with_asymptotes("x / (x + 1)")
