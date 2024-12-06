'''
Файл де створюються потрібні функції для прив'язки до кнопок/чекбоксів на вікні.
'''

import numpy, sympy
import matplotlib.ticker as ticker
# import matplotlib.pyplot as plot

from .main_elements import *

plots = []
plot_2 = None
plot_3 = None

plots_2d = []
plot_2_2 = None
plot_3_2 = None

ox_points = []
oy_points = None
h_lines = []

local_max_scatter = None
local_min_scatter = None

local_max_scatter_s = None
local_min_scatter_s = None

local_min_scatter_text = None
local_max_scatter_text = None

local_max_scatter_2 = None
local_min_scatter_2 = None
local_max_scatter_text_2 = None
local_min_scatter_text_2 = None

background = "#A76E56"
frame_background = "#BA7D65"
text_color = "#392D20"
button_color = "#7B4C39"
text_button_color = "#F1D5BA"
input_color = "#FAF0E6"
input_border_color = "#EAD1B8"
input_textholder_color = "#CAA37D"
hover_color_menu = "#F3E4D5"
button_hover_color = "#9D6249"
checkbox_hover_color = "#EBCDAE"

def build_colors_labels():
    red_gr.place(x = 1031, y = 25)
    green_gr.place(x = 1031, y = 70)
    blue_gr.place(x = 1031, y = 115)

def focus_on_elements(event):
    # isinstance(object, classinfo)
    main.focus_set()
    print(f"Focus on main window")

def build_DSK():
    # Устанавливаем сетку (фон в клеточку)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='black')

    # Делаем оси ох и оу
    ax.axhline(y=0, color='black', linewidth=1.5)
    ax.axvline(x=0, color='black', linewidth=1.5)

    # Диапазон значений по осям
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])

    # Устанавливаем положение меток на осях (по обе стороны от осей)
    ax.xaxis.set_ticks_position('both')
    ax.yaxis.set_ticks_position('both')

    # Добавляем метки к осям
    ax.set_xlabel('x', color='black')
    ax.set_ylabel('y', color='black', rotation=0, labelpad=15, ha='right')

    # Устанавливаем цвет меток на осях
    ax.tick_params(axis='x', colors='black')
    ax.tick_params(axis='y', colors='black')

    # Устанавливаем шаг сетки
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

    # Устанавливаем положение меток осей рядом с осями
    ax.xaxis.set_label_coords(1.05, 0.5)
    ax.yaxis.set_label_coords(0.5, 1.05)
# перемещение значения по осям 
    ax.xaxis.set_tick_params(pad=-260)
    ax.yaxis.set_tick_params(pad=-225)    

    # цвет для фона ДСК
    ax.set_facecolor('#FAF0E6')

    canvas.draw()

def appear_menu(event):
    # очистка frame_menu от существующих кнопок внутри
    for button in frame_menu.winfo_children(): # winfo_children  чтобы получить все дочерние виджеты frame_menu
        button.destroy()
    frame_menu.place(x = 743,y = 59)
    # фрейм поверх всех елементов окна
    frame_menu.lift()
    input_graphic.lift(frame_menu)

    el_functions = [
                    'x','1/x', 'sqrt(x)','abs(x)','x**2', 'x**3', 
                    'x**-2', 'x**-3','x**(1/2)','x**(2/3)',
                    'x**(-1/2)','x**(-2/3)', 'sin(x)', 'cos(x)', 
                    'tan(x)', 'cot(x)','arccos(x)','arcsin(x)',
                    'arctan(x)'
                    ]

    for func in el_functions:

        func_button = ctk.CTkButton(
            master=frame_menu,
            text=func,
            width=195, 
            height=40,
            anchor = 'w',
            fg_color = input_border_color,
            hover_color = hover_color_menu,
            text_color = text_color,
            font=("Roboto Slab", 15),
            command=lambda f=func: frame_buttons_func(f)  # Использование lambda для передачи текста функции
        )
        func_button.pack(pady=2, anchor='w')

def disappear_menu(event):
    frame_menu.place_forget()

