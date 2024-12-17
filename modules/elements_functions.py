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

# функція для знаходження області визначення функції / function to find the domain of the function
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

# функція для побудови і дослідження графіку функції y = ax**3 + bx**2 + cx + d / function to plot and analyze the graph of the function y = ax**3 + bx**2 + cx + d
def build_graphic_1():
    global plots  # оголошуємо глобальну змінну plots / declaring the global variable plots
    
    ax.clear()  # очищаємо вісь графіка / clearing the graph axis
    build_DSK()  # будуємо сітку координат / building the coordinate grid

    # отримуємо значення коефіцієнтів a, b, c, d з полів вводу / getting the values of coefficients a, b, c, d from input fields
    a = a_1.get()
    b = b_1.get()
    c = c_1.get()
    d = d_1.get()

    # похідні / derivatives

    if a and b and c and d:  # перевіряємо, що всі поля не пусті / checking that all fields are not empty
        # try:
        # ставимо чекбокси / placing checkboxes
        first_dev.place(x = 1055, y = 70)
        second_dev.place(x = 1055, y = 115)
        main_graphic_label.place(x = 1055, y = 25)
        build_colors_labels()  # розміщуємо кольорові лейбли / placing colored labels

        # видаляємо значення в полях похідних, щоб уникнути помилок повторення символів / deleting values in derivative fields to avoid symbol repetition errors
        a_2.delete(0,"end")
        b_2.delete(0,"end")
        c_2.delete(0,"end")

        a_3.delete(0,"end")
        b_3.delete(0,"end")
        
        x = sympy.symbols('x')  # створюємо символ x / creating the symbol x
        a = float(a)  # перетворюємо значення a в число з плаваючою комою / converting the value of a to a float
        b = float(b)  # перетворюємо значення b в число з плаваючою комою / converting the value of b to a float
        c = float(c)  # перетворюємо значення c в число з плаваючою комою / converting the value of c to a float
        d = float(d)  # перетворюємо значення d в число з плаваючою комою / converting the value of d to a float

        expr = a*x**3 + b*x**2 + c*x + d  # створюємо вираз для функції / creating the expression for the function
        if isinstance(expr, sympy.Number):  # перевіряємо, чи є вираз числом / checking if the expression is a number
            const_plot = plot_constant_function(float(expr), 'blue')  # будуємо графік для константної функції / plot the constant function
        else:
            global func1
            func1 = sympy.lambdify(x, expr, 'numpy')  # перетворюємо функцію у форму, придатну для числових обчислень / convert the function to a form suitable for numerical calculations

            x_vals = numpy.linspace(-10, 10, 400)  # створюємо значення x в діапазоні від -10 до 10 / creating x values in the range from -10 to 10
            y_vals = func1(x_vals)  # обчислюємо значення y для функції / calculating the y values for the function

            plot, = ax.plot(x_vals, y_vals, label=f'y = {a}x^3 + {b}x^2 + {c}x + {d}', color='red')  # будуємо графік функції / plotting the function
            plots.append(plot)  # додаємо графік до списку / adding the plot to the list

            # додаємо легенду / adding the legend
            ax.legend()
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
            points_zero = points_0x_0y['points_zero']  # отримуємо точки перетину з Ox / getting intersection points with Ox

            points_0x_text = "; ".join([f"({x:.2f}, 0)" for x in points_zero])  # форматуємо текст для точок перетину з Ox / format text for Ox intersection points

            # отримуємо координати точки перетину з Oy / getting the coordinates of the intersection point with Oy
            oy_point = points_0x_0y['0y']
            oy_text = "не існує"  # якщо точка не існує / if the point does not exist
            if oy_point:
                offsets = oy_point.get_offsets()  # отримуємо координати точки / getting the point coordinates
                if len(offsets) > 0:
                    oy_coords = offsets[0]  # отримуємо першу точку / getting the first point
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

            punctured_dots(expr)  # перевіряємо наявність точок розриву у функції / check for punctured points in the function

            print(range)
            print(plots)  # виводимо список графіків / outputting
# функція для очищення зайвих елементів на ДСК і старих коєфіцієнтів / function to clear unnecessary elements on the coordinate grid and old coefficients
def clean_button():
    first_dev.place_forget()  # приховуємо першу похідну / hiding the first derivative
    second_dev.place_forget()  # приховуємо другу похідну / hiding the second derivative
    ax.clear()  # очищаємо вісь графіка / clearing the graph axis
    a_1.delete(0,"end")  # очищаємо поле для коефіцієнта a / clearing the field for coefficient a
    b_1.delete(0,"end")  # очищаємо поле для коефіцієнта b / clearing the field for coefficient b
    c_1.delete(0,"end")  # очищаємо поле для коефіцієнта c / clearing the field for coefficient c
    d_1.delete(0,"end")  # очищаємо поле для коефіцієнта d / clearing the field for coefficient d

    a_2.delete(0,"end")  # очищаємо поле для коефіцієнта a у' похідної / clearing the field for coefficient a of the second derivative
    b_2.delete(0,"end")  # очищаємо поле для коефіцієнта b у' похідної / clearing the field for coefficient b of the second derivative
    c_2.delete(0,"end")  # очищаємо поле для коефіцієнта c у' похідної / clearing the field for coefficient c of the second derivative

    a_3.delete(0,"end")  # очищаємо поле для коефіцієнта a у'' похідної / clearing the field for coefficient a of the third derivative
    b_3.delete(0,"end")  # очищаємо поле для коефіцієнта b у'' похідної / clearing the field for coefficient b of the third derivative

    a_drob_1.delete(0,"end")  # очищаємо поле для коефіцієнта a дробової функції / clearing the field for coefficient a of the fractional function
    a_drob_3.delete(0,"end")  # очищаємо поле для коефіцієнта b дробової функції / clearing the field for coefficient b of the fractional function

    a_th_drob.delete(0,"end")  # очищаємо поле для коефіцієнта a третьої дробової функції / clearing the field for coefficient a of the third fractional function

    a4_drob.delete(0,"end")  # очищаємо поле для коефіцієнта a четвертої дробової функції / clearing the field for coefficient a of the fourth fractional function

    input_graphic.delete(0,"end")  # очищаємо поле вводу графіка / clearing the graph input field

    local_max_min_label.configure(text = '4) Локальний макс. і мін. функції')  # оновлюємо текст лейблу локальних макс. і мін. / updating the label text for local max. and min.

    even_or_odd_func_l.configure(text = '2) Парна чи непарна ф-ція')  # оновлюємо текст лейблу для парності функції / updating the label text for function parity

    zn_function_label.configure(text = '5) Мін. і макс. значення функції')  # оновлюємо текст лейблу для мін. і макс. значень функції / updating the label text for min. and max. function values

    interval_label.configure(text = '3) Проміжок спадання і зростання функції')  # оновлюємо текст лейблу для інтервалів зростання та спадання функції / updating the label text for intervals of increase and decrease

    scope_label.configure(text = '1) Область визначення функції')  # оновлюємо текст лейблу області визначення функції / updating the label text for the function domain

    drob_first_dev_lable.configure(text = "y' = ")  # очищаємо текст лейблу першої похідної дробової функції / clearing the label text for the first derivative of the fractional function
    drob_second_dev_lable.configure(text = "y'' = ")  # очищаємо текст лейблу другої похідної дробової функції / clearing the label text for the second derivative of the fractional function

    third_f_dev_label.configure(text = "y' = ")  # очищаємо текст лейблу першої похідної третьої функції / clearing the label text for the first derivative of the third function
    third_s_dev_label.configure(text = "y'' = ")  # очищаємо текст лейблу другої похідної третьої функції / clearing the label text for the second derivative of the third function

    fourth_f_dev_label.configure(text = "y' = ")  # очищаємо текст лейблу першої похідної четвертої функції / clearing the label text for the first derivative of the fourth function
    fourth_s_dev_label.configure(text = "y'' = ")  # очищаємо текст лейблу другої похідної четвертої функції / clearing the label text for the second derivative of the fourth function

    points_ox_oy_label.configure(text="6) Точки перетину з осями ох і оу")  # оновлюємо текст лейблу для точок перетину з осями / updating the label text for intersection points with axes

    points_zero_label.configure(text="7) Нулі функції")  # оновлюємо текст лейблу для нулів функції / updating the label text for function zeros

    intervals_identity_l.configure(text = '8) Проміжки знакосталості ф-ції')  # оновлюємо текст лейблу для інтервалів знакосталості / updating the label text for intervals of constancy

    inflection_points_label.configure(text = '9) Точки перегину')  # оновлюємо текст лейблу для точок перегину / updating the label text for inflection points

    convexity_intervals_label.configure(text = '10) Проміжки опуклості')  # оновлюємо текст лейблу для інтервалів опуклості / updating the label text for convexity intervals

    slope_asymptote.configure(text = '11) Похила асимптота')  # оновлюємо текст лейблу для похилої асимптоти / updating the label text for the oblique asymptote

    main_graphic_label.place_forget()  # приховуємо лейбл головного графіка / hiding the main graph label
    # викликаємо функцію для побудови ДСК / calling the function to build the coordinate grid
    build_DSK()
