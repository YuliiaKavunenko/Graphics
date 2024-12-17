'''
Файл де створюються потрібні функції для прив'язки до кнопок/чекбоксів на вікні / File where required functions are created for binding to buttons/checkboxes on the window
'''
# Імпортуємо numpy і sympy для роботи з математичними символами / Importing numpy and sympy for working with math symbols
import numpy, sympy
# Імпортуємо бібліотеку ticker з matplotlib для роботи з графіками / Importing library ticker from matplotlib for working with graphs
import matplotlib.ticker as ticker
# Імпортуємо усі елементи головного вікна з main_elements / Importing all main window elements from another module
from .main_elements import *

# листи для збереження графіку і його похідних, y = ax**3 + bx**2 + cx + d / lists for storing the graph and its derivatives, y = ax**3 + bx**2 + cx + d
plots = []
plot_2 = None
plot_3 = None

# листи для збереження графіку і його похідних, у = (x**2 - a)/(x - b) / lists for storing the graph and its derivatives, y = (x**2 - a)/(x - b)
plots_2d = []
plot_2_2 = None
plot_3_2 = None

# листи для збереження точок перетину, перегину і пунктирних ліній, y = ax**3 + bx**2 + cx + d / lists for storing intersection points, inflection points, and dashed lines, y = ax**3 + bx**2 + cx + d
ox_points_first = []
h_lines_first = []

ox_points_second = []
h_lines_second = []
inflection_points_scatter = []

# листи для збереження точок локального макс. і мін. функції, y = ax**3 + bx**2 + cx + d / lists for storing local max and min points of the function, y = ax**3 + bx**2 + cx + d
local_max_scatter = None
local_min_scatter = None

local_max_scatter_s = None
local_min_scatter_s = None

local_min_scatter_text = None
local_max_scatter_text = None

# листи для збереження точок локального макс. і мін. функції, у = (x**2 - a)/(x - b) / lists for storing local max and min points of the function, y = (x**2 - a)/(x - b)
local_max_scatter_2 = None
local_min_scatter_2 = None

local_max_scatter_text_2 = None
local_min_scatter_text_2 = None

# листи для збереження точок перетину, перегину і пунктирних ліній, y = (x**2 - a**2)/x / lists for storing intersection points, inflection points, and dashed lines, y = (x**2 - a**2)/x
ox_points_third_first = []
ox_points_third_second = []
h_lines_third_first = []
h_lines_third_second = []
inflection_points_third_scatter = []

# листи для збереження графіку і його похідних, y = (x**2 - a**2)/x / lists for storing the graph and its derivatives, y = (x**2 - a**2)/x
plot_third_first = None
plot_third_second = None

# листи для збереження точок локального макс. і мін. функції, y = (x**2 - a**2)/x / lists for storing local max and min points of the function, y = (x**2 - a**2)/x
local_max_third_first = None
local_min_third_first = None
local_max_text_third_first = None
local_min_text_third_first = None

# листи для збереження графіку і його похідних, y = x/(x**2 + a) / lists for storing the graph and its derivatives, y = x/(x**2 + a)
plot_fourth_first = None
plot_fourth_second = None

# листи для збереження точок перетину, перегину і пунктирних ліній, y = x/(x**2 + a) / lists for storing intersection points, inflection points, and dashed lines, y = x/(x**2 + a)
ox_points_fourth_first = []
h_lines_fourth_first = []

ox_points_fourth_second = []
h_lines_fourth_second = []
inflection_points_fourth_scatter = []

# листи для збереження точок локального макс. і мін. функції, y = x/(x**2 + a) / lists for storing local max and min points of the function, y = x/(x**2 + a)
local_max_fourth_first = None
local_min_fourth_first = None
local_max_text_fourth_first = None
local_min_text_fourth_first = None

# кольори для елементів у вікні  / colors for elements in the window
# колір для фону вікна / color for window background
background = "#A76E56"
# колір для фону фреймів / color for frame background
frame_background = "#BA7D65"
# колір для тексту label / color for label text
text_color = "#392D20"
# колір для фону кнопки / color for button background
button_color = "#7B4C39"
# колір для тексту кнопки / color for button text
text_button_color = "#F1D5BA"
# колір для фону input / color for input background
input_color = "#FAF0E6"
# колір для бортиків input / color for input borders
input_border_color = "#EAD1B8"
# колір для внутрішнього тексту input / color for input placeholder text
input_textholder_color = "#CAA37D"
# колір при наведенні на кнопку scroll frame (меню усіх базових функцій) / color when hovering over the scroll frame button (menu of all basic functions)
hover_color_menu = "#F3E4D5"
# колір при наведенні на кнопку / color when hovering over the button
button_hover_color = "#9D6249"
# колір при наведенні на checkbox / color when hovering over the checkbox
checkbox_hover_color = "#EBCDAE"

# функція для розташування кольорових лейблів / function for placing colored labels
def build_colors_labels():
    red_gr.place(x = 1031, y = 25)
    green_gr.place(x = 1031, y = 70)
    blue_gr.place(x = 1031, y = 115)

# функція для зміни фокусу з інпута на інший елемент головного вікна / function to change focus from input to another element on the main window
def focus_on_elements(event):
    main.focus_set()
    print(f"Focus on main window")

# функція для побудови ДСК на холсті / function to build the coordinate grid on the canvas
def build_DSK():
    # Встановлюємо сітку (фон в клітинку) / setting the grid (background in grid)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='black')

    # Створюємо осі ох та оу / creating the x and y axes
    ax.axhline(y=0, color='black', linewidth=1.5)
    ax.axvline(x=0, color='black', linewidth=1.5)

    # Діапазон значень по осях / setting the range of values on the axes
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])

    # Встановлюємо положення міток на осях (з обох боків осей) / setting the position of labels on the axes (on both sides of the axes)
    ax.xaxis.set_ticks_position('both')
    ax.yaxis.set_ticks_position('both')

    # Додаємо мітки до осей / adding labels to the axes
    ax.set_xlabel('x', color='black')
    ax.set_ylabel('y', color='black', rotation=0, labelpad=15, ha='right')

    # Встановлюємо колір міток на осях / setting the color of labels on the axes
    ax.tick_params(axis='x', colors='black')
    ax.tick_params(axis='y', colors='black')

    # Встановлюємо крок сітки / setting the grid step
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

    # Встановлюємо положення міток осей поруч з осями / setting the position of axis labels next to the axes
    ax.xaxis.set_label_coords(1.05, 0.5)
    ax.yaxis.set_label_coords(0.5, 1.05)

    # Переміщення значення по осям / moving value along the axes
    ax.xaxis.set_tick_params(pad=-260)
    ax.yaxis.set_tick_params(pad=-225)

    # Колір для фона ДСК / color for the coordinate grid background
    ax.set_facecolor('#FAF0E6')

    canvas.draw()

# функція для відображення фрейму базових функцій для побудови / function to display the frame with basic functions for building
def appear_menu(event):
    # Очищення frame_menu від існуючих кнопок всередині / clearing frame_menu from existing buttons inside
    for button in frame_menu.winfo_children(): # winfo_children to get all child widgets of frame_menu
        button.destroy()
    frame_menu.place(x = 743, y = 59)
    # Фрейм поверх всіх елементів вікна / frame above all window elements
    frame_menu.lift()
    input_graphic.lift(frame_menu)
    # список наших базових функцій / a list of our core features
    el_functions = [
                    'x', '1/x', 'sqrt(x)', 'abs(x)', 'x**2', 'x**3', 
                    'x**-2', 'x**-3', 'x**(1/2)', 'x**(2/3)',
                    'x**(-1/2)', 'x**(-2/3)', 'sin(x)', 'cos(x)', 
                    'tan(x)', 'cot(x)', 'arccos(x)', 'arcsin(x)',
                    'arctan(x)'
                    ]
    # створення кнопок для вибору функцій / creation of buttons for selecting functions
    for func in el_functions:
        func_button = ctk.CTkButton(
            master=frame_menu,
            text=func,
            width=195, 
            height=40,
            anchor='w',
            fg_color=input_border_color,
            hover_color=hover_color_menu,
            text_color=text_color,
            font=("Roboto Slab", 15),
            command=lambda f=func: frame_buttons_func(f)  # Використання lambda для передачі тексту функції / using lambda to pass function text
        )
        func_button.pack(pady=2, anchor='w')

# функція для зникнення меню базових функцій / function to hide the menu of basic functions
def disappear_menu(event):
    frame_menu.place_forget()

