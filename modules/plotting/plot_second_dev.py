import sympy, numpy
from ..main_elements import *
from ..variables_constants import *
from ..data_calculation import points_ox_oy, find_inflection_points, find_convexity_intervals
# функція для побудови і виконання дослідження похідної у'' другого графіку функції / Function for constructing and analyzing the second derivative of the second graph function
def base_second_dev():
    from .plot_constant_function import plot_constant_function

    check = base_dev_checkbox2.get()  # Отримання значення чекбоксу / Getting the value of the checkbox

    base_second_dev = dictionary_of_variables['base_second_dev']  # Отримання графіку зі словника / Getting the plot from the dictionary
    base_second_ox = dictionary_of_variables['base_second_ox']  # Отримання графіку зі словника / Getting the plot from the dictionary
    base_second_lines = dictionary_of_variables['base_second_lines']  # Отримання графіку зі словника / Getting the plot from the dictionary
    base_second_inflection_points = dictionary_of_variables['base_second_inflection_points']  # Отримання графіку зі словника / Getting the plot from the dictionary

    if check == 1:  # Якщо чекбокс активований / If the checkbox is checked
        # Отримання значень функції інтерфейсу / Getting the values of parameters a and b from the interface
        function_text = input_graphic.get()

        if function_text.strip():  # Перевірка, чи існують значення інпуту / Checking if a and b values exist
            expr = sympy.sympify(function_text)
            x = sympy.symbols('x')  # Оголошення змінної x як символічної / Declaring x as a symbolic variable

            dev_of_function = sympy.diff(expr, x)  # Обчислення першої похідної функції / Calculating the first derivative of the function
            second_dev_of_function = sympy.diff(dev_of_function, x)  # Обчислення другої похідної функції / Calculating the second derivative of the function

            rounded_derivative = second_dev_of_function  
            for atom in second_dev_of_function.atoms():
                # Если атом является числом с плавающей точкой
                if atom.is_Float:
                    # Заменяем его на округлённое значение
                    rounded_derivative = rounded_derivative.xreplace({atom: round(atom, 2)})

            drob_second_dev_lable.configure(text=f"y'' = {rounded_derivative}")  # Оновлення тексту для другої похідної / Updating the text for the second derivative

            expr = second_dev_of_function  # Встановлення виразу для другої похідної / Setting the expression for the second derivative
            func = sympy.lambdify(x, expr, 'numpy')  # Перетворення виразу другої похідної у функцію для обчислень / Converting the second derivative expression to a function for calculations

            if isinstance(func, sympy.Number) or expr.is_constant():  # Якщо вираз є числом / If the expression is a number
                if expr.is_constant():  # Якщо вираз є числом
                    try:
                        base_second_dev = plot_constant_function(float(expr), 'blue')  # Побудова графіка для константи
                        dictionary_of_variables['base_second_dev'] = base_second_dev  # Збереження графіку другої похідної / Storing the second derivative graph

                    except ValueError:
                        print("Передано некоректне значення для константи")
                else:  # Якщо це не константа, обчислюємо другу похідну
                    x_values = numpy.linspace(-100, 100, num = 4000)
                    y_values = func(x_values)
                    second_derivative_values = numpy.gradient(numpy.gradient(y_values, x_values), x_values)
                    base_second_dev = ax.plot(x_values, second_derivative_values, color='blue', label='y'' = f''(x)')
                    dictionary_of_variables['base_second_dev'] = base_second_dev  # Збереження графіку другої похідної / Storing the second derivative graph


            else:

                # пошук і побудова точок перегину / Finding and plotting inflection points
                inflection_points = find_inflection_points(second_dev_of_function)  # Пошук точок перегину / Finding inflection points
                hover_points = []
                hover_annotations = []

                for point in inflection_points:
                    y_val = expr.subs(x, point)
                    scatter = ax.scatter(float(point), float(y_val), color='blue', zorder=5, picker=5)
                    base_second_inflection_points.append(scatter)
                    hover_points.append(scatter)

                    annotation = ax.annotate(f'({float(point):.2f}, {float(y_val):.2f})',
                                (float(point), float(y_val)),
                                textcoords="offset points",
                                xytext=(0, -15),
                                ha='center', color='blue',
                                visible=False)
                    hover_annotations.append(annotation)
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

                # оновлення лейблу з точками перегину / Updating the label with inflection points
                if inflection_points:
                    formatted_points = "; ".join([f"x{i+1} = {float(pt):.2f}" for i, pt in enumerate(inflection_points)])
                    inflection_points_label.configure(text=f"9) Точки перегину: {formatted_points}")  # Оновлення тексту мітки з точками перегину / Updating the text for the inflection points label
                else:
                    inflection_points_label.configure(text="9) Точки перегину: не існує")  # Виведення повідомлення про відсутність точок перегину / Displaying message about the absence of inflection points

                # Визначення діапазону значень x / Defining the range of x values
                x_vals = numpy.linspace(-100, 100, 4000)
                y_vals = func(x_vals)  # Обчислення значень y для відповідних x / Calculating y values for the corresponding x values

                # Побудова графіку другої похідної функції / Plotting the second derivative function graph
                base_second_dev = ax.plot(x_vals, y_vals, label=f"y'' = {rounded_derivative}", color='blue')

                # побудова точок 0х і пунктирних ліній / Plotting 0x points and dashed lines
                points_0x_0y = points_ox_oy(expr, 'blue', label=False, lines=True, include_oy=False)
                base_second_ox = points_0x_0y['0x']  # Точки 0х / Points on the x-axis
                base_second_lines = points_0x_0y['lines']  # Пунктирні лінії / Dashed lines

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
                convexity_intervals_label.configure(text = convexity_text, anchor="w", justify = "left")

                ax.legend()  # Виведення легенди на графіку / Displaying the legend on the graph
                legend = ax.legend()
                
                for text in legend.get_texts():
                    
                    text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
                canvas.draw()  # Оновлення графіку / Redrawing the canvas

                dictionary_of_variables['base_second_ox'] = base_second_ox  # Збереження точок перетину з віссю x / Storing intersection points with the x-axis
                dictionary_of_variables['base_second_lines'] = base_second_lines  # Збереження пунктирних ліній / Storing dashed lines
                dictionary_of_variables['base_second_dev'] = base_second_dev  # Збереження графіку другої похідної / Storing the second derivative graph
                dictionary_of_variables['base_second_inflection_points'] = base_second_inflection_points  # Збереження точок перегину / Storing inflection points
                dictionary_of_variables['inflection_points_label'] = inflection_points_label  # Збереження лейблу з точками перегину / Storing the label with inflection points

                # except Exception as e:
                #     print(f"Помилка другої дробової похідної: {e}")  # Виведення повідомлення про помилку другої дробової похідної / Displaying message about the second fractional derivative error

    elif check == 0 and base_second_dev:  # Якщо чекбокс вимкнений і графік існує у списку / If the checkbox is unchecked and the plot exists in the list
        # видалення графіка / Removing the plot
        if base_second_dev:
            for line in base_second_dev:
                line.remove()
            base_second_dev.clear()
            canvas.draw()

        # видалення точок 0х, пунктирних ліній і точок перегину / Removing 0x points, dashed lines, and inflection points
        if base_second_inflection_points:
            for point in base_second_inflection_points:
                point.remove()  # Видалення точок перегину / Removing inflection points
            base_second_inflection_points.clear()

        if base_second_ox:
            for point in base_second_ox:
                point.remove()  # Видалення точок перетину з віссю x / Removing intersection points with x-axis
            base_second_ox.clear()

        if base_second_lines:
            for line in base_second_lines:
                line.remove()  # Видалення горизонтальних ліній / Removing horizontal lines
            base_second_lines.clear()

        ax.legend().remove()  # Видалення легенди / Removing the legend
        ax.legend()  # Оновлення легенди / Updating the legend
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
        canvas.draw()  # Оновлення графіку / Redrawing the canvas