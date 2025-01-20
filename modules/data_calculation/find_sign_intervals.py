import sympy


def find_sign_intervals(func):
    x = sympy.symbols('x')  # Створюємо символ x

    # Отделяем числитель и знаменатель
    numer, denom = sympy.fraction(func)

    # Находим корни числителя (где f(x) = 0) и знаменателя (где разрывы)
    roots_numer = sympy.solveset(numer, x, domain=sympy.S.Reals)
    roots_denom = sympy.solveset(denom, x, domain=sympy.S.Reals)

    # Объединяем корни и сортируем их
    critical_points = sorted(
        {float(pt) for pt in roots_numer.union(roots_denom) if pt.is_real}
    )

    # Добавляем -∞ и +∞ для построения интервалов
    intervals = [(-sympy.oo, critical_points[0])] if critical_points else [(-sympy.oo, sympy.oo)]
    for i in range(len(critical_points) - 1):
        intervals.append((critical_points[i], critical_points[i + 1]))
    intervals.append((critical_points[-1], sympy.oo))

    # Создаем список для сохранения результатов
    sign_intervals = []

    # Обрабатываем каждый интервал
    for interval in intervals:
        test_point = None  # Начальная тестовая точка
        if interval[0] == -sympy.oo:
            test_point = interval[1] - 1
        elif interval[1] == sympy.oo:
            test_point = interval[0] + 1
        else:
            mid_point = (interval[0] + interval[1]) / 2
            test_point = mid_point

        # Проверяем знак функции в тестовой точке
        sign_at_point = None
        try:
            if test_point is not None:
                value = func.subs(x, test_point)
                if value.is_finite:
                    sign_at_point = value
        except (sympy.SympifyError, ZeroDivisionError):
            sign_at_point = None

        # Округляем границы интервала для вывода
        rounded_interval = (
            round(interval[0], 2) if interval[0] != -sympy.oo else "-∞",
            round(interval[1], 2) if interval[1] != sympy.oo else "+∞",
        )

        if sign_at_point is not None:
            if sign_at_point > 0:
                sign_intervals.append((rounded_interval, "y > 0"))
            elif sign_at_point < 0:
                sign_intervals.append((rounded_interval, "y < 0"))
        else:
            sign_intervals.append((rounded_interval, ""))

    return sign_intervals  # Возвращаем список интервалов