# Проміжки спадання зростання
def find_intervals(first_dev, function):
    x = sympy.symbols('x')  # створюємо символ x
    # знаходимо критичні точки (значення x, при яких перша похідна дорівнює нулю)
    crit_points = sympy.solve(first_dev, x)
    # залишаємо тільки дійсні критичні точки і знаходимо їх числове значення
    crit_points = [float(point.evalf()) for point in crit_points if point.is_real]
    # додаємо граничні точки інтервалу [-10, 10] до критичних точок
    crit_points = [-10] + crit_points + [10]

    # створюємо список для збереження інтервалів і їх властивостей (зростання/спадання)
    intervals = []
    local_max = []
    local_min = []
    
    # Проходимо по всім парам сусідніх критичних точок
    for i in range(len(crit_points) - 1):
        left = crit_points[i]  # лівий кінець інтервалу
        right = crit_points[i + 1]  # правий кінець інтервалу
        midpoint = (left + right) / 2  # середня точка інтервалу
        
        # Перевіряємо, чи є значення в середині інтервалу дійсним і визначеним
        midpoint_value = first_dev.subs(x, midpoint)
        if midpoint_value.is_real and not midpoint_value.has(sympy.zoo, sympy.nan, sympy.oo, sympy.I):
            # якщо похідна > 0, функція зростає
            if midpoint_value > 0:
                intervals.append((left, right, "- проміжок зростання"))
            # якщо похідна < 0, функція спадає
            else:
                intervals.append((left, right, "- проміжок спадання"))
        else:
            intervals.append((left, right, "- не існує"))  # якщо похідна не визначена або комплексна
    
    # Знаходимо локальні максимуми та мінімуми
    for point in crit_points[1:-1]:  # Виключаємо граничні точки інтервалу
        second_dev = sympy.diff(first_dev, x)  # Обчислюємо другу похідну функції
        curvature = second_dev.subs(x, point)  # Знаходимо значення другої похідної в критичній точці
        
        # якщо друга похідна < 0, це локальний максимум
        if curvature.is_real and not curvature.has(sympy.zoo, sympy.nan, sympy.oo, sympy.I):
            if curvature < 0:
                local_max.append((point, function.subs(x, point)))
            # якщо друга похідна > 0, це локальний мінімум
            elif curvature > 0:
                local_min.append((point, function.subs(x, point)))

    # if len(local_max) == 0:
    #     local_max.append('не існує')

    # if len(local_min) == 0:
    #     local_min.append('не існує')
        

    # Знаходимо максимальне і мінімальне значення функції на інтервалі [-10, 10]
    boundary_values = [(point, function.subs(x, point)) for point in crit_points]
    global_max = max(boundary_values, key=lambda t: t[1])
    global_min = min(boundary_values, key=lambda t: t[1])

    print(f'{local_max} - local max', f'{local_min} - local min')

    # подписи точек локал макс и мин

    return {
        'інтервали': intervals,
        'локальний максимум': local_max,
        'локальний мінімум': local_min,
        'макс. значення ф-ції': global_max,
        'мін. значення ф-ції': global_min
    }

# перефразирования для Д(у)

def scope_of_function(expr):
    x = sympy.symbols('x')  # створення символа x 
    domain = sympy.calculus.util.continuous_domain(expr, x, sympy.S.Reals)  # Определение области определения выражения
    intervals = []  # створення листу для збереження інтервалів області визначення (D(y))
    
    if isinstance(domain, sympy.Set):  # перевірка, що domain є об'єктом Set в sympy
        if domain.is_Interval:  # перевірка, що domain є інтервалом
            intervals.append(domain)  # додавання інтервала в лист intervals
        elif domain.is_Union:  # перевірка, що domain є об'єднанням інтервалів
            for subdomain in domain.args:  # перебираємо кожен підінтервал в об'єднанні
                if subdomain.is_Interval:  # перевірка, що підінтервал є інтервалом
                    intervals.append(subdomain)  # додавання підінтервала до списку intervals

    print(intervals)
                    
    return intervals  # повертаємо список інтервалів області визначення
