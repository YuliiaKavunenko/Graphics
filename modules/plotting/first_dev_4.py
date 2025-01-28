import sympy, numpy
from ..main_elements import *
from textwrap import wrap
from ..data_calculation import points_ox_oy,find_intervals
from ..variables_constants import dictionary_of_variables
# Функція для побудови і дослідження похідної у' четвертого графіку функції / Function to construct and analyze the derivative of the fourth function plot
def fourth_first_dev():
    from .plot_constant_function import plot_constant_function
    # Перевірка, чи увімкнено четверту похідну / Check if the fourth derivative is enabled
    check = first_dev_fourth.get()
    plot_fourth_first = dictionary_of_variables['plot_fourth_first']
    ox_points_fourth_first = dictionary_of_variables['ox_points_fourth_first']
    h_lines_fourth_first = dictionary_of_variables['h_lines_fourth_first']
    local_max_fourth_first = dictionary_of_variables['local_max_fourth_first']
    local_min_fourth_first = dictionary_of_variables['local_min_fourth_first']

    
    if check == 1:  # Якщо чекбокс ввімкнено / If the checkbox is enabled

        # Отримання значення змінної "a" для четвертої похідної / Retrieve the value of variable "a" for the fourth derivative
        a = a4_drob.get()
        if a:  # Перевірка, чи значення "a" не є порожнім / Check if "a" value is not empty
            x = sympy.symbols('x')  # Створення символічної змінної x / Create symbolic variable x
            a = float(a)  # Конвертація значення "a" у дійсне число / Convert the "a" value to a floating-point number

            # Визначення функції та її похідної / Define the function and its derivative
            function = x/(x**2 + a)  # Основна функція / The main function
            
            dev_of_function = sympy.diff(function, x)  # Обчислення похідної функції / Calculate the derivative of the function
            rounded_derivative = dev_of_function  
            for atom in dev_of_function.atoms():
                # Если атом является числом с плавающей точкой
                if atom.is_Float:
                    # Заменяем его на округлённое значение
                    rounded_derivative = rounded_derivative.xreplace({atom: round(atom, 2)})
            if isinstance(dev_of_function, sympy.Number):  # Якщо вираз є числом / If the expression is a number
                plot_constant_function(float(dev_of_function), 'green')  # Побудова графіка для константи / Plotting the graph for the constant
            else:
                # Визначення інтервалів зростання і спадання / Determine intervals of increase and decrease
                intervals_data = find_intervals(dev_of_function, function)  # Виклик функції для пошуку інтервалів / Call the function to find intervals
                if len(intervals_data['інтервали']) != 0:  # Перевірка наявності інтервалів / Check for existing intervals
                    interval_text = "\n".join([f"({str(left)[0:4]}; {str(right)[0:4]}) {state}" for left, right, state in intervals_data['інтервали']])
                else:
                    interval_text = "Інтервалів зростання/спадання не існує"  # Текст, якщо інтервалів немає / Text if no intervals exist

                # Оновлення текстового віджета для інтервалів / Update the text widget for intervals
                interval_label.configure(text=f'3) {interval_text}')

                # Формування тексту для локальних максимумів і мінімумів / Form text for local maxima and minima
                hover_points = []
                hover_annotations = []

                if intervals_data['локальний максимум'] != "не існує":
                    local_max_text = "Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
                    local_max = intervals_data['локальний максимум'][0]
                    l_max_x, l_max_y = local_max
                    local_max_fourth_first = ax.scatter(l_max_x, l_max_y, color='#FF0899', s=40, picker=5)
                    hover_points.append(local_max_fourth_first)
                    local_max_text_fourth_first = ax.annotate(f'({l_max_x:.2f}, {l_max_y:.2f})',
                                                            (l_max_x, l_max_y),
                                                            textcoords="offset points",
                                                            xytext=(0, -15),
                                                            ha='center',
                                                            visible=False)
                    hover_annotations.append(local_max_text_fourth_first)
                else:
                    local_max_text = "Локальний максимум: не існує"  # Якщо мінімумів немає / If no minima exist

                if intervals_data['локальний мінімум'] != "не існує":
                    local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
                    local_min = intervals_data['локальний мінімум'][0]
                    l_min_x, l_min_y = local_min
                    local_min_fourth_first = ax.scatter(l_min_x, l_min_y, color='#FF0899', s=40, picker=5)
                    hover_points.append(local_min_fourth_first)
                    local_min_text_fourth_first = ax.annotate(f'({l_min_x:.2f}, {l_min_y:.2f})',
                                                            (l_min_x, l_min_y),
                                                            textcoords="offset points",
                                                            xytext=(0, -15),
                                                            ha='center',
                                                            visible=False)
                    hover_annotations.append(local_min_text_fourth_first)
                else:
                    local_min_text = "Локальний мінімум: не існує"  # Якщо мінімумів немає / If no minima exist
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

                # Оновлення текстових віджетів для максимумів і мінімумів / Update text widgets for maxima and minima
                local_max_min_text = f'4) {local_max_text}\n{local_min_text}'
                local_max_min_label.configure(text=local_max_min_text)

                # Оновлення тексту для загального максимуму та мінімуму функції / Update text for overall function maxima and minima
                zn_function_text = f'5) {funct_max_text}\n{func_min_text}'
                zn_function_label.configure(text=zn_function_text)

                # Оновлення тексту похідної функції / Update the derivative function text
                drob_first_dev_lable.configure(text=f"y' = {rounded_derivative}")

                # Лямбда-функція для розрахунку похідної / Lambda function to calculate the derivative
                expr = dev_of_function
                func = sympy.lambdify(x, expr, 'numpy')  # Конвертація у числову функцію / Convert to a numerical function

                # Побудова графіку похідної / Plot the derivative graph
                x_vals = numpy.linspace(-100, 100, 4000)  # Генерація x-значень / Generate x-values
                y_vals = func(x_vals)  # Обчислення y-значень похідної / Calculate y-values for the derivative
                label = f"{rounded_derivative}"
                wrapped_label = '\n'.join(wrap(label, 60))
                plot_fourth_first = ax.plot(x_vals, y_vals, label=f"y' = {wrapped_label}", color='green')

                # Пошук точок перетину з віссю Ox / Find intersection points with the x-axis
                points_0x_0y = points_ox_oy(dev_of_function, 'green', label=False, lines=True, include_oy=False)

                ox_points_fourth_first = points_0x_0y['0x']  # Ось ми присвоюємо координати X точок до змінної / Here we assign the X coordinates of the points to a variable
                h_lines_fourth_first = points_0x_0y['lines']  # Тут ми присвоюємо лінії до іншої змінної / Here we assign lines to another variable

                # Додавання легенди до графіка / Adding legend to the graph
                ax.legend()
                legend = ax.legend()

                fourth_f_dev_label.configure(
                    text = f"y' = {rounded_derivative}"  # Оновлюємо текст ярлика з похідною функцією / Updating the label text with the derivative function
                )

                # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
                for text in legend.get_texts():
                    
                    text.set_color('red')
                canvas.draw()  # Перемальовуємо графік / Redrawing the canvas
                dictionary_of_variables['plot_fourth_first'] = plot_fourth_first
                dictionary_of_variables['ox_points_fourth_first'] = ox_points_fourth_first
                dictionary_of_variables['h_lines_fourth_first'] = h_lines_fourth_first
                dictionary_of_variables['local_max_fourth_first'] = local_max_fourth_first
                dictionary_of_variables['local_max_text_fourth_first'] = local_max_text_fourth_first
                dictionary_of_variables['local_min_fourth_first'] = local_min_fourth_first
                dictionary_of_variables['local_min_text_fourth_first'] = local_min_text_fourth_first
                
                # Приклад обробки винятків при знаходженні першої дробової похідної / Example of exception handling in finding the first fractional derivative
                # except Exception as e:
                #     print(f"Помилка першої дробовох похідної: {e}")  # Виведення повідомлення про помилку / Printing error message

    # Перевірка стану check і наявності графіка / Checking the state of 'check' and presence of graph
    elif check == 0:  
        # Видалення графіка / Removing the graph
        if plot_fourth_first:
            for line in plot_fourth_first:
                line.remove()
            plot_fourth_first.clear()
        canvas.draw()
        # plot_fourth_first.remove()
        # plot_fourth_first = None

        # Видалення точок, ліній, максимумів і мінімумів / Removing points, lines, maxima and minima
        if ox_points_fourth_first:
            for point in ox_points_fourth_first:
                point.remove()  # Видалення кожної точки / Removing each point
            ox_points_fourth_first.clear()  # Очищення списку точок / Clearing the list of points

        if h_lines_fourth_first:
            for line in h_lines_fourth_first:
                line.remove()  # Видалення кожної лінії / Removing each line
            h_lines_fourth_first.clear()  # Очищення списку ліній / Clearing the list of lines
        try:
            if local_max_fourth_first:
                local_max_fourth_first.remove()  # Видалення локального максимуму з графіка / Removing local maximum from the graph
                local_max_fourth_first = None
        except:
            pass

        try:
            if local_min_fourth_first:
                local_min_fourth_first.remove()  # Видалення локального мінімуму з графіка / Removing local minimum from the graph
                local_min_fourth_first = None
        except:
            pass

        ax.legend().remove()  # Видалення легенди / Removing the legend
        ax.legend()  # Оновлення легенди / Updating the legend
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
        canvas.draw()  # Перемальовуємо графік / Redrawing the canvas