# функція для побудови і виконання дослідження похідної у' першого графіку функції / function to plot and analyze the first derivative of the first graph of the function
def check_first_dev():
    global plots, plot_2, local_max_scatter, local_min_scatter, local_max_scatter_text, local_min_scatter_text
    global ox_points_first, h_lines_first

    check = first_dev.get()  # отримуємо стан чекбоксу для першої похідної / getting the state of the checkbox for the first derivative
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
                x_vals = numpy.linspace(-10, 10, 400)  # створюємо значення x в діапазоні від -10 до 10 / creating x values in the range from -10 to 10
                y_vals = func(x_vals)  # обчислюємо значення y для похідної / calculating the y values for the derivative

                plot_2, = ax.plot(x_vals, y_vals, label=f'y = 3*{a}x^2 + 2*{b}x + {c}', color='green')  # будуємо графік першої похідної / plotting the first derivative
                plots.append(plot_2)  # додаємо графік до списку / adding the plot to the list

                # додаємо легенду / adding the legend
                ax.legend()
                legend = ax.legend()
                for text in legend.get_texts():
                    text.set_color('red')  # встановлюємо червоний колір тексту легенди / setting the legend text color to red
                canvas.draw()  # перерисовуємо холст / redrawing the canvas

            # Обчислення точок локального максимуму та мінімуму / Calculating local maximum and minimum points
            intervals_data = find_intervals(expr, function)  # знаходимо інтервали та екстремуми / finding intervals and extrema

            # Видалення старих точок, якщо вони є / Removing old points if they exist
            if local_max_scatter:
                local_max_scatter.remove()  # видаляємо точки локального максимуму / removing local maximum points
                local_max_scatter_text.remove()  # видаляємо текст для точок локального максимуму / removing text for local maximum points
                local_max_scatter = None
                local_max_scatter_text = None
            if local_min_scatter:
                local_min_scatter.remove()  # видаляємо точки локального мінімуму / removing local minimum points
                local_min_scatter_text.remove()  # видаляємо текст для точок локального мінімуму / removing text for local minimum points
                local_min_scatter = None
                local_min_scatter_text = None

            # видалення старих точок перетину і пунктирних ліній / removing old intersection points and dashed lines
            if ox_points_first:
                for point in ox_points_first:
                    point.remove()  # видаляємо точки перетину з Ox / removing intersection points with Ox
                ox_points_first.clear()
            if h_lines_first:
                for line in h_lines_first:
                    line.remove()  # видаляємо пунктирні лінії / removing dashed lines
                h_lines_first.clear()

            # Обчислення точок перетину з віссю Ox та побудова пунктирних ліній / Calculating intersection points with the Ox axis and plotting dashed lines
            points_0x_0y = points_ox_oy(expr, 'green', label=False, lines=True, include_oy=False)
            ox_points_first = points_0x_0y['0x']  # зберігаємо точки перетину з Ox / storing intersection points with Ox
            h_lines_first = points_0x_0y['lines']  # зберігаємо пунктирні лінії / storing dashed lines

            # Додавання нових точок / Adding new points
            if len(intervals_data['локальний максимум']) != 0:  # якщо є локальні максимуми / if there are local maxima
                local_max = intervals_data['локальний максимум'][0]
                l_max_x, l_max_y = local_max
                local_max_scatter = ax.scatter(l_max_x, l_max_y, color='#FF0899', s=40)  # додаємо точки локального максимуму / adding local maximum points
                local_max_scatter_text = ax.annotate(f'({l_max_x:.2f}, {l_max_y:.2f})',
                                                     (l_max_x, l_max_y),
                                                     textcoords="offset points",
                                                     xytext=(15, 15),
                                                     ha='center')  # додаємо текст для точок локального максимуму / adding text for local maximum points

            if len(intervals_data['локальний мінімум']) != 0:  # якщо є локальні мінімуми / if there are local minima
                local_min = intervals_data['локальний мінімум'][0]
                l_min_x, l_min_y = local_min
                local_min_scatter = ax.scatter(l_min_x, l_min_y, color='#FF0899', s=40)  # додаємо точки локального мінімуму / adding local minimum points
                local_min_scatter_text = ax.annotate(f'({l_min_x:.2f}, {l_min_y:.2f})',
                                                    (l_min_x, l_min_y),
                                                    textcoords="offset points",
                                                    xytext=(15, 15),
                                                    ha='center')  # додаємо текст для точок локального мінімуму / adding text for local minimum points

            if len(intervals_data['інтервали']) != 0:  # Перевірка наявності інтервалів зростання/спадання / Checking for growth/decay intervals
                interval_text = "\n".join([f"({left:.2f}; {right:.2f}) {state}" for left, right, state in intervals_data['інтервали']])
            else:
                interval_text = "Інтервалів зростання/спадання не існує"  # Виведення повідомлення про відсутність інтервалів зростання/спадання / Displaying message about absence of growth/decay intervals

            interval_label.configure(text=f'3) {interval_text}')  # Налаштування тексту мітки для інтервалів зростання/спадання / Setting text for growth/decay intervals label

            # Формуємо текст для локальних максимумів і мінімумів / Forming text for local maxima and minima
            if len(intervals_data['локальний максимум']) != 0:  # Перевірка наявності локальних максимумів / Checking for local maxima
                local_max_text = "Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
            else:
                local_max_text = "Локальний максимум: не існує"  # Виведення повідомлення про відсутність локальних максимумів / Displaying message about absence of local maxima

            if len(intervals_data['локальний мінімум']) != 0:  # Перевірка наявності локальних мінімумів / Checking for local minima
                local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
            else:
                local_min_text = "Локальний мінімум: не існує"  # Виведення повідомлення про відсутність локальних мінімумів / Displaying message about absence of local minima

            # макс значення функції / max function value
            if intervals_data['макс. значення ф-ції']:  # Перевірка наявності макс. значення функції / Checking for max function value
                funct_max_text = f"Макс. значення ф-ції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
            else:
                funct_max_text = "Макс. значення ф-ції: не існує"  # Виведення повідомлення про відсутність макс. значення функції / Displaying message about absence of max function value

            # Мінімальне значення функції / min function value
            if intervals_data['мін. значення ф-ції']:  # Перевірка наявності мін. значення функції / Checking for min function value
                func_min_text = f"Мін. значення ф-ції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
            else:
                func_min_text = "Мін. значення ф-ції: не існує"  # Виведення повідомлення про відсутність мін. значення функції / Displaying message about absence of min function value

            local_max_min_text = f'4) {local_max_text}\n{local_min_text}'  # Формування тексту для локальних максимумів і мінімумів / Forming text for local maxima and minima
            local_max_min_label.configure(text=local_max_min_text)  # Налаштування тексту мітки для локальних максимумів і мінімумів / Setting text for local maxima and minima label

            zn_function_text = f'5) {funct_max_text}\n{func_min_text}'  # Формування тексту для макс. та мін. значень функції / Forming text for max and min function values
            zn_function_label.configure(text=zn_function_text)  # Налаштування тексту мітки для макс. та мін. значень функції / Setting text for max and min function values label

            # except Exception as e:
            #     print(f"Помилка другого графіку: {e}")  # Виведення повідомлення про помилку другого графіку / Displaying message about second graph error

            canvas.draw()  # Оновлення графіку / Redrawing the canvas

        elif check == 0 and plot_2 in plots:
            # Видалення графіка та точок / Removing the graph and points
            plot_2.remove()  # Видалення другого графіку / Removing the second graph
            plots.remove(plot_2)  # Видалення другого графіку з переліку графіків / Removing the second graph from the list of plots

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
            print("NO FIRST DEV!")  # Виведення повідомлення про відсутність першої похідної / Displaying message about absence of first derivative
# Функція для побудови і виконання дослідження похідної у'' першого графіку функції / Function for constructing and researching the second derivative of the first graph function
def check_second_dev():
    global plots, plot_3, func1, ox_points_second, h_lines_second, inflection_points_scatter, inflection_points_l

    check = second_dev.get()
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

                inflection_points_scatter = []  # Список для точок перегину / List for inflection points
                inflection_points_l = []  # Список для підписів точок перегину / List for inflection points labels

                # Формуємо форматований рядок для лейблу / Formatted string for the label
                formatted_points = "; ".join([f"x{i+1} = {point}" for i, point in enumerate(inflection_points)])

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

                plot_3, = ax.plot(x_vals, y_vals, label=f'y = 6*{a}x + 2 * {b}', color='blue')  # Побудова графіку другої похідної / Plotting the second derivative graph
                plots.append(plot_3)

                # Побудова точок перетину 0x і пунктирних ліній / Plotting intersection points with 0x and dashed lines
                points_0x_0y = points_ox_oy(expr, 'blue', label=False, lines=True, include_oy=False)
                ox_points_second = points_0x_0y['0x']  # Графічні об'єкти точок перетину / Graphical objects of intersection points
                h_lines_second = points_0x_0y['lines']  # Графічні об'єкти пунктирних ліній / Graphical objects of dashed lines

                # Знаходимо проміжки опуклості / Find the intervals of convexity
                convexity_intervals = find_convexity_intervals(expr)

                # Створюємо текст для лейблу / Create text for the label
                convexity_text = "Проміжки опуклості графіка:\n"  # "Intervals of graph convexity:\n"
                for interval, convexity in convexity_intervals:
                    left, right = interval
                    left = "-∞" if left == float('-inf') else f"{left:.2f}"
                    right = "+∞" if right == float('inf') else f"{right:.2f}"
                    convexity_text += f"{convexity} при x ∈ ({left}; {right})\n"  # "{convexity} at x ∈ ({left}; {right})\n"

                # Виводимо текст у лейбл / Output the text to the label
                convexity_intervals_label.configure(text=convexity_text)
                ax.legend()  # Виводимо легенду на графіку / Output the legend on the graph
                legend = ax.legend()

                for text in legend.get_texts():
                    text.set_color('red')  # Змінюємо колір тексту легенди на червоний / Change legend text color to red
                canvas.draw()  # Оновлюємо графік / Redraw the canvas

                # except Exception as e:
                #     print(f"Помилка третьої похідної: {e}")  # Виведення повідомлення про помилку третьої похідної / Outputting message about third derivative error
    elif check == 0 and plot_3 in plots:  # Якщо перевірка не активна і графік є у списку / If the check is not active and the plot is in the list
        plot_3.remove()  # Видалення графіку третьої похідної / Remove the third derivative plot
        plots.remove(plot_3)

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
        for scatter in inflection_points_scatter:
            scatter.remove()
        inflection_points_scatter.clear()
        # Видалення підписів точок / Removing point labels
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
        print("NOT SECOND DEV!")  # Виведення повідомлення про відсутність другої похідної / Outputting message about absence of the second derivative
# функція для побудови і дослідження графіку функції у = (x**2 - a)/(x - b) / Function for constructing and studying the graph of the function y = (x**2 - a)/(x - b)
def build_drob_graphic():
    global plots  # Використання глобальної змінної plots / Using the global variable plots
    ax.clear()  # Очищення графічної області / Clearing the plotting area
    build_DSK()  # Виклик функції побудови ДСК / Calling the function to build DSK (not sure what DSK stands for)
    
    # Отримання значень параметрів a і b з інтерфейсу / Getting the values of parameters a and b from the interface
    a = a_drob_1.get()
    b_data_3 = a_drob_3.get()
    
    # Розміщення чекбоксів / Placing checkboxes
    first_dev_fdrob.place(x=1055, y=70)
    second_dev_fdrob.place(x=1055, y=115)
    main_graphic_label.place(x=1055, y=25)
    
    # Виклик функції для налаштування кольорових міток / Calling the function to set up color labels
    build_colors_labels()
    
    if a and b_data_3:  # Перевірка, чи існують значення a і b / Checking if a and b values exist
        x = sympy.symbols('x')  # Оголошення змінної x як символічної / Declaring x as a symbolic variable
        a = float(a)  # Перетворення a у число з плаваючою крапкою / Converting a to a float
        b_data_3 = float(b_data_3)  # Перетворення b у число з плаваючою крапкою / Converting b to a float
        expr = (x**2 - a) / (x - b_data_3)  # Визначення виразу функції / Defining the function expression
        
        if isinstance(expr, sympy.Number):  # Якщо вираз є числом / If the expression is a number
            plot_constant_function(float(expr), 'red')  # Побудова графіка для константи / Plotting the graph for the constant
        else:
            func = sympy.lambdify(x, expr, 'numpy')  # Перетворення виразу у функцію для обчислень / Converting the expression to a function for calculations

            x_vals = numpy.linspace(-10, 10, 400)  # Визначення діапазону значень x / Defining the range of x values
            y_vals = func(x_vals)  # Обчислення значень y для відповідних x / Calculating y values for the corresponding x values

            plot, = ax.plot(x_vals, y_vals, label=f'y = (х²-{a})/(х-{b_data_3})', color='red')  # Побудова графіка функції / Plotting the function graph
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

            print(plots)  # Виведення списку графіків / Printing the list of plots
            # except Exception as e:
            #     print(f"Помилка першого графіку: {e}")  # Виведення повідомлення про помилку побудови першого графіку / Displaying message about the first graph building error
