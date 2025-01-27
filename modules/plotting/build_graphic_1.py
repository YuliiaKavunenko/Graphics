import sympy, numpy
from ..main_elements import *
from ..error_window import show_error_window

from ..data_calculation import (
    scope_of_function, 
    format_intervals, 
    check_even_odd_func, 
    points_ox_oy, 
    find_sign_intervals, 
    plot_horizontal_asymptotes
)
from ..variables_constants import dictionary_of_variables

# функція для побудови і дослідження графіку функції y = ax**3 + bx**2 + cx + d / function to plot and analyze the graph of the function y = ax**3 + bx**2 + cx + d
def build_graphic_1():
    from .clean import clean_for_functions 
    from .build_DSK import build_DSK
    from .build_colors_labels import build_colors_labels
    from .plot_constant_function import plot_constant_function
    from .punctured_dots import punctured_dots
    
    ax.clear()  # очищаємо вісь графіка / clearing the graph axis
    build_DSK()  # будуємо сітку координат / building the coordinate grid
    clean_for_functions()

    # отримуємо значення коефіцієнтів a, b, c, d з полів вводу / getting the values of coefficients a, b, c, d from input fields
    a = a_1.get()
    b = b_1.get()
    c = c_1.get()
    d = d_1.get()

    # похідні / derivatives

    if a and b and c and d:  # перевіряємо, що всі поля не пусті / checking that all fields are not empty
        # try:
        
        x = sympy.symbols('x')  # створюємо символ x / creating the symbol x
        try:
            a = float(a)  # перетворюємо значення a в число з плаваючою комою / converting the value of a to a float
            b = float(b)  # перетворюємо значення b в число з плаваючою комою / converting the value of b to a float
            c = float(c)  # перетворюємо значення c в число з плаваючою комою / converting the value of c to a float
            d = float(d)  # перетворюємо значення d в число з плаваючою комою / converting the value of d to a float
            # ставимо чекбокси / placing checkboxes
            if a == 0 and b == 0:
                red_gr.place(x = 1, y = 20)
                main_graphic_label.place(x=25, y=20)
                constant_function_label.place(x = 0, y = 60)
            else:
                first_dev.place(x = 25, y = 65)
                first_dev.deselect()
                second_dev.place(x = 25, y = 110)
                second_dev.deselect()
                main_graphic_label.place(x = 25, y = 20)
                build_colors_labels()  # розміщуємо кольорові лейбли / placing colored labels

            # видаляємо значення в полях похідних, щоб уникнути помилок повторення символів / deleting values in derivative fields to avoid symbol repetition errors
            a_2.delete(0,"end")
            b_2.delete(0,"end")
            c_2.delete(0,"end")

            a_3.delete(0,"end")
            b_3.delete(0,"end")
        except ValueError:
            show_error_window("Помилка! Всі коефіцієнти повинні бути числами!")

        expr = a*x**3 + b*x**2 + c*x + d  # створюємо вираз для функції / creating the expression for the function
        if isinstance(expr, sympy.Number):  # перевіряємо, чи є вираз числом / checking if the expression is a number
            plot_constant_function(float(expr), 'red')  # будуємо графік для константної функції / plot the constant function
            domain = scope_of_function(expr)  # визначаємо область визначення функції / determine the domain of the function
            domain_text = f"1) D(y) = {format_intervals(domain)}"  # форматування інтервалів області визначення / format the domain intervals
            scope_label.configure(text=domain_text)  # оновлюємо лейбл області визначення / update the domain label

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

            even_or_odd_func_l.configure(text ='2) Функція загального вигляду')  # оновлюємо лейбл для парності функції / update the label for the function's parity

            try:
                sign_intervals = find_sign_intervals(expr)  # знаходимо інтервали знакосталості функції / find sign intervals of the function
                all_sign_intervals_text = ""
                for interval, sign in sign_intervals:
                    all_sign_intervals_text += f"{sign} при х ∈ {interval}\n"  # додаємо кожний інтервал у текст / adding each interval to the text

                intervals_identity_l.configure(text=f"8) Проміжки знакосталості:\n{all_sign_intervals_text}")  # оновлюємо лейбл для інтервалів знакосталості / update the label for sign intervals
            except Exception as e:
                print(f"Помилка обчислення проміжків знакосталості: {e}")  # помилка під час обчислення інтервалів знакосталості / error calculating sign intervals
                intervals_identity_l.configure(text="8) Проміжки знакосталості")  # не вдалося обчислити інтервали знакосталості / unable to calculate sign intervals

        else:
            func1 = sympy.lambdify(x, expr, 'numpy') # перетворюємо функцію у форму, придатну для числових обчислень / convert the function to a form suitable for numerical calculations
            # list_functions.append(func1)
            dictionary_of_variables['func1'] = func1
            x_vals = numpy.linspace(-20, 20, 400)  # створюємо значення x в діапазоні від -10 до 10 / creating x values in the range from -10 to 10
            y_vals = func1(x_vals)  # обчислюємо значення y для функції / calculating the y values for the function

            plot = ax.plot(x_vals, y_vals, label=f'y = {a}x^3 + {b}x^2 + {c}x + {d}', color='red')  # будуємо графік функції / plotting the function
            dictionary_of_variables['plots'].append(plot)  # додаємо графік до списку / adding the plot to the list

            # додаємо легенду / adding the legend
            legend = ax.legend()
            for text in legend.get_texts():
                text.set_color('red')  # встановлюємо червоний колір тексту легенди / setting the legend text color to red
            canvas.draw()  # перерисовуємо холст / redrawing the canvas

            # замінюємо значення для похідних / replacing values for derivatives
            a_2.insert(0,f"{int(a)}")
            b_2.insert(0,f"{int(b)}")
            c_2.insert(0, f"{int(c)}")

            a_3.insert(0,f"{int(a)}")
            b_3.insert(0,f"{int(b)}")
            domain = scope_of_function(expr)  # визначаємо область визначення функції / determine the domain of the function
            domain_text = f"1) D(y) = {format_intervals(domain)}"  # форматування інтервалів області визначення / format the domain intervals
            scope_label.configure(text=domain_text)  # оновлюємо лейбл області визначення / update the domain label

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


            even_or_odd = check_even_odd_func(expr)  # перевіряємо, чи функція парна чи непарна / check if the function is even or odd
            even_or_odd_func_l.configure(text = f'{even_or_odd}')  # оновлюємо лейбл для парності функції / update the label for the function's parity

            try:
                sign_intervals = find_sign_intervals(expr)  # знаходимо інтервали знакосталості функції / find sign intervals of the function
                all_sign_intervals_text = ""
                for interval, sign in sign_intervals:
                    all_sign_intervals_text += f"{sign} при х ∈ {interval}\n"  # додаємо кожний інтервал у текст / adding each interval to the text

                intervals_identity_l.configure(text=f"8) Проміжки знакосталості:\n{all_sign_intervals_text}")  # оновлюємо лейбл для інтервалів знакосталості / update the label for sign intervals
            except Exception as e:
                print(f"Помилка обчислення проміжків знакосталості: {e}")  # помилка під час обчислення інтервалів знакосталості / error calculating sign intervals
                intervals_identity_l.configure(text="8) Проміжки знакосталості:\nнеможливо обчислити")  # не вдалося обчислити інтервали знакосталості / unable to calculate sign intervals

            punctured_asymptots_text = punctured_dots(expr)  # перевіряємо наявність точок розриву у функції / check for punctured points in the function

            plot_horizontal_asymptotes(expr = expr)
    else:
        show_error_window('Помилка! Для початку введіть усі коєфіцієнти!')