# функція для пошуків проміжків спадання і зростання функції, локал. макс. і мін. і макс. і мін. значення функції / 
# function to find intervals of decrease and increase of the function, local max and min, and max and min values of the function
def find_intervals(first_dev, function):
    x = sympy.symbols('x')  # створюємо символ x / creating the symbol x
    # знаходимо критичні точки (значення x, при яких перша похідна дорівнює нулю) / finding critical points (values of x where the first derivative is zero)
    crit_points = sympy.solve(first_dev, x)
    
    # залишаємо тільки дійсні критичні точки і знаходимо їх числове значення / keeping only real critical points and finding their numeric values
    crit_points = [float(point.evalf()) for point in crit_points if point.is_real]
    # додаємо граничні точки інтервалу [-10, 10] до критичних точок / adding boundary points of the interval [-10, 10] to the critical points
    crit_points = [-10] + crit_points + [10]

    # створюємо список для збереження інтервалів і їх властивостей (зростання/спадання) / creating a list to store intervals and their properties (increase/decrease)
    intervals = []
    local_max = []
    local_min = []
    
    # Проходимо по всім парам сусідніх критичних точок / Iterating through all pairs of adjacent critical points
    for i in range(len(crit_points) - 1):
        left = crit_points[i]  # лівий кінець інтервалу / left end of the interval
        right = crit_points[i + 1]  # правий кінець інтервалу / right end of the interval
        midpoint = (left + right) / 2  # середня точка інтервалу / midpoint of the interval
        
        # Перевіряємо, чи є значення в середині інтервалу дійсним і визначеним / Checking if the value in the middle of the interval is real and defined
        midpoint_value = first_dev.subs(x, midpoint)
        if midpoint_value.is_real and not midpoint_value.has(sympy.zoo, sympy.nan, sympy.oo, sympy.I):
            # якщо похідна > 0, функція зростає / if the derivative > 0, the function increases
            if midpoint_value > 0:
                intervals.append((left, right, "- проміжок зростання"))  # increasing interval
            # якщо похідна < 0, функція спадає / if the derivative < 0, the function decreases
            else:
                intervals.append((left, right, "- проміжок спадання"))  # decreasing interval
        else:
            # якщо похідна не визначена або комплексна / if the derivative is undefined or complex
            intervals.append((left, right, "- не існує"))  # interval does not exist
    
    # Знаходимо локальні максимуми та мінімуми / Finding local maxima and minima
    for point in crit_points[1:-1]:  # Виключаємо граничні точки інтервалу / Excluding boundary points of the interval
        second_dev = sympy.diff(first_dev, x)  # Обчислюємо другу похідну функції / Calculating the second derivative of the function
        curvature = second_dev.subs(x, point)  # Знаходимо значення другої похідної в критичній точці / Finding the value of the second derivative at the critical point
        
        # якщо друга похідна < 0, це локальний максимум / if the second derivative < 0, it is a local maximum
        if curvature.is_real and not curvature.has(sympy.zoo, sympy.nan, sympy.oo, sympy.I):
            if curvature < 0:
                local_max.append((point, function.subs(x, point)))
            # якщо друга похідна > 0, це локальний мінімум / if the second derivative > 0, it is a local minimum
            elif curvature > 0:
                local_min.append((point, function.subs(x, point)))

    # Знаходимо максимальне і мінімальне значення функції на інтервалі [-10, 10] / Finding the maximum and minimum values of the function on the interval [-10, 10]
    boundary_values = [(point, function.subs(x, point)) for point in crit_points]
    global_max = max(boundary_values, key=lambda t: t[1])
    global_min = min(boundary_values, key=lambda t: t[1])

    print(f'{local_max} - local max', f'{local_min} - local min')

    return {
        'інтервали': intervals,  # intervals
        'локальний максимум': local_max,  # local maximum
        'локальний мінімум': local_min,  # local minimum
        'макс. значення ф-ції': global_max,  # maximum value of the function
        'мін. значення ф-ції': global_min  # minimum value of the function
    }

# функція яка перетворює отриману відповідь у математичну потрібну для Д(у) / function that converts the obtained answer into the mathematical one needed for D(y)
def scope_of_function(expr):
    x = sympy.symbols('x')  # створення символа x / creating the symbol x
    domain = sympy.calculus.util.continuous_domain(expr, x, sympy.S.Reals)  # визначення області визначення виразу / determining the domain of the expression
    intervals = []  # створення листу для збереження інтервалів області визначення (D(y)) / creating a list to store intervals of the domain (D(y))
    
    if isinstance(domain, sympy.Set):  # перевірка, що domain є об'єктом Set в sympy / checking that domain is a Set object in sympy
        if domain.is_Interval:  # перевірка, що domain є інтервалом / checking that domain is an interval
            intervals.append(domain)  # додавання інтервала в лист intervals / adding the interval to the intervals list
        elif domain.is_Union:  # перевірка, що domain є об'єднанням інтервалів / checking that domain is a union of intervals
            for subdomain in domain.args:  # перебираємо кожен підінтервал в об'єднанні / iterating through each subinterval in the union
                if subdomain.is_Interval:  # перевірка, що підінтервал є інтервалом / checking that subinterval is an interval
                    intervals.append(subdomain)  # додавання підінтервала до списку intervals / adding the subinterval to the intervals list

    print(intervals)
                    
    return intervals  # повертаємо список інтервалів області визначення / returning the list of domain intervals

# Д(у)
def format_intervals(intervals):
    formatted_intervals = []  # створення списку для збереження відформатованих інтервалів / creating a list to store formatted intervals
    
    for interval in intervals:  # перебираємо кожен інтервал у списку intervals / iterating through each interval in the intervals list
        # визначення типу дужки для лівої границі інтервала / determining the type of bracket for the left boundary of the interval
        left_bracket = "[" if interval.left_open == False else "("
        left = f"{left_bracket}{round(interval.start)}" if interval.start != -sympy.oo else "(-∞"

        # визначення типу дужки для правої границі інтервала / determining the type of bracket for the right boundary of the interval
        right_bracket = "]" if interval.right_open == False else ")"
        right = f"{round(interval.end)}{right_bracket}" if interval.end != sympy.oo else "∞)"
        
        formatted_intervals.append(f"{left}; {right}")  # форматування інтервалу і додавання до списку formatted_intervals / formatting the interval and adding to the formatted_intervals list
    
    if not formatted_intervals:  # якщо список formatted_intervals порожній / if the formatted_intervals list is empty
        return "∅"  # повертаємо рядок, який вказує на порожню область визначення / returning a string indicating an empty domain
    elif len(formatted_intervals) == 1 and formatted_intervals[0] == "(-∞; ∞)":  # якщо є тільки один інтервал і це весь діапазон дійсних чисел / if there is only one interval and it is the entire range of real numbers
        return "R"  # повертаємо рядок, що на область є дійсною для усіх чисел / returning a string indicating the domain is all real numbers
    else:
        return " ∪ ".join(formatted_intervals)  # об'єднання всіх інтервалів за допомогою символа "∪" і повернення у типі строки / joining all intervals with the symbol "∪" and returning as a string
# функція для побудови графіка / function to plot the graph
def plot_graph(ax, canvas):
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
            
# функція для побудови функцій-констант / function for constructing constant functions
def plot_constant_function(a, color):
    # створення значень x в діапазоні від -10 до 10 / creating x values in the range from -10 to 10
    x_vals = numpy.linspace(-10, 10, 400)
    # створення значень y, які дорівнюють a для кожного значення x / creating y values equal to a for each x value
    y_vals = [a] * len(x_vals)
    # побудова графіка константної функції / plotting the constant function
    plot_const, = ax.plot(x_vals, y_vals, label=f'y = {a}', color=color)
    plots.append(plot_const)  # додавання графіка до списку / adding the plot to the list
    # додаємо легенду / adding the legend
    ax.legend()
    legend = ax.legend()
    for text in legend.get_texts():
        text.set_color('red')  # встановлюємо червоний колір тексту легенди / setting the legend text color to red
    canvas.draw()  # перерисовуємо холст / redrawing the canvas
    return plot_const  # повертаємо графік константної функції / returning the constant function plot

# функція для кнопки / function for the button
def build_graphic():
    plot_graph(ax, canvas)  # виклик функції побудови графіка / calling the function to plot the graph
# первый график с похидними
def build_graphic_1():
    global plots
    
    ax.clear()
    build_DSK()

    a = a_1.get()
    b = b_1.get()
    c = c_1.get()
    d = d_1.get()

    #похідні
    

    if a and b and c and d:
        # try:
        # ставим чекбоксы
        first_dev.place(x = 1055, y = 70)
        second_dev.place(x = 1055, y = 115)
        main_graphic_label.place(x = 1055, y = 25)
        build_colors_labels()
        # Удаления значения в похідних что  б не было ошибки повторения символов
        a_2.delete(0,"end")
        b_2.delete(0,"end")
        c_2.delete(0,"end")

        a_3.delete(0,"end")
        b_3.delete(0,"end")
        
        x = sympy.symbols('x')
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)

        expr = a*x**3 + b*x**2 + c*x + d
        if isinstance(expr, sympy.Number):
            const_plot = plot_constant_function(float(expr), 'blue')
        else:
            global func1
            func1 = sympy.lambdify(x, expr, 'numpy')

            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func1(x_vals)

            plot, = ax.plot(x_vals, y_vals, label=f'y = {a}x^3 + {b}x^2 + {c}x + {d}', color='red')
            plots.append(plot)

            ax.legend()
            legend = ax.legend()
            for text in legend.get_texts():
                text.set_color('red')
            canvas.draw()

            
            # замена значения для похідних
            a_2.insert(0,f"{int(a)}")
            b_2.insert(0,f"{int(b)}")
            c_2.insert(0, f"{int(c)}")

            a_3.insert(0,f"{int(a)}")
            b_3.insert(0,f"{int(b)}")
            domain = scope_of_function(expr)
            domain_text = f"1) D(y) = {format_intervals(domain)}"
            scope_label.configure(text=domain_text)

            # перетин 0х і 0у
            points_0x_0y = points_ox_oy(expr,'red', True)
            points_zero = points_0x_0y['points_zero']

            points_0x_text = "; ".join([f"({x:.2f}, 0)" for x in points_zero])  # 0x-координаты

            # отримуємл координати і точку 0у
            oy_point = points_0x_0y['0y']
            oy_text = "не існує"
            if oy_point:
                offsets = oy_point.get_offsets()  # координати точки
                if len(offsets) > 0:
                    oy_coords = offsets[0]  # перша точка
                    oy_text = f"(0, {oy_coords[1]:.2f})"

            points_0x_0y_text = (
                f"6) Точки перетину з Ox:\n{points_0x_text}\n"
                f"Точка перетину з Oy:\n{oy_text}"
            )

            points_ox_oy_label.configure(text=points_0x_0y_text)

            # Отримуємо список точок нулів функції
            points_zero = points_0x_0y['points_zero']

            # Формуємо текст для лейблу
            points_zero_text = "7) Нулі функції: " + ", ".join([f"x{i+1} = {point}" for i, point in enumerate(points_zero)])

            # Встановлюємо текст лейблу
            points_zero_label.configure(text=points_zero_text)

            even_or_odd = check_even_odd_func(expr)
            even_or_odd_func_l.configure(text = f'{even_or_odd}')

            try:
                sign_intervals = find_sign_intervals(expr)
                all_sign_intervals_text = ""
                for interval, sign in sign_intervals:
                    all_sign_intervals_text += f"{sign} при х ∈ {interval}\n"  # додаємо кожний інтервал у текст

                intervals_identity_l.configure(text=f"8) Проміжки знакосталості:\n{all_sign_intervals_text}")
            except Exception as e:
                print(f"Помилка обчислення проміжків знакосталості: {e}")
                intervals_identity_l.configure(text="8) Проміжки знакосталості:\nнеможливо обчислити")

            punctured_dots(expr)

            print(range)

            print(plots)
            # except Exception as e:
            #     print(f"Помилка першого графіку: {e}")
            print(plots)