# функція для побудови і виконання дослідження похідної у' другого графіку функції / Function for constructing and analyzing the first derivative of the second graph function
def drob_first_dev():
    global plots_2d, plot_2_2, ox_points_first, h_lines_first, local_max_scatter_2, local_min_scatter_2
    global local_max_scatter_text_2, local_min_scatter_text_2

    check = first_dev_fdrob.get()  # Отримання значення чекбоксу / Getting the value of the checkbox
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

            # обчислення локальних максимумів, мінімумів та інтервалів зростання/спадання / Calculating local maxima, minima and growth/decay intervals
            intervals_data = find_intervals(dev_of_function, function)

            # видалення старих точок, якщо вони є / Removing old points if they exist
            if local_max_scatter_2:
                local_max_scatter_2.remove()  # Видалення старих точок локального максимуму / Removing old local maximum points
                local_max_scatter_text_2.remove()  # Видалення тексту старих точок локального максимуму / Removing old local maximum points text
                local_max_scatter_2 = None
                local_max_scatter_text_2 = None
            if local_min_scatter_2:
                local_min_scatter_2.remove()  # Видалення старих точок локального мінімуму / Removing old local minimum points
                local_min_scatter_text_2.remove()  # Видалення тексту старих точок локального мінімуму / Removing old local minimum points text
                local_min_scatter_2 = None
                local_min_scatter_text_2 = None

            # видалення точок перетину і пунктирних ліній / Removing intersection points and dashed lines
            if ox_points_first:
                for point in ox_points_first:
                    point.remove()  # Видалення точок перетину з віссю x / Removing intersection points with x-axis
                ox_points_first.clear()
            if h_lines_first:
                for line in h_lines_first:
                    line.remove()  # Видалення горизонтальних ліній / Removing horizontal lines
                h_lines_first.clear()

            # побудова нових точок перетину і пунктирних ліній / Plotting new intersection points and dashed lines
            points_0x_0y = points_ox_oy(dev_of_function, 'green', label=False, lines=True, include_oy=False)
            ox_points_first = points_0x_0y['0x']  # Точки 0х / Points on the x-axis
            h_lines_first = points_0x_0y['lines']  # Пунктирні лінії / Dashed lines

            # додавання нових точок локальних максимумів і мінімумів / Adding new local maxima and minima points
            if len(intervals_data['локальний максимум']) != 0:  # Перевірка наявності локальних максимумів / Checking for local maxima
                local_max = intervals_data['локальний максимум'][0]
                l_max_x, l_max_y = local_max
                local_max_scatter_2 = ax.scatter(l_max_x, l_max_y, color='#FF0899', s=40)  # Додавання точок локального максимуму / Adding local maximum points
                local_max_scatter_text_2 = ax.annotate(f'({l_max_x:.2f}, {l_max_y:.2f})',
                                                       (l_max_x, l_max_y),
                                                       textcoords="offset points",
                                                       xytext=(15, 15),
                                                       ha='center')  # Додавання тексту для точок локального максимуму / Adding text for local maximum points

            if len(intervals_data['локальний мінімум']) != 0:  # Перевірка наявності локальних мінімумів / Checking for local minima
                local_min = intervals_data['локальний мінімум'][0]
                l_min_x, l_min_y = local_min
                local_min_scatter_2 = ax.scatter(l_min_x, l_min_y, color='#FF0899', s=40)  # Додавання точок локального мінімуму / Adding local minimum points
                local_min_scatter_text_2 = ax.annotate(f'({l_min_x:.2f}, {l_min_y:.2f})',
                                                       (l_min_x, l_min_y),
                                                       textcoords="offset points",
                                                       xytext=(15, 15),
                                                       ha='center')  # Додавання тексту для точок локального мінімуму / Adding text for local minimum points

            # оновлення тексту похідної / Updating the derivative text
            drob_first_dev_lable.configure(text=f"y' = {dev_of_function}")

            if len(intervals_data['інтервали']) != 0:  # Перевірка наявності інтервалів зростання/спадання / Checking for growth/decay intervals
                interval_text = "\n".join([f"({left:.2f}; {right:.2f}) {state}" for left, right, state in intervals_data['інтервали']])
            else:
                interval_text = "Інтервалів зростання/спадання не існує"  # Виведення повідомлення про відсутність інтервалів зростання/спадання / Displaying message about the absence of growth/decay intervals

            interval_label.configure(text=f'3) {interval_text}')  # Налаштування тексту мітки для інтервалів зростання/спадання / Setting text for growth/decay intervals label

            # Формуємо текст для локальних максимумів і мінімумів / Forming text for local maxima and minima
            if len(intervals_data['локальний максимум']) != 0:  # Перевірка наявності локальних максимумів / Checking for local maxima
                local_max_text = "Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
            else:
                local_max_text = "Локальний максимум: не існує"  # Виведення повідомлення про відсутність локальних максимумів / Displaying message about the absence of local maxima

            if len(intervals_data['локальний мінімум']) != 0:  # Перевірка наявності локальних мінімумів / Checking for local minima
                local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
            else:
                local_min_text = "Локальний мінімум: не існує"  # Виведення повідомлення про відсутність локальних мінімумів / Displaying message about the absence of local minima

            # макс значення функції / max function value
            if intervals_data['макс. значення ф-ції']:  # Перевірка наявності макс. значення функції / Checking for max function value
                funct_max_text = f"Макс. значення ф-ції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
            else:
                funct_max_text = "Макс. значення ф-ції: не існує"  # Виведення повідомлення про відсутність макс. значення функції / Displaying message about the absence of max function value

            # Мінімальне значення функції / Minimum function value
            if intervals_data['мін. значення ф-ції']:  # Перевірка наявності мінімального значення функції / Checking for the minimum function value
                func_min_text = f"Мін. значення ф-ції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
            else:
                func_min_text = "Мін. значення ф-ції: не існує"  # Виведення повідомлення про відсутність мінімального значення функції / Displaying message about the absence of minimum function value

            local_max_min_text = f'4) {local_max_text}\n{local_min_text}'  # Формування тексту для локальних максимумів та мінімумів / Forming text for local maxima and minima
            local_max_min_label.configure(text=local_max_min_text)  # Налаштування тексту мітки для локальних максимумів і мінімумів / Setting text for local maxima and minima label

            zn_function_text = f'5) {funct_max_text}\n{func_min_text}'  # Формування тексту для макс. та мін. значень функції / Forming text for max and min function values
            zn_function_label.configure(text=zn_function_text)  # Налаштування тексту мітки для макс. та мін. значень функції / Setting text for max and min function values label

            # Оновлення тексту похідної / Updating the derivative text
            drob_first_dev_lable.configure(
                text=f"y' = {dev_of_function}",
            )

            print(dev_of_function)  # Виведення похідної у консоль / Printing the derivative in the console

            expr = dev_of_function  # Встановлення виразу для похідної / Setting the expression for the derivative

            # Перетворення виразу похідної у функцію для обчислень / Converting the derivative expression to a function for calculations
            func = sympy.lambdify(x, expr, 'numpy')

            # Визначення діапазону значень x / Defining the range of x values
            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)  # Обчислення значень y для відповідних x / Calculating y values for the corresponding x values

            # Побудова графіку похідної функції / Plotting the derivative function graph
            plot_2_2, = ax.plot(x_vals, y_vals, label=f"y' = {dev_of_function}", color='green')
            plots_2d.append(plot_2_2)  # Додавання графіку до списку графіків / Adding the plot to the list of plots

            ax.legend()  # Виведення легенди на графіку / Displaying the legend on the graph
            legend = ax.legend()

            for text in legend.get_texts():
                text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
            canvas.draw()  # Оновлення графіку / Redrawing the canvas

            third_first_dev()  # Виклик функції третьої похідної / Calling the third derivative function

            # except Exception as e:
            #     print(f"Помилка першої дробової похідної: {e}")  # Виведення повідомлення про помилку обчислення першої дробової похідної / Displaying message about first fractional derivative calculation error

        elif check == 0 and plot_2_2 in plots_2d:  # Якщо чекбокс вимкнений і графік існує у списку / If the checkbox is unchecked and the plot exists in the list
            # видалення графіка / Removing the plot
            plot_2_2.remove()
            plots_2d.remove(plot_2_2)

            # видалення локальних максимумів та мінімумів / Removing local maxima and minima
            if local_max_scatter_2:
                local_max_scatter_2.remove()  # Видалення точок локального максимуму / Removing local maximum points
                local_max_scatter_text_2.remove()  # Видалення тексту точок локального максимуму / Removing local maximum points text
                local_max_scatter_2 = None
                local_max_scatter_text_2 = None

            if local_min_scatter_2:
                local_min_scatter_2.remove()  # Видалення точок локального мінімуму / Removing local minimum points
                local_min_scatter_text_2.remove()  # Видалення тексту точок локального мінімуму / Removing local minimum points text
                local_min_scatter_2 = None
                local_min_scatter_text_2 = None

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
            print("NO FIRST DEV!")  # Виведення повідомлення про відсутність першої похідної / Displaying message about the absence of the first derivative
# функція для побудови і виконання дослідження похідної у'' другого графіку функції / Function for constructing and analyzing the second derivative of the second graph function
def drob_second_dev():
    global plots_2d, plot_3_2, ox_points_second, h_lines_second, inflection_points_scatter, inflection_points_label

    check = second_dev_fdrob.get()  # Отримання значення чекбоксу / Getting the value of the checkbox
    if check == 1:  # Якщо чекбокс активований / If the checkbox is checked
        a = a_drob_1.get()
        b_data_3 = a_drob_3.get()

        if a and b_data_3:  # Перевірка, чи існують значення a і b / Checking if a and b values exist
            x = sympy.symbols('x')  # Оголошення змінної x як символічної / Declaring x as a symbolic variable
            a = float(a)  # Перетворення a у число з плаваючою крапкою / Converting a to a float
            b_data_3 = float(b_data_3)  # Перетворення b у число з плаваючою крапкою / Converting b to a float

            function = (x**2 - a) / (x - b_data_3)  # Визначення виразу функції / Defining the function expression
            dev_of_function = sympy.diff(function, x)  # Обчислення першої похідної функції / Calculating the first derivative of the function
            second_dev_of_function = sympy.diff(dev_of_function, x)  # Обчислення другої похідної функції / Calculating the second derivative of the function

            drob_second_dev_lable.configure(text=f"y'' = {second_dev_of_function}")  # Оновлення тексту для другої похідної / Updating the text for the second derivative

            expr = second_dev_of_function  # Встановлення виразу для другої похідної / Setting the expression for the second derivative
            func = sympy.lambdify(x, expr, 'numpy')  # Перетворення виразу другої похідної у функцію для обчислень / Converting the second derivative expression to a function for calculations

            # видалення старих точок перегину, пунктирних ліній і точок 0х / Removing old inflection points, dashed lines, and 0x points
            if inflection_points_scatter:
                for point in inflection_points_scatter:
                    point.remove()  # Видалення точок перегину / Removing inflection points
                inflection_points_scatter.clear()

            if ox_points_second:
                for point in ox_points_second:
                    point.remove()  # Видалення точок перетину з віссю x / Removing intersection points with x-axis
                ox_points_second.clear()

            if h_lines_second:
                for line in h_lines_second:
                    line.remove()  # Видалення горизонтальних ліній / Removing horizontal lines
                h_lines_second.clear()

            # пошук і побудова точок перегину / Finding and plotting inflection points
            inflection_points = find_inflection_points(second_dev_of_function)  # Пошук точок перегину / Finding inflection points
            for point in inflection_points:
                y_val = function.subs(x, point)  # Обчислення значення функції в точці перегину / Calculating the function value at the inflection point
                scatter = ax.scatter(float(point), float(y_val), color='blue', zorder=5)  # Побудова точок перегину на графіку / Plotting inflection points on the graph
                inflection_points_scatter.append(scatter)

                ax.annotate(f'({float(point):.2f}, {float(y_val):.2f})',
                            (float(point), float(y_val)),
                            textcoords="offset points",
                            xytext=(0, 10),
                            ha='center', color='blue')  # Додавання тексту для точок перегину / Adding text for inflection points

            # оновлення лейблу з точками перегину / Updating the label with inflection points
            if inflection_points:
                formatted_points = "; ".join([f"x{i+1} = {float(pt):.2f}" for i, pt in enumerate(inflection_points)])
                inflection_points_label.configure(text=f"9) Точки перегину: {formatted_points}")  # Оновлення тексту мітки з точками перегину / Updating the text for the inflection points label
            else:
                inflection_points_label.configure(text="9) Точки перегину: не існує")  # Виведення повідомлення про відсутність точок перегину / Displaying message about the absence of inflection points

            # Визначення діапазону значень x / Defining the range of x values
            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)  # Обчислення значень y для відповідних x / Calculating y values for the corresponding x values

            # Побудова графіку другої похідної функції / Plotting the second derivative function graph
            plot_3_2, = ax.plot(x_vals, y_vals, label=f"y'' = {second_dev_of_function}", color='blue')
            plots_2d.append(plot_3_2)  # Додавання графіку до списку графіків / Adding the plot to the list of plots

            # побудова точок 0х і пунктирних ліній / Plotting 0x points and dashed lines
            points_0x_0y = points_ox_oy(expr, 'blue', label=False, lines=True, include_oy=False)
            ox_points_second = points_0x_0y['0x']  # Точки 0х / Points on the x-axis
            h_lines_second = points_0x_0y['lines']  # Пунктирні лінії / Dashed lines

            ax.legend()  # Виведення легенди на графіку / Displaying the legend on the graph
            legend = ax.legend()
            
            for text in legend.get_texts():
                text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
            canvas.draw()  # Оновлення графіку / Redrawing the canvas

            # except Exception as e:
            #     print(f"Помилка другої дробової похідної: {e}")  # Виведення повідомлення про помилку другої дробової похідної / Displaying message about the second fractional derivative error

    elif check == 0 and plot_3_2 in plots_2d:  # Якщо чекбокс вимкнений і графік існує у списку / If the checkbox is unchecked and the plot exists in the list
        # видалення графіка / Removing the plot
        plot_3_2.remove()
        plots_2d.remove(plot_3_2)

        # видалення точок 0х, пунктирних ліній і точок перегину / Removing 0x points, dashed lines, and inflection points
        if inflection_points_scatter:
            for point in inflection_points_scatter:
                point.remove()  # Видалення точок перегину / Removing inflection points
            inflection_points_scatter.clear()

        if ox_points_second:
            for point in ox_points_second:
                point.remove()  # Видалення точок перетину з віссю x / Removing intersection points with x-axis
            ox_points_second.clear()

        if h_lines_second:
            for line in h_lines_second:
                line.remove()  # Видалення горизонтальних ліній / Removing horizontal lines
            h_lines_second.clear()

        ax.legend().remove()  # Видалення легенди / Removing the legend
        ax.legend()  # Оновлення легенди / Updating the legend
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
        canvas.draw()  # Оновлення графіку / Redrawing the canvas
        print("NO SECOND DEV!")  # Виведення повідомлення про відсутність другої похідної / Displaying message about the absence of the second derivative
