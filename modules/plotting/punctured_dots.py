import sympy
from ..main_elements import *

# Функція для знаходження і побудови асимптот та виколотих точок / Function for finding and plotting asymptotes and punctured points
def punctured_dots(function):
    points = []
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
    # Для уникнення дублікатів у легенді створимо множину / To avoid duplicates in the legend, use a set
    added_labels = set()

    for point in punctured_points:
        if point.is_finite:  # Перевіряємо, чи точка є скінченною / Check if the point is finite
            label = f'вертикальна асимптота: x = {str(point)[0:4]}'  # Текст для мітки / Label text
            if label not in added_labels:  # Додаємо мітку тільки один раз / Add label only once
                ax.axvline(x=point, color='black', linestyle='--', linewidth=2, label=label)  # Вертикальна лінія з міткою
                added_labels.add(label)  # Зберігаємо додану мітку / Save the added label
            else:
                ax.axvline(x=point, color='black', linestyle='--', linewidth=2)  # Вертикальна лінія без мітки

            y_value = float(function.subs(x, float(point) + 0.01))  # Обчислення значення функції поблизу виколотої точки / Compute the function value near the punctured point

            # Округлення для підпису / Rounding for label
            point_rounded = round(point)  # Округлення координати x / Rounding x coordinate
            y_value_rounded = round(y_value)  # Округлення значення y / Rounding y value

            ax.scatter(point, y_value, facecolors='none', edgecolors='black', s=50)  # Кружечок без заливки / Circle without fill
            ax.annotate(f'({point_rounded}, {y_value_rounded})',
                        (point, y_value),
                        textcoords="offset points",
                        xytext=(10, 10),
                        ha='center')  # Додавання підпису до виколотої точки / Adding a label to the punctured point
            points.append(point)

            
    legend = ax.legend()            
    for text in legend.get_texts():
                text.set_color('red')  # встановлюємо червоний колір тексту легенди / setting the legend text color to red
    canvas.draw()  # Оновлення графіка / Updating the canvas
    return points