def clean_button():
    first_dev.place_forget()
    second_dev.place_forget()
    ax.clear()
    a_1.delete(0,"end")
    b_1.delete(0,"end")
    c_1.delete(0,"end")
    d_1.delete(0,"end")

    a_2.delete(0,"end")
    b_2.delete(0,"end")
    c_2.delete(0,"end")

    a_3.delete(0,"end")
    b_3.delete(0,"end")

    a_drob_1.delete(0,"end")
    a_drob_3.delete(0,"end")

    a_th_drob.delete(0,"end")

    a4_drob.delete(0,"end")

    input_graphic.delete(0,"end")

    local_max_min_label.configure(text = '4) Локальний макс. і мін. функції')

    even_or_odd_func_l.configure(text = '2) Парна чи непарна ф-ція')

    zn_function_label.configure(text = '5) Мін. і макс. значення функції')

    interval_label.configure(text = '3) Проміжок спадання і зростання функції')

    scope_label.configure(text = '1) Область визначення функції')

    drob_first_dev_lable.configure(text = "y' = ")
    drob_second_dev_lable.configure(text = "y'' = ")

    third_f_dev_label.configure(text = "y' = ")
    third_s_dev_label.configure(text = "y'' = ")

    fourth_f_dev_label.configure(text = "y' = ")
    fourth_s_dev_label.configure(text = "y'' = ")

    points_ox_oy_label.configure(text="6) Точки перетину з осями ох і оу")

    points_zero_label.configure(text="7) Нулі функції")

    intervals_identity_l.configure(text = '8) Проміжки знакосталості ф-ції')

    inflection_points_label.configure(text = '9) Точки перегину')

    convexity_intervals_label.configure(text = '10) Проміжки опуклості')

    slope_asymptote.configure(text = '11) Похила асимптота')

    main_graphic_label.place_forget()

    build_DSK()

def check_first_dev():
    global plots, plot_2, local_max_scatter, local_min_scatter, local_max_scatter_text, local_min_scatter_text
    global ox_points_first, h_lines_first

    check = first_dev.get()
    if check == 1:
        # Обчислення й побудова графіка першої похідної
        a = a_2.get()
        b = b_2.get()
        c = c_2.get()

        a_f = a_1.get()
        b_f = b_1.get()
        c_f = c_1.get()
        d_f = d_1.get()

        if a and b and c:
            x = sympy.symbols('x')
            a = float(a)
            b = float(b)
            c = float(c)

            a_f = float(a_f)
            b_f = float(b_f)
            c_f = float(c_f)
            d_f = float(d_f)

            function = a_f * x**3 + b_f * x**2 + c_f * x + d_f
            expr = 3 * a * x**2 + 2 * b * x + c

            if isinstance(expr, sympy.Number):
                plot_2 = plot_constant_function(float(expr), 'green')
            else:
                func = sympy.lambdify(x, expr, 'numpy')
                x_vals = numpy.linspace(-10, 10, 400)
                y_vals = func(x_vals)

                plot_2, = ax.plot(x_vals, y_vals, label=f'y = 3*{a}x^2 + 2*{b}x + {c}', color='green')
                plots.append(plot_2)

                ax.legend()
                legend = ax.legend()
                for text in legend.get_texts():
                    text.set_color('red')
                canvas.draw()

                

            # Обчислення точок локального максимуму та мінімуму
            intervals_data = find_intervals(expr, function)

            # Видалення старих точок, якщо вони є
            if local_max_scatter:
                local_max_scatter.remove()
                local_max_scatter_text.remove()
                local_max_scatter = None
                local_max_scatter_text = None
            if local_min_scatter:
                local_min_scatter.remove()
                local_min_scatter_text.remove()
                local_min_scatter = None
                local_min_scatter_text = None

            # видалення старих точок перетину и пунктирних ліній
            if ox_points_first:
                for point in ox_points_first:
                    point.remove()
                ox_points_first.clear()
            if h_lines_first:
                for line in h_lines_first:
                    line.remove()
                h_lines_first.clear()

            # 0х і пунктирні лінії
            points_0x_0y = points_ox_oy(expr, 'green', label=False, lines=True, include_oy=False)
            ox_points_first = points_0x_0y['0x']
            h_lines_first = points_0x_0y['lines']

            # додавання нових точок
            if len(intervals_data['локальний максимум']) != 0:
                local_max = intervals_data['локальний максимум'][0]
                l_max_x, l_max_y = local_max
                local_max_scatter = ax.scatter(l_max_x, l_max_y, color='#FF0899', s=40)
                local_max_scatter_text = ax.annotate(f'({l_max_x:.2f}, {l_max_y:.2f})',
                                                     (l_max_x, l_max_y),
                                                     textcoords="offset points",
                                                     xytext=(15, 15),
                                                     ha='center')

            if len(intervals_data['локальний мінімум']) != 0:
                local_min = intervals_data['локальний мінімум'][0]
                l_min_x, l_min_y = local_min
                local_min_scatter = ax.scatter(l_min_x, l_min_y, color='#FF0899', s=40)
                local_min_scatter_text = ax.annotate(f'({l_min_x:.2f}, {l_min_y:.2f})',
                                                     (l_min_x, l_min_y),
                                                     textcoords="offset points",
                                                     xytext=(15, 15),
                                                     ha='center')
            
            if len(intervals_data['інтервали']) != 0:
                interval_text = "\n".join([f"({left:.2f}; {right:.2f}) {state}" for left, right, state in intervals_data['інтервали']])
            else:
                interval_text = "Інтервалів зростання/спадання не існує"

            interval_label.configure(text=f'3) {interval_text}')

        

            
            # Формуємо текст для локальних максимумів і мінімумів
            if len(intervals_data['локальний максимум']) != 0:
                local_max_text = "Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
            else:
                local_max_text = "Локальний максимум: не існує"

            if len(intervals_data['локальний мінімум']) != 0:
                local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
            else:
                local_min_text = "Локальний мінімум: не існує"


            # макс значення функції
            if intervals_data['макс. значення ф-ції']:
                funct_max_text = f"Макс. значення ф-ції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
            else:
                funct_max_text = "Макс. значення ф-ції: не існує"

            # Мінімальне значення функції
            if intervals_data['мін. значення ф-ції']:
                func_min_text = f"Мін. значення ф-ції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
            else:
                func_min_text = "Мін. значення ф-ції: не існує"
            local_max_min_text =f'4) {local_max_text}\n{local_min_text}'
            local_max_min_label.configure(text = local_max_min_text)

            zn_function_text = f'5) {funct_max_text}\n{func_min_text}'
            zn_function_label.configure(text =zn_function_text)

            


            # except Exception as e:
            #     print(f"Помилка другого графіку: {e}")

            canvas.draw()

    elif check == 0 and plot_2 in plots:
        # Видалення графіка та точок
        plot_2.remove()
        plots.remove(plot_2)

        if local_max_scatter:
            local_max_scatter.remove()
            local_max_scatter_text.remove()
            local_max_scatter = None
            local_max_scatter_text = None

        if local_min_scatter:
            local_min_scatter.remove()
            local_min_scatter_text.remove()
            local_min_scatter = None
            local_min_scatter_text = None

        # видалення точек пересечения и пунктирных линий

        if ox_points_first:
            for point in ox_points_first:
                point.remove()
            ox_points_first.clear()
        if h_lines_first:
            for line in h_lines_first:
                line.remove()
            h_lines_first.clear()

        ax.legend().remove()
        ax.legend()
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')
        canvas.draw()
        print("NO FIRST DEV!")


def check_second_dev():
    global plots, plot_3, func1, ox_points_second, h_lines_second, inflection_points_scatter, inflection_points_l

    check = second_dev.get()
    if check == 1:  
        a = a_3.get()
        b = b_3.get()

        if a and b:
            # try:
            x = sympy.symbols('x')
            a = float(a)
            b = float(b)
