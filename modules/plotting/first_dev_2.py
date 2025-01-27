import sympy, numpy
from ..main_elements import *
from ..data_calculation import points_ox_oy,find_intervals
from ..variables_constants import dictionary_of_variables
from .plot_constant_function import plot_constant_function
# функція для побудови і виконання дослідження похідної у' другого графіку функції / Function for constructing and analyzing the first derivative of the second graph function
def drob_first_dev():
    check = first_dev_fdrob.get()  # Отримання значення чекбоксу / Getting the value of the checkbox
    plots_2d = dictionary_of_variables['plots_2d']
    plot_2_2 = dictionary_of_variables['plot_2_2']
    local_max_scatter_2 = dictionary_of_variables['local_max_scatter_2']
    local_min_scatter_2 = dictionary_of_variables['local_min_scatter_2']
    ox_points_first = dictionary_of_variables['ox_points_first'] # Точки перетину з віссю x / Intersection points with the x-axis
    h_lines_first = dictionary_of_variables['h_lines_first']  # Пунктирні лінії / Dashed lines 
    local_max_scatter_text_2 = dictionary_of_variables['local_max_scatter_text_2']
    local_min_scatter_text_2 = dictionary_of_variables['local_min_scatter_text_2']

    if check == 1:  # Якщо чекбокс активований / If the checkbox is checked

        # Отримання значень параметрів a та b з інтерфейсу / Getting the values of parameters a and b from the interface
        a = a_drob_1.get()
        b_data_3 = a_drob_3.get()
        if a and b_data_3:  # Перевірка, чи існують значення a і b / Checking if a and b values exist
            x = sympy.symbols('x')  # Оголошення змінної x як символічної / Declaring x as a symbolic variable
            a = float(a)  # Перетворення a у число з плаваючою крапкою / Converting a to a float
            b_data_3 = float(b_data_3)  # Перетворення b у число з плаваючою крапкою / Converting b to a float
            function = (x**2 - a) / (x - b_data_3)  # Визначення виразу функції / Defining the function expression
            dev_of_function = sympy.diff(function, x)  # Обчислення першої похідної функції / Calculating the first derivative of the function
            rounded_derivative = dev_of_function  
            for atom in dev_of_function.atoms():
                # Если атом является числом с плавающей точкой
                if atom.is_Float:
                    # Заменяем его на округлённое значение
                    rounded_derivative = rounded_derivative.xreplace({atom: round(atom, 2)})

            if isinstance(dev_of_function, sympy.Number):  # Якщо вираз є числом / If the expression is a number
                plot_constant_function(float(dev_of_function), 'green')  # Побудова графіка для константи / Plotting the graph for the constant
            else:
                # обчислення локальних максимумів, мінімумів та інтервалів зростання/спадання / Calculating local maxima, minima and growth/decay intervals
                intervals_data = find_intervals(dev_of_function, function)

                # побудова нових точок перетину і пунктирних ліній / Plotting new intersection points and dashed lines
                points_0x_0y = points_ox_oy(dev_of_function, 'green', label=False, lines=True, include_oy=False)
                ox_points_first = points_0x_0y['0x']  # Точки 0х / Points on the x-axis
                h_lines_first = points_0x_0y['lines']  # Пунктирні лінії / Dashed lines

                hover_points = []
                hover_annotations = []

                if intervals_data['локальний максимум'] != 'не існує':
                    local_max = intervals_data['локальний максимум'][0]
                    l_max_x, l_max_y = local_max
                    local_max_scatter_2 = ax.scatter(l_max_x, l_max_y, color='#FF0899', s=40, picker=5)
                    hover_points.append(local_max_scatter_2)
                    local_max_annotation = ax.annotate(f'({l_max_x:.2f}, {l_max_y:.2f})',
                                                    (l_max_x, l_max_y),
                                                    textcoords="offset points",
                                                    xytext=(0, -15),
                                                    ha='center',
                                                    visible=False)
                    hover_annotations.append(local_max_annotation)

                if intervals_data['локальний мінімум'] != "не існує":
                    local_min = intervals_data['локальний мінімум'][0]
                    l_min_x, l_min_y = local_min
                    local_min_scatter_2 = ax.scatter(l_min_x, l_min_y, color='#FF0899', s=40, picker=5)
                    hover_points.append(local_min_scatter_2)
                    local_min_annotation = ax.annotate(f'({l_min_x:.2f}, {l_min_y:.2f})',
                                                    (l_min_x, l_min_y),
                                                    textcoords="offset points",
                                                    xytext=(0, -15),
                                                    ha='center',
                                                    visible=False)
                    hover_annotations.append(local_min_annotation)

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
                # оновлення тексту похідної / Updating the derivative text
                drob_first_dev_lable.configure(text=f"y' = {rounded_derivative}")

                if len(intervals_data['інтервали']) != 0:  # Перевірка наявності інтервалів зростання/спадання / Checking for growth/decay intervals
                    interval_text = "\n".join([f"({str(left)[0:4]}; {str(right)[0:4]}) {state}" for left, right, state in intervals_data['інтервали']])
                else:
                    interval_text = "Інтервалів зростання/спадання не існує"  # Виведення повідомлення про відсутність інтервалів зростання/спадання / Displaying message about the absence of growth/decay intervals

                interval_label.configure(text=f'3) {interval_text}')  # Налаштування тексту мітки для інтервалів зростання/спадання / Setting text for growth/decay intervals label

                # Формуємо текст для локальних максимумів і мінімумів / Forming text for local maxima and minima
                if intervals_data['локальний максимум'] != 'не існує':  # Перевірка наявності локальних максимумів / Checking for local maxima
                    local_max_text = "Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
                else:
                    local_max_text = "Локальний максимум: не існує"  # Виведення повідомлення про відсутність локальних максимумів / Displaying message about the absence of local maxima

                if intervals_data['локальний мінімум'] != 'не існує':  # Перевірка наявності локальних мінімумів / Checking for local minima
                    local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
                else:
                    local_min_text = "Локальний мінімум: не існує"  # Виведення повідомлення про відсутність локальних мінімумів / Displaying message about the absence of local minima

                # макс значення функції / max function value
                if isinstance(intervals_data['макс. значення ф-ції'], tuple):  # Перевірка, чи значення є кортежем / Checking if value is a tuple
                    funct_max_text = f"Макс. значення ф-ції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
                else:
                    funct_max_text = f"Макс. значення ф-ції: {intervals_data['макс. значення ф-ції']}"  # Виводимо текст без форматування / Display text without formatting

                # Мінімальне значення функції / min function value
                if isinstance(intervals_data['мін. значення ф-ції'], tuple):  # Перевірка, чи значення є кортежем / Checking if value is a tuple
                    func_min_text = f"Мін. значення ф-ції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
                else:
                    func_min_text = f"Мін. значення ф-ції: {intervals_data['мін. значення ф-ції']}"  # Виводимо текст без форматування / Display text without formatting
                local_max_min_text = f'4) {local_max_text}\n{local_min_text}'  # Формування тексту для локальних максимумів та мінімумів / Forming text for local maxima and minima
                local_max_min_label.configure(text=local_max_min_text)  # Налаштування тексту мітки для локальних максимумів і мінімумів / Setting text for local maxima and minima label

                zn_function_text = f'5) {funct_max_text}\n{func_min_text}'  # Формування тексту для макс. та мін. значень функції / Forming text for max and min function values
                zn_function_label.configure(text=zn_function_text)  # Налаштування тексту мітки для макс. та мін. значень функції / Setting text for max and min function values label

                # Оновлення тексту похідної / Updating the derivative text
                drob_first_dev_lable.configure(
                    text=f"y' = {rounded_derivative}",
                )

                expr = dev_of_function  # Встановлення виразу для похідної / Setting the expression for the derivative

                # Перетворення виразу похідної у функцію для обчислень / Converting the derivative expression to a function for calculations
                func = sympy.lambdify(x, expr, 'numpy')

                # Визначення діапазону значень x / Defining the range of x values
                x_vals = numpy.linspace(-100, 100, 4000)
                y_vals = func(x_vals)  # Обчислення значень y для відповідних x / Calculating y values for the corresponding x values

                # Побудова графіку похідної функції / Plotting the derivative function graph
                plot_2_2 = ax.plot(x_vals, y_vals, label=f"y' = {rounded_derivative}", color='green')
                plots_2d.append(plot_2_2)  # Додавання графіку до списку графіків / Adding the plot to the list of plots

                ax.legend()  # Виведення легенди на графіку / Displaying the legend on the graph
                legend = ax.legend()

                for text in legend.get_texts():
                    
                    text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
                canvas.draw()  # Оновлення графіку / Redrawing the canvas

                dictionary_of_variables['plot_2_2'] = plot_2_2
                dictionary_of_variables['local_max_scatter_2'] = local_max_scatter_2
                dictionary_of_variables['local_min_scatter_2'] = local_min_scatter_2
                dictionary_of_variables['local_max_scatter_text_2'] = local_max_scatter_text_2
                dictionary_of_variables['local_min_scatter_text_2'] = local_min_scatter_text_2
                dictionary_of_variables['ox_points_first'] = ox_points_first
                dictionary_of_variables['h_lines_first'] = h_lines_first

                # third_first_dev()  # Виклик функції третьої похідної / Calling the third derivative function

                # except Exception as e:
                #     print(f"Помилка першої дробової похідної: {e}")  # Виведення повідомлення про помилку обчислення першої дробової похідної / Displaying message about first fractional derivative calculation error

    elif check == 0 and plot_2_2 in plots_2d:  # Якщо чекбокс вимкнений і графік існує у списку / If the checkbox is unchecked and the plot exists in the list
        # видалення графіка / Removing the plot
        if plot_2_2:
            for line in plot_2_2:
                line.remove()
            plot_2_2.clear()
            canvas.draw()
        # plots_2d.remove(plot_2_2)

        # видалення локальних максимумів та мінімумів / Removing local maxima and minima
        if local_max_scatter_2:
            local_max_scatter_2.remove()  # Видалення точок локального максимуму / Removing local maximum points
            local_max_scatter_2 = None

        if local_min_scatter_2:
            local_min_scatter_2.remove()  # Видалення точок локального мінімуму / Removing local minimum points
            local_min_scatter_2 = None

        # видалення точок 0х та пунктирних ліній / Removing 0x points and dashed lines
        if ox_points_first:
            for point in ox_points_first:
                point.remove()  # Видалення точок перетину з віссю x / Removing intersection points with x-axis
            ox_points_first.clear()
        if h_lines_first:
            for line in h_lines_first:
                line.remove()  # Видалення горизонтальних ліній / Removing horizontal lines
            h_lines_first.clear()

        ax.legend().remove()  # Видалення легенди / Removing the legend
        ax.legend()  # Оновлення легенди / Updating the legend
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
        canvas.draw()  # Оновлення графіку / Redrawing the canvas