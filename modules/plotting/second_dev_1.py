
import sympy, numpy
from ..main_elements import *
from ..data_calculation import points_ox_oy, find_inflection_points, find_simple_convexity_intervals
from ..variables_constants import *

# Функція для побудови і виконання дослідження похідної у'' першого графіку функції / Function for constructing and researching the second derivative of the first graph function
def check_second_dev():
    from .plot_constant_function import plot_constant_function
    from ..variables_constants import dictionary_of_variables
    check = second_dev.get()
    func1 = dictionary_of_variables['func1']   # Отримуємо функцію з словника / Get the function from the dictionary
    plots = dictionary_of_variables['plots']  # Отримуємо графіки з словника / Get the plots from the dictionary
    plot_3 = dictionary_of_variables['plot_3']  # Отримуємо графік з словника / Get the plot from the dictionary
    ox_points_second = dictionary_of_variables['ox_points_second']  # Отримуємо точки перетину з віссю x / Get the intersection points with the x-axis
    h_lines_second = dictionary_of_variables['h_lines_second']  # Отримуємо пунктирні лінії / Get the dashed lines

    inflection_points_scatter = dictionary_of_variables['inflection_points_scatter'] # Список для точок перегину / List for inflection points
    inflection_points_l = dictionary_of_variables['inflection_points_l'] # Список для підписів точок перегину / List for inflection points labels
    if check == 1:  # Якщо перевірка активна / If the check is active
        a = a_3.get()
        b = b_3.get()

        if a and b:

            # Отримуємо значення a і b з інтерфейсу / Get values a and b from the interface
            x = sympy.symbols('x')  # Оголошуємо символічну змінну x / Declare symbolic variable x
            a = float(a)
            b = float(b)
            # Визначаємо вираз для другої похідної / Define the expression for the second derivative
            expr = 6*a*x + 2*b

            if isinstance(expr, sympy.Number):  # Якщо вираз є числом / If the expression is a number
                plot_3 = plot_constant_function(float(expr), 'blue')  # Побудова графіка для константи / Plotting the graph for the constant function
            else:
                # Отримуємо точки перегину / Get the inflection points
                inflection_points = find_inflection_points(expr)

                # Формуємо форматований рядок для лейблу / Formatted string for the label
                formatted_points = "; ".join([f"x{i+1} = {point:.1f}" for i, point in enumerate(inflection_points)])

                # Виводимо точки перегину на графіку / Plot the inflection points on the graph
                for point in inflection_points:
                    # Обчислюємо значення функції в точці перегину / Calculate the function value at the inflection point

                    y_inflection = func1(point)
                    # Малюємо точки перегину на графіку / Draw inflection points on the graph
                    scatter = ax.scatter(point, y_inflection, color='blue', zorder=5)
                    inflection_points_scatter.append(scatter)  # Зберігаємо об'єкт точки / Store the point object
                    label_point_inflection = ax.annotate(f'({point:.1f}, {y_inflection:.1f})',  # Додаємо підпис з округленням / Add label with rounding
                                (point, y_inflection),
                                textcoords="offset points", 
                                xytext=(0, 10),
                                ha='center', color='blue')
                    inflection_points_l.append(label_point_inflection)

                # Оновлюємо лейбл з точками перегину / Update the label with inflection points
                inflection_points_label.configure(text=f"9) Точки перегину: {formatted_points}")
                func = sympy.lambdify(x, expr, 'numpy')  # Перетворення виразу у функцію для обчислень / Convert expression to function for calculations

                x_vals = numpy.linspace(-10, 10, 400)  # Задаємо діапазон значень x / Set the range of x values
                y_vals = func(x_vals)  # Обчислюємо значення y / Calculate y values

                plot_3 = ax.plot(x_vals, y_vals, label=f'y = 6*{a}x + 2 * {b}', color='blue')  # Побудова графіку другої похідної / Plotting the second derivative graph

                plots.append(plot_3)

                # Побудова точок перетину 0x і пунктирних ліній / Plotting intersection points with 0x and dashed lines
                points_0x_0y = points_ox_oy(expr, 'blue', label=False, lines=True, include_oy=False)
                ox_points_second = points_0x_0y['0x']  # Графічні об'єкти точок перетину / Graphical objects of intersection points
                h_lines_second = points_0x_0y['lines']  # Графічні об'єкти пунктирних ліній / Graphical objects of dashed lines

                # Знаходимо проміжки опуклості / Find the intervals of convexity
                convexity_intervals = find_simple_convexity_intervals(expr)

                # Створюємо текст для лейблу / Create text for the label
                convexity_text = "10) Проміжки опуклості графіка:\n"  # "Intervals of graph convexity:\n"
                for interval, convexity in convexity_intervals:
                    left, right = interval
                    left = "-∞" if left == float('-inf') else f"{left:.2f}"
                    right = "+∞" if right == float('inf') else f"{right:.2f}"
                    convexity_text += f"{convexity} при x ∈ ({left}; {right})\n"  # "{convexity} at x ∈ ({left}; {right})\n"

                # Виводимо текст у лейбл / Output the text to the label
                convexity_intervals_label.configure(text=convexity_text, anchor="w", justify = "left")
                ax.legend()  # Виводимо легенду на графіку / Output the legend on the graph
                legend = ax.legend()

                for text in legend.get_texts():
                    
                    text.set_color('red')  # Змінюємо колір тексту легенди на червоний / Change legend text color to red
                canvas.draw()  # Оновлюємо графік / Redraw the canvas
                # зберігаємо графік у словник / save the plot to the dictionary
                dictionary_of_variables['plot_3'] = plot_3

                dictionary_of_variables['ox_points_second'] = ox_points_second
                dictionary_of_variables['h_lines_second'] = h_lines_second
                dictionary_of_variables['inflection_points_scatter'] = inflection_points_scatter
                dictionary_of_variables['inflection_points_l'] = inflection_points_l

                # except Exception as e:
                #     print(f"Помилка третьої похідної: {e}")  # Виведення повідомлення про помилку третьої похідної / Outputting message about third derivative error
    elif check == 0:  # Якщо перевірка не активна і графік є у списку / If the check is not active and the plot is in the list
        # видаляємо графік другої похідної / remove the second derivative plot
        if plot_3 in plots:
            for line in plot_3:
                line.remove()
            plot_3.clear()
            canvas.draw()

            # plot_3.remove()
            # plots.remove(plot_3)

        # Видалення точок перетину і пунктирних ліній / Removing intersection points and dashed lines
        if ox_points_second:
            for point in ox_points_second:
                point.remove()  # Видалення точок перетину з віссю x / Remove points of intersection with the x-axis
            ox_points_second.clear()
        if h_lines_second:
            for line in h_lines_second:
                line.remove()  # Видалення горизонтальних ліній / Remove horizontal lines
            h_lines_second.clear()

        # Видалення точок перегину / Removing inflection points
        if inflection_points_scatter:
            for scatter in inflection_points_scatter:
                scatter.remove()
            inflection_points_scatter.clear()

        # Видалення тексту точки перегину / Removing inflection points text
        if inflection_points_l:
            for label in inflection_points_l:
                label.remove()
            inflection_points_l.clear()
            
        # Оновлення легенди / Updating the legend
        ax.legend().remove()
        ax.legend()
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')  # Змінюємо колір тексту легенди на червоний / Change legend text color to red
        canvas.draw()  # Оновлюємо графік / Redraw the canvas