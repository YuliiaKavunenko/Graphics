import sympy, numpy
from ..main_elements import *
from ..data_calculation import scope_of_function, format_intervals, check_even_odd_func, points_ox_oy, find_sign_intervals, find_intervals
# функція для побудови графіка / function to plot the graph
def plot_graph(ax, canvas):
    from .plot_constant_function import plot_constant_function
    from .punctured_dots import punctured_dots
    # очищаємо поточний графік / clearing the current graph
    # ax.clear()
    # Переводимо фокус на кнопку, щоб прибрати курсор з CTkEntry / shifting focus to the button to remove the caret from CTkEntry
    button_get.focus()
    # отримуємо текст з поля вводу / getting text from the input field
    function_text = input_graphic.get()

    # якщо поле вводу не пусте / if the input field is not empty
    if function_text.strip():
        
        # намагаємося побудувати графік / trying to plot the graph
        # try:
        # створюємо символьну змінну для використання в sympy / creating a symbolic variable for use in sympy
        x = sympy.symbols('x')
        # встановлюємо фон в клітинку / setting the grid background

        # парсимо функцію та компілюємо її / parsing and compiling the function
        expr = sympy.sympify(function_text)
        if isinstance(expr, sympy.Number):
            plot_constant_function(float(expr),'purple')  # будуємо графік для константної функції / plot a constant function
        else:
            dev_expr = sympy.diff(expr, x)  # обчислюємо похідну функції / calculate the derivative of the function
            print(dev_expr)
            func = sympy.lambdify(x, expr, 'numpy')  # перетворюємо функцію у форму, придатну для числових обчислень / convert the function to a form suitable for numerical calculations

            # обчислюємо значення функції для заданого діапазону x / calculate the function values for a given range of x
            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)

            # будуємо графік / plotting the graph
            ax.plot(x_vals, y_vals, label=f'y = {function_text}', color='purple')

            # додаємо легенду / adding the legend
            ax.legend()

            # встановлюємо колір тексту легенди / setting the legend text color
            legend = ax.legend()
            for text in legend.get_texts():
                text.set_color('red')

            # перерисовуємо холст / redrawing the canvas
            canvas.draw()
            # ПОМИЛКИ ДЛЯ ДЕЯКИХ ФУНКЦІЙ! / ERRORS FOR SOME FUNCTIONS!
            # Д(y) / D(y)
            domain = scope_of_function(expr)  # визначаємо область визначення функції / determine the domain of the function

            domain_text = f"1) D(y) = {format_intervals(domain)}"  # форматування інтервалів області визначення / format the domain intervals
            scope_label.configure(text=domain_text)

    # визначення інтервалів зростання та спадання / determining intervals of increase and decrease
            intervals_data = find_intervals(dev_expr, expr)  # знаходимо інтервали зростання та спадання / find intervals of increase and decrease
            if len(intervals_data['інтервали']) != 0:  # якщо існують інтервали зростання або спадання / if there are intervals of increase or decrease
                interval_text = "\n".join([f"({left:.2f}; {right:.2f}) {state}" for left, right, state in intervals_data['інтервали']])
            else:
                interval_text = "Інтервалів зростання/спадання не існує"  # не існують інтервали зростання або спадання / no intervals of increase or decrease exist

            interval_label.configure(text=f'3) {interval_text}')  # оновлюємо лейбл для інтервалів / update the interval label

            # Формуємо текст для локальних максимумів і мінімумів / forming text for local maxima and minima
            if len(intervals_data['локальний максимум']) != 0:  # якщо існують локальні максимуми / if there are local maxima
                local_max_text = "4) Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
            else:
                local_max_text = "4) Локальний максимум: не існує"  # не існує локальних максимумів / no local maxima exist

            if len(intervals_data['локальний мінімум']) != 0:  # якщо існують локальні мінімуми / if there are local minima
                local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
            else:
                local_min_text = "Локальний мінімум: не існує"  # не існує локальних мінімумів / no local minima exist

            # максимальне значення функції / maximum value of the function
            if intervals_data['макс. значення ф-ції']:
                funct_max_text = f"5) Макс. значення функції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
            else:
                funct_max_text = "5) Макс. значення функції: не існує"  # не існує максимального значення / no maximum value exists

            # мінімальне значення функції / minimum value of the function
            if intervals_data['мін. значення ф-ції']:
                func_min_text = f"Мін. значення функції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
            else:
                func_min_text = "Мін. значення функції: не існує"  # не існує мінімального значення / no minimum value exists

            local_max_min_text = f'{local_max_text}\n{local_min_text}'  # об'єднуємо текст для локальних максимумів та мінімумів / combine local max and min text
            local_max_min_label.configure(text=local_max_min_text)  # оновлюємо лейбл для локальних максимумів та мінімумів / update the label for local max and min

            zn_function_text = f'{funct_max_text}\n{func_min_text}'  # об'єднуємо текст для максимального та мінімального значень / combine text for max and min values
            zn_function_label.configure(text=zn_function_text)  # оновлюємо лейбл для максимального та мінімального значень / update the label for max and min values

            points_0x_0y = points_ox_oy(expr,'purple', True)  # визначаємо точки перетину з осями / determine intersection points with axes
            # перетин 0х і 0у / intersection with Ox and Oy
            points_zero = points_0x_0y['points_zero']  # отримуємо точки перетину з Ox / get intersection points with Ox

            points_0x_text = "; ".join([f"({x:.2f}, 0)" for x in points_zero])  # форматуємо текст для точок перетину з Ox / format text for Ox intersection points

            # отримуємо координати і точку 0у / getting coordinates and point 0y
            oy_point = points_0x_0y['0y']
            oy_text = "не існує"  # не існує / does not exist
            if oy_point:
                offsets = oy_point.get_offsets()  # отримуємо координати точки / get point coordinates
                if len(offsets) > 0:
                    oy_coords = offsets[0]  # отримуємо першу точку / get first point
                    oy_text = f"(0, {oy_coords[1]:.2f})"

            points_0x_0y_text = (
                f"6) Точки перетину з Ox:\n{points_0x_text}\n"
                f"Точка перетину з Oy:\n{oy_text}"
            )

            points_ox_oy_label.configure(text=points_0x_0y_text)  # оновлюємо лейбл для точок перетину з осями / update the label for intersection points with axes

            # отримуємо список точок нулів функції / getting the list of zero points of the function
            points_zero = points_0x_0y['points_zero']

            # формуємо текст для лейблу / forming text for the label
            points_zero_text = "7) Нулі функції: " + ", ".join([f"x{i+1} = {point}" for i, point in enumerate(points_zero)])

            # встановлюємо текст лейблу / setting the label text
            points_zero_label.configure(text=points_zero_text)

            even_or_odd = check_even_odd_func(expr)  # перевіряємо, чи функція парна чи непарна / check if the function is even or odd
            even_or_odd_func_l.configure(text = f'{even_or_odd}')

            try:
                sign_intervals = find_sign_intervals(expr)  # знаходимо інтервали знакосталості функції / find sign intervals of the function
                all_sign_intervals_text = ""
                for interval, sign in sign_intervals:
                    all_sign_intervals_text += f"{sign} при х ∈ {interval}\n"  # додаємо кожний інтервал у текст / adding each interval to the text

                intervals_identity_l.configure(text=f"8) Проміжки знакосталості:\n{all_sign_intervals_text}")  # оновлюємо лейбл для інтервалів знакосталості / update the label for sign intervals
            except Exception as e:
                print(f"Помилка обчислення проміжків знакосталості: {e}")  # помилка під час обчислення інтервалів знакосталості / error calculating sign intervals
                intervals_identity_l.configure(text="8) Проміжки знакосталості:\nнеможливо обчислити")  # не вдалося обчислити інтервали знакосталості / unable to calculate sign intervals

            punctured_dots(expr)  # перевіряємо наявність точок розриву у функції / check for punctured points in the function

            # except Exception as e:
            #     print(f"Помилка: {e}")  # обробляємо помилки / handle errors

# функція для кнопки / function for the button
def build_graphic():
    plot_graph(ax, canvas)  # виклик функції побудови графіка / calling the function to plot the graph