# Д(у)
def format_intervals(intervals):
    formatted_intervals = []  # створення список для збереження відформатованих інтервалів
    
    for interval in intervals:  # перебираємо кожен інтервал у списку intervals
        # визначення типу дужки для лівої границі інтервала
        left_bracket = "[" if interval.left_open == False else "("
        left = f"{left_bracket}{round(interval.start)}" if interval.start != -sympy.oo else "(-∞"

        # визначення типу дужки для правої границі інтервала
        right_bracket = "]" if interval.right_open == False else ")"
        right = f"{round(interval.end)}{right_bracket}" if interval.end != sympy.oo else "∞)"
        
        formatted_intervals.append(f"{left}; {right}")  # форматування інтервалу і додавання до списку formatted_intervals
    
    if not formatted_intervals:  # якщо список formatted_intervals порожній
        return "∅"  # повертаємо рядок, який вказує на порожню область визначення
    elif len(formatted_intervals) == 1 and formatted_intervals[0] == "(-∞; ∞)":  # якшо є тільки один інтервал и це весь діапазон дійсних чисел
        return "R"  # повертаємо рядок, що на область є дійсною для усіх чисел
    else:
        return " ∪ ".join(formatted_intervals)  # якщо об'єднанні всі інтервали за допомогою символа "∪" і поверьає їх у типі строки

# Функция для построения графика
def plot_graph(ax, canvas):
    # Очищаем текущий график
    # ax.clear()
    # Перевод фокуса на кнопку, чтобы убрать каретку из CTkEntry
    button_get.focus()
    # Получаем текст из поля ввода
    function_text = input_graphic.get()

    # Если поле ввода не пустое
    if function_text.strip():
        
        # Пытаемся построить график
        # try:
        # Создаем символьную переменную для использования в sympy
        x = sympy.symbols('x')
        # Устанавливаем фон в клеточку

        # Парсим функцию и компилируем её
        expr = sympy.sympify(function_text)
        if isinstance(expr, sympy.Number):
            plot_constant_function(float(expr),'purple')
        else:
            dev_expr = sympy.diff(expr,x)
            print(dev_expr)
            func = sympy.lambdify(x, expr, 'numpy')

            # Вычисляем значения функции для заданного диапазона x
            x_vals = numpy.linspace(-10, 10, 400)
            y_vals = func(x_vals)

            # Строим график
            ax.plot(x_vals, y_vals, label = f'y = {function_text}', color='purple')

            # Добавляем легенду
            ax.legend()

            # Устанавливаем цвет текста легенды
            legend = ax.legend()
            for text in legend.get_texts():
                text.set_color('red')

            # Перерисовываем холст
            canvas.draw()
            # ПОМИЛКИ ДЛЯ ДЕЯКИХ ФУНКЦІЙ!
            # Д(х)
            domain = scope_of_function(expr)

            domain_text = f"1) D(y) = {format_intervals(domain)}"
            scope_label.configure(text=domain_text)

    # спадання зростання
            intervals_data = find_intervals(dev_expr, expr)
            if len(intervals_data['інтервали']) != 0:
                interval_text = "\n".join([f"({left:.2f}; {right:.2f}) {state}" for left, right, state in intervals_data['інтервали']])
            else:
                interval_text = "Інтервалів зростання/спадання не існує"

            interval_label.configure(text=f'3) {interval_text}')

            # Формуємо текст для локальних максимумів і мінімумів
            if len(intervals_data['локальний максимум']) != 0:
                local_max_text = "4) Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
            else:
                local_max_text = "4) Локальний максимум: не існує"

            if len(intervals_data['локальний мінімум']) != 0:
                local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
            else:
                local_min_text = "Локальний мінімум: не існує"

            # макс значення функції
            if intervals_data['макс. значення ф-ції']:
                funct_max_text = f"5) Максимальне значення функції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
            else:
                funct_max_text = "5) Максимальне значення функції: не існує"

            # Мінімальне значення функції
            if intervals_data['мін. значення ф-ції']:
                func_min_text = f"Мінімальне значення функції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
            else:
                func_min_text = "Мінімальне значення функції: не існує"

            local_max_min_text =f'{local_max_text}\n{local_min_text}'
            local_max_min_label.configure(text = local_max_min_text)

            zn_function_text = f'{funct_max_text}\n{func_min_text}'
            zn_function_label.configure(text =zn_function_text)

            points_0x_0y = points_ox_oy(expr,'purple', True)
            points_0x_0y_text = f"6) Точки перетину з Ox: {'; '.join([f'({x}, {y})' for x, y in points_0x_0y['0x']])}\nточка перетину з Oy: {points_0x_0y['0y']}"
            points_ox_oy_label.configure(text = points_0x_0y_text)

            # Отримуємо список точок нулів функції
            points_zero = points_0x_0y['points_zero']

            # Формуємо текст для лейблу
            points_zero_text = "7) Нулі функції: " + ", ".join([f"x{i+1} = {point}" for i, point in enumerate(points_zero)])

            # Встановлюємо текст лейблу
            points_zero_label.configure(text=points_zero_text)

            even_or_odd = check_even_odd_func(expr)
            even_or_odd_func_l.configure(text = f'{even_or_odd}')

            sign_intervals = find_sign_intervals(expr)

            all_sign_intervals_text = ""
            for interval, sign in sign_intervals:
                all_sign_intervals_text += f"На інтервалі {interval}: {sign}\n"  # Добавляем каждый интервал в текст

            intervals_identity_l.configure(text = all_sign_intervals_text)

            punctured_dots(expr)

            # except Exception as e:
            #     print(f"Помилка: {e}")
