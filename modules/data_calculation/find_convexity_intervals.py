import sympy
from sympy import Symbol, S, oo

def find_convexity_intervals(expr):
    x = Symbol('x')
    intervals = []

    # знаходимо критичні точки другої похідної
    critical_points = set()

    # знаходимо корені другої похідної
    try:
        critical_points.update(sympy.solve(expr, x))

    except NotImplementedError:
        try:
            numerical_roots = sympy.nroots(expr, n=100, maxsteps=500)
            critical_points.update(root for root in numerical_roots if root.is_real)
        except Exception as e:
            print(f"помилка: {e}")

    # Додаємо потенційні розриви (де знаменники дорівнюють нулю)
    denominators = [denom for denom in expr.as_numer_denom()[1].as_ordered_factors() if denom.has(x)]
    for denom in denominators:
        try:
            critical_points.update(sympy.solve(denom, x))
        except NotImplementedError:
            try:
                numerical_roots = sympy.nroots(denom, n=100, maxsteps=500)
                critical_points.update(root for root in numerical_roots if root.is_real)
            except Exception as e:
                print(f"Error finding discontinuities: {e}")

    # конвертуємо до типу даних float і сортуємо
    critical_points = sorted(float(point.evalf()) for point in critical_points if point.is_real)
    # створюємо точки для тестування
    test_points = [-oo] + critical_points + [oo]
    fixed_points = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    # перевіряємо значення другої похідної для кожної з цих точок
    for i in range(len(test_points) - 1):
        left, right = test_points[i], test_points[i + 1]

        # фільтруємо точки, щоб  вони належали нашому інтервалу ОДЗ
        points_in_interval = [point for point in fixed_points if left < point < right]

        if not points_in_interval:
            continue
        
        # перевіряємо другу похідну в точках інтервалу
        is_convex_up = all(expr.subs(x, point) > 0 for point in points_in_interval)
        is_convex_down = all(expr.subs(x, point) < 0 for point in points_in_interval)

        if is_convex_up:
            if not any(interval == ((left, right), "опуклість вниз") for interval in intervals):
                intervals.append(((left, right), "опуклість вниз"))
        elif is_convex_down:
            if not any(interval == ((left, right), "опуклість вгору") for interval in intervals):
                intervals.append(((left, right), "опуклість вгору"))

    return intervals
