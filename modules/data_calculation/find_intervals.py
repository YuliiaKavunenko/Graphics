import sympy

# Функція для пошуку проміжків спадання і зростання функції, локальних максимумів і мінімумів, а також максимальних і мінімальних значень функції
def find_intervals(first_dev, function):
    x = sympy.symbols('x')  # створюємо символ x
    # Знаходимо критичні точки (значення x, при яких перша похідна дорівнює нулю)
    crit_points = sympy.solveset(first_dev, x, domain=sympy.S.Reals)
    
    # залишаємо тільки дійсні критичні точки і знаходимо їх числове значення
    crit_points = sorted([float(point.evalf()) for point in crit_points if point.is_real])
    
    # створюємо список для збереження інтервалів
    intervals = []
    intervals_with_state = []
    local_max = []
    local_min = []
    
    # Додаємо -∞ і +∞ для побудови інтервалів
    if crit_points:
        intervals.append((-sympy.oo, crit_points[0]))
        for i in range(len(crit_points) - 1):
            intervals.append((crit_points[i], crit_points[i + 1]))
        intervals.append((crit_points[-1], sympy.oo))
    else:
        intervals.append((-sympy.oo, sympy.oo))
    
    # Перевіряємо кожен інтервал
    for left, right in intervals:
        midpoint = (left + right) / 2

        # Перевіряємо, чи є значення в середині інтервалу дійсним і визначеним
        try:
            midpoint_value = first_dev.subs(x, midpoint)
            if midpoint_value.is_real and not midpoint_value.has(sympy.zoo, sympy.nan, sympy.oo, sympy.I):
                # якщо похідна > 0, функція зростає
                if midpoint_value > 0:
                    intervals_with_state.append((left, right, "проміжок зростання"))
                # якщо похідна < 0, функція спадає
                elif midpoint_value < 0:
                    intervals_with_state.append((left, right, "проміжок спадання"))
                else:
                    intervals_with_state.append((left, right, "інтервал не визначений"))
            else:
                intervals_with_state.append((left, right, "інтервал не визначений"))
        except:
            intervals_with_state.append((left, right, "інтервал не визначений"))

    # Знаходимо локальні максимуми та мінімуми
    for point in crit_points:
        second_dev = sympy.diff(first_dev, x)
        curvature = second_dev.subs(x, point)
        
        # якщо друга похідна < 0, це локальний максимум
        if curvature.is_real and not curvature.has(sympy.zoo, sympy.nan, sympy.oo, sympy.I):
            if curvature < 0:
                local_max.append((point, function.subs(x, point)))
            # якщо друга похідна > 0, це локальний мінімум
            elif curvature > 0:
                local_min.append((point, function.subs(x, point)))
  
    if not local_max:
        local_max = "не існує"
    if not local_min:
        local_min = "не існує"
    global_max = "не існує"
    global_min = "не існує"
    
    try:
        domain = sympy.calculus.util.continuous_domain(function, x, sympy.S.Reals)
        if domain.is_finite:
            boundary_values = [(point, function.subs(x, point)) for point in domain]
            global_max = max(boundary_values, key=lambda t: t[1])
            global_min = min(boundary_values, key=lambda t: t[1])
    except:
        pass
    
    return {
        'інтервали': intervals_with_state,
        'локальний максимум': local_max,
        'локальний мінімум': local_min,
        'макс. значення ф-ції': global_max,
        'мін. значення ф-ції': global_min
    }
