import sympy, numpy
from ..main_elements import *
from ..data_calculation import points_ox_oy,find_intervals
from ..variables_constants import *
from .plot_constant_function import plot_constant_function
# функція для побудови і виконання дослідження похідної у' першого графіку функції / function to plot and analyze the first derivative of the first graph of the function
def check_first_dev():
    check = first_dev.get()  # отримуємо стан чекбоксу для першої похідної / getting the state of the checkbox for the first derivative

    plots = dictionary_of_variables['plots'] 
    plot_2 = dictionary_of_variables['plot_2']     
    plot2 = []
    local_max_scatter = dictionary_of_variables['local_max_scatter'] 
    local_min_scatter = dictionary_of_variables['local_min_scatter'] 
    local_max_scatter_text = dictionary_of_variables['local_max_scatter_text'] 
    local_min_scatter_text = dictionary_of_variables['local_min_scatter_text'] 
    ox_points_first = dictionary_of_variables['ox_points_first'] 
    h_lines_first = dictionary_of_variables['h_lines_first']

    if check == 1:
        # Обчислення й побудова графіка першої похідної / Calculating and plotting the first derivative graph
        a = a_2.get()  # отримуємо значення коефіцієнта a для першої похідної / getting the value of coefficient a for the first derivative
        b = b_2.get()  # отримуємо значення коефіцієнта b для першої похідної / getting the value of coefficient b for the first derivative
        c = c_2.get()  # отримуємо значення коефіцієнта c для першої похідної / getting the value of coefficient c for the first derivative

        a_f = a_1.get()  # отримуємо значення коефіцієнта a функції / getting the value of coefficient a of the function
        b_f = b_1.get()  # отримуємо значення коефіцієнта b функції / getting the value of coefficient b of the function
        c_f = c_1.get()  # отримуємо значення коефіцієнта c функції / getting the value of coefficient c of the function
        d_f = d_1.get()  # отримуємо значення коефіцієнта d функції / getting the value of coefficient d of the function

        if a and b and c:
            x = sympy.symbols('x')  # створюємо символ x / creating the symbol x
            a = float(a)  # перетворюємо значення a в число з плаваючою комою / converting the value of a to a float
            b = float(b)  # перетворюємо значення b в число з плаваючою комою / converting the value of b to a float
            c = float(c)  # перетворюємо значення c в число з плаваючою комою / converting the value of c to a float

            a_f = float(a_f)  # перетворюємо значення a функції в число з плаваючою комою / converting the value of a of the function to a float
            b_f = float(b_f)  # перетворюємо значення b функції в число з плаваючою комою / converting the value of b of the function to a float
            c_f = float(c_f)  # перетворюємо значення c функції в число з плаваючою комою / converting the value of c of the function to a float
            d_f = float(d_f)  # перетворюємо значення d функції в число з плаваючою комою / converting the value of d of the function to a float

            function = a_f * x**3 + b_f * x**2 + c_f * x + d_f  # створюємо вираз для функції / creating the expression for the function
            expr = 3 * a * x**2 + 2 * b * x + c  # створюємо вираз для першої похідної функції / creating the expression for the first derivative of the function

            if isinstance(expr, sympy.Number):  # перевіряємо, чи є вираз числом / checking if the expression is a number
                plot_2 = plot_constant_function(float(expr), 'green')  # будуємо графік для константної похідної / plotting the constant derivative
            else:
                func = sympy.lambdify(x, expr, 'numpy')  # перетворюємо похідну у форму, придатну для числових обчислень / converting the derivative to a form suitable for numerical calculations
                x_vals = numpy.linspace(-100, 100, 4000)  # створюємо значення x в діапазоні від -10 до 10 / creating x values in the range from -10 to 10
                y_vals = func(x_vals)  # обчислюємо значення y для похідної / calculating the y values for the derivative
                plot_2 = ax.plot(x_vals, y_vals, label = f'y = 3*{a}x^2 + 2*{b}x + {c}', color='green')  # будуємо графік першої похідної / plotting the first derivative
                plot2.append(plot_2)
                # plots.append(plot_2)  # додаємо графік до списку / adding the plot to the list
                # додаємо легенду / adding the legend
                ax.legend()
                legend = ax.legend()
                for text in legend.get_texts():
                    text.set_color('red')  # встановлюємо червоний колір тексту легенди / setting the legend text color to red
                canvas.draw()  # перерисовуємо холст / redrawing the canvas

            # Обчислення точок локального максимуму та мінімуму / Calculating local maximum and minimum points
            intervals_data = find_intervals(expr, function)  # знаходимо інтервали та екстремуми / finding intervals and extrema

            # Обчислення точок перетину з віссю Ox та побудова пунктирних ліній / Calculating intersection points with the Ox axis and plotting dashed lines
            points_0x_0y = points_ox_oy(expr, 'green', label=False, lines=True, include_oy=False)
            ox_points_first = points_0x_0y['0x']  # зберігаємо точки перетину з Ox / storing intersection points with Ox
            h_lines_first = points_0x_0y['lines']  # зберігаємо пунктирні лінії / storing dashed lines

            hover_points = []
            hover_annotations = []

            # Формування тексту для локальних максимумів і мінімумів / Form text for local maxima and minima
            if intervals_data['локальний максимум'] != "не існує":  # Перевірка наявності локальних максимумів / Check for local maxima
                local_max_text = "Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
                local_max = intervals_data['локальний максимум'][0]
                l_max_x, l_max_y = local_max
                local_max_seventh_first = ax.scatter(l_max_x, l_max_y, color='#FF0899', s=40, picker=5)  # Додавання точок локального максимуму / Adding local maximum points
                hover_points.append(local_max_seventh_first)
                local_max_text_seventh_first = ax.annotate(f'({l_max_x:.2f}, {l_max_y:.2f})',
                                                    (l_max_x, l_max_y),
                                                    textcoords="offset points",
                                                    xytext=(0, -15),
                                                    ha='center',
                                                    visible=False)  # Додавання тексту для точок локального максимуму / Adding text for local maximum points
                hover_annotations.append(local_max_text_seventh_first)
            else:
                local_max_text = "Локальний максимум: не існує"  # Якщо максимумів немає / If no maxima exist

            if intervals_data['локальний мінімум'] != "не існує":  # Перевірка наявності локальних мінімумів / Check for local minima
                local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
                local_min = intervals_data['локальний мінімум'][0]
                l_min_x, l_min_y = local_min
                local_min_seventh_first = ax.scatter(l_min_x, l_min_y, color='#FF0899', s=40, picker=5)  # Додавання точок локального мінімуму / Adding local minimum points
                hover_points.append(local_min_seventh_first)
                local_min_text_seventh_first = ax.annotate(f'({l_min_x:.2f}, {l_min_y:.2f})',
                                                    (l_min_x, l_min_y),
                                                    textcoords="offset points",
                                                    xytext=(0, -15),
                                                    ha='center',
                                                    visible=False)  # Додавання тексту для точок локального мінімуму / Adding text for local minimum points
                hover_annotations.append(local_min_text_seventh_first)
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
            if len(intervals_data['інтервали']) != 0:  # Перевірка наявності інтервалів зростання/спадання / Checking for growth/decay intervals
                interval_text = "\n".join([f"({str(left)[0:5]}; {str(right)[0:5]}) {state}" for left, right, state in intervals_data['інтервали']])
            else:
                interval_text = "Інтервалів зростання/спадання не існує"  # Виведення повідомлення про відсутність інтервалів зростання/спадання / Displaying message about absence of growth/decay intervals

            interval_label.configure(text=f'3) {interval_text}')  # Налаштування тексту мітки для інтервалів зростання/спадання / Setting text for growth/decay intervals label

            # Формуємо текст для локальних максимумів і мінімумів / Forming text for local maxima and minima
            if intervals_data['локальний максимум'] != 'не існує' :  # Перевірка наявності локальних максимумів / Checking for local maxima
                local_max_text = "Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
            else:
                local_max_text = "Локальний максимум: не існує"  # Виведення повідомлення про відсутність локальних максимумів / Displaying message about absence of local maxima

            if intervals_data['локальний мінімум'] != 'не існує':  # Перевірка наявності локальних мінімумів / Checking for local minima
                local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
            else:
                local_min_text = "Локальний мінімум: не існує"  # Виведення повідомлення про відсутність локальних мінімумів / Displaying message about absence of local minima

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
            
            dictionary_of_variables['plot_2'] = plot_2
            dictionary_of_variables['local_max_scatter'] = local_max_scatter
            dictionary_of_variables['local_min_scatter'] = local_min_scatter
            dictionary_of_variables['local_max_scatter_text'] = local_max_scatter_text
            dictionary_of_variables['local_min_scatter_text'] = local_min_scatter_text
            dictionary_of_variables['ox_points_first'] = ox_points_first
            dictionary_of_variables['h_lines_first'] = h_lines_first
            dictionary_of_variables['plots'] = plots
            # except Exception as e:
            #     print(f"Помилка другого графіку: {e}")  # Виведення повідомлення про помилку другого графіку / Displaying message about second graph error

            canvas.draw()  # Оновлення графіку / Redrawing the canvas
    elif check == 0:
        # Видалення графіка та точок / Removing the graph and points
        if plot_2:
            for line in plot_2:
                line.remove()
            plot_2.clear()
            canvas.draw()
        if local_max_scatter:
            local_max_scatter.remove()  # Видалення точок локальних максимумів / Removing local maxima points
            local_max_scatter_text.remove()  # Видалення тексту локальних максимумів / Removing local maxima text
            local_max_scatter = None
            local_max_scatter_text = None

        if local_min_scatter:
            local_min_scatter.remove()  # Видалення точок локальних мінімумів / Removing local minima points
            local_min_scatter_text.remove()  # Видалення тексту локальних мінімумів / Removing local minima text
            local_min_scatter = None
            local_min_scatter_text = None

        # видалення точок перетину і пунктирних ліній / removing intersection points and dashed lines
        if ox_points_first:
            for point in ox_points_first:
                point.remove()  # Видалення точок перетину з віссю x / Removing intersection points with x-axis
            ox_points_first.clear()
        if h_lines_first:
            for line in h_lines_first:
                line.remove()  # Видалення горизонтальних ліній / Removing horizontal lines
            h_lines_first.clear()

        ax.legend().remove()  # Видалення легенди / Removing legend
        ax.legend()  # Оновлення легенди / Updating legend
        legend = ax.legend()
        for text in legend.get_texts():
            
            text.set_color('red')  # Зміна кольору тексту в легенді на червоний / Changing legend text color to red
        canvas.draw()  # Оновлення графіку / Redrawing the canvas