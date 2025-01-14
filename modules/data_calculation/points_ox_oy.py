import numpy, sympy
from ..main_elements import canvas, ax
# Функція для знаходження точок перетину з вісю 0х і 0у, нулів функції / Function for finding intersections with the Ox and Oy axes, zeros of the function
def points_ox_oy(graphic, color, label=False, lines=False, include_oy=True):
    x = sympy.symbols('x')  # Оголошення символічної змінної x / Declaring symbolic variable x

    # Знаходимо точку перетину з віссю 0y (x = 0) / Find the intersection with the Oy axis (x = 0)
    y_intercept = graphic.subs(x, 0)  # функція subs підставляє в рівняння замість x - 0 / The subs function substitutes 0 for x in the equation

    # Знаходимо точки перетину з віссю 0x (y = 0) / Find intersections with the Ox axis (y = 0)
    x_intercepts = sympy.solve(graphic, x)  # Розв'язуємо рівняння для знаходження коренів / Solve the equation to find roots
    print('Hi', x_intercepts)
    # Відфільтровуємо тільки дійсні корені та не округлюємо їх передчасно / Filter only real roots and avoid premature rounding
    x_intercepts = [root.evalf() for root in x_intercepts if root.is_real and not root.has(sympy.I)]
    print('Hi', x_intercepts)
    # x_int = []
    # for root in x_intercepts:
    #     if root.is_real and root.has(sympy.I):
    #         x_int.append(root.evalf())
    # print()
    # print('Hi', x_int)

    # Округляємо тільки після перевірки, що це дійсне число / Round only after confirming it is a real number
    # x_intercepts = x_int
    x_intercepts = [round(float(root), 1) for root in x_intercepts]  # Округлення коренів / Rounding the roots

    points_zero = []  # Нулі функції / Zeros of the function
    ox_points = []  # Точки перетину з віссю Ox / Intersection points with the Ox axis
    dashed_lines = []  # Пунктирні лінії / Dashed lines

    if x_intercepts:  # Якщо знайдено точки перетину / If intersection points are found
        for x_cor in x_intercepts:
            # Точка перетину з віссю Ox / Intersection point with the Ox axis
            point = ax.scatter(x_cor, 0, color=color, s=40)  # Додавання точки на графік / Adding the point to the graph
            ox_points.append(point)  # Збереження точки / Storing the point
            points_zero.append(x_cor)  # Збереження значення x для нуля функції / Storing x value for the zero of the function

            # Підпис точки / Label the point
            if label != False:
                ax.annotate(f'({x_cor:.2f}, 0)',
                            (x_cor, 0),
                            textcoords="offset points",
                            xytext=(10, 10),
                            ha='center')  # Додавання підпису до точки / Adding a label to the point
            if lines:  # Пунктирні лінії / Dashed lines
                line = ax.axvline(x=x_cor, color=color, linestyle='--', linewidth=1)  # Додавання пунктирної лінії на графік / Adding a dashed line to the graph
                dashed_lines.append(line)  # Збереження лінії / Storing the line

    oy_point = None  # Початкове значення для точки перетину з Oy / Initial value for Oy intersection point
    if include_oy and y_intercept.is_real:  # Якщо включено Oy і y є дійсним числом / If Oy is included and y is a real number
        y_cor = round(float(y_intercept), 2)  # Округлення значення y / Rounding the y value
        oy_point = ax.scatter(0, y_cor, color=color, s=40)  # Додавання точки на Oy / Adding the point on Oy
        if label:  # Якщо потрібно додати підпис / If label is needed
            ax.annotate(f'(0, {y_cor})',
                        (0, y_cor),
                        textcoords="offset points",
                        xytext=(10, 10),
                        ha='center')  # Додавання підпису до точки на Oy / Adding a label to the Oy point

    canvas.draw()  # Оновлення графіка / Updating the canvas

    return {
        '0y': oy_point,  # Точка перетину з Oy / Oy intersection point
        '0x': ox_points,  # Точки перетину з Ox / Ox intersection points
        'points_zero': points_zero,  # Нулі функції / Zeros of the function
        'lines': dashed_lines  # Пунктирні лінії для наглядного розуміння локал макс. і локал мін. + друга похідна - точка перегину / Dashed lines for better understanding of local
    }