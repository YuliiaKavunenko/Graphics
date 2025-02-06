import sympy

def find_intervals(first_dev, function):
    x = sympy.symbols('x')  # створюємо символ x

    # Знаходимо критичні точки для першої похідної
    critical_points = sympy.solveset(first_dev, x, domain=sympy.S.Reals)

    # Знаходимо точки розриву (знаменник дорівнює 0)
    numer, denom = sympy.fraction(function)
    points_of_discontinuity = sympy.solveset(denom, x, domain=sympy.S.Reals)

    # Об'єднуємо критичні точки і точки розриву
    all_points = critical_points.union(points_of_discontinuity)
    sorted_points = sorted([float(pt.evalf()) for pt in all_points if pt.is_real])

    # Створюємо інтервали з урахуванням ∞
    intervals = []
    if sorted_points:
        intervals.append((-sympy.oo, sorted_points[0]))
        for i in range(len(sorted_points) - 1):
            intervals.append((sorted_points[i], sorted_points[i + 1]))
        intervals.append((sorted_points[-1], sympy.oo))
    else:
        intervals.append((-sympy.oo, sympy.oo))

    # Аналізуємо кожен інтервал
    intervals_with_state = []
    for left, right in intervals:
        midpoint = None
        if left == -sympy.oo:
            midpoint = right - 1  # Вибираємо точку ближче до межі
        elif right == sympy.oo:
            midpoint = left + 1  # Вибираємо точку ближче до межі
        else:
            midpoint = (left + right) / 2

        try:
            value_at_midpoint = first_dev.subs(x, midpoint).evalf()
            if value_at_midpoint > 0:
                intervals_with_state.append((left, right, "проміжок зростання"))
            elif value_at_midpoint < 0:
                intervals_with_state.append((left, right, "проміжок спадання"))
            else:
                intervals_with_state.append((left, right, "інтервал стаціонарний"))
        except:
            intervals_with_state.append((left, right, "інтервал не визначений"))

    # Локальні екстремуми
    local_max = []
    local_min = []
    second_dev = sympy.diff(first_dev, x)

    for point in critical_points:
        if point.is_real:
            curvature = second_dev.subs(x, point).evalf()
            if curvature < 0:
                local_max.append((float(point), float(function.subs(x, point).evalf())))
            elif curvature > 0:
                local_min.append((float(point), float(function.subs(x, point).evalf())))

    # Пошук глобального максимуму і мінімуму (на визначеній області)
    global_max = "не існує"
    global_min = "не існує"

    # Знаходимо область значень функції
    possible_values = []
    for point in critical_points:
        if point.is_real and -100 <= point <= 100:
            possible_values.append((float(point), float(function.subs(x, point).evalf())))

    # Значення функції на межах x = -100 і x = 100
    bound_values = [(-100, function.subs(x, -100).evalf()), (100, function.subs(x, 100).evalf())]
    possible_values.extend(bound_values)

    # Визначення глобальних екстремумів
    if possible_values:
        max_point, max_value = max(possible_values, key=lambda t: t[1])
        min_point, min_value = min(possible_values, key=lambda t: t[1])
        
        if max_point not in [-100, 100]:
            global_max = (max_point, max_value)
        if min_point not in [-100, 100]:
            global_min = (min_point, min_value)

    # Замінюємо -∞ та ∞ на символи
    formatted_intervals = []
    for left, right, state in intervals_with_state:
        left_str = "-∞" if left == -sympy.oo else str(left)
        right_str = "∞" if right == sympy.oo else str(right)
        formatted_intervals.append((left_str, right_str, state))

    return {
        'інтервали': formatted_intervals,
        'локальний максимум': local_max or "не існує",
        'локальний мінімум': local_min or "не існує",
        'макс. значення ф-ції': global_max,
        'мін. значення ф-ції': global_min
    }