def plot_constant_function(a, color):
    x_vals = numpy.linspace(-10, 10, 400)
    y_vals = [a] * len(x_vals)

    plot_const, = ax.plot(x_vals, y_vals, label=f'y = {a}', color=color)
    plots.append(plot_const)

    ax.legend()
    legend = ax.legend()
    for text in legend.get_texts():
        text.set_color('red')
    canvas.draw()
    
    return plot_const
# функция для кнопки
def build_graphic():
    plot_graph(ax, canvas)
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
            # ставим галочку, если ее нет (или построение автоматически производных)
            # if first_dev.get() == 0:
            #     # toggle - перемикає стан на поставлену галочку
            #     first_dev.toggle(1)
            # else:
            #     check_first_dev()
            # if second_dev.get() == 0:
            #     second_dev.toggle(1)
            # else:
            #     check_second_dev()
            # D(y) хіхіхіхі    
            domain = scope_of_function(expr)
            domain_text = f"1) D(y) = {format_intervals(domain)}"
            scope_label.configure(text=domain_text)

            points_0x_0y = points_ox_oy(expr, 'red', True)
            points_0x_0y_text = f"6) Точки перетину з Ox: {'; '.join([f'({x}, {y})' for x, y in points_0x_0y['0x']])}\nточка перетину з Oy: {points_0x_0y['0y']}"
            points_ox_oy_label.configure(text = points_0x_0y_text)

            # Отримуємо список точок нулів функції
            points_zero = points_0x_0y['points_zero']

            # Формуємо текст для лейблу
            points_zero_text = "7) Нулі функції: " + ", ".join([f"x{i+1} = {point}" for i, point in enumerate(points_zero)])

            # Встановлюємо текст лейблу
            points_zero_label.configure(text=points_zero_text)

            even_or_odd = check_even_odd_func(expr)
            even_or_odd_func_l.configure(text = f'{even_or_odd}')

            sign_intervals = find_sign_intervals(expr)

            all_sign_intervals_text = ""
            for interval, sign in sign_intervals:
                all_sign_intervals_text += f"{sign} при х ∈ {interval}\n"  # Добавляем каждый интервал в текст

            intervals_identity_l.configure(text = f"8) Проміжки знакосталості:\n{all_sign_intervals_text}")

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

    points_ox_oy_label.configure(text="6) Точки перетину з осями ох і оу")

    points_zero_label.configure(text="7) Нулі функції")

    intervals_identity_l.configure(text = '8) Проміжки знакосталості ф-ції')

    build_DSK()

def check_first_dev():
    global plots, plot_2, local_max_scatter, local_min_scatter, local_max_scatter_text, local_min_scatter_text
    global ox_points, oy_points, h_lines

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

                # спадання зростання
                points_0x_0y = points_ox_oy(expr, 'green', False, True)
#                 # ox_points = points_0x_0y['0x']
#                 # oy_points = points_0x_0y['0y']
#                 # h_lines = points_0x_0y['points_zero']


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

            # Додавання нових точок
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
                funct_max_text = f"Максимальне значення функції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
            else:
                funct_max_text = "Максимальне значення функції: не існує"

            # Мінімальне значення функції
            if intervals_data['мін. значення ф-ції']:
                func_min_text = f"Мінімальне значення функції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
            else:
                func_min_text = "Мінімальне значення функції: не існує"
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

        ax.legend().remove()
        ax.legend()
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')
        canvas.draw()
        print("NO FIRST DEV!")


