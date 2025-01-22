import sympy, numpy
from ..main_elements import *
from ..variables_constants import *
from ..data_calculation import points_ox_oy, find_inflection_points, find_convexity_intervals
# функція для побудови і виконання дослідження похідної у'' першого графіку функції / Function for constructing and analyzing the second derivative of the first graph function
def third_second_dev():
    from .plot_constant_function import plot_constant_function
    check = second_dev_sdrob.get()  # Отримання значення чекбоксу / Getting the value of the checkbox
    plot_third_second = dictionary_of_variables['plot_third_second']  # Отримання графіку зі словника / Getting the plot from the dictionary
    inflection_points_third_scatter = dictionary_of_variables['inflection_points_third_scatter']  # Отримання точок перегину / Getting the inflection points
    ox_points_third_second = dictionary_of_variables['ox_points_third_second']  # Отримання точок перетину з віссю x / Getting the intersection points with the x-axis
    h_lines_third_second = dictionary_of_variables['h_lines_third_second']  # Отримання пунктирних ліній / Getting the dashed lines
    inflection_points_th = []  # Ініціалізація списку точок перегину / Initializing the list of inflection points

    if check == 1:  # Якщо чекбокс активований / If the checkbox is checked
       
        a = a_th_drob.get()  # Отримання значення параметра a з інтерфейсу / Getting the value of parameter a from the interface
        if a:  # Перевірка, чи існує значення a / Checking if a value exists
            x = sympy.symbols('x')  # Оголошення змінної x як символічної / Declaring x as a symbolic variable
            a = float(a)  # Перетворення a у число з плаваючою крапкою / Converting a to a float

            function = (x**2 - a**2) / x  # Визначення виразу функції / Defining the function expression
            dev_of_function = sympy.diff(function, x)  # Обчислення першої похідної функції / Calculating the first derivative of the function
            second_dev_of_function = sympy.diff(dev_of_function, x)  # Обчислення другої похідної функції / Calculating the second derivative of the function
            print(second_dev_of_function)  # Виведення другої похідної у консоль / Printing the second derivative in the console

            drob_second_dev_lable.configure(text=f"y'' = {second_dev_of_function}")  # Оновлення тексту для другої похідної / Updating the text for the second derivative

            expr = second_dev_of_function  # Встановлення виразу для другої похідної / Setting the expression for the second derivative
            func = sympy.lambdify(x, expr, 'numpy')  # Перетворення виразу другої похідної у функцію для обчислень / Converting the second derivative expression to a function for calculations
            if isinstance(func, sympy.Number):  # Якщо вираз є числом / If the expression is a number
                plot_3 = plot_constant_function(float(func), 'blue')  # Побудова графіка для константи / Plotting the graph for the constant function
            else:
                # Визначення діапазону значень x / Defining the range of x values
                x_vals = numpy.linspace(-10, 10, 400)
                y_vals = func(x_vals)  # Обчислення значень y для відповідних x / Calculating y values for the corresponding x values

                # Побудова графіку другої похідної / Plotting the second derivative graph
                plot_third_second = ax.plot(x_vals, y_vals, label=f"y'' = {second_dev_of_function}", color='blue')

                # пошук точок перегину / Finding inflection points
                inflection_points = find_inflection_points(second_dev_of_function)
                for point in inflection_points:
                    y_val = function.subs(x, point)  # Обчислення значення функції в точці перегину / Calculating the function value at the inflection point
                    scatter = ax.scatter(float(point), float(y_val), color='blue', zorder=5)  # Додавання точок перегину на графік / Adding inflection points to the graph
                    inflection_points_third_scatter.append(scatter)
                    inflection_points_th_l = ax.annotate(
                        f'({float(point):.2f}, {float(y_val):.2f})',
                        (float(point), float(y_val)),
                        textcoords="offset points",
                        xytext=(0, 10),
                        ha='center',
                        color='blue'
                    )  # Додавання тексту для точок перегину / Adding text for inflection points
                    inflection_points_th.append(inflection_points_th_l)

                # пошук точок пересічення з Ox і побудова пунктирних ліній / Finding intersection points with Ox and plotting dashed lines
                points_0x_0y = points_ox_oy(second_dev_of_function, 'blue', label=False, lines=True, include_oy=False)
                ox_points_third_second = points_0x_0y['0x']  # Збереження точок перетину з Ox / Storing intersection points with Ox
                h_lines_third_second = points_0x_0y['lines']  # Збереження пунктирних ліній / Storing dashed lines

                ax.legend()  # Додавання легенди до графіка / Adding a legend to the graph
                legend = ax.legend()

                third_s_dev_label.configure(
                    text=f"y'' = {second_dev_of_function}"  # Оновлення тексту для другої похідної / Updating the text for the second derivative
                )

                # оновлення лейблу з точками перегину / Updating the label with inflection points
                if inflection_points:
                    formatted_points = "; ".join([f"x{i+1} = {float(pt):.2f}" for i, pt in enumerate(inflection_points)])
                    inflection_points_label.configure(text=f"9) Точки перегину: {formatted_points}")  # Оновлення тексту мітки з точками перегину / Updating the text for the inflection points label
                else:
                    inflection_points_label.configure(text="9) Точки перегину: не існує")  # Виведення повідомлення про відсутність точок перегину / Displaying message about the absence of inflection points

                points_0x_0y = points_ox_oy(expr, 'blue', label=False, lines=True, include_oy=False)
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
                for text in legend.get_texts():
                    
                    text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
                canvas.draw()  # Оновлення графіку / Redrawing the canvas

                dictionary_of_variables['ox_points_third_second'] = ox_points_third_second  # Збереження точок перетину з віссю x / Storing intersection points with the x-axis
                dictionary_of_variables['h_lines_third_second'] = h_lines_third_second  # Збереження пунктирних ліній / Storing dashed lines
                dictionary_of_variables['plot_third_second'] = plot_third_second  # Збереження графіку другої похідної / Storing the second derivative graph
                dictionary_of_variables['inflection_points_third_scatter'] = inflection_points_third_scatter  # Збереження точок перегину / Storing inflection points
                dictionary_of_variables['inflection_points_th'] = inflection_points_th  # Збереження підписів точок перегину / Storing inflection point labels
                dictionary_of_variables['inflection_points_label'] = inflection_points_label  # Збереження лейблу з точками перегину / Storing the label with inflection points

    elif check == 0 and plot_third_second:  # Якщо чекбокс вимкнений і графік другої похідної існує / If the checkbox is unchecked and the second derivative plot exists
        # видалення графіка другої похідної / Removing the second derivative plot
        if plot_third_second:
            for line in plot_third_second:
                line.remove()
            plot_third_second.clear()
            canvas.draw()
        # plot_third_second.remove()
        # plot_third_second = None

        # видалення точок перегину / Removing inflection points
        if inflection_points_third_scatter:
            for point in inflection_points_third_scatter:
                point.remove()  # Видалення точок перегину / Removing inflection points
            inflection_points_third_scatter.clear()

        # видалення підпису точок / Removing point labels
        for label in inflection_points_th:
            label.remove()
        inflection_points_th.clear()

        # видалення точок перетину з Ox і пунктирних ліній / Removing intersection points with Ox and dashed lines
        if ox_points_third_second:
            for point in ox_points_third_second:
                point.remove()  # Видалення точок перетину з віссю x / Removing intersection points with x-axis
            ox_points_third_second.clear()

        if h_lines_third_second:
            for line in h_lines_third_second:
                line.remove()  # Видалення горизонтальних ліній / Removing horizontal lines
            h_lines_third_second.clear()

        # оновлення легенди / Updating the legend
        ax.legend().remove()  # Видалення легенди / Removing the legend
        ax.legend()  # Оновлення легенди / Updating the legend
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
        canvas.draw()  # Оновлення графіку / Redrawing the canvas