# функція для побудови і дослідження графіку функції y = (x**2 - a**2)/x / Function for constructing and studying the graph of the function y = (x**2 - a**2)/x
def build_third_func():
    global plots  # Використання глобальної змінної plots / Using the global variable plots
    ax.clear()  # Очищення графічної області / Clearing the plotting area
    build_DSK()  # Виклик функції побудови ДСК / Calling the function to build DSK
    print('build!')  # Виведення повідомлення про початок побудови / Printing the message about starting the build
    a = a_th_drob.get()  # Отримання значення параметра a з інтерфейсу / Getting the value of parameter a from the interface

    # Розміщення чекбоксів / Placing checkboxes
    first_dev_sdrob.place(x=1055, y=70)
    second_dev_sdrob.place(x=1055, y=115)
    main_graphic_label.place(x=1055, y=25)
    build_colors_labels()  # Виклик функції для налаштування кольорових міток / Calling the function to set up color labels
    
    if a:  # Перевірка, чи існує значення a / Checking if a value exists
        x = sympy.symbols('x')  # Оголошення змінної x як символічної / Declaring x as a symbolic variable
        a = float(a)  # Перетворення a у число з плаваючою крапкою / Converting a to a float
        expr = (x**2 - a**2) / x  # Визначення виразу функції / Defining the function expression
        
        if isinstance(expr, sympy.Number):  # Якщо вираз є числом / If the expression is a number
            plot_constant_function(float(expr), 'red')  # Побудова графіка для константи / Plotting the graph for the constant
        else:
            func = sympy.lambdify(x, expr, 'numpy')  # Перетворення виразу у функцію для обчислень / Converting the expression to a function for calculations

            # Визначення діапазону значень x / Defining the range of x values
            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)  # Обчислення значень y для відповідних x / Calculating y values for the corresponding x values

            # Побудова графіку функції / Plotting the function graph
            plot, = ax.plot(x_vals, y_vals, label=f'y = (х²-{a}²)/(х)', color='red')
            plots.append(plot)  # Додавання графіку до списку / Adding the plot to the list

            ax.legend()  # Додавання легенди до графіка / Adding a legend to the graph
            legend = ax.legend()
            for text in legend.get_texts():
                text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
            canvas.draw()  # Оновлення графіка / Redrawing the canvas

            # виклик функцій для побудови похідних / Calling functions to build derivatives
            third_first_dev()
            third_second_dev()

            domain = scope_of_function(expr)  # Обчислення області визначення функції / Calculating the domain of the function
            domain_text = f"1) D(y) = {format_intervals(domain)}"  # Форматування тексту області визначення / Formatting the domain text
            scope_label.configure(text=domain_text)  # Налаштування тексту мітки для області визначення / Setting the text for the domain label

            # обчислення та виведення точок перетину з осями Ox і Oy / Calculating and displaying the intersection points with axes Ox and Oy
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

            punctured_dots(expr)  # Визначення й побудова розривних точок / Defining and plotting punctured points

            # Пошук і побудова косої асимптоти / Finding and plotting the slant asymptote
            slant_asymptote_label = slope_asymptote  # Рівняння асимптоти / Equation of the asymptote
            find_and_plot_slant_asymptote(expr, x, label_widget=slope_asymptote)

            print(plots)  # Виведення списку графіків / Printing the list of plots
            # except Exception as e:
            #     print(f"Помилка першого графіку: {e}")  # Виведення повідомлення про помилку побудови першого графіку / Displaying message about the first graph building error
# функція для побудови і виконання дослідження похідної у' третього графіку функції / Function for constructing and analyzing the first derivative of the third graph function
def third_first_dev():
    global plots, plot_third_first, ox_points_third_first, h_lines_third_first
    global local_max_third_first, local_min_third_first, local_max_text_third_first, local_min_text_third_first

    check = first_dev_sdrob.get()  # Отримання значення чекбоксу / Getting the value of the checkbox
    
    if check == 1:  # Якщо чекбокс активований / If the checkbox is checked
        
        a = a_th_drob.get()  # Отримання значення параметра a з інтерфейсу / Getting the value of parameter a from the interface
        if a:  # Перевірка, чи існує значення a / Checking if a value exists
            x = sympy.symbols('x')  # Оголошення змінної x як символічної / Declaring x as a symbolic variable
            a = float(a)  # Перетворення a у число з плаваючою крапкою / Converting a to a float

            function = (x**2 - a**2) / x  # Визначення виразу функції / Defining the function expression
            dev_of_function = sympy.diff(function, x)  # Обчислення першої похідної функції / Calculating the first derivative of the function

            # Видалення старих точок, ліній, графіка, максимумів і мінімумів / Removing old points, lines, graph, maxima, and minima
            if plot_third_first:
                plot_third_first.remove()  # Видалення старого графіка / Removing the old graph
                plot_third_first = None

            if ox_points_third_first:
                for point in ox_points_third_first:
                    point.remove()  # Видалення старих точок перетину з віссю x / Removing old intersection points with x-axis
                ox_points_third_first.clear()

            if h_lines_third_first:
                for line in h_lines_third_first:
                    line.remove()  # Видалення старих горизонтальних ліній / Removing old horizontal lines
                h_lines_third_first.clear()

            if local_max_third_first:
                local_max_third_first.remove()  # Видалення старих точок локального максимуму / Removing old local maximum points
                local_max_text_third_first.remove()  # Видалення тексту старих точок локального максимуму / Removing old local maximum points text
                local_max_third_first = None
                local_max_text_third_first = None

            if local_min_third_first:
                local_min_third_first.remove()  # Видалення старих точок локального мінімуму / Removing old local minimum points
                local_min_text_third_first.remove()  # Видалення тексту старих точок локального мінімуму / Removing old local minimum points text
                local_min_third_first = None
                local_min_text_third_first = None

            # Обчислення інтервалів зростання і спадання / Calculating growth and decay intervals
            intervals_data = find_intervals(dev_of_function, function)
            if len(intervals_data['інтервали']) != 0:  # Перевірка наявності інтервалів зростання/спадання / Checking for growth/decay intervals
                interval_text = "\n".join([f"({left:.2f}; {right:.2f}) {state}" for left, right, state in intervals_data['інтервали']])
            else:
                interval_text = "Інтервалів зростання/спадання не існує"  # Виведення повідомлення про відсутність інтервалів зростання/спадання / Displaying message about the absence of growth/decay intervals

            interval_label.configure(text=f'3) {interval_text}')  # Налаштування тексту мітки для інтервалів зростання/спадання / Setting text for growth/decay intervals label

            # Формування тексту для локальних максимумів і мінімумів / Forming text for local maxima and minima
            if len(intervals_data['локальний максимум']) != 0:  # Перевірка наявності локальних максимумів / Checking for local maxima
                local_max_text = "Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
            else:
                local_max_text = "Локальний максимум: не існує"  # Виведення повідомлення про відсутність локальних максимумів / Displaying message about the absence of local maxima

            if len(intervals_data['локальний мінімум']) != 0:  # Перевірка наявності локальних мінімумів / Checking for local minima
                local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
            else:
                local_min_text = "Локальний мінімум: не існує"  # Виведення повідомлення про відсутність локальних мінімумів / Displaying message about the absence of local minima

            # Макс значення функції / Max function value
            if intervals_data['макс. значення ф-ції']:  # Перевірка наявності макс. значення функції / Checking for max function value
                funct_max_text = f"Макс. значення ф-ції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
            else:
                funct_max_text = "Макс. значення ф-ції: не існує"  # Виведення повідомлення про відсутність макс. значення функції / Displaying message about the absence of max function value

            # Мінімальне значення функції / Min function value
            if intervals_data['мін. значення ф-ції']:  # Перевірка наявності мін. значення функції / Checking for min function value
                func_min_text = f"Мін. значення ф-ції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
            else:
                func_min_text = "Мін. значення ф-ції: не існує"  # Виведення повідомлення про відсутність мін. значення функції / Displaying message about the absence of min function value

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

            plot_third_first, = ax.plot(x_vals, y_vals, label=f"y' = {dev_of_function}", color='green')  # Побудова графіку першої похідної / Plotting the first derivative graph
            # plots.append(plot)

            # Пошук точок перетину з Ox / Finding intersection points with Ox
            # пошук точок перетину похідної з Ox / Finding intersection points of the derivative with Ox
            points_0x_0y = points_ox_oy(dev_of_function, 'green', label=False, lines=True, include_oy=False)
            ox_points_third_first = points_0x_0y['0x']  # Збереження точок перетину з Ox / Storing intersection points with Ox
            h_lines_third_first = points_0x_0y['lines']  # Збереження пунктирних ліній / Storing dashed lines

            # пошук локальних максимумів і мінімумів / Finding local maxima and minima
            intervals_data = find_intervals(dev_of_function, function)
            if len(intervals_data['локальний максимум']) != 0:  # Перевірка наявності локальних максимумів / Checking for local maxima
                max_point = intervals_data['локальний максимум'][0]
                local_max_third_first = ax.scatter(max_point[0], max_point[1], color='#FF0899', s=40)  # Додавання точок локального максимуму / Adding local maximum points
                local_max_text_third_first = ax.annotate(
                    f'({max_point[0]:.2f}, {max_point[1]:.2f})',
                    (max_point[0], max_point[1]),
                    textcoords="offset points",
                    xytext=(15, 15),
                    ha='center'
                )  # Додавання тексту для точок локального максимуму / Adding text for local maximum points

            if len(intervals_data['локальний мінімум']) != 0:  # Перевірка наявності локальних мінімумів / Checking for local minima
                min_point = intervals_data['локальний мінімум'][0]
                local_min_third_first = ax.scatter(min_point[0], min_point[1], color='#FF0899', s=40)  # Додавання точок локального мінімуму / Adding local minimum points
                local_min_text_third_first = ax.annotate(
                    f'({min_point[0]:.2f}, {min_point[1]:.2f})',
                    (min_point[0], min_point[1]),
                    textcoords="offset points",
                    xytext=(15, 15),
                    ha='center'
                )  # Додавання тексту для точок локального мінімуму / Adding text for local minimum points

            ax.legend()  # Додавання легенди до графіка / Adding a legend to the graph
            legend = ax.legend()

            third_f_dev_label.configure(
                text=f"y' = {dev_of_function}"  # Оновлення тексту для першої похідної / Updating the text for the first derivative
            )

            for text in legend.get_texts():
                text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
            canvas.draw()  # Оновлення графіку / Redrawing the canvas

            # except Exception as e:
            #     print(f"Помилка першої дробової похідної: {e}")  # Виведення повідомлення про помилку першої похідної / Displaying message about the first derivative error

        elif check == 0 and plot_third_first:  # Якщо чекбокс вимкнений і графік першої похідної існує / If the checkbox is unchecked and the first derivative plot exists
            # видалення графіка першої похідної / Removing the first derivative plot
            plot_third_first.remove()
            plot_third_first = None

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
            canvas.draw()  # Оновлення графіку / Redrawing the canvas
