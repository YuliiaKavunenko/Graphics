import sympy, numpy
from ..main_elements import *
from ..variables_constants import *
from ..data_calculation import points_ox_oy, find_inflection_points, find_convexity_intervals
from .plot_constant_function import plot_constant_function
# функція для побудови і виконання дослідження похідної у'' другого графіку функції / Function for constructing and analyzing the second derivative of the second graph function
def sixth_second_dev():
    check = second_dev_sixth.get()  # Отримання значення чекбоксу / Getting the value of the checkbox
    plot_sixth_second = dictionary_of_variables['plot_sixth_second']  # Отримання графіку зі словника / Getting the plot from the dictionary
    ox_points_second_6 = dictionary_of_variables['ox_points_second_6']  # Отримання точок перетину з віссю x / Getting the intersection points with the x-axis
    h_lines_second_6 = dictionary_of_variables['h_lines_second_6']  # Отримання пунктирних ліній / Getting the dashed lines
    inflection_points_scatter_6 = dictionary_of_variables['inflection_points_scatter_6']  # Отримання точок перегину / Getting the inflection points
    inflection_points_label_6 = dictionary_of_variables['inflection_points_label_6']  # Отримання лейблу з точками перегину / Getting the label with inflection points

    if check == 1:  # Якщо чекбокс активований / If the checkbox is checked
        print('чекбокс 2 пятой функции oN')
        a1 = a1_sixth.get()
        a2 = a2_sixth.get()

        if a1 and a2:  # Перевірка, чи існують значення a і b / Checking if a and b values exist
            x = sympy.symbols('x')  # Оголошення змінної x як символічної / Declaring x as a symbolic variable
            a1 = float(a1)  # Перетворення a у число з плаваючою крапкою / Converting a to a float
            a2 = float(a2)  # Перетворення b у число з плаваючою крапкою / Converting b to a float

            function = (a1/x**2) + (x/a2) # Визначення виразу функції / Defining the function expression
            dev_of_function = sympy.diff(function, x)  # Обчислення першої похідної функції / Calculating the first derivative of the function
            second_dev_of_function = sympy.diff(dev_of_function, x)  # Обчислення другої похідної функції / Calculating the second derivative of the function

            sixth_s_dev_label.configure(text=f"y'' = {second_dev_of_function}")  # Оновлення тексту для другої похідної / Updating the text for the second derivative

            expr = second_dev_of_function  # Встановлення виразу для другої похідної / Setting the expression for the second derivative
            func = sympy.lambdify(x, expr, 'numpy')  # Перетворення виразу другої похідної у функцію для обчислень / Converting the second derivative expression to a function for calculations
            if isinstance(func, sympy.Number):  # Якщо вираз є числом / If the expression is a number
                plot_3 = plot_constant_function(float(func), 'blue')  # Побудова графіка для константи / Plotting the graph for the constant function
            else:
                # пошук і побудова точок перегину / Finding and plotting inflection points
                inflection_points = find_inflection_points(second_dev_of_function)  # Пошук точок перегину / Finding inflection points
                for point in inflection_points:
                    if sympy.im(point) == 0:  # Тільки дійсні точки
                        y_val = function.subs(x, point)
                        scatter = ax.scatter(float(point), float(y_val), color='blue', zorder=6)
                        inflection_points_scatter_6.append(scatter)

                        inflection_label_6 = ax.annotate(f'({float(point):.2f}, {float(y_val):.2f})',
                                    (float(point), float(y_val)),
                                    textcoords="offset points",
                                    xytext=(0, 10),
                                    ha='center', color='blue')
                        inflection_points_label_6.append(inflection_label_6)

                # оновлення лейблу з точками перегину / Updating the label with inflection points
                if inflection_points:
                    if sympy.im(point) == 0:  # Тільки дійсні точки
                        formatted_points = "; ".join([f"x{i+1} = {float(pt):.2f}" for i, pt in enumerate(inflection_points)])
                        inflection_points_label.configure(text=f"9) Точки перегину: {formatted_points}")  # Оновлення тексту мітки з точками перегину / Updating the text for the inflection points label
                else:
                    inflection_points_label.configure(text="9) Точки перегину: не існує")  # Виведення повідомлення про відсутність точок перегину / Displaying message about the absence of inflection points

                # Визначення діапазону значень x / Defining the range of x values
                x_vals = numpy.linspace(-10, 10, 400)
                y_vals = func(x_vals)  # Обчислення значень y для відповідних x / Calculating y values for the corresponding x values

                # Побудова графіку другої похідної функції / Plotting the second derivative function graph
                plot_sixth_second = ax.plot(x_vals, y_vals, label=f"y'' = {second_dev_of_function}", color='blue')
                # plots_2d.append(plot_3_2)  # Додавання графіку до списку графіків / Adding the plot to the list of plots

                # побудова точок 0х і пунктирних ліній / Plotting 0x points and dashed lines
                points_0x_0y = points_ox_oy(expr, 'blue', label=False, lines=True, include_oy=False)
                ox_points_second_6 = points_0x_0y['0x']  # Точки 0х / Points on the x-axis
                h_lines_second_6 = points_0x_0y['lines']  # Пунктирні лінії / Dashed lines
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

                ax.legend()  # Виведення легенди на графіку / Displaying the legend on the graph
                legend = ax.legend()
                
                for text in legend.get_texts():
                    text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
                canvas.draw()  # Оновлення графіку / Redrawing the canvas

                dictionary_of_variables['ox_points_second_6'] = ox_points_second_6  # Збереження точок перетину з віссю x / Storing intersection points with the x-axis
                dictionary_of_variables['h_lines_second_6'] = h_lines_second_6  # Збереження пунктирних ліній / Storing dashed lines
                dictionary_of_variables['plot_sixth_second'] = plot_sixth_second  # Збереження графіку другої похідної / Storing the second derivative graph
                dictionary_of_variables['inflection_points_scatter_6'] = inflection_points_scatter_6  # Збереження точок перегину / Storing inflection points
                dictionary_of_variables['inflection_points_label_6'] = inflection_points_label_6  # Збереження лейблу з точками перегину / Storing the label with inflection points

                # except Exception as e:
                #     print(f"Помилка другої дробової похідної: {e}")  # Виведення повідомлення про помилку другої дробової похідної / Displaying message about the second fractional derivative error

    elif check == 0:  # Якщо чекбокс вимкнений і графік існує у списку / If the checkbox is unchecked and the plot exists in the list
        # видалення графіка / Removing the plot
        print('чекбокс 2 пятой функции off')
        # Видалення графіка / Removing the graph
        if plot_sixth_second:
            for line in plot_sixth_second:
                line.remove()
            plot_sixth_second.clear()
            canvas.draw()
        # plot_3_2.remove()
        # plots_2d.remove(plot_3_2)

        # видалення точок 0х, пунктирних ліній і точок перегину / Removing 0x points, dashed lines, and inflection points
        if inflection_points_scatter_6:
            for point in inflection_points_scatter_6:
                point.remove()  # Видалення точок перегину / Removing inflection points
            inflection_points_scatter_6.clear()

        if ox_points_second_6:
            for point in ox_points_second_6:
                point.remove()  # Видалення точок перетину з віссю x / Removing intersection points with x-axis
            ox_points_second_6.clear()

        if h_lines_second_6:
            for line in h_lines_second_6:
                line.remove()  # Видалення горизонтальних ліній / Removing horizontal lines
            h_lines_second_6.clear()

        ax.legend().remove()  # Видалення легенди / Removing the legend
        ax.legend()  # Оновлення легенди / Updating the legend
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
        canvas.draw()  # Оновлення графіку / Redrawing the canvas
    print(f'check = {check}')