def check_second_dev():
    global plots, plot_3, func1
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
                for point in inflection_points:
                    # Обчислюємо значення функції в точці перегину
                    y_inflection = func1(point)
                    
                    # Малюємо точки перегину на графіку
                    ax.scatter(point, y_inflection, color='blue', zorder=5)
                    ax.annotate(f'({point:.2f}, {y_inflection:.2f})',  # виправлено: y_inflection без індексу
                                (point, y_inflection),
                                textcoords="offset points", 
                                xytext=(0, 10),
                                ha='center', color='blue')

                # Оновлюємо лейбл з точками перегину
                inflection_points_label.configure(text=f"9) Точки перегину: {inflection_points}")
                func = sympy.lambdify(x, expr, 'numpy')

                x_vals = numpy.linspace(-10, 10, 400)
                y_vals = func(x_vals)

                plot_3, = ax.plot(x_vals, y_vals, label=f'y = 6*{a}x + 2 * {b}', color='blue')
                plots.append(plot_3)

                ax.legend()
                legend = ax.legend()
                points_0x_0y = points_ox_oy(expr, 'blue', False, True)
                for text in legend.get_texts():
                    text.set_color('red')
                canvas.draw()

                # except Exception as e:
                #     print(f"Помилка третьої похідної: {e}")
    elif check == 0 and plot_3 in plots:
        plot_3.remove()
        plots.remove(plot_3)
        ax.legend().remove()
        ax.legend()
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')
        canvas.draw()
        print("NOT SECOND DEV!")
# второй график с похидной
def build_drob_graphic():
    global plots
    ax.clear()
    build_DSK()
    a = a_drob_1.get()
    # a_2 = a_drob_2.get()
    b_data_3 = a_drob_3.get()
    first_dev_fdrob.place(x = 1055, y =70)
    second_dev_fdrob.place(x = 1055, y = 115)
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

            plot, = ax.plot(x_vals, y_vals, label=f'y = (х²-{a})/(х-{a_3})', color='red')
            plots.append(plot)

            ax.legend()
            legend = ax.legend()
            for text in legend.get_texts():
                text.set_color('red')
            canvas.draw()
            # похідні додати потрібно умову з чекбоксами
            # drob_first_dev()
            # drob_second_dev()
            # замена значения для похідних (будет) ne budet tam palka

            
            domain = scope_of_function(expr)
            domain_text = f"1) D(y) = {format_intervals(domain)}"
            scope_label.configure(text=domain_text)

            points_0x_0y = points_ox_oy(expr,'red', True)
            points_0x_0y_text = f"6) Точки перетину з Ox: {'; '.join([f'({x}, {y})' for x, y in points_0x_0y['0x']])}\nточка перетину з Oy: {points_0x_0y['0y']}"
            points_ox_oy_label.configure(text = points_0x_0y_text)

            # Отримуємо список точок нулів функції
            points_zero = points_0x_0y['points_zero']

            # Формуємо текст для лейблу
            points_zero_text = "7) Нулі функції: " + ", ".join([f"x{i+1} = {point}" for i, point in enumerate(points_zero)])

            # Встановлюємо текст лейблу
            points_zero_label.configure(text=points_zero_text)

            even_or_odd = check_even_odd_func(expr)
            even_or_odd_func_l.configure(text = f'{even_or_odd}')

            sign_intervals = find_sign_intervals(expr)

            all_sign_intervals_text = ""
            for interval, sign in sign_intervals:
                all_sign_intervals_text += f"Н{sign} при х ∈ {interval}\n"  # Добавляем каждый интервал в текст

            intervals_identity_l.configure(text = f"8) Проміжки знакосталості:\n{all_sign_intervals_text}")


            punctured_dots(expr)

            print(plots)
            # except Exception as e:
            #     print(f"Помилка першого графіку: {e}")
            print(plots)