# функція для побудови і виконання дослідження похідної у'' першого графіку функції / Function for constructing and analyzing the second derivative of the first graph function
def third_second_dev():
    global plots, plot_third_second, ox_points_third_second, h_lines_third_second, inflection_points_third_scatter, inflection_points_th
    check = second_dev_sdrob.get()  # Отримання значення чекбоксу / Getting the value of the checkbox

    if check == 1:  # Якщо чекбокс активований / If the checkbox is checked
        inflection_points_th = []  # Ініціалізація списку точок перегину / Initializing the list of inflection points
        a = a_th_drob.get()  # Отримання значення параметра a з інтерфейсу / Getting the value of parameter a from the interface
        if a:  # Перевірка, чи існує значення a / Checking if a value exists
            x = sympy.symbols('x')  # Оголошення змінної x як символічної / Declaring x as a symbolic variable
            a = float(a)  # Перетворення a у число з плаваючою крапкою / Converting a to a float

            function = (x**2 - a**2) / x  # Визначення виразу функції / Defining the function expression
            dev_of_function = sympy.diff(function, x)  # Обчислення першої похідної функції / Calculating the first derivative of the function
            second_dev_of_function = sympy.diff(dev_of_function, x)  # Обчислення другої похідної функції / Calculating the second derivative of the function
            print(second_dev_of_function)  # Виведення другої похідної у консоль / Printing the second derivative in the console

            drob_second_dev_lable.configure(text=f"y'' = {second_dev_of_function}")  # Оновлення тексту для другої похідної / Updating the text for the second derivative

            expr = second_dev_of_function  # Встановлення виразу для другої похідної / Setting the expression for the second derivative
            func = sympy.lambdify(x, expr, 'numpy')  # Перетворення виразу другої похідної у функцію для обчислень / Converting the second derivative expression to a function for calculations

            # Визначення діапазону значень x / Defining the range of x values
            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)  # Обчислення значень y для відповідних x / Calculating y values for the corresponding x values

            # видалення старих елементів / Removing old elements
            if plot_third_second:
                plot_third_second.remove()  # Видалення старого графіка / Removing the old graph
                plot_third_second = None

            if inflection_points_third_scatter:
                for point in inflection_points_third_scatter:
                    point.remove()  # Видалення старих точок перегину / Removing old inflection points
                inflection_points_third_scatter.clear()

            if ox_points_third_second:
                for point in ox_points_third_second:
                    point.remove()  # Видалення старих точок перетину з віссю x / Removing old intersection points with x-axis
                ox_points_third_second.clear()

            if h_lines_third_second:
                for line in h_lines_third_second:
                    line.remove()  # Видалення старих горизонтальних ліній / Removing old horizontal lines
                h_lines_third_second.clear()

            # Побудова графіку другої похідної / Plotting the second derivative graph
            plot_third_second, = ax.plot(x_vals, y_vals, label=f"y'' = {second_dev_of_function}", color='blue')

            # пошук точок перегину / Finding inflection points
            inflection_points = find_inflection_points(second_dev_of_function)
            for point in inflection_points:
                y_val = function.subs(x, point)  # Обчислення значення функції в точці перегину / Calculating the function value at the inflection point
                scatter = ax.scatter(float(point), float(y_val), color='blue', zorder=5)  # Додавання точок перегину на графік / Adding inflection points to the graph
                inflection_points_third_scatter.append(scatter)
                inflection_points_th_l = ax.annotate(
                    f'({float(point):.2f}, {float(y_val):.2f})',
                    (float(point), float(y_val)),
                    textcoords="offset points",
                    xytext=(0, 10),
                    ha='center',
                    color='blue'
                )  # Додавання тексту для точок перегину / Adding text for inflection points
                inflection_points_th.append(inflection_points_th_l)

            # пошук точок пересічення з Ox і побудова пунктирних ліній / Finding intersection points with Ox and plotting dashed lines
            points_0x_0y = points_ox_oy(second_dev_of_function, 'blue', label=False, lines=True, include_oy=False)
            ox_points_third_second = points_0x_0y['0x']  # Збереження точок перетину з Ox / Storing intersection points with Ox
            h_lines_third_second = points_0x_0y['lines']  # Збереження пунктирних ліній / Storing dashed lines

            ax.legend()  # Додавання легенди до графіка / Adding a legend to the graph
            legend = ax.legend()

            third_s_dev_label.configure(
                text=f"y'' = {second_dev_of_function}"  # Оновлення тексту для другої похідної / Updating the text for the second derivative
            )

            # оновлення лейблу з точками перегину / Updating the label with inflection points
            if inflection_points:
                formatted_points = "; ".join([f"x{i+1} = {float(pt):.2f}" for i, pt in enumerate(inflection_points)])
                inflection_points_label.configure(text=f"9) Точки перегину: {formatted_points}")  # Оновлення тексту мітки з точками перегину / Updating the text for the inflection points label
            else:
                inflection_points_label.configure(text="9) Точки перегину: не існує")  # Виведення повідомлення про відсутність точок перегину / Displaying message about the absence of inflection points

            points_0x_0y = points_ox_oy(expr, 'blue', label=False, lines=True, include_oy=False)
            for text in legend.get_texts():
                text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
            canvas.draw()  # Оновлення графіку / Redrawing the canvas

    elif check == 0 and plot_third_second:  # Якщо чекбокс вимкнений і графік другої похідної існує / If the checkbox is unchecked and the second derivative plot exists
        # видалення графіка другої похідної / Removing the second derivative plot
        plot_third_second.remove()
        plot_third_second = None

        # видалення точок перегину / Removing inflection points
        if inflection_points_third_scatter:
            for point in inflection_points_third_scatter:
                point.remove()  # Видалення точок перегину / Removing inflection points
            inflection_points_third_scatter.clear()

        # видалення підпису точок / Removing point labels
        for label in inflection_points_th:
            label.remove()
        inflection_points_th.clear()

        # видалення точок перетину з Ox і пунктирних ліній / Removing intersection points with Ox and dashed lines
        if ox_points_third_second:
            for point in ox_points_third_second:
                point.remove()  # Видалення точок перетину з віссю x / Removing intersection points with x-axis
            ox_points_third_second.clear()

        if h_lines_third_second:
            for line in h_lines_third_second:
                line.remove()  # Видалення горизонтальних ліній / Removing horizontal lines
            h_lines_third_second.clear()

        # оновлення легенди / Updating the legend
        ax.legend().remove()
        canvas.draw()  # Оновлення графіку / Redrawing the canvas
# функція для побудови і дослідження графіку функції y = x/(x**2 + a) / Function for constructing and analyzing the graph of the function y = x/(x**2 + a)
def build_fourth_func():
    global plots  # Використання глобальної змінної plots / Using the global variable plots
    ax.clear()  # Очищення графічної області / Clearing the plotting area
    build_DSK()  # Виклик функції побудови ДСК / Calling the function to build DSK
    print('build!')  # Виведення повідомлення про початок побудови / Printing the message about starting the build
    a = a4_drob.get()  # Отримання значення параметра a з інтерфейсу / Getting the value of parameter a from the interface
    
    # Розміщення чекбоксів / Placing checkboxes
    first_dev_fourth.place(x=1055, y=70)
    second_dev_fourth.place(x=1055, y=115)
    main_graphic_label.place(x=1055, y=25)
    build_colors_labels()  # Виклик функції для налаштування кольорових міток / Calling the function to set up color labels
    
    if a:  # Перевірка, чи існує значення a / Checking if a value exists
        x = sympy.symbols('x')  # Оголошення змінної x як символічної / Declaring x as a symbolic variable
        a = float(a)  # Перетворення a у число з плаваючою крапкою / Converting a to a float

        expr = x / (x**2 + a)  # Визначення виразу функції / Defining the function expression
        if isinstance(expr, sympy.Number):  # Якщо вираз є числом / If the expression is a number
            plot_constant_function(float(expr), 'red')  # Побудова графіка для константи / Plotting the graph for the constant
        else:
            func = sympy.lambdify(x, expr, 'numpy')  # Перетворення виразу у функцію для обчислень / Converting the expression to a function for calculations

            # Визначення діапазону значень x / Defining the range of x values
            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)  # Обчислення значень y для відповідних x / Calculating y values for the corresponding x values

            # Побудова графіку функції / Plotting the function graph
            plot, = ax.plot(x_vals, y_vals, label=f'y = х/(х²+{a})', color='red')
            plots.append(plot)  # Додавання графіку до списку / Adding the plot to the list

            ax.legend()  # Додавання легенди до графіка / Adding a legend to the graph
            legend = ax.legend()
            for text in legend.get_texts():
                text.set_color('red')  # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
            canvas.draw()  # Оновлення графіка / Redrawing the canvas

            # виклик функцій для побудови похідних / Calling functions to build derivatives
            fourth_first_dev()
            fourth_second_dev()

            domain = scope_of_function(expr)  # Обчислення області визначення функції / Calculating the domain of the function
            domain_text = f"1) D(y) = {format_intervals(domain)}"  # Форматування тексту області визначення / Formatting the domain text
            scope_label.configure(text=domain_text)  # Налаштування тексту мітки для області визначення / Setting the text for the domain label

            # обчислення та виведення точок перетину з осями Ox і Oy / Calculating and displaying the intersection points with axes Ox and Oy
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

            punctured_dots(expr)  # Визначення й побудова розривних точок / Defining and plotting punctured points

            # Пошук і побудова косої асимптоти / Finding and plotting the slant asymptote
            slant_asymptote_label = slope_asymptote  # Рівняння асимптоти / Equation of the asymptote
            find_and_plot_slant_asymptote(expr, x, label_widget=slope_asymptote)

            print(plots)  # Виведення списку графіків / Printing the list of plots
            # except Exception as e:
            #     print(f"Помилка першого графіку: {e}")  # Виведення повідомлення про помилку побудови першого графіку / Displaying message about the first graph building error