# y = 6*           *x + 2*         
            # func = sympy.lambdify(x, expr, 'numpy')
            expr = 6*a*x + 2*b

            if isinstance(expr, sympy.Number):
                plot_3 = plot_constant_function(float(expr), 'blue')
            else:
                # Отримуємо точки перегину
                inflection_points = find_inflection_points(expr)

                inflection_points_scatter = []  # лист для точек перегиба
                inflection_points_l = [] # підпис точки

                # форматований рядок для лейбла
                formatted_points = "; ".join([f"x{i+1} = {point}" for i, point in enumerate(inflection_points)])

                # виводимо точки перегину на графіку
                for point in inflection_points:
                    # Обчислюємо значення функції в точці перегину
                    y_inflection = func1(point)
                    # Малюємо точки перегину на графіку
                    scatter = ax.scatter(point, y_inflection, color='blue', zorder=5)
                    inflection_points_scatter.append(scatter)  # Сохраняем объект точки
                    label_point_inflection = ax.annotate(f'({point:.1f}, {y_inflection:.1f})', # з округленням
                                (point, y_inflection),
                                textcoords="offset points", 
                                xytext=(0, 10),
                                ha='center', color='blue')
                    inflection_points_l.append(label_point_inflection)

                # Оновлюємо лейбл з точками перегину
                inflection_points_label.configure(text=f"9) Точки перегину: {formatted_points}")
                func = sympy.lambdify(x, expr, 'numpy')

                x_vals = numpy.linspace(-10, 10, 400)
                y_vals = func(x_vals)

                plot_3, = ax.plot(x_vals, y_vals, label=f'y = 6*{a}x + 2 * {b}', color='blue')
                plots.append(plot_3)

                # Построение точек пересечения 0x и пунктирных линий
                points_0x_0y = points_ox_oy(expr, 'blue', label=False, lines=True, include_oy=False)
                ox_points_second = points_0x_0y['0x']  # Графические объекты точек пересечения
                h_lines_second = points_0x_0y['lines']  # Графические объекты пунктирных линий

                # знайти проміжки опуклості
                convexity_intervals = find_convexity_intervals(expr)

                # створити текст для лейблу
                convexity_text = "Проміжки опуклості графіка:\n"
                for interval, convexity in convexity_intervals:
                    left, right = interval
                    left = "-∞" if left == float('-inf') else f"{left:.2f}"
                    right = "+∞" if right == float('inf') else f"{right:.2f}"
                    convexity_text += f"{convexity} при x ∈ ({left}; {right})\n"

                # вивести у лейбл
                convexity_intervals_label.configure(text=convexity_text)
                ax.legend()
                legend = ax.legend()

                for text in legend.get_texts():
                    text.set_color('red')
                canvas.draw()

                # except Exception as e:
                #     print(f"Помилка третьої похідної: {e}")
    elif check == 0 and plot_3 in plots:
        plot_3.remove()
        plots.remove(plot_3)

        # видалення точок перетину і пунктирних ліній
        if ox_points_second:
            for point in ox_points_second:
                point.remove()
            ox_points_second.clear()
        if h_lines_second:
            for line in h_lines_second:
                line.remove()
            h_lines_second.clear()

        # видалення точок перегину
        for scatter in inflection_points_scatter:
            scatter.remove()
        inflection_points_scatter.clear()
        # видалення підпису точок
        for label in inflection_points_l:
            label.remove()
        inflection_points_l.clear()



        ax.legend().remove()
        ax.legend()
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')
        canvas.draw()
        print("NOT SECOND DEV!")
# второй график с похидними
def build_drob_graphic():
    global plots
    ax.clear()
    build_DSK()
    a = a_drob_1.get()
    b_data_3 = a_drob_3.get()
    # чекбокси
    first_dev_fdrob.place(x = 1055, y =70)
    second_dev_fdrob.place(x = 1055, y = 115)
    main_graphic_label.place(x = 1055, y = 25)
    build_colors_labels()
    if a and b_data_3:
        # try:
        
        x = sympy.symbols('x')
        a = float(a)
        b_data_3 = float(b_data_3)
#  (х*х-а*а)/(х-а)
        expr = (x**2-a)/(x-b_data_3)
        if isinstance(expr, sympy.Number):
            plot_constant_function(float(expr),'red')
        else:
            func = sympy.lambdify(x, expr, 'numpy')

            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)

            plot, = ax.plot(x_vals, y_vals, label=f'y = (х²-{a})/(х-{b_data_3})', color='red')
            plots.append(plot)

            ax.legend()
            legend = ax.legend()
            for text in legend.get_texts():
                text.set_color('red')
            canvas.draw()
            
            domain = scope_of_function(expr)
            domain_text = f"1) D(y) = {format_intervals(domain)}"
            scope_label.configure(text=domain_text)
            # перетин 0х і 0у
            points_0x_0y = points_ox_oy(expr,'red', True)
            points_zero = points_0x_0y['points_zero']

            points_0x_text = "; ".join([f"({x:.2f}, 0)" for x in points_zero])  # 0x-координаты

            # отримуємл координати і точку 0у
            oy_point = points_0x_0y['0y']
            oy_text = "не існує"
            if oy_point:
                offsets = oy_point.get_offsets()  # координати точки
                if len(offsets) > 0:
                    oy_coords = offsets[0]  # перша точка
                    oy_text = f"(0, {oy_coords[1]:.2f})"

            points_0x_0y_text = (
                f"6) Точки перетину з Ox:\n{points_0x_text}\n"
                f"Точка перетину з Oy:\n{oy_text}"
            )

            points_ox_oy_label.configure(text=points_0x_0y_text)

            # Отримуємо список точок нулів функції
            points_zero = points_0x_0y['points_zero']

            # Формуємо текст для лейблу
            points_zero_text = "7) Нулі функції: " + ", ".join([f"x{i+1} = {point}" for i, point in enumerate(points_zero)])

            # Встановлюємо текст лейблу
            points_zero_label.configure(text=points_zero_text)

            even_or_odd = check_even_odd_func(expr)
            even_or_odd_func_l.configure(text = f'{even_or_odd}')

            try:
                sign_intervals = find_sign_intervals(expr)
                all_sign_intervals_text = ""
                for interval, sign in sign_intervals:
                    all_sign_intervals_text += f"{sign} при х ∈ {interval}\n"  # додаємо кожний інтервал у текст

                intervals_identity_l.configure(text=f"8) Проміжки знакосталості:\n{all_sign_intervals_text}")
            except Exception as e:
                print(f"Помилка обчислення проміжків знакосталості: {e}")
                intervals_identity_l.configure(text="8) Проміжки знакосталості:\nнеможливо обчислити")

            slant_asymptote_label = slope_asymptote  # рівняння асимптоти
            find_and_plot_slant_asymptote(expr, x, label_widget = slope_asymptote)


            punctured_dots(expr)

            print(plots)
            # except Exception as e:
            #     print(f"Помилка першого графіку: {e}")
            print(plots)

def drob_first_dev():
    global plots_2d, plot_2_2, ox_points_first, h_lines_first, local_max_scatter_2, local_min_scatter_2
    global local_max_scatter_text_2, local_min_scatter_text_2

    check = first_dev_fdrob.get()
    if check == 1:

        a = a_drob_1.get()
        b_data_3 = a_drob_3.get()
        if a and b_data_3:
            # try:
            x = sympy.symbols('x')
            a = float(a)
            b_data_3 = float(b_data_3)
            function = (x**2-a)/(x-b_data_3)
            dev_of_function = sympy.diff(function, x)


            # обчислення локальних максимумів, мінімумів та інтервалів зростання/спадання
            intervals_data = find_intervals(dev_of_function, function)

            # видалення старих точок, якщо вони є
            if local_max_scatter_2:
                local_max_scatter_2.remove()
                local_max_scatter_text_2.remove()
                local_max_scatter_2 = None
                local_max_scatter_text_2 = None
            if local_min_scatter_2:
                local_min_scatter_2.remove()
                local_min_scatter_text_2.remove()
                local_min_scatter_2 = None
                local_min_scatter_text_2 = None

            # видалення точок перетину і пунктирних ліній
            if ox_points_first:
                for point in ox_points_first:
                    point.remove()
                ox_points_first.clear()
            if h_lines_first:
                for line in h_lines_first:
                    line.remove()
                h_lines_first.clear()

            # побудова нових точок перетину і пунктирних ліній
            points_0x_0y = points_ox_oy(dev_of_function, 'green', label=False, lines=True, include_oy=False)
            ox_points_first = points_0x_0y['0x']  # точки 0х
            h_lines_first = points_0x_0y['lines']  # пунктирні лінії

            # додавання нових точок локальних максимумів і мінімумів
            if len(intervals_data['локальний максимум']) != 0:
                local_max = intervals_data['локальний максимум'][0]
                l_max_x, l_max_y = local_max
                local_max_scatter_2 = ax.scatter(l_max_x, l_max_y, color='#FF0899', s=40)
                local_max_scatter_text_2 = ax.annotate(f'({l_max_x:.2f}, {l_max_y:.2f})',
                                                       (l_max_x, l_max_y),
                                                       textcoords="offset points",
                                                       xytext=(15, 15),
                                                       ha='center')

            if len(intervals_data['локальний мінімум']) != 0:
                local_min = intervals_data['локальний мінімум'][0]
                l_min_x, l_min_y = local_min
                local_min_scatter_2 = ax.scatter(l_min_x, l_min_y, color='#FF0899', s=40)
                local_min_scatter_text_2 = ax.annotate(f'({l_min_x:.2f}, {l_min_y:.2f})',
                                                       (l_min_x, l_min_y),
                                                       textcoords="offset points",
                                                       xytext=(15, 15),
                                                       ha='center')

            # оновлення тексту похідної
            drob_first_dev_lable.configure(text=f"y' = {dev_of_function}")

            if len(intervals_data['інтервали']) != 0:
                interval_text = "\n".join([f"({left:.2f}; {right:.2f}) {state}" for left, right, state in intervals_data['інтервали']])
            else:
                interval_text = "Інтервалів зростання/спадання не існує"

            interval_label.configure(text=f'3) {interval_text}')

            # Формуємо текст для локальних максимумів і мінімумів
            if len(intervals_data['локальний максимум']) != 0:
                local_max_text = "Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
            else:
                local_max_text = "Локальний максимум: не існує"

            if len(intervals_data['локальний мінімум']) != 0:
                local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
            else:
                local_min_text = "Локальний мінімум: не існує"

            # макс значення функції
            if intervals_data['макс. значення ф-ції']:
                funct_max_text = f"Макс. значення ф-ції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
            else:
                funct_max_text = "Макс. значення ф-ції: не існує"

            # Мінімальне значення функції
            if intervals_data['мін. значення ф-ції']:
                func_min_text = f"Мін. значення ф-ції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
            else:
                func_min_text = "Мін. значення ф-ції: не існує"

            local_max_min_text =f'4) {local_max_text}\n{local_min_text}'
            local_max_min_label.configure(text = local_max_min_text)

            zn_function_text = f'5) {funct_max_text}\n{func_min_text}'
            zn_function_label.configure(text =zn_function_text)

            drob_first_dev_lable.configure(
                text = f"y' = {dev_of_function}",
                
            )

            print(dev_of_function)

            expr = dev_of_function
            
            func = sympy.lambdify(x, expr, 'numpy')

            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)

            plot_2_2, = ax.plot(x_vals, y_vals, label=f"y' ={dev_of_function}", color='green')
            plots_2d.append(plot_2_2)

            ax.legend()
            legend = ax.legend()

            for text in legend.get_texts():
                text.set_color('red')
            canvas.draw()

            third_first_dev()
            




            # except Exception as e:
            #     print(f"Помилка першої дробовох похідної: {e}")
    elif check == 0 and plot_2_2 in plots_2d:
        # видалення графіка
        plot_2_2.remove()
        plots_2d.remove(plot_2_2)

        # видалення локальних максимумів та мінімумів
        if local_max_scatter_2:
            local_max_scatter_2.remove()
            local_max_scatter_text_2.remove()
            local_max_scatter_2 = None
            local_max_scatter_text_2 = None

        if local_min_scatter_2:
            local_min_scatter_2.remove()
            local_min_scatter_text_2.remove()
            local_min_scatter_2 = None
            local_min_scatter_text_2 = None

        # видалення точок 0х та пунктирних ліній
        if ox_points_first:
            for point in ox_points_first:
                point.remove()
            ox_points_first.clear()
        if h_lines_first:
            for line in h_lines_first:
                line.remove()
            h_lines_first.clear()

        ax.legend().remove()
        ax.legend()
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')
        canvas.draw()
        print("NO FIRST DEV!")