def drob_first_dev():
    global plots_2d, plot_2_2, local_max_scatter_2, local_min_scatter_2, local_max_scatter_text_2, local_min_scatter_text_2

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


            # спадання зростання
            intervals_data = find_intervals(dev_of_function, function)

            # Видалення старих точок, якщо вони є
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
                funct_max_text = f"Максимальне значення функції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
            else:
                funct_max_text = "Максимальне значення функції: не існує"

            # Мінімальне значення функції
            if intervals_data['мін. значення ф-ції']:
                func_min_text = f"Мінімальне значення функції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
            else:
                func_min_text = "Мінімальне значення функції: не існує"

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

            plot_2_2, = ax.plot(x_vals, y_vals, label=f"y' ={dev_of_function}", color='green')
            plots_2d.append(plot_2_2)

            ax.legend()
            legend = ax.legend()
            points_0x_0y = points_ox_oy(expr, 'green', False, True)
            for text in legend.get_texts():
                text.set_color('red')
            canvas.draw()

            third_first_dev()
            




            # except Exception as e:
            #     print(f"Помилка першої дробовох похідної: {e}")
    elif check == 0 and plot_2_2 in plots:
        # Видалення графіка та точок
        plot_2_2.remove()
        plots.remove(plot_2_2)

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

        ax.legend().remove()
        ax.legend()
        legend = ax.legend()
        for text in legend.get_texts():
            text.set_color('red')
        canvas.draw()
        print("NO FIRST DEV!")

def drob_second_dev():
    global plots

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

        x_vals = numpy.linspace(-10, 10, 400)
        y_vals = func(x_vals)

        plot, = ax.plot(x_vals, y_vals, label=f"y'' = {second_dev_of_function}", color='blue')
        plots.append(plot)

        ax.legend()
        legend = ax.legend()
        points_0x_0y = points_ox_oy(expr, 'blue', False, True)
        for text in legend.get_texts():
            text.set_color('red')
        canvas.draw()

        


        # except Exception as e:
        #     print(f"Помилка другої дробової похідної: {e}")

def build_third_func():
    global plots
    ax.clear()
    build_DSK()
    print('build!')
    a = a_th_drob.get()

    first_dev_sdrob.place(x = 1055, y = 70)
    second_dev_sdrob.place(x = 1055, y = 115)
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
            # замена значения для похідних (будет) ne budet tam palka

            
            domain = scope_of_function(expr)
            domain_text = f"1) D(y) = {format_intervals(domain)}"
            scope_label.configure(text=domain_text)

            points_0x_0y = points_ox_oy(expr,'red', True)
            points_0x_0y_text = f"6) Точки перетину з Ox: {'; '.join([f'({x}, {y})' for x, y in points_0x_0y['0x']])}\nточка перетину з Oy: {points_0x_0y['0y']}"
            points_ox_oy_label.configure(text = points_0x_0y_text)

            # Отримуємо список точок нулів функції
            points_zero = points_0x_0y['points_zero']

            # Формуємо текст для лейблу
            points_zero_text = "7) Нулі функції: " + ", ".join([f"x{i+1} = {point}" for i, point in enumerate(points_zero)])

            # Встановлюємо текст лейблу
            points_zero_label.configure(text=points_zero_text)

            even_or_odd = check_even_odd_func(expr)
            even_or_odd_func_l.configure(text = f'{even_or_odd}')

            sign_intervals = find_sign_intervals(expr)

            all_sign_intervals_text = ""
            for interval, sign in sign_intervals:
                all_sign_intervals_text += f"{sign} при х ∈ {interval}\n"  # Добавляем каждый интервал в текст

            intervals_identity_l.configure(text = f"8) Проміжки знакосталості:\n{all_sign_intervals_text}")


            punctured_dots(expr)

            print(plots)
            # except Exception as e:
            #     print(f"Помилка першого графіку: {e}")
            print(plots)

def third_first_dev():
    global plots

    a = a_th_drob.get()

    if a:
        # try:
        x = sympy.symbols('x')
        a = float(a)

        function = (x**2-a**2)/(x)
        dev_of_function = sympy.diff(function, x)


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
            funct_max_text = f"Максимальне значення функції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
        else:
            funct_max_text = "Максимальне значення функції: не існує"

        # Мінімальне значення функції
        if intervals_data['мін. значення ф-ції']:
            func_min_text = f"Мінімальне значення функції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
        else:
            func_min_text = "Мінімальне значення функції: не існує"

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

        plot, = ax.plot(x_vals, y_vals, label=f"y' ={dev_of_function}", color='green')
        plots.append(plot)

        ax.legend()
        legend = ax.legend()

        third_f_dev_label.configure(
                text = f"y' = {dev_of_function}"
            )
        # points_0x_0y = points_ox_oy(expr, 'green', False, True)
        for text in legend.get_texts():
            text.set_color('red')
        canvas.draw()
        




        # except Exception as e:
        #     print(f"Помилка першої дробовох похідної: {e}")

