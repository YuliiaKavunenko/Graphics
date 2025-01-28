import sympy, numpy
from ..main_elements import *
from ..data_calculation import (
    scope_of_function, 
    format_intervals, 
    check_even_odd_func, 
    points_ox_oy, 
    find_sign_intervals, 
    find_intervals, 
    find_inflection_points, 
    find_convexity_intervals,
    plot_horizontal_asymptotes,
    find_and_plot_slant_asymptote
    )

def plot_graph(ax, canvas):
    from .plot_constant_function import plot_constant_function
    from .punctured_dots import punctured_dots
    from .build_DSK import build_DSK
    from ..error_window import show_error_window

    ax.clear()
    build_DSK()
    button_get.focus()
    function_text = input_graphic.get()

    if function_text.strip():
        # base_dev_checkbox1.place(x = 25, y = 65)
        # base_dev_checkbox2.place(x = 25, y = 110)
        x = sympy.symbols('x')
        try:
            expr = sympy.sympify(function_text)
            if isinstance(expr, sympy.Number):
                plot_constant_function(float(expr), 'red')
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

                even_or_odd_func_l.configure(text ='Функція загального вигляду')  # оновлюємо лейбл для парності функції / update the label for the function's parity

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
                # build_colors_labels()
                # main_graphic_label.place(x = 25, y = 20)
                # base_dev_checkbox1.place(x = 25, y = 65)
                # base_dev_checkbox2.place(x = 25, y = 110)
                dev_expr = sympy.diff(expr, x)
                second_dev_expr = sympy.diff(dev_expr, x)
                func = sympy.lambdify(x, expr, 'numpy')

                x_vals = numpy.linspace(-100, 100, 4000)
                y_vals = func(x_vals)

                ax.plot(x_vals, y_vals, label=f'y = {function_text}', color='red')
                ax.legend()
                legend = ax.legend()
                for text in legend.get_texts():
                    
                    text.set_color('red')
                canvas.draw()

                # Existing calculations
                domain = scope_of_function(expr)
                domain_text = f"1) D(y) = {format_intervals(domain)}"
                scope_label.configure(text=domain_text)

                intervals_data = find_intervals(dev_expr, expr)
                if len(intervals_data['інтервали']) != 0:
                    interval_text = "\n".join([f"({str(left)[0:4]}; {str(right)[0:4]}) {state}" for left, right, state in intervals_data['інтервали']])
                else:
                    interval_text = "Інтервалів зростання/спадання не існує"
                interval_label.configure(text=f'3) {interval_text}')

                if intervals_data['локальний максимум'] != 'не існує':
                    local_max_text = "4) Локальний максимум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний максимум']])
                    for point, value in intervals_data['локальний максимум']:
                        scatter = ax.scatter(point, value, color='#FF0899', zorder=5, picker=5)
                        annotation = ax.annotate(f'({point:.2f}, {value:.2f})',
                                                (point, value),
                                                textcoords="offset points",
                                                xytext=(0, -15),
                                                ha='center',
                                                visible=False)
                        scatter.annotation = annotation
                else:
                    local_max_text = "4) Локальний максимум: не існує"

                if intervals_data['локальний мінімум'] != "не існує":
                    local_min_text = "Локальний мінімум:\n" + "\n".join([f"x = {point:.2f}, y = {value:.2f}" for point, value in intervals_data['локальний мінімум']])
                    for point, value in intervals_data['локальний мінімум']:
                        scatter = ax.scatter(point, value, color='#FF0899', zorder=5, picker=5)
                        annotation = ax.annotate(f'({point:.2f}, {value:.2f})',
                                                (point, value),
                                                textcoords="offset points",
                                                xytext=(0, -15),
                                                ha='center',
                                                visible=False)
                        scatter.annotation = annotation
                else:
                    local_min_text = "Локальний мінімум: не існує"

                if isinstance(intervals_data['макс. значення ф-ції'], tuple):
                    funct_max_text = f"Макс. значення ф-ції: x = {intervals_data['макс. значення ф-ції'][0]:.2f}, y = {intervals_data['макс. значення ф-ції'][1]:.2f}"
                else:
                    funct_max_text = f"Макс. значення ф-ції: {intervals_data['макс. значення ф-ції']}"

                if isinstance(intervals_data['мін. значення ф-ції'], tuple):
                    func_min_text = f"Мін. значення ф-ції: x = {intervals_data['мін. значення ф-ції'][0]:.2f}, y = {intervals_data['мін. значення ф-ції'][1]:.2f}"
                else:
                    func_min_text = f"Мін. значення ф-ції: {intervals_data['мін. значення ф-ції']}"

                local_max_min_text = f'{local_max_text}\n{local_min_text}'
                local_max_min_label.configure(text=local_max_min_text)

                zn_function_text = f'5) {funct_max_text}\n{func_min_text}'
                zn_function_label.configure(text=zn_function_text)

                points_0x_0y = points_ox_oy(expr, 'red', True)
                points_zero = points_0x_0y['points_zero']
                if points_zero:
                    points_0x_text = "; ".join([f"({x:.2f}, 0)" for x in points_zero])
                else:
                    points_0x_text = "не існує"

                oy_point = points_0x_0y['0y']
                oy_text = "не існує"
                if oy_point:
                    offsets = oy_point.get_offsets()
                    if len(offsets) > 0:
                        oy_coords = offsets[0]
                        oy_text = f"(0, {oy_coords[1]:.2f})"

                points_0x_0y_text = (
                    f"6) Точки перетину з Ox:\n{points_0x_text}\n"
                    f"Точка перетину з Oy:\n{oy_text}"
                )
                points_ox_oy_label.configure(text=points_0x_0y_text)

                if points_zero:
                    points_zero_text = "7) Нулі функції: " + ", ".join([f"x{i+1} = {point:.2f}" for i, point in enumerate(points_zero)])
                else:
                    points_zero_text = "7) Нулі функції: не існує"
                points_zero_label.configure(text=points_zero_text)

                even_or_odd = check_even_odd_func(expr)
                even_or_odd_func_l.configure(text=f'{even_or_odd}')

                try:
                    sign_intervals = find_sign_intervals(expr)
                    all_sign_intervals_text = ""
                    for interval, sign in sign_intervals:
                        all_sign_intervals_text += f"{sign} при х ∈ {interval}\n"
                    intervals_identity_l.configure(text=f"8) Проміжки знакосталості:\n{all_sign_intervals_text}")
                except Exception as e:
                    print(f"Помилка обчислення проміжків знакосталості: {e}")
                    intervals_identity_l.configure(text="8) Проміжки знакосталості:\nнеможливо обчислити")

                punctured_dots(expr)

                inflection_points = find_inflection_points(second_dev_expr)
                if inflection_points:
                    formatted_points = "; ".join([f"x = {float(pt):.2f}" for pt in inflection_points if sympy.im(pt) == 0])
                    inflection_points_label.configure(text=f"9) Точки перегину: {formatted_points}")
                    # Plot inflection points
                    for point in inflection_points:
                        if sympy.im(point) == 0:
                            y_val = expr.subs(x, point)
                            scatter = ax.scatter(float(point), float(y_val), color='blue', zorder=5, picker=5)
                            annotation = ax.annotate(f'({float(point):.2f}, {float(y_val):.2f})',
                                                    (float(point), float(y_val)),
                                                    textcoords="offset points",
                                                    xytext=(0, -15),
                                                    ha='center',
                                                    color='blue',
                                                    visible=False)
                            scatter.annotation = annotation
                else:
                    inflection_points_label.configure(text="9) Точки перегину: не існує")

                convexity_intervals = find_convexity_intervals(second_dev_expr)
                convexity_text = "10) Проміжки опуклості графіка:\n"
                for interval, convexity in convexity_intervals:
                    left, right = interval
                    left = "-∞" if left == float('-inf') else f"{left:.2f}"
                    right = "+∞" if right == float('inf') else f"{right:.2f}"
                    convexity_text += f"{convexity} при x ∈ ({left}; {right})\n"
                convexity_intervals_label.configure(text=convexity_text)

                def on_hover(event):
                    for scatter in ax.collections:
                        if hasattr(scatter, 'annotation'):
                            cont, ind = scatter.contains(event)
                            if cont:
                                scatter.annotation.set_visible(True)
                            else:
                                scatter.annotation.set_visible(False)
                    canvas.draw_idle()

                canvas.mpl_connect('motion_notify_event', on_hover)
                # Пошук і побудова косої асимптоти / Finding and plotting the slant asymptote
                slant_asymptote_label = slope_asymptote  # Рівняння асимптоти / Equation of the asymptote
                find_and_plot_slant_asymptote(expr, x, label_widget=slope_asymptote)

                plot_horizontal_asymptotes(expr = expr)

                canvas.draw()
        except:
            show_error_window(error_message = "Помилка! Було введено некоректні дані. Перевірте функцію ще раз.")

def build_graphic():
    plot_graph(ax, canvas)