def drob_second_dev():
    global plots_2d, plot_3_2, ox_points_second, h_lines_second, inflection_points_scatter, inflection_points_label

    check = second_dev_fdrob.get()
    if check == 1:
        a = a_drob_1.get()
        b_data_3 = a_drob_3.get()

        if a and b_data_3:
            # try:
            x = sympy.symbols('x')
            a = float(a)
            b_data_3 = float(b_data_3)

            function = (x**2-a)/(x-b_data_3)


            dev_of_function = sympy.diff(function, x)

            second_dev_of_function = sympy.diff(dev_of_function, x)

            drob_second_dev_lable.configure(text = f"y'' = {second_dev_of_function}")

            expr = second_dev_of_function
            
            func = sympy.lambdify(x, expr, 'numpy')

            # видалення старих точок перегину, пунктирних ліній і точок 0х
            if inflection_points_scatter:
                for point in inflection_points_scatter:
                    point.remove()
                inflection_points_scatter.clear()

            if ox_points_second:
                for point in ox_points_second:
                    point.remove()
                ox_points_second.clear()

            if h_lines_second:
                for line in h_lines_second:
                    line.remove()
                h_lines_second.clear()

            # пошук і побудова точок перегину
            inflection_points = find_inflection_points(second_dev_of_function)
            for point in inflection_points:
                y_val = function.subs(x, point)
                scatter = ax.scatter(float(point), float(y_val), color='blue', zorder=5)
                inflection_points_scatter.append(scatter)

                ax.annotate(f'({float(point):.2f}, {float(y_val):.2f})',
                            (float(point), float(y_val)),
                            textcoords="offset points",
                            xytext=(0, 10),
                            ha='center', color='blue')

            # оновлення лейблу з точками перегину
            if inflection_points:
                formatted_points = "; ".join([f"x{i+1} = {float(pt):.2f}" for i, pt in enumerate(inflection_points)])
                inflection_points_label.configure(text=f"9) Точки перегину: {formatted_points}")
            else:
                inflection_points_label.configure(text="9) Точки перегину: не існує")

            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)

            plot_3_2, = ax.plot(x_vals, y_vals, label=f"y'' = {second_dev_of_function}", color='blue')
            plots_2d.append(plot_3_2)

             # побудова точок 0х і пунктирних ліній
            points_0x_0y = points_ox_oy(expr, 'blue', label=False, lines=True, include_oy=False)
            ox_points_second = points_0x_0y['0x']
            h_lines_second = points_0x_0y['lines']

            # # знайти проміжки опуклості
            # convexity_intervals = find_convexity_intervals(expr)

            # # створити текст для лейблу
            # convexity_text = "Проміжки опуклості графіка:\n"
            # for interval, convexity in convexity_intervals:
            #     left, right = interval
            #     left = "-∞" if left == float('-inf') else f"{left:.2f}"
            #     right = "+∞" if right == float('inf') else f"{right:.2f}"
            #     convexity_text += f"{convexity} при x ∈ ({left}; {right})\n"

            # # вивести у лейбл
            # convexity_intervals_label.configure(text=convexity_text)

            ax.legend()
            legend = ax.legend()
            
            for text in legend.get_texts():
                text.set_color('red')
            canvas.draw()

            # except Exception as e:
            #     print(f"Помилка другої дробової похідної: {e}")
    elif check == 0 and plot_3_2 in plots_2d:
        # видалення графіка
        plot_3_2.remove()
        plots_2d.remove(plot_3_2)

        # видалення точок 0х, пунктирних ліній і точок перегину
        if inflection_points_scatter:
            for point in inflection_points_scatter:
                point.remove()
            inflection_points_scatter.clear()

        if ox_points_second:
            for point in ox_points_second:
                point.remove()
            ox_points_second.clear()

        if h_lines_second:
            for line in h_lines_second:
                line.remove()
            h_lines_second.clear()

        ax.legend().remove()
        ax.legend()
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')
        canvas.draw()
        print("NO SECOND DEV!")

def build_third_func():
    global plots
    ax.clear()
    build_DSK()
    print('build!')
    a = a_th_drob.get()
    # чекбокси
    first_dev_sdrob.place(x = 1055, y = 70)
    second_dev_sdrob.place(x = 1055, y = 115)
    main_graphic_label.place(x = 1055, y = 25)
    build_colors_labels()
    if a:
        # try:
        
        x = sympy.symbols('x')
        a = float(a)
#  (х**2-а**2)/(х)
        expr = (x**2-a**2)/(x)
        if isinstance(expr, sympy.Number):
            plot_constant_function(float(expr),'red')
        else:
            func = sympy.lambdify(x, expr, 'numpy')

            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)

            plot, = ax.plot(x_vals, y_vals, label=f'y = (х²-{a}²)/(х)', color='red')
            plots.append(plot)

            ax.legend()
            legend = ax.legend()
            for text in legend.get_texts():
                text.set_color('red')
            canvas.draw()
            # похідні (в путі)
            third_first_dev()
            third_second_dev()
            # drob_second_dev()            
            domain = scope_of_function(expr)
            domain_text = f"1) D(y) = {format_intervals(domain)}"
            scope_label.configure(text=domain_text)

            # перетин 0х і 0у
            points_0x_0y = points_ox_oy(expr,'red', True)
            points_zero = points_0x_0y['points_zero']

            points_0x_text = "; ".join([f"({x:.2f}, 0)" for x in points_zero])  # 0x-координаты

            # отримуємл координати і точку 0у
            oy_point = points_0x_0y['0y']
            oy_text = "не існує"
            if oy_point:
                offsets = oy_point.get_offsets()  # координати точки
                if len(offsets) > 0:
                    oy_coords = offsets[0]  # перша точка
                    oy_text = f"(0, {oy_coords[1]:.2f})"

            points_0x_0y_text = (
                f"6) Точки перетину з Ox:\n{points_0x_text}\n"
                f"Точка перетину з Oy:\n{oy_text}"
            )

            points_ox_oy_label.configure(text=points_0x_0y_text)

            # Отримуємо список точок нулів функції
            points_zero = points_0x_0y['points_zero']

            # Формуємо текст для лейблу
            points_zero_text = "7) Нулі функції: " + ", ".join([f"x{i+1} = {point}" for i, point in enumerate(points_zero)])

            # Встановлюємо текст лейблу
            points_zero_label.configure(text=points_zero_text)

            even_or_odd = check_even_odd_func(expr)
            even_or_odd_func_l.configure(text = f'{even_or_odd}')

            try:
                sign_intervals = find_sign_intervals(expr)
                all_sign_intervals_text = ""
                for interval, sign in sign_intervals:
                    all_sign_intervals_text += f"{sign} при х ∈ {interval}\n"  # додаємо кожний інтервал у текст

                intervals_identity_l.configure(text=f"8) Проміжки знакосталості:\n{all_sign_intervals_text}")
            except Exception as e:
                print(f"Помилка обчислення проміжків знакосталості: {e}")
                intervals_identity_l.configure(text="8) Проміжки знакосталості:\nнеможливо обчислити")


            punctured_dots(expr)

            slant_asymptote_label = slope_asymptote  # рівняння асимптоти
            find_and_plot_slant_asymptote(expr, x, label_widget = slope_asymptote)

            print(plots)
            # except Exception as e:
            #     print(f"Помилка першого графіку: {e}")
            print(plots)