# Функція для побудови і дослідження похідної у' четвертого графіку функції / Function to construct and analyze the derivative of the fourth function plot
def fourth_first_dev():
    # Глобальні змінні для графіків, точок, ліній, максимумів та мінімумів / Global variables for plots, points, lines, maxima, and minima
    global plots, plot_fourth_first, ox_points_fourth_first, h_lines_fourth_first
    global local_max_fourth_first, local_min_fourth_first, local_max_text_fourth_first, local_min_text_fourth_first

    # Перевірка, чи увімкнено четверту похідну / Check if the fourth derivative is enabled
    check = first_dev_fourth.get()
    if check == 1:  # Якщо чекбокс ввімкнено / If the checkbox is enabled

        # Отримання значення змінної "a" для четвертої похідної / Retrieve the value of variable "a" for the fourth derivative
        a = a4_drob.get()
        if a:  # Перевірка, чи значення "a" не є порожнім / Check if "a" value is not empty
            x = sympy.symbols('x')  # Створення символічної змінної x / Create symbolic variable x
            a = float(a)  # Конвертація значення "a" у дійсне число / Convert the "a" value to a floating-point number

            # Визначення функції та її похідної / Define the function and its derivative
            function = x/(x**2 + a)  # Основна функція / The main function
            dev_of_function = sympy.diff(function, x)  # Обчислення похідної функції / Calculate the derivative of the function

            # Видалення старих графіків, точок, ліній, максимумів і мінімумів / Removing old plots, points, lines, maxima, and minima
            if plot_fourth_first:  # Якщо існує графік похідної / If a derivative plot exists
                plot_fourth_first.remove()  # Видалення графіку / Remove the plot
                plot_fourth_first = None

            if ox_points_fourth_first:  # Якщо існують точки перетину з Ox / If x-intersection points exist
                for point in ox_points_fourth_first:  # Видаляємо всі точки / Remove all points
                    point.remove()
                ox_points_fourth_first.clear()  # Очищення списку точок / Clear the list of points

            if h_lines_fourth_first:  # Якщо існують горизонтальні лінії / If horizontal lines exist
                for line in h_lines_fourth_first:  # Видаляємо всі лінії / Remove all lines
                    line.remove()
                h_lines_fourth_first.clear()  # Очищення списку ліній / Clear the list of lines

            if local_max_fourth_first:  # Якщо існує локальний максимум / If a local maximum exists
                local_max_fourth_first.remove()  # Видаляємо точку максимуму / Remove the maximum point
                local_max_text_fourth_first.remove()  # Видаляємо текст максимуму / Remove the maximum text
                local_max_fourth_first = None
                local_max_text_fourth_first = None

            if local_min_fourth_first:  # Якщо існує локальний мінімум / If a local minimum exists
                local_min_fourth_first.remove()  # Видаляємо точку мінімуму / Remove the minimum point
                local_min_text_fourth_first.remove()  # Видаляємо текст мінімуму / Remove the minimum text
                local_min_fourth_first = None
                local_min_text_fourth_first = None

            # Визначення інтервалів зростання і спадання / Determine intervals of increase and decrease
            intervals_data = find_intervals(dev_of_function, function)  # Виклик функції для пошуку інтервалів / Call the function to find intervals
            if len(intervals_data['інтервали']) != 0:  # Перевірка наявності інтервалів / Check for existing intervals
                interval_text = "\n".join([f"({left:.2f}; {right:.2f}) {state}" for left, right, state in intervals_data['інтервали']])
            else:
                interval_text = "Інтервалів зростання/спадання не існує"  # Текст, якщо інтервалів немає / Text if no intervals exist

            # Оновлення текстового віджета для інтервалів / Update the text widget for intervals
            interval_label.configure(text=f'3) {interval_text}')

            # Формування тексту для локальних максимумів і мінімумів / Form text for local maxima and minima
            if len(intervals_data['локальний максимум']) != 0:  # Перевірка наявності локальних максимумів / Check for local maxima
                local_max_text = "Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
            else:
                local_max_text = "Локальний максимум: не існує"  # Якщо максимумів немає / If no maxima exist

            if len(intervals_data['локальний мінімум']) != 0:  # Перевірка наявності локальних мінімумів / Check for local minima
                local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
            else:
                local_min_text = "Локальний мінімум: не існує"  # Якщо мінімумів немає / If no minima exist

            # Визначення максимального значення функції / Determine the maximum value of the function
            if intervals_data['макс. значення ф-ції']:  # Якщо максимальне значення існує / If the maximum value exists
                funct_max_text = f"Макс. значення ф-ції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
            else:
                funct_max_text = "Макс. значення ф-ції: не існує"  # Якщо максимальне значення не існує / If no maximum exists

            # Визначення мінімального значення функції / Determine the minimum value of the function
            if intervals_data['мін. значення ф-ції']:  # Якщо мінімальне значення існує / If the minimum value exists
                func_min_text = f"Мін. значення ф-ції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
            else:
                func_min_text = "Мін. значення ф-ції: не існує"  # Якщо мінімальне значення не існує / If no minimum exists

            # Оновлення текстових віджетів для максимумів і мінімумів / Update text widgets for maxima and minima
            local_max_min_text = f'4) {local_max_text}\n{local_min_text}'
            local_max_min_label.configure(text=local_max_min_text)

            # Оновлення тексту для загального максимуму та мінімуму функції / Update text for overall function maxima and minima
            zn_function_text = f'5) {funct_max_text}\n{func_min_text}'
            zn_function_label.configure(text=zn_function_text)

            # Оновлення тексту похідної функції / Update the derivative function text
            drob_first_dev_lable.configure(text=f"y' = {dev_of_function}")
            print(dev_of_function)  # Вивід похідної у консоль / Print the derivative in the console

            # Лямбда-функція для розрахунку похідної / Lambda function to calculate the derivative
            expr = dev_of_function
            func = sympy.lambdify(x, expr, 'numpy')  # Конвертація у числову функцію / Convert to a numerical function

            # Побудова графіку похідної / Plot the derivative graph
            x_vals = numpy.linspace(-10, 10, 400)  # Генерація x-значень / Generate x-values
            y_vals = func(x_vals)  # Обчислення y-значень похідної / Calculate y-values for the derivative

            plot_fourth_first, = ax.plot(x_vals, y_vals, label=f"y' = {dev_of_function}", color='green')

            # Пошук точок перетину з віссю Ox / Find intersection points with the x-axis
            points_0x_0y = points_ox_oy(dev_of_function, 'green', label=False, lines=True, include_oy=False)

            ox_points_fourth_first = points_0x_0y['0x']  # Ось ми присвоюємо координати X точок до змінної / Here we assign the X coordinates of the points to a variable
            h_lines_fourth_first = points_0x_0y['lines']  # Тут ми присвоюємо лінії до іншої змінної / Here we assign lines to another variable

            # Пошук локальних максимумів і мінімумів / Finding local maxima and minima
            intervals_data = find_intervals(dev_of_function, function)  # Викликаємо функцію для знаходження інтервалів даних / Calling a function to find data intervals

            # Якщо локальні максимуми знайдені, додаємо їх на графік / If local maxima are found, add them to the graph
            if len(intervals_data['локальний максимум']) != 0:  # Перевіряємо, чи є локальні максимуми / Checking for local maxima
                max_point = intervals_data['локальний максимум'][0]  # Беремо перший локальний максимум / Taking the first local maximum
                local_max_fourth_first = ax.scatter(max_point[0], max_point[1], color='#FF0899', s=40)  # Відмічаємо його на графіку / Marking it on the graph
                local_max_text_fourth_first = ax.annotate(
                    f'({max_point[0]:.2f}, {max_point[1]:.2f})',
                    (max_point[0], max_point[1]),
                    textcoords="offset points",
                    xytext=(15, 15),
                    ha='center'
                )  # Додаємо текстову анотацію до максимуму / Adding a text annotation to the maximum

            # Якщо локальні мінімуми знайдені, додаємо їх на графік / If local minima are found, add them to the graph
            if len(intervals_data['локальний мінімум']) != 0:  # Перевіряємо, чи є локальні мінімуми / Checking for local minima
                min_point = intervals_data['локальний мінімум'][0]  # Беремо перший локальний мінімум / Taking the first local minimum
                local_min_fourth_first = ax.scatter(min_point[0], min_point[1], color='#FF0899', s=40)  # Відмічаємо його на графіку / Marking it on the graph
                local_min_text_fourth_first = ax.annotate(
                    f'({min_point[0]:.2f}, {min_point[1]:.2f})',
                    (min_point[0], min_point[1]),
                    textcoords="offset points",
                    xytext=(15, 15),
                    ha='center'
                )  # Додаємо текстову анотацію до мінімуму / Adding a text annotation to the minimum

            # Додавання легенди до графіка / Adding legend to the graph
            ax.legend()
            legend = ax.legend()

            fourth_f_dev_label.configure(
                text = f"y' = {dev_of_function}"  # Оновлюємо текст ярлика з похідною функцією / Updating the label text with the derivative function
            )

            # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
            for text in legend.get_texts():
                text.set_color('red')
            canvas.draw()  # Перемальовуємо графік / Redrawing the canvas

            # Приклад обробки винятків при знаходженні першої дробової похідної / Example of exception handling in finding the first fractional derivative
            # except Exception as e:
            #     print(f"Помилка першої дробовох похідної: {e}")  # Виведення повідомлення про помилку / Printing error message

        # Перевірка стану check і наявності графіка / Checking the state of 'check' and presence of graph
        elif check == 0 and plot_fourth_first:  
            # Видалення графіка / Removing the graph
            plot_fourth_first.remove()
            plot_fourth_first = None

            # Видалення точок, ліній, максимумів і мінімумів / Removing points, lines, maxima and minima
            if ox_points_fourth_first:
                for point in ox_points_fourth_first:
                    point.remove()  # Видалення кожної точки / Removing each point
                ox_points_fourth_first.clear()  # Очищення списку точок / Clearing the list of points

            if h_lines_fourth_first:
                for line in h_lines_fourth_first:
                    line.remove()  # Видалення кожної лінії / Removing each line
                h_lines_fourth_first.clear()  # Очищення списку ліній / Clearing the list of lines

            if local_max_fourth_first:
                local_max_fourth_first.remove()  # Видалення локального максимуму з графіка / Removing local maximum from the graph
                local_max_text_fourth_first.remove()  # Видалення текстової анотації локального максимуму / Removing the text annotation of local maximum
                local_max_fourth_first = None
                local_max_text_fourth_first = None

            if local_min_fourth_first:
                local_min_fourth_first.remove()  # Видалення локального мінімуму з графіка / Removing local minimum from the graph
                local_min_text_fourth_first.remove()  # Видалення текстової анотації локального мінімуму / Removing the text annotation of local minimum
                local_min_fourth_first = None
                local_min_text_fourth_first = None

            ax.legend().remove()  # Видалення легенди / Removing the legend
            canvas.draw()  # Перемальовуємо графік / Redrawing the canvas