def third_second_dev():
    global plots

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

        plot, = ax.plot(x_vals, y_vals, label=f"y'' = {second_dev_of_function}", color='blue')
        plots.append(plot)

        ax.legend()
        legend = ax.legend()

        third_s_dev_label.configure(
            text = f"y'' = {second_dev_of_function}"
        )
        
        points_0x_0y = points_ox_oy(expr, 'blue', False, True)
        for text in legend.get_texts():
            text.set_color('red')
        canvas.draw()

def build_fourth_func():
    global plots
    ax.clear()
    build_DSK()
    print('build!')
    a = a4_drob.get()

    first_dev_fourth.place(x = 1055, y = 70)
    second_dev_fourth.place(x = 1055, y = 115)
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

            points_0x_0y = points_ox_oy(expr,'red', True)
            points_0x_0y_text = f"6) Точки перетину з Ox: {'; '.join([f'({x}, {y})' for x, y in points_0x_0y['0x']])}\nточка перетину з Oy: {points_0x_0y['0y']}"
            points_ox_oy_label.configure(text = points_0x_0y_text)

            # Отримуємо список точок нулів функції
            points_zero = points_0x_0y['points_zero']

            # Формуємо текст для лейблу
            points_zero_text = "7) Нулі функції: " + ", ".join([f"x{i+1} = {point}" for i, point in enumerate(points_zero)])

            # Встановлюємо текст лейблу
            points_zero_label.configure(text=points_zero_text)

            even_or_odd = check_even_odd_func(expr)
            even_or_odd_func_l.configure(text = f'{even_or_odd}')

            sign_intervals = find_sign_intervals(expr)

            all_sign_intervals_text = ""
            for interval, sign in sign_intervals:
                all_sign_intervals_text += f"{sign} при х ∈ {interval}\n"  # Добавляем каждый интервал в текст

            intervals_identity_l.configure(text = f"8) Проміжки знакосталості:\n{all_sign_intervals_text}")


            punctured_dots(expr)

            print(plots)
            # except Exception as e:
            #     print(f"Помилка першого графіку: {e}")
            print(plots)

def fourth_first_dev():
    global plots

    a = a4_drob.get()

    if a:
        # try:
        x = sympy.symbols('x')
        a = float(a)

        function = x/(x**2+a)
        dev_of_function = sympy.diff(function, x)


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
            funct_max_text = f"Максимальне значення функції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
        else:
            funct_max_text = "Максимальне значення функції: не існує"

        # Мінімальне значення функції
        if intervals_data['мін. значення ф-ції']:
            func_min_text = f"Мінімальне значення функції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
        else:
            func_min_text = "Мінімальне значення функції: не існує"

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

        plot, = ax.plot(x_vals, y_vals, label=f"y' ={dev_of_function}", color='green')
        plots.append(plot)

        ax.legend()
        legend = ax.legend()

        fourth_f_dev_label.configure(
            text = f"y' = {dev_of_function}"
        )
        # points_0x_0y = points_ox_oy(expr, 'green', False, True)
        for text in legend.get_texts():
            text.set_color('red')
        canvas.draw()

        # госпади поможи исправить эту ошибку
        # except Exception as e:
        #     print(f"Помилка першої дробовох похідної: {e}")

def fourth_second_dev():
    global plots

    a = a4_drob.get()

    if a:
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

        plot, = ax.plot(x_vals, y_vals, label=f"y'' = {second_dev_of_function}", color='blue')
        plots.append(plot)

        ax.legend()
        legend = ax.legend()

        fourth_s_dev_label.configure(
            text = f"y'' = {second_dev_of_function}"
        )

        points_0x_0y = points_ox_oy(expr, 'blue', False, True)
        for text in legend.get_texts():
            text.set_color('red')
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

