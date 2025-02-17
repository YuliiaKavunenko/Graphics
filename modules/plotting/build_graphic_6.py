import sympy, numpy
from ..main_elements import *
from ..error_window import show_error_window
from ..data_calculation import ( 
    scope_of_function, 
    format_intervals, 
    check_even_odd_func, 
    points_ox_oy, 
    find_sign_intervals, 
    find_and_plot_slant_asymptote,
    plot_horizontal_asymptotes
)
from ..variables_constants import *

# функція для побудови і дослідження графіку функції y = a/x**2 + x/a / Function for constructing and studying the graph of the function y = a/x**2 + x/a
def build_sixth_func():
    from .clean import clean_for_functions 
    from .build_DSK import build_DSK
    from .build_colors_labels import build_colors_labels
    from .plot_constant_function import plot_constant_function
    from .punctured_dots import punctured_dots

    ax.clear()  # Очищення графічної області / Clearing the plotting area
    build_DSK()  # Виклик функції побудови ДСК / Calling the function to build DSK (not sure what DSK stands for)
    clean_for_functions()
    
    # Отримання значень параметрів a і b з інтерфейсу / Getting the values of parameters a and b from the interface
    a1 = a1_sixth.get()
    a2 = a2_sixth.get()
    
    
    if a1 and a2:  # Перевірка, чи існують значення a і b / Checking if a and b values exist
        x = sympy.symbols('x')  # Оголошення змінної x як символічної / Declaring x as a symbolic variable
        
        try:
            a1 = float(a1)  # Перетворення a у число з плаваючою крапкою / Converting a to a float
            a2 = float(a2)  # Перетворення b у число з плаваючою крапкою / Converting b to a float
            if a1 != a2:
                show_error_window(' ! Коєфіцієнти "а" повинні бути однаковими!')
            else:
                if a1 == 0:
                    
                    show_error_window(' ! Ділити на нуль не можна!')
                    
                else:
                    # Розміщення чекбоксів / Placing checkboxes
                    first_dev_sixth.place(x = 25, y = 116)
                    first_dev_sixth.deselect()
                    second_dev_sixth.place(x = 25, y = 161)
                    second_dev_sixth.deselect()

                    main_graphic_label.place(x=25, y = 71)
            
                    # Виклик функції для налаштування кольорових міток / Calling the function to set up color labels
                    build_colors_labels()

                    expr = (a1/x**2) + (x/a2) # Визначення виразу функції / Defining the function expression
        
                    if isinstance(expr, sympy.Number):  # Якщо вираз є числом / If the expression is a number
                        plot_constant_function(float(expr), 'red')  # Побудова графіка для константи / Plotting the graph for the constant
                    else:
                        plots = dictionary_of_variables['plots']  # Отримання списку графіків / Getting the list of plots
                        func = sympy.lambdify(x, expr, 'numpy')  # Перетворення виразу у функцію для обчислень / Converting the expression to a function for calculations

                        x_vals = numpy.linspace(-100, 100, 4000)  # Визначення діапазону значень x / Defining the range of x values
                        y_vals = func(x_vals)  # Обчислення значень y для відповідних x / Calculating y values for the corresponding x values

                        plot = ax.plot(x_vals, y_vals, label=f'y = ({a1}/x**2) + (x/{a2})', color='red')  # Побудова графіка функції / Plotting the function graph
                        plots.append(plot)  # Додавання графіка до списку / Adding the plot to the list

                        domain = scope_of_function(expr)  # Обчислення області визначення функції / Calculating the domain of the function
                        domain_text = f"1) D(y) = {format_intervals(domain)}"  # Форматування тексту області визначення / Formatting the domain text
                        scope_label.configure(text=domain_text)  # Налаштування тексту мітки для області визначення / Setting the text for the domain label

                        # перетин з осями ох та оу / intersection with the Ox and Oy axes
                        points_0x_0y = points_ox_oy(expr,'red', True)

                        # отримуємо список точок нулів функції / getting the list of zero points of the function
                        points_zero = points_0x_0y['points_zero']
                        if points_zero:
                            # формуємо текст для лейблу / forming text for the label
                            points_zero_text = "7) Нулі функції: " + ", ".join([f"x{i+1} = {point}" for i, point in enumerate(points_zero)])
                        else:
                            points_zero_text = "7) Нулі функції: не існує"

                        # встановлюємо текст лейблу / setting the label text
                        points_zero_label.configure(text=points_zero_text)

                        # отримуємо координати точки перетину з Oy / getting the coordinates of the intersection point with Oy
                        oy_point = points_0x_0y['0y']
                        oy_text = "не існує"  # якщо точка не існує / if the point does not exist
                        if oy_point:
                            offsets = oy_point.get_offsets()  # отримуємо координати точки / getting the point coordinates
                            if len(offsets) > 0:
                                oy_coords = offsets[0]  # отримуємо першу точку / getting the first point
                                oy_text = f"(0, {oy_coords[1]:.2f})"

                        ox_points = points_0x_0y['0x']  # отримуємо точки перетину з Ox / getting intersection points with Ox

                        if ox_points:
                            points_0x_text = "; ".join([f"({x:.2f}, 0)" for x in points_zero])  # форматуємо текст для точок перетину з Ox / format text for Ox intersection points
                        else:
                            points_0x_text = "не існує"
                        points_0x_0y_text = (
                            f"6) Точки перетину з Ox:\n{points_0x_text}\n"
                            f"Точка перетину з Oy:\n{oy_text}"
                        )

                        points_ox_oy_label.configure(text = points_0x_0y_text)  # оновлюємо лейбл для точок перетину з осями / update the label for intersection points with axes

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
                            print(f"  обчислення проміжків знакосталості: {e}")  # Виведення повідомлення про помилку обчислення проміжків знакосталості / Displaying message about sign constancy intervals calculation error
                            intervals_identity_l.configure(text="8) Проміжки знакосталості:\nнеможливо обчислити")  # Виведення повідомлення про неможливість обчислення / Displaying message about inability to calculate

                        # Пошук і побудова косої асимптоти / Finding and plotting the slant asymptote
                        slant_asymptote_label = slope_asymptote  # Рівняння асимптоти / Equation of the asymptote
                        find_and_plot_slant_asymptote(expr, x, label_widget=slope_asymptote)

                        punctured_asymptots_text = punctured_dots(expr)  # перевіряємо наявність точок розриву у функції / check for punctured points in the function

                        plot_horizontal_asymptotes(expr = expr)

                        ax.legend()  # Додавання легенди до графіка / Adding a legend to the graph
                        legend = ax.legend()
                        for text in legend.get_texts():
                            
                            text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
                        canvas.draw()  # Оновлення графіка / Redrawing the canvas
                        # except Exception as e:
                        #     print(f"  першого графіку: {e}")  # Виведення повідомлення про помилку побудови першого графіку / Displaying message about the first graph building error
                
            
        except ValueError:
            show_error_window(" ! Коєфіцієнти повинні бути числами!")
    else:
                    show_error_window(' ! Для початку введіть усі коєфіцієнти!')