def third_first_dev():
    global plots, plot_third_first, ox_points_third_first, h_lines_third_first
    global local_max_third_first, local_min_third_first, local_max_text_third_first, local_min_text_third_first

    check = first_dev_sdrob.get()
    
    if check == 1:
        
        a = a_th_drob.get()
        if a:
            # try:
            x = sympy.symbols('x')
            a = float(a)

            function = (x**2-a**2)/(x)
            dev_of_function = sympy.diff(function, x)

            # видалення старих точок, ліній, графіка, максимумів і мінімумів
            if plot_third_first:
                plot_third_first.remove()
                plot_third_first = None

            if ox_points_third_first:
                for point in ox_points_third_first:
                    point.remove()
                ox_points_third_first.clear()

            if h_lines_third_first:
                for line in h_lines_third_first:
                    line.remove()
                h_lines_third_first.clear()

            if local_max_third_first:
                local_max_third_first.remove()
                local_max_text_third_first.remove()
                local_max_third_first = None
                local_max_text_third_first = None

            if local_min_third_first:
                local_min_third_first.remove()
                local_min_text_third_first.remove()
                local_min_third_first = None
                local_min_text_third_first = None



            # спадання зростання
            intervals_data = find_intervals(dev_of_function, function)
            if len(intervals_data['інтервали']) != 0:
                interval_text = "\n".join([f"({left:.2f}; {right:.2f}) {state}" for left, right, state in intervals_data['інтервали']])
            else:
                interval_text = "Інтервалів зростання/спадання не існує"

            interval_label.configure(text=f'3) {interval_text}')

            # Формуємо текст для локальних максимумів і мінімумів
            if len(intervals_data['локальний максимум']) != 0:
                local_max_text = "Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
            else:
                local_max_text = "Локальний максимум: не існує"

            if len(intervals_data['локальний мінімум']) != 0:
                local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
            else:
                local_min_text = "Локальний мінімум: не існує"

            # макс значення функції
            if intervals_data['макс. значення ф-ції']:
                funct_max_text = f"Макс. значення ф-ції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
            else:
                funct_max_text = "Макс. значення ф-ції: не існує"

            # Мінімальне значення функції
            if intervals_data['мін. значення ф-ції']:
                func_min_text = f"Мін. значення ф-ції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
            else:
                func_min_text = "Мін. значення ф-ції: не існує"

            local_max_min_text =f'4) {local_max_text}\n{local_min_text}'
            local_max_min_label.configure(text = local_max_min_text)

            zn_function_text = f'5) {funct_max_text}\n{func_min_text}'
            zn_function_label.configure(text =zn_function_text)

            drob_first_dev_lable.configure(
                text = f"y' = {dev_of_function}"
            )

            print(dev_of_function)

            expr = dev_of_function
            
            func = sympy.lambdify(x, expr, 'numpy')

            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)

            plot_third_first, = ax.plot(x_vals, y_vals, label=f"y' = {dev_of_function}", color='green')
            # plots.append(plot)
            # пошук точок перетину з Ox
            points_0x_0y = points_ox_oy(dev_of_function, 'green', label=False, lines=True, include_oy=False)
            ox_points_third_first = points_0x_0y['0x']
            h_lines_third_first = points_0x_0y['lines']

            # пошук локальних максимумів і мінімумів
            intervals_data = find_intervals(dev_of_function, function)
            if len(intervals_data['локальний максимум']) != 0:
                max_point = intervals_data['локальний максимум'][0]
                local_max_third_first = ax.scatter(max_point[0], max_point[1], color='#FF0899', s=40)
                local_max_text_third_first = ax.annotate(
                    f'({max_point[0]:.2f}, {max_point[1]:.2f})',
                    (max_point[0], max_point[1]),
                    textcoords="offset points",
                    xytext=(15, 15),
                    ha='center'
                )

            if len(intervals_data['локальний мінімум']) != 0:
                min_point = intervals_data['локальний мінімум'][0]
                local_min_third_first = ax.scatter(min_point[0], min_point[1], color='#FF0899', s=40)
                local_min_text_third_first = ax.annotate(
                    f'({min_point[0]:.2f}, {min_point[1]:.2f})',
                    (min_point[0], min_point[1]),
                    textcoords="offset points",
                    xytext=(15, 15),
                    ha='center'
                )

            ax.legend()
            legend = ax.legend()

            third_f_dev_label.configure(
                    text = f"y' = {dev_of_function}"
                )
            
            for text in legend.get_texts():
                text.set_color('red')
            canvas.draw()
        




            # except Exception as e:
            #     print(f"Помилка першої дробовох похідної: {e}")
    elif check == 0 and plot_third_first:
        # видалення графіка першої похідної
        plot_third_first.remove()
        plot_third_first = None

        # видалення точок і пунктирних ліній
        if ox_points_third_first:
            for point in ox_points_third_first:
                point.remove()
            ox_points_third_first.clear()

        if h_lines_third_first:
            for line in h_lines_third_first:
                line.remove()
            h_lines_third_first.clear()

        # видалення локальних максимумів і мінімумів
        if local_max_third_first:
            local_max_third_first.remove()
            local_max_text_third_first.remove()
            local_max_third_first = None
            local_max_text_third_first = None

        if local_min_third_first:
            local_min_third_first.remove()
            local_min_text_third_first.remove()
            local_min_third_first = None
            local_min_text_third_first = None

        ax.legend().remove()
        canvas.draw()

def third_second_dev():
    global plots, plot_third_second, ox_points_third_second, h_lines_third_second, inflection_points_third_scatter, inflection_points_th
    check = second_dev_sdrob.get()
    
    
    if check == 1:
        inflection_points_th = []
        a = a_th_drob.get()
        if a:
            # try:
            x = sympy.symbols('x')
            a = float(a)

            function = (x**2-a**2)/(x)

            dev_of_function = sympy.diff(function, x)

            second_dev_of_function = sympy.diff(dev_of_function, x)
            print(second_dev_of_function)

            drob_second_dev_lable.configure(text = f"y'' = {second_dev_of_function}")

            expr = second_dev_of_function
            
            func = sympy.lambdify(x, expr, 'numpy')

            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)

            # видалення старих елементів
            if plot_third_second:
                plot_third_second.remove()
                plot_third_second = None

            if inflection_points_third_scatter:
                for point in inflection_points_third_scatter:
                    point.remove()
                inflection_points_third_scatter.clear()

            if ox_points_third_second:
                for point in ox_points_third_second:
                    point.remove()
                ox_points_third_second.clear()

            if h_lines_third_second:
                for line in h_lines_third_second:
                    line.remove()
                h_lines_third_second.clear()

            plot_third_second, = ax.plot(x_vals, y_vals, label=f"y'' = {second_dev_of_function}", color='blue')
            # plots.append(plot)

            # пошук точок перегину
            inflection_points = find_inflection_points(second_dev_of_function)
            for point in inflection_points:
                y_val = function.subs(x, point)
                scatter = ax.scatter(float(point), float(y_val), color='blue', zorder=5)
                inflection_points_third_scatter.append(scatter)
                inflection_points_th_l = ax.annotate(
                    f'({float(point):.2f}, {float(y_val):.2f})',
                    (float(point), float(y_val)),
                    textcoords="offset points",
                    xytext=(0, 10),
                    ha='center',
                    color='blue'
                )
                inflection_points_th.append(inflection_points_th_l)

            # пошук точок пересічення з Ox і побудова пунктирних ліній
            points_0x_0y = points_ox_oy(second_dev_of_function, 'blue', label=False, lines=True, include_oy=False)
            ox_points_third_second = points_0x_0y['0x']
            h_lines_third_second = points_0x_0y['lines']

            ax.legend()
            legend = ax.legend()

            third_s_dev_label.configure(
                text = f"y'' = {second_dev_of_function}"
            )

            # оновлення лейблу з точками перегину
            if inflection_points:
                formatted_points = "; ".join([f"x{i+1} = {float(pt):.2f}" for i, pt in enumerate(inflection_points)])
                inflection_points_label.configure(text=f"9) Точки перегину: {formatted_points}")
            else:
                inflection_points_label.configure(text="9) Точки перегину: не існує")
            
            points_0x_0y = points_ox_oy(expr, 'blue', label=False, lines=True, include_oy=False)
            for text in legend.get_texts():
                text.set_color('red')
            canvas.draw()
    elif check == 0 and plot_third_second:
        # видалення графіка другої похідної
        plot_third_second.remove()
        plot_third_second = None

        # видалення точок перегину
        if inflection_points_third_scatter:
            for point in inflection_points_third_scatter:
                point.remove()
            inflection_points_third_scatter.clear()
                # видалення підпису точок
        for label in inflection_points_th:
            label.remove()
        inflection_points_th.clear()

        # видалення точок перетину з Ox і пунктирних ліній
        if ox_points_third_second:
            for point in ox_points_third_second:
                point.remove()
            ox_points_third_second.clear()

        if h_lines_third_second:
            for line in h_lines_third_second:
                line.remove()
            h_lines_third_second.clear()

        # оновлення легенди
        ax.legend().remove()
        canvas.draw()

def build_fourth_func():
    global plots
    ax.clear()
    build_DSK()
    print('build!')
    a = a4_drob.get()
    # чекбокси
    first_dev_fourth.place(x = 1055, y = 70)
    second_dev_fourth.place(x = 1055, y = 115)
    main_graphic_label.place(x = 1055, y = 25)
    build_colors_labels()#😱

    if a:
        # try:
        
        x = sympy.symbols('x')
        a = float(a)

        expr = (x)/(x**2+a)
        if isinstance(expr, sympy.Number):
            plot_constant_function(float(expr),'red')
        else:
            func = sympy.lambdify(x, expr, 'numpy')

            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)

            plot, = ax.plot(x_vals, y_vals, label=f'y = х/(х²+{a})', color='red')
            plots.append(plot)

            ax.legend()
            legend = ax.legend()
            for text in legend.get_texts():
                text.set_color('red')
            canvas.draw()
            # похідні (в путі)
            fourth_first_dev()
            fourth_second_dev()
            # drob_second_dev()
            # замена значения для похідних (будет) ne budet tam palka

            
            domain = scope_of_function(expr)
            domain_text = f"1) D(y) = {format_intervals(domain)}"
            scope_label.configure(text=domain_text)

            # перетин 0х і 0у
            points_0x_0y = points_ox_oy(expr,'red', True)
            points_zero = points_0x_0y['points_zero']

            points_0x_text = "; ".join([f"({x:.2f}, 0)" for x in points_zero])  # 0x-координаты

            # отримуємл координати і точку 0у
            oy_point = points_0x_0y['0y']
            oy_text = "не існує"
            if oy_point:
                offsets = oy_point.get_offsets()  # координати точки
                if len(offsets) > 0:
                    oy_coords = offsets[0]  # перша точка
                    oy_text = f"(0, {oy_coords[1]:.2f})"

            points_0x_0y_text = (
                f"6) Точки перетину з Ox:\n{points_0x_text}\n"
                f"Точка перетину з Oy:\n{oy_text}"
            )

            points_ox_oy_label.configure(text=points_0x_0y_text)

            # Отримуємо список точок нулів функції
            points_zero = points_0x_0y['points_zero']

            # Формуємо текст для лейблу
            points_zero_text = "7) Нулі функції: " + ", ".join([f"x{i+1} = {point}" for i, point in enumerate(points_zero)])

            # Встановлюємо текст лейблу
            points_zero_label.configure(text=points_zero_text)

            even_or_odd = check_even_odd_func(expr)
            even_or_odd_func_l.configure(text = f'{even_or_odd}')

            try:
                sign_intervals = find_sign_intervals(expr)
                all_sign_intervals_text = ""
                for interval, sign in sign_intervals:
                    all_sign_intervals_text += f"{sign} при х ∈ {interval}\n"  # додаємо кожний інтервал у текст

                intervals_identity_l.configure(text=f"8) Проміжки знакосталості:\n{all_sign_intervals_text}")
            except Exception as e:
                print(f"Помилка обчислення проміжків знакосталості: {e}")
                intervals_identity_l.configure(text="8) Проміжки знакосталості:\nнеможливо обчислити")


            punctured_dots(expr)

            slant_asymptote_label = slope_asymptote  # рівняння асимптоти
            find_and_plot_slant_asymptote(expr, x, label_widget = slope_asymptote)

            print(plots)
            # except Exception as e:
            #     print(f"Помилка першого графіку: {e}")
            print(plots)