def points_ox_oy(graphic, color, label = False, lines = False):
    # from .main_elements import ax
    
    x = sympy.symbols('x')

    # знаходимо точку перетину з віссю 0y (x = 0)
    y_intercept = graphic.subs(x, 0)  # функція subs підставляє в рівняння замість x - 0

    # знаходимо точки перетину з віссю 0x (y = 0)
    x_intercepts = sympy.solve(graphic, x)

    # відфільтровуємо тільки дійсні корені та не округлюємо їх передчасно
    x_intercepts = [root.evalf() for root in x_intercepts if root.is_real and not root.has(sympy.I)]

    # округляємо тільки після перевірки, що це дійсне число
    x_intercepts = [round(float(root), 1) for root in x_intercepts]

    points_zero = []

    print(f'{x_intercepts} x_intercepts iiii {y_intercept} - yyyy')

    
    if x_intercepts:
        for x_cor in x_intercepts:
            print(x_cor)
            print(type(x_cor))  
            ax.scatter(x_cor, 0, color=color, s=40)  # add points to the plot s - size
                
            if label == True:
                ax.annotate(f'({x_cor:.2f}, 0)',
                        (x_cor, 0),
                        textcoords="offset points",  # Відносні координати для підпису
                        xytext=(10,10),  # Відступ від точки (в пікселях)
                        ha='center')  # Горизонтальне вирівнювання підпису
            else:
                ax.plot([x_cor, x_cor], [-10**6, 10**6], color=color, linestyle='--', linewidth=1)
            points_zero.append(x_cor)
            canvas.draw()

    if y_intercept:
        if y_intercept.is_real:#перевірка на комплексне число
            y_cor = round(float(y_intercept), 2)
            ax.scatter(0, y_cor, color=color, s=40)  # add points to the plot s - size
            if label == True:
                ax.annotate(f'(0, {y_cor})',
                        (0, y_cor),
                        textcoords="offset points",  # Відносні координати для підпису
                        xytext=(10,10),  # Відступ від точки (в пікселях)
                        ha='center')  # Горизонтальне вирівнювання підпису
            canvas.draw()
        else:
            y_cor = y_intercept
            print(y_cor)
            print(type(y_cor))
            ax.scatter(0, y_cor, color=color, s=40)  # add points to the plot s - size
            if label == True:
                ax.annotate(f'(0, {y_cor})',
                        (0, y_cor),
                        textcoords="offset points",  # Відносні координати для підпису
                        xytext=(10,10),  # Відступ від точки (в пікселях)
                        ha='center')  # Горизонтальне вирівнювання підпису
            canvas.draw()

    return {
        '0y': (0, round(float(y_intercept), 1)),
        '0x': [(root, 0) for root in x_intercepts],
        'points_zero': points_zero
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
    x = sympy.symbols('x')  # создаем символ x

    # корені функції (де f(x) = 0)
    roots = sympy.solveset(func, x, domain=sympy.S.Reals)
    roots = sorted([float(root) for root in roots if root.is_real])  # Преобразуем корни в числа и сортируем

    # додаємо мінус і плюс нескінченності для створення інтервалу
    intervals = [(-sympy.oo, roots[0])] if roots else [(-sympy.oo, sympy.oo)]
    for i in range(len(roots) - 1):
        intervals.append((roots[i], roots[i + 1]))
    intervals.append((roots[-1], sympy.oo))

    # лист для збереження інтервалів знакосталості
    sign_intervals = []

    # визначаємо знак функції на кожному інтервалі
    for interval in intervals:
        # Похідна точки в інтервалі (середня точка)
        if interval[0] == -sympy.oo:
            test_point = interval[1] - 1  # Берем точку трохи лівіше, якщо ліва межа -∞
        elif interval[1] == sympy.oo:
            test_point = interval[0] + 1  # Берем точку трохи правіше, якщо права межа ∞
        else:
            test_point = (interval[0] + interval[1]) / 2  # Середня точка інтервалу

        # визначаємо значення функції в тест точці
        sign_at_point = func.subs(x, test_point)

        # округляем границы интервалов до 1 знака після коми
        rounded_interval = (round(interval[0], 1), round(interval[1], 1))

        # визначаємо знак і добаємо інтервал до результату
        if sign_at_point > 0:
            sign_intervals.append((rounded_interval, 'y > 0'))
        elif sign_at_point < 0:
            sign_intervals.append((rounded_interval, 'y < 0'))
        else:
            sign_intervals.append((rounded_interval, 'y = 0'))

    return sign_intervals

# Функція для пошуку точок перегину
def find_inflection_points(second_derivative):
    x = sympy.symbols('x')

    # Знаходимо нулі другої похідної (тобто потенційні точки перегину)
    inflection_points = sympy.solve(second_derivative, x)

    # Округлюємо кожну точку до заданої точності
    inflection_points_rounded = [round(point, 2) for point in inflection_points]

    # Повертаємо список точок перегину
    return inflection_points_rounded