# Функція для побудови і виконання дослідження похідної у'' четвертого графіку функції / Function to construct and study the second derivative of the fourth graph of the function
def fourth_second_dev():
    global plots, plot_fourth_second, ox_points_fourth_second, h_lines_fourth_second, inflection_points_fourth_scatter, inflection_points_l_3

    check = second_dev_fourth.get()  # Отримання значення перемикача для другого графіку / Getting the toggle value for the second graph
    if check == 1:  # Якщо перемикач увімкнено / If toggle is on
        a = a4_drob.get()  # Отримання значення дробового коефіцієнта / Getting the fractional coefficient

        if a:  # Якщо значення a не порожнє / If a is not empty
            inflection_points_l_3 = []  # Ініціалізація списку для точок перегину / Initializing list for inflection points
            # try:
            x = sympy.symbols('x')  # Оголошення символічної змінної x / Declaring symbolic variable x
            a = float(a)  # Перетворення значення a у числовий формат / Converting value a to numeric format

            function = x/(x**2+a)  # Визначення математичної функції / Defining the mathematical function

            dev_of_function = sympy.diff(function, x)  # Визначення першої похідної функції / Finding the first derivative of the function

            second_dev_of_function = sympy.diff(dev_of_function, x)  # Визначення другої похідної функції / Finding the second derivative of the function
            print(second_dev_of_function)  # Виведення другої похідної на екран для перевірки / Printing the second derivative for checking

            drob_second_dev_lable.configure(text = f"y'' = {second_dev_of_function}")  # Оновлення тексту лейблу з другою похідною / Updating the label text with the second derivative

            expr = second_dev_of_function  # Присвоєння виразу другої похідної змінній / Assigning the second derivative expression to a variable
            
            func = sympy.lambdify(x, expr, 'numpy')  # Перетворення виразу у функцію для обчислення значень / Converting the expression to a function for computing values

            x_vals = numpy.linspace(-10, 10, 400)  # Генерація значень x від -10 до 10 / Generating x values from -10 to 10
            y_vals = func(x_vals)  # Обчислення значень функції для заданих x / Computing function values for given x

            # Видалення старих елементів / Removing old elements
            if plot_fourth_second:
                plot_fourth_second.remove()  # Видалення старого графіка / Removing the old plot
                plot_fourth_second = None

            if inflection_points_fourth_scatter:
                for point in inflection_points_fourth_scatter:
                    point.remove()  # Видалення старих точок перегину / Removing old inflection points
                inflection_points_fourth_scatter.clear()

            if ox_points_fourth_second:
                for point in ox_points_fourth_second:
                    point.remove()  # Видалення старих точок перетину з віссю Ox / Removing old points of intersection with the Ox axis
                ox_points_fourth_second.clear()

            if h_lines_fourth_second:
                for line in h_lines_fourth_second:
                    line.remove()  # Видалення старих горизонтальних ліній / Removing old horizontal lines
                h_lines_fourth_second.clear()

            plot_fourth_second, = ax.plot(x_vals, y_vals, label=f"y'' = {second_dev_of_function}", color='blue')  # Побудова нового графіка другої похідної / Plotting the new second derivative graph
            # plots.append(plot)
            
            # Пошук точок перегину / Finding inflection points
            inflection_points = find_inflection_points(second_dev_of_function)  # Виклик функції для пошуку точок перегину / Calling the function to find inflection points
            for point in inflection_points:
                y_val = function.subs(x, point)  # Обчислення значення функції у точці перегину / Computing the function value at the inflection point
                scatter = ax.scatter(float(point), float(y_val), color='blue', zorder=5)  # Відмічення точки перегину на графіку / Marking the inflection point on the graph
                inflection_points_fourth_scatter.append(scatter)  # Додавання точки перегину до списку / Adding the inflection point to the list
                label_point_inflection_3 = ax.annotate(
                    f'({float(point):.2f}, {float(y_val):.2f})',
                    (float(point), float(y_val)),
                    textcoords="offset points",
                    xytext=(0, 10),
                    ha='center',
                    color='blue'
                )  # Додавання текстової анотації до точки перегину / Adding a text annotation to the inflection point
                inflection_points_l_3.append(label_point_inflection_3)  # Додавання анотації до списку / Adding the annotation to the list

            # Пошук точок перетину з віссю Ox / Finding points of intersection with the Ox axis
            points_0x_0y = points_ox_oy(second_dev_of_function, 'blue', label=False, lines=True, include_oy=False)  # Виклик функції для пошуку точок перетину та горизонтальних ліній / Calling the function to find points of intersection and horizontal lines
            ox_points_fourth_second = points_0x_0y['0x']  # Отримання точок перетину з віссю Ox / Getting the points of intersection with the Ox axis
            h_lines_fourth_second = points_0x_0y['lines']  # Отримання горизонтальних ліній / Getting the horizontal lines

            # Оновлення лейблу з точками перегину / Updating the label with inflection points
            if inflection_points:
                formatted_points = "; ".join([f"x{i+1} = {float(pt):.2f}" for i, pt in enumerate(inflection_points)])  # Форматування точок перегину для виводу / Formatting inflection points for display
                inflection_points_label.configure(text=f"9) Точки перегину: {formatted_points}")  # Оновлення тексту лейблу / Updating the label text
            else:
                inflection_points_label.configure(text="9) Точки перегину: не існує")  # Якщо точок перегину немає, оновлюємо лейбл відповідно / If no inflection points exist, update label accordingly

            ax.legend()  # Додавання легенди до графіка / Adding legend to the graph
            legend = ax.legend()

            fourth_s_dev_label.configure(
                text = f"y'' = {second_dev_of_function}"  # Оновлення тексту лейблу з другою похідною / Updating the label text with the second derivative
            )

            # Зміна кольору тексту легенди на червоний / Changing the legend text color to red
            for text in legend.get_texts():
                text.set_color('red')
            canvas.draw()  # Перемальовування графіка / Redrawing the canvas
    elif check == 0 and plot_fourth_second:
        # Видалення графіка / Removing the graph
        plot_fourth_second.remove()
        plot_fourth_second = None

        # Видалення точок, ліній і точок перегину / Removing points, lines, and inflection points
        if inflection_points_fourth_scatter:
            for point in inflection_points_fourth_scatter:
                point.remove()  # Видалення кожної точки перегину / Removing each inflection point
            inflection_points_fourth_scatter.clear()

        # Видалення підпису точок / Removing point labels
        for label in inflection_points_l_3:
            label.remove()  # Видалення кожного підпису / Removing each label
        inflection_points_l_3.clear()

        if ox_points_fourth_second:
            for point in ox_points_fourth_second:
                point.remove()  # Видалення кожної точки перетину / Removing each intersection point
            ox_points_fourth_second.clear()

        if h_lines_fourth_second:
            for line in h_lines_fourth_second:
                line.remove()  # Видалення кожної горизонтальної лінії / Removing each horizontal line
            h_lines_fourth_second.clear()

        ax.legend().remove()  # Видалення легенди / Removing the legend
        canvas.draw()  # Перемальовування графіка / Redrawing the canvas
# Функція для кнопок меню базових функцій, при натисканні обирається базовий графік функції у input / Function for menu buttons of basic functions, selecting a basic graph of the function in input on click
def frame_buttons_func(funct): 
    print(funct)  # Виведення обраної функції у консоль / Output of the selected function to the console
    global input_graphic, frame_menu  # Використання глобальних змінних / Using global variables

    input_graphic.insert(0,f"{funct}")  # Вставка функції у поле введення / Inserting the function into the input field
    frame_menu.place_forget()  # Приховування меню після вибору функції / Hiding the menu after selecting the function

# Функція для знаходження і побудови асимптот та виколотих точок / Function for finding and plotting asymptotes and punctured points
def punctured_dots(function):
    x = sympy.symbols('x')  # Оголошення символічної змінної x / Declaring symbolic variable x

    # Отримуємо область визначення функції / Getting the domain of the function
    domain = sympy.calculus.util.continuous_domain(function, x, sympy.S.Reals)

    # Перевіряємо, чи є розриви в області визначення (об'єднання інтервалів) / Checking for discontinuities in the domain (union of intervals)
    punctured_points = []  # Список для збереження виколотих точок / List to store punctured points

    if isinstance(domain, sympy.Union):  # Якщо область визначення є об'єднанням інтервалів / If the domain is a union of intervals
        for interval in domain.args:  # Проходимо по кожному інтервалу / Iterating over each interval
            if isinstance(interval, sympy.Interval):  # Якщо це інтервал / If it is an interval
                # Якщо інтервал не включає кінцеву точку (виколота точка) / If the interval does not include an endpoint (punctured point)
                if interval.left_open:
                    punctured_points.append(interval.start)  # Ліва точка інтервалу є виколотою / Left endpoint is punctured
                if interval.right_open:
                    punctured_points.append(interval.end)  # Права точка інтервалу є виколотою / Right endpoint is punctured

    # Будуємо вертикальні пунктирні лінії для виколотих точок і кружечки без заливки / Plot vertical dashed lines for punctured points and circles without fill
    for point in punctured_points:
        if point.is_finite:  # Перевіряємо, чи точка є скінченною / Check if the point is finite
            ax.axvline(x=point, color='black', linestyle='--', linewidth=2)  # Вертикальна лінія / Vertical line

            y_value = float(function.subs(x, float(point) + 0.01))  # Обчислення значення функції поблизу виколотої точки / Compute the function value near the punctured point

            # Округлення для підпису / Rounding for label

            point_rounded = round(point)  # Округлення координати x / Rounding x coordinate
            y_value_rounded = round(y_value)  # Округлення значення y / Rounding y value

            ax.scatter(point, y_value, facecolors='none', edgecolors='black', s = 40)  # Кружечок без заливки / Circle without fill
            ax.annotate(f'({point_rounded}, {y_value_rounded})',
                        (point, y_value),
                        textcoords="offset points",
                        xytext=(10, 10),
                        ha='center')  # Додавання підпису до виколотої точки / Adding a label to the punctured point
    canvas.draw()  # Оновлення графіка / Updating the canvas