def fourth_first_dev():
    global plots, plot_fourth_first, ox_points_fourth_first, h_lines_fourth_first
    global local_max_fourth_first, local_min_fourth_first, local_max_text_fourth_first, local_min_text_fourth_first

    check = first_dev_fourth.get()
    if check == 1:

        a = a4_drob.get()
        if a:
            # try:
            x = sympy.symbols('x')
            a = float(a)

            function = x/(x**2+a)
            dev_of_function = sympy.diff(function, x)

            # видалення старих графіків, точок, ліній, максимумів і мінімумів
            if plot_fourth_first:
                plot_fourth_first.remove()
                plot_fourth_first = None

            if ox_points_fourth_first:
                for point in ox_points_fourth_first:
                    point.remove()
                ox_points_fourth_first.clear()

            if h_lines_fourth_first:
                for line in h_lines_fourth_first:
                    line.remove()
                h_lines_fourth_first.clear()

            if local_max_fourth_first:
                local_max_fourth_first.remove()
                local_max_text_fourth_first.remove()
                local_max_fourth_first = None
                local_max_text_fourth_first = None

            if local_min_fourth_first:
                local_min_fourth_first.remove()
                local_min_text_fourth_first.remove()
                local_min_fourth_first = None
                local_min_text_fourth_first = None

            # спадання зростання
            intervals_data = find_intervals(dev_of_function, function)
            if len(intervals_data['інтервали']) != 0:
                interval_text = "\n".join([f"({left:.2f}; {right:.2f}) {state}" for left, right, state in intervals_data['інтервали']])
            else:
                interval_text = "Інтервалів зростання/спадання не існує"

            interval_label.configure(text=f'3) {interval_text}')

            # Формуємо текст для локальних максимумів і мінімумів
            if len(intervals_data['локальний максимум']) != 0:
                local_max_text = "Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
            else:
                local_max_text = "Локальний максимум: не існує"

            if len(intervals_data['локальний мінімум']) != 0:
                local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
            else:
                local_min_text = "Локальний мінімум: не існує"

            # макс значення функції
            if intervals_data['макс. значення ф-ції']:
                funct_max_text = f"Макс. значення ф-ції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
            else:
                funct_max_text = "Макс. значення ф-ції: не існує"

            # Мінімальне значення функції
            if intervals_data['мін. значення ф-ції']:
                func_min_text = f"Мін. значення ф-ції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
            else:
                func_min_text = "Мін. значення ф-ції: не існує"

            local_max_min_text =f'4) {local_max_text}\n{local_min_text}'
            local_max_min_label.configure(text = local_max_min_text)

            zn_function_text = f'5) {funct_max_text}\n{func_min_text}'
            zn_function_label.configure(text =zn_function_text)

            drob_first_dev_lable.configure(
                text = f"y' = {dev_of_function}"
            )

            print(dev_of_function)

            expr = dev_of_function
            
            func = sympy.lambdify(x, expr, 'numpy')

            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)

            plot_fourth_first, = ax.plot(x_vals, y_vals, label=f"y' = {dev_of_function}", color='green')
            # plots.append(plot)
            # пошук точок перетину з Ox
            points_0x_0y = points_ox_oy(dev_of_function, 'green', label=False, lines=True, include_oy=False)
            ox_points_fourth_first = points_0x_0y['0x']
            h_lines_fourth_first = points_0x_0y['lines']

            # пошук локальних максимумів і мінімумів
            intervals_data = find_intervals(dev_of_function, function)
            if len(intervals_data['локальний максимум']) != 0:
                max_point = intervals_data['локальний максимум'][0]
                local_max_fourth_first = ax.scatter(max_point[0], max_point[1], color='#FF0899', s=40)
                local_max_text_fourth_first = ax.annotate(
                    f'({max_point[0]:.2f}, {max_point[1]:.2f})',
                    (max_point[0], max_point[1]),
                    textcoords="offset points",
                    xytext=(15, 15),
                    ha='center'
                )

            if len(intervals_data['локальний мінімум']) != 0:
                min_point = intervals_data['локальний мінімум'][0]
                local_min_fourth_first = ax.scatter(min_point[0], min_point[1], color='#FF0899', s=40)
                local_min_text_fourth_first = ax.annotate(
                    f'({min_point[0]:.2f}, {min_point[1]:.2f})',
                    (min_point[0], min_point[1]),
                    textcoords="offset points",
                    xytext=(15, 15),
                    ha='center'
                )


            ax.legend()
            legend = ax.legend()

            fourth_f_dev_label.configure(
                text = f"y' = {dev_of_function}"
            )
            
            for text in legend.get_texts():
                text.set_color('red')
            canvas.draw()

            # 
            # except Exception as e:
            #     print(f"Помилка першої дробовох похідної: {e}")
    elif check == 0 and plot_fourth_first:
        # видалення графіка
        plot_fourth_first.remove()
        plot_fourth_first = None

        # видалення точок, ліній, максимумів і мінімумів
        if ox_points_fourth_first:
            for point in ox_points_fourth_first:
                point.remove()
            ox_points_fourth_first.clear()

        if h_lines_fourth_first:
            for line in h_lines_fourth_first:
                line.remove()
            h_lines_fourth_first.clear()

        if local_max_fourth_first:
            local_max_fourth_first.remove()
            local_max_text_fourth_first.remove()
            local_max_fourth_first = None
            local_max_text_fourth_first = None

        if local_min_fourth_first:
            local_min_fourth_first.remove()
            local_min_text_fourth_first.remove()
            local_min_fourth_first = None
            local_min_text_fourth_first = None

        ax.legend().remove()
        canvas.draw()

def fourth_second_dev():
    global plots, plot_fourth_second, ox_points_fourth_second, h_lines_fourth_second, inflection_points_fourth_scatter, inflection_points_l_3

    check = second_dev_fourth.get()
    if check == 1:
        a = a4_drob.get()

        if a:
            inflection_points_l_3 = []
            # try:
            x = sympy.symbols('x')
            a = float(a)

            function = x/(x**2+a)

            dev_of_function = sympy.diff(function, x)

            second_dev_of_function = sympy.diff(dev_of_function, x)
            print(second_dev_of_function)

            drob_second_dev_lable.configure(text = f"y'' = {second_dev_of_function}")

            expr = second_dev_of_function
            
            func = sympy.lambdify(x, expr, 'numpy')

            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)

            # видалення старих елементів
            if plot_fourth_second:
                plot_fourth_second.remove()
                plot_fourth_second = None

            if inflection_points_fourth_scatter:
                for point in inflection_points_fourth_scatter:
                    point.remove()
                inflection_points_fourth_scatter.clear()

            if ox_points_fourth_second:
                for point in ox_points_fourth_second:
                    point.remove()
                ox_points_fourth_second.clear()

            if h_lines_fourth_second:
                for line in h_lines_fourth_second:
                    line.remove()
                h_lines_fourth_second.clear()

            plot_fourth_second, = ax.plot(x_vals, y_vals, label=f"y'' = {second_dev_of_function}", color='blue')
            # plots.append(plot)
            # пошук точок перегину
            inflection_points = find_inflection_points(second_dev_of_function)
            for point in inflection_points:
                y_val = function.subs(x, point)
                scatter = ax.scatter(float(point), float(y_val), color='blue', zorder=5)
                inflection_points_fourth_scatter.append(scatter)
                label_point_inflection_3 = ax.annotate(
                    f'({float(point):.2f}, {float(y_val):.2f})',
                    (float(point), float(y_val)),
                    textcoords="offset points",
                    xytext=(0, 10),
                    ha='center',
                    color='blue'
                )
                inflection_points_l_3.append(label_point_inflection_3)

            # пошук точок пересічення з Ox
            points_0x_0y = points_ox_oy(second_dev_of_function, 'blue', label=False, lines=True, include_oy=False)
            ox_points_fourth_second = points_0x_0y['0x']
            h_lines_fourth_second = points_0x_0y['lines']

            # оновлення лейблу з точками перегину
            if inflection_points:
                formatted_points = "; ".join([f"x{i+1} = {float(pt):.2f}" for i, pt in enumerate(inflection_points)])
                inflection_points_label.configure(text=f"9) Точки перегину: {formatted_points}")
            else:
                inflection_points_label.configure(text="9) Точки перегину: не існує")

            ax.legend()
            legend = ax.legend()

            fourth_s_dev_label.configure(
                text = f"y'' = {second_dev_of_function}"
            )

            # points_0x_0y = points_ox_oy(expr, 'blue', label=False, lines=True, include_oy=False)
            for text in legend.get_texts():
                text.set_color('red')
            canvas.draw()
    elif check == 0 and plot_fourth_second:
        # видалення графіка
        plot_fourth_second.remove()
        plot_fourth_second = None

        # видалення точок, ліній і точок перегину
        if inflection_points_fourth_scatter:
            for point in inflection_points_fourth_scatter:
                point.remove()
            inflection_points_fourth_scatter.clear()

        # видалення підпису точок
        for label in inflection_points_l_3:
            label.remove()
        inflection_points_l_3.clear()

        if ox_points_fourth_second:
            for point in ox_points_fourth_second:
                point.remove()
            ox_points_fourth_second.clear()

        if h_lines_fourth_second:
            for line in h_lines_fourth_second:
                line.remove()
            h_lines_fourth_second.clear()

        ax.legend().remove()
        canvas.draw()

