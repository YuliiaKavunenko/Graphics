import sympy, numpy
from ..main_elements import *
from ..variables_constants import *
from ..data_calculation import points_ox_oy, find_inflection_points, find_convexity_intervals
# Функція для побудови і виконання дослідження похідної у'' четвертого графіку функції / Function to construct and study the second derivative of the fourth graph of the function
def fourth_second_dev():
    from .plot_constant_function import plot_constant_function
    check = second_dev_fourth.get()  # Отримання значення перемикача для другого графіку / Getting the toggle value for the second graph
    plot_fourth_second = dictionary_of_variables['plot_fourth_second']  # Отримання графіку зі словника / Getting the plot from the dictionary
    inflection_points_fourth_scatter = dictionary_of_variables['inflection_points_fourth_scatter']  # Отримання точок перегину / Getting the inflection points
    ox_points_fourth_second = dictionary_of_variables['ox_points_fourth_second']  # Отримання точок перетину з віссю Ox / Getting the intersection points with the Ox axis
    h_lines_fourth_second = dictionary_of_variables['h_lines_fourth_second']  # Отримання горизонтальних ліній / Getting the horizontal lines
    inflection_points_l_3 = dictionary_of_variables['inflection_points_l_3']  # Отримання тексту для точок перегину / Getting text for inflection points
    

    if check == 1:  # Якщо перемикач увімкнено / If toggle is on
        a = a4_drob.get()  # Отримання значення дробового коефіцієнта / Getting the fractional coefficient

        if a:  # Якщо значення a не порожнє / If a is not empty
            inflection_points_l_3 = []  # Ініціалізація списку для точок перегину / Initializing list for inflection points
            # try:
            x = sympy.symbols('x')  # Оголошення символічної змінної x / Declaring symbolic variable x
            a = float(a)  # Перетворення значення a у числовий формат / Converting value a to numeric format

            function = x/(x**2+a)  # Визначення математичної функції / Defining the mathematical function

            dev_of_function = sympy.diff(function, x)  # Визначення першої похідної функції / Finding the first derivative of the function

            second_dev_of_function = sympy.diff(dev_of_function, x)  # Визначення другої похідної функції / Finding the second derivative of the function
            rounded_derivative = second_dev_of_function  
            for atom in second_dev_of_function.atoms():
                # Если атом является числом с плавающей точкой
                if atom.is_Float:
                    # Заменяем его на округлённое значение
                    rounded_derivative = rounded_derivative.xreplace({atom: round(atom, 2)})
            drob_second_dev_lable.configure(text = f"y'' = {rounded_derivative}")  # Оновлення тексту лейблу з другою похідною / Updating the label text with the second derivative

            expr = rounded_derivative  # Присвоєння виразу другої похідної змінній / Assigning the rounded second derivative expression to a variable
            
            func = sympy.lambdify(x, expr, 'numpy')  # Перетворення виразу у функцію для обчислення значень / Converting the expression to a function for computing values
            if isinstance(func, sympy.Number):  # Якщо вираз є числом / If the expression is a number
                plot_3 = plot_constant_function(float(func), 'blue')  # Побудова графіка для константи / Plotting the graph for the constant function
            else:
                x_vals = numpy.linspace(-20, 20, 400)  # Генерація значень x від -10 до 10 / Generating x values from -10 to 10
                y_vals = func(x_vals)  # Обчислення значень функції для заданих x / Computing function values for given x

                plot_fourth_second = ax.plot(x_vals, y_vals, label=f"y'' = {rounded_derivative}", color='blue')  # Побудова нового графіка другої похідної / Plotting the new second derivative graph
                # plots.append(plot)
                
                # Пошук точок перегину / Finding inflection points
                inflection_points = find_inflection_points(second_dev_of_function)  # Виклик функції для пошуку точок перегину / Calling the function to find inflection points
                hover_points = []
                hover_annotations = []

                for point in inflection_points:
                    y_val = function.subs(x, point)
                    scatter = ax.scatter(float(point), float(y_val), color='blue', zorder=5, picker=5)
                    inflection_points_fourth_scatter.append(scatter)
                    hover_points.append(scatter)

                    annotation = ax.annotate(
                        f'({float(point):.2f}, {float(y_val):.2f})',
                        (float(point), float(y_val)),
                        textcoords="offset points",
                        xytext=(0, -15),
                        ha='center',
                        color='blue',
                        visible=False
                    )
                    hover_annotations.append(annotation)
                    inflection_points_l_3.append(annotation)
                def on_hover(event):
                    if event.inaxes == ax:
                        for i, point in enumerate(hover_points):
                            cont, _ = point.contains(event)
                            if cont:
                                hover_annotations[i].set_visible(True)
                            else:
                                hover_annotations[i].set_visible(False)
                        canvas.draw_idle()

                canvas.mpl_connect('motion_notify_event', on_hover)

                # Пошук точок перетину з віссю Ox / Finding points of intersection with the Ox axis
                points_0x_0y = points_ox_oy(second_dev_of_function, 'blue', label=False, lines=True, include_oy=False)  # Виклик функції для пошуку точок перетину та горизонтальних ліній / Calling the function to find points of intersection and horizontal lines
                ox_points_fourth_second = points_0x_0y['0x']  # Отримання точок перетину з віссю Ox / Getting the points of intersection with the Ox axis
                h_lines_fourth_second = points_0x_0y['lines']  # Отримання горизонтальних ліній / Getting the horizontal lines

                # Оновлення лейблу з точками перегину / Updating the label with inflection points
                if inflection_points:
                    formatted_points = "; ".join([f"x{i+1} = {float(pt):.2f}" for i, pt in enumerate(inflection_points)])  # Форматування точок перегину для виводу / Formatting inflection points for display
                    inflection_points_label.configure(text=f"9) Точки перегину: {formatted_points}")  # Оновлення тексту лейблу / Updating the label text
                else:
                    inflection_points_label.configure(text="9) Точки перегину: не існує")  # Якщо точок перегину немає, оновлюємо лейбл відповідно / If no inflection points exist, update label accordingly
                # Знаходимо проміжки опуклості / Find the intervals of convexity
                convexity_intervals = find_convexity_intervals(expr)

                # Створюємо текст для лейблу / Create text for the label
                convexity_text = "10) Проміжки опуклості графіка:\n"  # "Intervals of graph convexity:\n"
                for interval, convexity in convexity_intervals:
                    left, right = interval
                    left = "-∞" if left == float('-inf') else f"{left:.2f}"
                    right = "+∞" if right == float('inf') else f"{right:.2f}"
                    convexity_text += f"{convexity} при x ∈ ({left}; {right})\n"  # "{convexity} at x ∈ ({left}; {right})\n"

                # Виводимо текст у лейбл / Output the text to the label
                convexity_intervals_label.configure(text=convexity_text, anchor="w", justify = "left")

                ax.legend()  # Додавання легенди до графіка / Adding legend to the graph
                legend = ax.legend()

                fourth_s_dev_label.configure(
                    text = f"y'' = {rounded_derivative}"  # Оновлення тексту лейблу з другою похідною / Updating the label text with the second derivative
                )

                # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
                for text in legend.get_texts():
                    
                    text.set_color('red')
                canvas.draw()  # Перемальовування графіка / Redrawing the canvas
                dictionary_of_variables['ox_points_fourth_second'] = ox_points_fourth_second  # Збереження точок перетину з віссю Ox / Storing intersection points with the Ox axis
                dictionary_of_variables['h_lines_fourth_second'] = h_lines_fourth_second  # Збереження горизонтальних ліній / Storing horizontal lines
                dictionary_of_variables['plot_fourth_second'] = plot_fourth_second  # Збереження графіку другої похідної / Storing the second derivative graph
                dictionary_of_variables['inflection_points_fourth_scatter'] = inflection_points_fourth_scatter  # Збереження точок перегину / Storing inflection points
                dictionary_of_variables['inflection_points_l_3'] = inflection_points_l_3  # Збереження тексту для точок перегину / Storing text for inflection points
                dictionary_of_variables['inflection_points_label'] = inflection_points_label  # Збереження лейблу з точками перегину / Storing the label with inflection points
    elif check == 0 and plot_fourth_second:
        # Видалення графіка / Removing the graph
        if plot_fourth_second:
            for line in plot_fourth_second:
                line.remove()
            plot_fourth_second.clear()
            canvas.draw()

        # Видалення точок, ліній і точок перегину / Removing points, lines, and inflection points
        if inflection_points_fourth_scatter:
            for point in inflection_points_fourth_scatter:
                point.remove()  # Видалення кожної точки перегину / Removing each inflection point
            inflection_points_fourth_scatter.clear()

        # Видалення підпису точок / Removing point labels
        for label in inflection_points_l_3:
            label.remove()  # Видалення кожного підпису / Removing each label
        inflection_points_l_3.clear()

        if ox_points_fourth_second:
            for point in ox_points_fourth_second:
                point.remove()  # Видалення кожної точки перетину / Removing each intersection point
            ox_points_fourth_second.clear()

        if h_lines_fourth_second:
            for line in h_lines_fourth_second:
                line.remove()  # Видалення кожної горизонтальної лінії / Removing each horizontal line
            h_lines_fourth_second.clear()

        ax.legend().remove()  # Видалення легенди / Removing the legend
        ax.legend()  # Оновлення легенди / Updating the legend
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
        canvas.draw()  # Перемальовування графіка / Redrawing the canvas