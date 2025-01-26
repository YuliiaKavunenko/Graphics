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
    try:
        domain = sympy.calculus.util.continuous_domain(function, x, sympy.S.Reals)
        if domain.is_finite:
            boundary_values = [(pt, function.subs(x, pt).evalf()) for pt in domain]
            global_max = max(boundary_values, key=lambda t: t[1])
            global_min = min(boundary_values, key=lambda t: t[1])
    except:
        pass

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
