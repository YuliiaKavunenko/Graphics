import sympy, numpy
from ..main_elements import *
from ..data_calculation import points_ox_oy,find_intervals
from ..variables_constants import dictionary_of_variables
# функція для побудови і виконання дослідження похідної у' третього графіку функції / Function for constructing and analyzing the first derivative of the third graph function
def third_first_dev():
    from .plot_constant_function import plot_constant_function
    check = first_dev_sdrob.get()  # Отримання значення чекбоксу / Getting the value of the checkbox
    plot_third_first = dictionary_of_variables['plot_third_first']  # Отримання графіку першої похідної / Getting the first derivative plot
    ox_points_third_first = dictionary_of_variables['ox_points_third_first']  # Отримання точок перетину з віссю x / Getting intersection points with the x-axis
    h_lines_third_first = dictionary_of_variables['h_lines_third_first']  # Отримання пунктирних ліній / Getting dashed lines
    local_max_third_first = dictionary_of_variables['local_max_third_first']  # Отримання точок локального максимуму / Getting local maximum points
    local_min_third_first = dictionary_of_variables['local_min_third_first']  # Отримання точок локального мінімуму / Getting local minimum points
    local_max_text_third_first = dictionary_of_variables['local_max_text_third_first']  # Отримання тексту точок локального максимуму / Getting text of local maximum points
    local_min_text_third_first = dictionary_of_variables['local_min_text_third_first']  # Отримання тексту точок локального мінімуму / Getting text of local minimum points
    
    if check == 1:  # Якщо чекбокс активований / If the checkbox is checked
        
        a = a_th_drob.get()  # Отримання значення параметра a з інтерфейсу / Getting the value of parameter a from the interface
        if a:  # Перевірка, чи існує значення a / Checking if a value exists
            x = sympy.symbols('x')  # Оголошення змінної x як символічної / Declaring x as a symbolic variable
            a = float(a)  # Перетворення a у число з плаваючою крапкою / Converting a to a float

            function = (x**2 - a**2) / x  # Визначення виразу функції / Defining the function expression
            dev_of_function = sympy.diff(function, x)  # Обчислення першої похідної функції / Calculating the first derivative of the function
            if isinstance(dev_of_function, sympy.Number):  # Якщо вираз є числом / If the expression is a number
                plot_constant_function(float(dev_of_function), 'green')  # Побудова графіка для константи / Plotting the graph for the constant
            else:
                # Обчислення інтервалів зростання і спадання / Calculating growth and decay intervals
                intervals_data = find_intervals(dev_of_function, function)
                if len(intervals_data['інтервали']) != 0:  # Перевірка наявності інтервалів зростання/спадання / Checking for growth/decay intervals
                    interval_text = "\n".join([f"({str(left)[0:4]}; {str(right)[0:4]}) {state}" for left, right, state in intervals_data['інтервали']])
                else:
                    interval_text = "Інтервалів зростання/спадання не існує"  # Виведення повідомлення про відсутність інтервалів зростання/спадання / Displaying message about the absence of growth/decay intervals

                interval_label.configure(text=f'3) {interval_text}')  # Налаштування тексту мітки для інтервалів зростання/спадання / Setting text for growth/decay intervals label
                
                # print(intervals_data['локальний максимум'])
                # print(len(intervals_data['локальний максимум']))
                # Формування тексту для локальних максимумів і мінімумів / Forming text for local maxima and minima
                if intervals_data['локальний максимум'] != 'не існує':  # Перевірка наявності локальних максимумів / Checking for local maxima
                    local_max_text = "Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
                    local_max = intervals_data['локальний максимум'][0]
                    l_max_x, l_max_y = local_max
                    local_max_third_first = ax.scatter(l_max_x, l_max_y, color='#FF0899', s=40)  # Додавання точок локального максимуму / Adding local maximum points
                    local_max_text_third_first = ax.annotate(f'({l_max_x:.2f}, {l_max_y:.2f})',
                                                        (l_max_x, l_max_y),
                                                        textcoords="offset points",
                                                        xytext=(15, 15),
                                                        ha='center')  # Додавання тексту для точок локального максимуму / Adding text for local maximum points
                    
                else:
                    local_max_text = "Локальний максимум: не існує"  # Виведення повідомлення про відсутність локальних максимумів / Displaying message about the absence of local maxima

                if intervals_data['локальний мінімум'] != 'не існує':  # Перевірка наявності локальних мінімумів / Checking for local minima
                    local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
                    local_min = intervals_data['локальний мінімум'][0]
                    l_min_x, l_min_y = local_min
                    local_min_third_first = ax.scatter(l_min_x, l_min_y, color='#FF0899', s=40)  # Додавання точок локального мінімуму / Adding local minimum points
                    local_min_text_third_first = ax.annotate(f'({l_min_x:.2f}, {l_min_y:.2f})',
                                                        (l_min_x, l_min_y),
                                                        textcoords="offset points",
                                                        xytext=(15, 15),
                                                        ha='center')  # Додавання тексту для точок локального мінімуму / Adding text for local minimum points
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

                local_max_min_text = f'4) {local_max_text}\n{local_min_text}'  # Формування тексту для локальних максимумів і мінімумів / Forming text for local maxima and minima
                local_max_min_label.configure(text=local_max_min_text)  # Налаштування тексту мітки для локальних максимумів і мінімумів / Setting text for local maxima and minima label

                zn_function_text = f'5) {funct_max_text}\n{func_min_text}'  # Формування тексту для макс. та мін. значень функції / Forming text for max and min function values
                zn_function_label.configure(text=zn_function_text)  # Налаштування тексту мітки для макс. та мін. значень функції / Setting text for max and min function values label

                # Оновлення тексту похідної / Updating the derivative text
                drob_first_dev_lable.configure(
                    text=f"y' = {dev_of_function}"
                )

                print(dev_of_function)  # Виведення похідної у консоль / Printing the derivative in the console

                expr = dev_of_function  # Встановлення виразу для похідної / Setting the expression for the derivative
                func = sympy.lambdify(x, expr, 'numpy')  # Перетворення виразу похідної у функцію для обчислень / Converting the derivative expression to a function for calculations

                x_vals = numpy.linspace(-10, 10, 400)  # Визначення діапазону значень x / Defining the range of x values
                y_vals = func(x_vals)  # Обчислення значень y для відповідних x / Calculating y values for the corresponding x values

                plot_third_first = ax.plot(x_vals, y_vals, label=f"y' = {dev_of_function}", color='green')  # Побудова графіку першої похідної / Plotting the first derivative graph
                # plots.append(plot)

                # Пошук точок перетину з Ox / Finding intersection points with Ox
                # пошук точок перетину похідної з Ox / Finding intersection points of the derivative with Ox
                points_0x_0y = points_ox_oy(dev_of_function, 'green', label=False, lines=True, include_oy=False)
                ox_points_third_first = points_0x_0y['0x']  # Збереження точок перетину з Ox / Storing intersection points with Ox
                h_lines_third_first = points_0x_0y['lines']  # Збереження пунктирних ліній / Storing dashed lines

                ax.legend()  # Додавання легенди до графіка / Adding a legend to the graph
                legend = ax.legend()

                third_f_dev_label.configure(
                    text=f"y' = {dev_of_function}"  # Оновлення тексту для першої похідної / Updating the text for the first derivative
                )

                for text in legend.get_texts():
                    text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
                canvas.draw()  # Оновлення графіку / Redrawing the canvas
                dictionary_of_variables['plot_third_first'] = plot_third_first  # Збереження графіку першої похідної / Saving the first derivative plot
                dictionary_of_variables['ox_points_third_first'] = ox_points_third_first  # Збереження точок перетину з Ox / Saving intersection points with Ox
                dictionary_of_variables['h_lines_third_first'] = h_lines_third_first  # Збереження пунктирних ліній / Saving dashed lines
                dictionary_of_variables['local_max_third_first'] = local_max_third_first  # Збереження точок локального максимуму / Saving local maximum points
                dictionary_of_variables['local_min_third_first'] = local_min_third_first  # Збереження точок локального мінімуму / Saving local minimum points
                dictionary_of_variables['local_max_text_third_first'] = local_max_text_third_first  # Збереження тексту точок локального максимуму / Saving text of local maximum points
                dictionary_of_variables['local_min_text_third_first'] = local_min_text_third_first  # Збереження тексту точок локального мінімуму / Saving text of local minimum points
                # except Exception as e:
                #     print(f"Помилка першої дробової похідної: {e}")  # Виведення повідомлення про помилку першої похідної / Displaying message about the first derivative error

    elif check == 0 and plot_third_first:  # Якщо чекбокс вимкнений і графік першої похідної існує / If the checkbox is unchecked and the first derivative plot exists
        # видалення графіка першої похідної / Removing the first derivative plot
        print(plot_third_first)
        if plot_third_first:
            for line in plot_third_first:
                line.remove()
            plot_third_first.clear()
            canvas.draw()

        # видалення точок і пунктирних ліній / Removing points and dashed lines
        if ox_points_third_first:
            for point in ox_points_third_first:
                point.remove()  # Видалення точок перетину з віссю x / Removing intersection points with x-axis
            ox_points_third_first.clear()

        if h_lines_third_first:
            for line in h_lines_third_first:
                line.remove()  # Видалення горизонтальних ліній / Removing horizontal lines
            h_lines_third_first.clear()

        # видалення локальних максимумів і мінімумів / Removing local maxima and minima
        if local_max_third_first:
            local_max_third_first.remove()  # Видалення точок локального максимуму / Removing local maximum points
            local_max_text_third_first.remove()  # Видалення тексту точок локального максимуму / Removing local maximum points text
            local_max_third_first = None
            local_max_text_third_first = None

        if local_min_third_first:
            local_min_third_first.remove()  # Видалення точок локального мінімуму / Removing local minimum points
            local_min_text_third_first.remove()  # Видалення тексту точок локального мінімуму / Removing local minimum points text
            local_min_third_first = None
            local_min_text_third_first = None

        ax.legend().remove()  # Видалення легенди / Removing the legend
        ax.legend()  # Оновлення легенди / Updating the legend
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
        canvas.draw()  # Оновлення графіку / Redrawing the canvas