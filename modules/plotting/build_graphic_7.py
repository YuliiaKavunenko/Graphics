import sympy, numpy
from ..main_elements import *
from ..data_calculation import ( 
    scope_of_function, 
    format_intervals, 
    check_even_odd_func, 
    points_ox_oy, 
    find_sign_intervals, 
    find_and_plot_slant_asymptote
)
from ..variables_constants import *

# функція для побудови і дослідження графіку функції у = (x**2 - a)/(x - b) / Function for constructing and studying the graph of the function y = (x**2 - a)/(x - b)
def build_seventh_func():
    from .build_DSK import build_DSK
    from .build_colors_labels import build_colors_labels
    from .plot_constant_function import plot_constant_function
    from .punctured_dots import punctured_dots
    ax.clear()  # Очищення графічної області / Clearing the plotting area
    build_DSK()  # Виклик функції побудови ДСК / Calling the function to build DSK (not sure what DSK stands for)
    
    # Отримання значення параметра a з інтерфейсу / Getting the values of parameters a and b from the interface
    a = a1_seventh.get()
    
    # Розміщення чекбоксів / Placing checkboxes
    first_dev_seventh.place(x = 25, y = 65)
    second_dev_seventh.place(x = 25, y = 110)
    main_graphic_label.place(x=25, y=20)
    
    # Виклик функції для налаштування кольорових міток / Calling the function to set up color labels
    build_colors_labels()
    
    if a:  # Перевірка, чи існують значення a і b / Checking if a and b values exist
        x = sympy.symbols('x')  # Оголошення змінної x як символічної / Declaring x as a symbolic variable
        a = float(a)  # Перетворення a у число з плаваючою крапкою / Converting a to a float
        expr = (x**2 + x + a)/x  # Визначення виразу функції / Defining the function expression
        
        if isinstance(expr, sympy.Number):  # Якщо вираз є числом / If the expression is a number
            plot_constant_function(float(expr), 'red')  # Побудова графіка для константи / Plotting the graph for the constant
        else:
            plots = dictionary_of_variables['plots']  # Отримання списку графіків / Getting the list of plots
            func = sympy.lambdify(x, expr, 'numpy')  # Перетворення виразу у функцію для обчислень / Converting the expression to a function for calculations

            x_vals = numpy.linspace(-10, 10, 400)  # Визначення діапазону значень x / Defining the range of x values
            y_vals = func(x_vals)  # Обчислення значень y для відповідних x / Calculating y values for the corresponding x values

            plot = ax.plot(x_vals, y_vals, label=f'y = (x**2 + x + {a})/x ', color='red')  # Побудова графіка функції / Plotting the function graph
            plots.append(plot)  # Додавання графіка до списку / Adding the plot to the list

            ax.legend()  # Додавання легенди до графіка / Adding a legend to the graph
            legend = ax.legend()
            for text in legend.get_texts():
                text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
            canvas.draw()  # Оновлення графіка / Redrawing the canvas

            domain = scope_of_function(expr)  # Обчислення області визначення функції / Calculating the domain of the function
            domain_text = f"1) D(y) = {format_intervals(domain)}"  # Форматування тексту області визначення / Formatting the domain text
            scope_label.configure(text=domain_text)  # Налаштування тексту мітки для області визначення / Setting the text for the domain label

            # Обчислення та виведення точок перетину з осями Ox і Oy / Calculating and displaying the intersection points with axes Ox and Oy
            points_0x_0y = points_ox_oy(expr, 'red', True)
            points_zero = points_0x_0y['points_zero']

            points_0x_text = "; ".join([f"({x:.2f}, 0)" for x in points_zero])  # Форматування точок перетину з Ox / Formatting the intersection points with Ox

            # Отримання координат точки перетину з Oy / Getting the coordinates of the intersection point with Oy
            oy_point = points_0x_0y['0y']
            oy_text = "не існує"  # Виведення повідомлення про відсутність точки перетину з Oy / Displaying message about the absence of an intersection point with Oy
            if oy_point:
                offsets = oy_point.get_offsets()  # Отримання координат точки / Getting the point coordinates
                if len(offsets) > 0:
                    oy_coords = offsets[0]  # Отримання координат першої точки / Getting the coordinates of the first point
                    oy_text = f"(0, {oy_coords[1]:.2f})"  # Форматування координат точки перетину з Oy / Formatting the coordinates of the intersection point with Oy

            points_0x_0y_text = (
                f"6) Точки перетину з Ox:\n{points_0x_text}\n"  # Виведення тексту для точок перетину з Ox / Displaying the text for the intersection points with Ox
                f"Точка перетину з Oy:\n{oy_text}"  # Виведення тексту для точки перетину з Oy / Displaying the text for the intersection point with Oy
            )

            points_ox_oy_label.configure(text=points_0x_0y_text)  # Налаштування тексту мітки для точок перетину з осями / Setting the text for the intersection points label

            # Отримання списку нулів функції та їх форматування / Getting the list of function zeros and formatting them
            points_zero = points_0x_0y['points_zero']
            points_zero_text = "7) Нулі функції: " + ", ".join([f"x{i+1} = {point}" for i, point in enumerate(points_zero)])
            points_zero_label.configure(text=points_zero_text)  # Налаштування тексту мітки для нулів функції / Setting the text for the function zeros label

            # Перевірка парності або непарності функції / Checking the function for evenness or oddness
            even_or_odd = check_even_odd_func(expr)
            even_or_odd_func_l.configure(text=f'{even_or_odd}')  # Налаштування тексту для результату перевірки / Setting the text for the check result

            try:
                sign_intervals = find_sign_intervals(expr)  # Знаходження проміжків знакосталості / Finding the intervals of sign constancy
                all_sign_intervals_text = ""
                for interval, sign in sign_intervals:
                    all_sign_intervals_text += f"{sign} при х ∈ {interval}\n"  # Додавання кожного інтервалу до тексту / Adding each interval to the text

                intervals_identity_l.configure(text=f"8) Проміжки знакосталості:\n{all_sign_intervals_text}")  # Налаштування тексту мітки для проміжків знакосталості / Setting the text for the sign constancy intervals label
            except Exception as e:
                print(f"Помилка обчислення проміжків знакосталості: {e}")  # Виведення повідомлення про помилку обчислення проміжків знакосталості / Displaying message about sign constancy intervals calculation error
                intervals_identity_l.configure(text="8) Проміжки знакосталості:\nнеможливо обчислити")  # Виведення повідомлення про неможливість обчислення / Displaying message about inability to calculate

            # Пошук і побудова косої асимптоти / Finding and plotting the slant asymptote
            slant_asymptote_label = slope_asymptote  # Рівняння асимптоти / Equation of the asymptote
            find_and_plot_slant_asymptote(expr, x, label_widget=slope_asymptote)

            punctured_dots(expr)  # Визначення й побудова розривних точок / Defining and plotting punctured points

            print(dictionary_of_variables['plots'])  # Виведення списку графіків / Printing the list of plots
            # except Exception as e:
            #     print(f"Помилка першого графіку: {e}")  # Виведення повідомлення про помилку побудови першого графіку / Displaying message about the first graph building error