# Функція для знаходження точок перетину з вісю 0х і 0у, нулів функції / Function for finding intersections with the Ox and Oy axes, zeros of the function
def points_ox_oy(graphic, color, label=False, lines=False, include_oy=True):
    global ax  # Використання глобальної змінної ax / Using global variable ax
    x = sympy.symbols('x')  # Оголошення символічної змінної x / Declaring symbolic variable x

    # Знаходимо точку перетину з віссю 0y (x = 0) / Find the intersection with the Oy axis (x = 0)
    y_intercept = graphic.subs(x, 0)  # функція subs підставляє в рівняння замість x - 0 / The subs function substitutes 0 for x in the equation

    # Знаходимо точки перетину з віссю 0x (y = 0) / Find intersections with the Ox axis (y = 0)
    x_intercepts = sympy.solve(graphic, x)  # Розв'язуємо рівняння для знаходження коренів / Solve the equation to find roots

    # Відфільтровуємо тільки дійсні корені та не округлюємо їх передчасно / Filter only real roots and avoid premature rounding
    x_intercepts = [root.evalf() for root in x_intercepts if root.is_real and not root.has(sympy.I)]

    # Округляємо тільки після перевірки, що це дійсне число / Round only after confirming it is a real number
    x_intercepts = [round(float(root), 1) for root in x_intercepts]  # Округлення коренів / Rounding the roots

    points_zero = []  # Нулі функції / Zeros of the function
    ox_points = []  # Точки перетину з віссю Ox / Intersection points with the Ox axis
    dashed_lines = []  # Пунктирні лінії / Dashed lines

    if x_intercepts:  # Якщо знайдено точки перетину / If intersection points are found
        for x_cor in x_intercepts:
            # Точка перетину з віссю Ox / Intersection point with the Ox axis
            point = ax.scatter(x_cor, 0, color=color, s=40)  # Додавання точки на графік / Adding the point to the graph
            ox_points.append(point)  # Збереження точки / Storing the point
            points_zero.append(x_cor)  # Збереження значення x для нуля функції / Storing x value for the zero of the function

            # Підпис точки / Label the point
            if label != False:
                ax.annotate(f'({x_cor:.2f}, 0)',
                            (x_cor, 0),
                            textcoords="offset points",
                            xytext=(10, 10),
                            ha='center')  # Додавання підпису до точки / Adding a label to the point
            if lines:  # Пунктирні лінії / Dashed lines
                line = ax.axvline(x=x_cor, color=color, linestyle='--', linewidth=1)  # Додавання пунктирної лінії на графік / Adding a dashed line to the graph
                dashed_lines.append(line)  # Збереження лінії / Storing the line

    oy_point = None  # Початкове значення для точки перетину з Oy / Initial value for Oy intersection point
    if include_oy and y_intercept.is_real:  # Якщо включено Oy і y є дійсним числом / If Oy is included and y is a real number
        y_cor = round(float(y_intercept), 2)  # Округлення значення y / Rounding the y value
        oy_point = ax.scatter(0, y_cor, color=color, s=40)  # Додавання точки на Oy / Adding the point on Oy
        if label:  # Якщо потрібно додати підпис / If label is needed
            ax.annotate(f'(0, {y_cor})',
                        (0, y_cor),
                        textcoords="offset points",
                        xytext=(10, 10),
                        ha='center')  # Додавання підпису до точки на Oy / Adding a label to the Oy point

    canvas.draw()  # Оновлення графіка / Updating the canvas

    return {
        '0y': oy_point,  # Точка перетину з Oy / Oy intersection point
        '0x': ox_points,  # Точки перетину з Ox / Ox intersection points
        'points_zero': points_zero,  # Нулі функції / Zeros of the function
        'lines': dashed_lines  # Пунктирні лінії для наглядного розуміння локал макс. і локал мін. + друга похідна - точка перегину / Dashed lines for better understanding of local
    }
# Функція для визначення парності функції / Function to determine if a function is even or odd
def check_even_odd_func(function):
    x = sympy.symbols('x')  # Створюємо символ x / Create the symbol x
    neg_x_func = function.subs(x, -x)  # Підставляємо -x у функцію / Substitute -x into the function

    # Перевірка на парність функції / Checking if the function is even
    if sympy.simplify(function - neg_x_func) == 0:  # Якщо різниця функцій дорівнює нулю / If the difference between functions is zero
        return "2) Функція парна"  # Функція парна / The function is even
    
    # Перевірка на непарність функції / Checking if the function is odd
    if sympy.simplify(function + neg_x_func) == 0:  # Якщо сума функцій дорівнює нулю / If the sum of the functions is zero
        return "2) Функція непарна"  # Функція непарна / The function is odd
    
    return "2) Функція загального вигляду"  # Функція загального вигляду / The function is of general form

# Функція для знаходження проміжків знакосталості графіку функції / Function to find intervals where the function is positive or negative
def find_sign_intervals(func):
    x = sympy.symbols('x')  # Створюємо символ x / Create the symbol x

    # Знаходимо корені функції (де f(x) = 0) / Find the roots of the function (where f(x) = 0)
    roots = sympy.solveset(func, x, domain=sympy.S.Reals)  # Знаходимо всі дійсні корені / Find all real roots
    roots = sorted([float(root) for root in roots if root.is_real])  # Перетворюємо корені в числа і сортуємо їх / Convert roots to numbers and sort them

    # Додаємо -∞ і +∞ для побудови інтервалів / Add -∞ and +∞ to create intervals
    intervals = [(-sympy.oo, roots[0])] if roots else [(-sympy.oo, sympy.oo)]  # Створюємо початковий інтервал / Create the initial interval
    for i in range(len(roots) - 1):
        intervals.append((roots[i], roots[i + 1]))  # Додаємо проміжки між коренями / Add intervals between roots
    intervals.append((roots[-1], sympy.oo))  # Додаємо кінцевий інтервал / Add the final interval

    # Створюємо список для збереження результатів / Create a list to store results
    sign_intervals = []

    # Обробляємо кожний інтервал / Process each interval
    for interval in intervals:
        # Перевіряємо, чи межі інтервалу визначені у функції / Check if the boundaries of the interval are defined in the function
        if interval[0] == -sympy.oo:
            test_point = interval[1] - 1  # Беремо точку трохи лівіше, якщо ліва межа -∞ / Take a point slightly to the left if the left boundary is -∞
        elif interval[1] == sympy.oo:
            test_point = interval[0] + 1  # Беремо точку трохи правіше, якщо права межа ∞ / Take a point slightly to the right if the right boundary is ∞
        else:
            test_point = (interval[0] + interval[1]) / 2  # Середня точка інтервалу / The midpoint of the interval

        # Перевіряємо, чи визначена функція в тестовій точці / Check if the function is defined at the test point
        try:
            sign_at_point = func.subs(x, test_point)  # Обчислюємо значення функції в тестовій точці / Compute the function value at the test point
        except (sympy.SympifyError, ZeroDivisionError):
            sign_at_point = None  # Якщо виникає помилка, призначаємо значення None / If an error occurs, set the value to None

        # Округлюємо межі інтервалу до одного знака після коми / Round the interval boundaries to one decimal place
        rounded_interval = (round(interval[0], 1) if interval[0] != -sympy.oo else '-∞',
                            round(interval[1], 1) if interval[1] != sympy.oo else '+∞')

        # Визначаємо знак і додаємо результат / Determine the sign and add the result
        if sign_at_point is not None:
            if sign_at_point > 0:
                sign_intervals.append((rounded_interval, 'y > 0'))  # Додаємо інтервал з позитивним значенням / Add interval with positive value
            elif sign_at_point < 0:
                sign_intervals.append((rounded_interval, 'y < 0'))  # Додаємо інтервал з негативним значенням / Add interval with negative value
            else:
                sign_intervals.append((rounded_interval, 'y = 0'))  # Додаємо інтервал з нульовим значенням / Add interval with zero value

    return sign_intervals  # Повертаємо список інтервалів / Return the list of intervals

# Функція для знаходження точок перегину графіку функцій / Function to find inflection points of function graphs
def find_inflection_points(second_derivative):
    x = sympy.symbols('x')  # Створюємо символ x / Create the symbol x

    # Знаходимо нулі другої похідної (тобто потенційні точки перегину) / Find the zeros of the second derivative (potential inflection points)
    inflection_points = sympy.solve(second_derivative, x)  # Розв'язуємо рівняння для другої похідної / Solve the equation for the second derivative

    # Округлюємо кожну точку до заданої точності / Round each point to the specified precision
    inflection_points_rounded = [round(point, 1) for point in inflection_points]  # Округлення точок перегину / Rounding inflection points

    # Повертаємо список точок перегину / Return the list of inflection points
    return inflection_points_rounded
# Функція для знаходження і побудови похилої асимптоти / Function to find and plot the slant asymptote
def find_and_plot_slant_asymptote(expr, x_symbol, label_widget=None):
    global ax  # Використання глобальної змінної ax / Using global variable ax
    
    try:
        # Визначаємо k як границю f(x)/x при x -> ±∞ / Determine k as the limit of f(x)/x as x -> ±∞
        k = sympy.limit(expr / x_symbol, x_symbol, sympy.oo)

        # Перевіряємо, чи k є числом / Check if k is a number
        if not k.is_real:  # Якщо k не є числом / If k is not a number
            if label_widget:
                label_widget.configure(text="11) Похила асимптота: немає")  # Оновлюємо текст лейблу / Update the label text
            return

        # Визначаємо b як границю f(x) - kx при x -> ±∞ / Determine b as the limit of f(x) - kx as x -> ±∞
        b = sympy.limit(expr - k * x_symbol, x_symbol, sympy.oo)

        # Перевіряємо, чи b є числом / Check if b is a number
        if not b.is_real:  # Якщо b не є числом / If b is not a number
            if label_widget:
                label_widget.configure(text="11) Похила асимптота: немає")  # Оновлюємо текст лейблу / Update the label text
            return

        # Формуємо рівняння асимптоти / Form the equation of the asymptote
        asymptote_expr = k * x_symbol + b
        asymptote_func = sympy.lambdify(x_symbol, asymptote_expr, 'numpy')

        # Будуємо асимптоту / Plot the asymptote
        x_vals = numpy.linspace(-10, 10, 400)  # Генеруємо значення x від -10 до 10 / Generate x values from -10 to 10
        y_vals = asymptote_func(x_vals)  # Обчислюємо значення y для асимптоти / Compute the y values for the asymptote

        ax.plot(x_vals, y_vals, linestyle='--', color='brown', label=f"y = {k:.2f}x + {b:.2f}")  # Додаємо асимптоту на графік / Add the asymptote to the graph

        # Додаємо текст рівняння в лейбл / Add the equation text to the label
        if label_widget:
            label_widget.configure(text=f"11) Похила асимптота: y = {k:.2f}x + {b:.2f}")  # Оновлюємо текст лейблу / Update the label text

        # Оновлюємо легенду / Update the legend
        ax.legend()  # Додаємо легенду до графіка / Add the legend to the graph
        canvas.draw()  # Оновлюємо графік / Update the canvas

    except Exception as e:
        print(f"Помилка: {e}")  # Виведення повідомлення про помилку / Print the error message
        if label_widget:
            label_widget.configure(text="11) Похилої асимптоти не існує")  # Оновлюємо текст лейблу при помилці / Update the label text on error

# Функція для знаходження проміжків опуклості функції / Function to find intervals of concavity
def find_convexity_intervals(second_derivative):
    x = sympy.symbols('x')  # Створюємо символ x / Create the symbol x
    intervals = []  # Список для збереження інтервалів опуклості / List to store intervals of concavity

    # Знайти критичні точки другої похідної / Find critical points of the second derivative
    critical_points = sympy.solveset(second_derivative, x, domain=sympy.S.Reals)  # Розв'язуємо рівняння другої похідної / Solve the second derivative equation
    critical_points = sorted([float(pt) for pt in critical_points if pt.is_real])  # Перетворюємо критичні точки в числа і сортуємо їх / Convert critical points to numbers and sort them

    # Розділити область на проміжки / Split the domain into intervals
    test_points = []
    if len(critical_points) > 0:  # Якщо є критичні точки / If there are critical points
        test_points.append(float('-inf'))  # Зліва від першої критичної точки / Left of the first critical point
        test_points.extend(critical_points)  # Додаємо критичні точки / Add critical points
        test_points.append(float('inf'))  # Справа від останньої критичної точки / Right of the last critical point
    else:
        test_points = [float('-inf'), float('inf')]  # Якщо критичних точок немає / If there are no critical points

    # Визначити знаки другої похідної на кожному інтервалі / Determine signs of the second derivative on each interval
    for i in range(len(test_points) - 1):
        left, right = test_points[i], test_points[i + 1]  # Межі інтервалу / Interval boundaries
        test_value = (left + right) / 2  # Точка всередині інтервалу / Point inside the interval
        value = second_derivative.subs(x, test_value)  # Обчислюємо значення другої похідної в цій точці / Compute the value of the second derivative at this point

        if value > 0:
            intervals.append(((left, right), "опуклість вверх"))  # Інтервал де функція опукла вгору / Interval where the function is concave up
        elif value < 0:
            intervals.append(((left, right), "опуклість вниз"))  # Інтервал де функція опукла вниз / Interval where the function is concave down

    return intervals  # Повертаємо список інтервалів опуклості / Return the list of concavity intervals