def frame_buttons_func(funct): 
    print(funct)
    global input_graphic, frame_menu

    input_graphic.insert(0,f"{funct}")
    # input_graphic.configure(text=funct)
    frame_menu.place_forget()


def punctured_dots(function):
    x = sympy.symbols('x')

    # Отримуємо область визначення функції
    domain = sympy.calculus.util.continuous_domain(function, x, sympy.S.Reals)

    # Перевіряємо, чи є розриви в області визначення (об'єднання інтервалів)
    punctured_points = []

    if isinstance(domain, sympy.Union):
        for interval in domain.args:
            if isinstance(interval, sympy.Interval):
                # Якщо інтервал не включає кінцеву точку ( виколота точка)
                if interval.left_open:
                    punctured_points.append(interval.start)  # Ліва точка інтервалу є виколотою
                if interval.right_open:
                    punctured_points.append(interval.end)  # Права точка інтервалу є виколотою

    # Будуємо вертикальні пунктирні лінії для виколотих точок і кружечки без заливки
    for point in punctured_points:
        if point.is_finite:  # Перевіряємо, чи точка є скінченною
            ax.axvline(x=point, color='black', linestyle='--', linewidth=2)  # Вертикальна лінія

            y_value = float(function.subs(x, float(point) + 0.01))

            # Округлення для підпису

            point_rounded = round(point)
            y_value_rounded = round(y_value)


            ax.scatter(point, y_value, facecolors='none', edgecolors='black', s = 40)  # Кружечок без заливки
            ax.annotate(f'({point_rounded}, {y_value_rounded})',
                        (point, y_value),
                        textcoords="offset points",
                        xytext=(10, 10),
                        ha='center')  
    canvas.draw()

def points_ox_oy(graphic, color, label=False, lines=False, include_oy=True):
    global ax
    x = sympy.symbols('x')

    # знаходимо точку перетину з віссю 0y (x = 0)
    y_intercept = graphic.subs(x, 0)  # функція subs підставляє в рівняння замість x - 0

    # знаходимо точки перетину з віссю 0x (y = 0)
    x_intercepts = sympy.solve(graphic, x)

    # відфільтровуємо тільки дійсні корені та не округлюємо їх передчасно
    x_intercepts = [root.evalf() for root in x_intercepts if root.is_real and not root.has(sympy.I)]

    # округляємо тільки після перевірки, що це дійсне число
    x_intercepts = [round(float(root), 1) for root in x_intercepts]

    points_zero = []  # нулі функції
    ox_points = []  # 0х
    dashed_lines = []  # пунктирні лінії

    if x_intercepts:
        for x_cor in x_intercepts:
            # 0х
            point = ax.scatter(x_cor, 0, color=color, s=40)
            ox_points.append(point)  # точку зберегти
            points_zero.append(x_cor)  # знач точки зберегти

            # підпис
            if label != False:
                ax.annotate(f'({x_cor:.2f}, 0)',
                            (x_cor, 0),
                            textcoords="offset points",
                            xytext=(10, 10),
                            ha='center')
            if lines:  # пунктирні лінії
                line = ax.axvline(x=x_cor, color=color, linestyle='--', linewidth=1)
                dashed_lines.append(line)

    oy_point = None
    if include_oy and y_intercept.is_real:
        y_cor = round(float(y_intercept), 2)
        oy_point = ax.scatter(0, y_cor, color=color, s=40)
        if label:
            ax.annotate(f'(0, {y_cor})',
                        (0, y_cor),
                        textcoords="offset points",
                        xytext=(10, 10),
                        ha='center')

    canvas.draw()

    return {
        '0y': oy_point,  # 0у
        '0x': ox_points,  # 0х
        'points_zero': points_zero,  # нулі функції
        'lines': dashed_lines  #пунктирні лінії для наглядного розуміння локал макс. і локал мін. + друга похідна - точка перегину
    }


def check_even_odd_func(function):
    x = sympy.symbols('x')  # создаем символ x
    neg_x_func = function.subs(x, -x)  # подставляем -x в функцию

    # четность
    if sympy.simplify(function - neg_x_func) == 0:
        return "2) Функція парна"
    
    # нечетность
    if sympy.simplify(function + neg_x_func) == 0:
        return "2) Функція непарна"
    
    return "2) Функція загального вигляду"

def find_sign_intervals(func):
    x = sympy.symbols('x')  # створюємо символ x

    # знаходимо корені функції (де f(x) = 0)
    roots = sympy.solveset(func, x, domain=sympy.S.Reals)
    roots = sorted([float(root) for root in roots if root.is_real])  # перетворюємо корені в числа і сортуємо

    # додаємо -∞ і +∞ для побудови інтервалів
    intervals = [(-sympy.oo, roots[0])] if roots else [(-sympy.oo, sympy.oo)]
    for i in range(len(roots) - 1):
        intervals.append((roots[i], roots[i + 1]))
    intervals.append((roots[-1], sympy.oo))

    # створюємо список для збереження результатів
    sign_intervals = []

    # обробляємо кожний інтервал
    for interval in intervals:
        # перевіряємо, чи межі інтервалу визначені у функції
        if interval[0] == -sympy.oo:
            test_point = interval[1] - 1  # беремо точку трохи лівіше, якщо ліва межа -∞
        elif interval[1] == sympy.oo:
            test_point = interval[0] + 1  # беремо точку трохи правіше, якщо права межа ∞
        else:
            test_point = (interval[0] + interval[1]) / 2  # середня точка інтервалу

        # перевіряємо, чи визначена функція в тестовій точці
        try:
            sign_at_point = func.subs(x, test_point)
        except (sympy.SympifyError, ZeroDivisionError):
            sign_at_point = None

        # округлюємо межі інтервалу до одного знака після коми
        rounded_interval = (round(interval[0], 1) if interval[0] != -sympy.oo else '-∞',
                            round(interval[1], 1) if interval[1] != sympy.oo else '+∞')

        # визначаємо знак і додаємо результат
        if sign_at_point is not None:
            if sign_at_point > 0:
                sign_intervals.append((rounded_interval, 'y > 0'))
            elif sign_at_point < 0:
                sign_intervals.append((rounded_interval, 'y < 0'))
            else:
                sign_intervals.append((rounded_interval, 'y = 0'))

    return sign_intervals


# Точки перегину
def find_inflection_points(second_derivative):
    x = sympy.symbols('x')

    # Знаходимо нулі другої похідної (тобто потенційні точки перегину)
    inflection_points = sympy.solve(second_derivative, x)

    # Округлюємо кожну точку до заданої точності
    inflection_points_rounded = [round(point, 1) for point in inflection_points]

    # Повертаємо список точок перегину
    return inflection_points_rounded
def find_and_plot_slant_asymptote(expr, x_symbol, label_widget=None):
    global ax
    
    try:
        # визначаємо k як границю f(x)/x при x -> ±∞
        k = sympy.limit(expr / x_symbol, x_symbol, sympy.oo)

        # перевіряємо, чи k є числом
        if not k.is_real:
            if label_widget:
                label_widget.configure(text="11) Похила асимптота: немає")
            return

        # визначаємо b як границю f(x) - kx при x є ±∞
        b = sympy.limit(expr - k * x_symbol, x_symbol, sympy.oo)

        # перевіряємо, чи b є числом
        if not b.is_real:
            if label_widget:
                label_widget.configure(text="11) Похила асимптота: немає")
            return

        # формуємо рівняння асимптоти
        asymptote_expr = k * x_symbol + b
        asymptote_func = sympy.lambdify(x_symbol, asymptote_expr, 'numpy')

        # будуємо асимптоту
        x_vals = numpy.linspace(-10, 10, 400)
        y_vals = asymptote_func(x_vals)

        ax.plot(x_vals, y_vals, linestyle='--', color='brown', label=f"y = {k:.2f}x + {b:.2f}")

        # додаємо текст рівняння в лейбл
        if label_widget:
            label_widget.configure(text=f"11) Похила асимптота: y = {k:.2f}x + {b:.2f}")

        # оновлюємо легенду
        ax.legend()
        canvas.draw()

    except Exception as e:
        print(f"Помилка: {e}")
        if label_widget:
            label_widget.configure(text="11) Похилої асимптоти не існує")

def find_convexity_intervals(second_derivative):
    x = sympy.symbols('x')
    intervals = []

    # знайти критичні точки другої похідної
    critical_points = sympy.solveset(second_derivative, x, domain=sympy.S.Reals)
    critical_points = sorted([float(pt) for pt in critical_points if pt.is_real])

    # розділити область на проміжки
    test_points = []
    if len(critical_points) > 0:
        test_points.append(float('-inf'))  # зліва від першої критичної точки
        test_points.extend(critical_points)
        test_points.append(float('inf'))  # справа від останньої критичної точки
    else:
        test_points = [float('-inf'), float('inf')]  # якщо критичних точок немає

    # визначити знаки другої похідної на кожному інтервалі
    for i in range(len(test_points) - 1):
        left, right = test_points[i], test_points[i + 1]
        test_value = (left + right) / 2  # точка всередині інтервалу
        value = second_derivative.subs(x, test_value)

        if value > 0:
            intervals.append(((left, right), "опуклість вверх"))
        elif value < 0:
            intervals.append(((left, right), "опуклість вниз"))

    return intervals

