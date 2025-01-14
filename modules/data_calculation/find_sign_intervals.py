import sympy

def find_sign_intervals(func):
    x = sympy.symbols('x')  # Створюємо символ x
    
    # Знаходимо корені функції (де f(x) = 0)
    roots = sympy.solveset(func, x, domain=sympy.S.Reals)  # Знаходимо всі дійсні корені
    roots = sorted([float(root) for root in roots if root.is_real])  # Перетворюємо корені в числа і сортуємо їх
    
    # Додаємо -∞ і +∞ для побудови інтервалів
    intervals = [(-sympy.oo, roots[0])] if roots else [(-sympy.oo, sympy.oo)]  # Створюємо початковий інтервал
    for i in range(len(roots) - 1):
        intervals.append((roots[i], roots[i + 1]))  # Додаємо проміжки між коренями
    intervals.append((roots[-1], sympy.oo))  # Додаємо кінцевий інтервал
    
    # Створюємо список для збереження результатів
    sign_intervals = []
    
    # Обробляємо кожний інтервал
    for interval in intervals:
        test_point = None  # Початково призначаємо тестовій точці значення None
        if interval[0] == -sympy.oo:
            test_point = interval[1] - 1  # Беремо точку трохи лівіше, якщо ліва межа -∞
        elif interval[1] == sympy.oo:
            test_point = interval[0] + 1  # Беремо точку трохи правіше, якщо права межа ∞
        else:
            mid_point = (interval[0] + interval[1]) / 2  # Середня точка інтервалу
            if func.subs(x, mid_point).is_finite:
                test_point = mid_point  # Якщо середня точка визначена у функції, використовуємо її

        try:
            if test_point is not None and func.subs(x, test_point).is_finite:
                sign_at_point = func.subs(x, test_point)  # Обчислюємо значення функції в тестовій точці
            else:
                sign_at_point = None
        except (sympy.SympifyError, ZeroDivisionError):
            sign_at_point = None  # Якщо виникає помилка, призначаємо значення None
        
        rounded_interval = (round(interval[0], 1) if interval[0] != -sympy.oo else '-∞',
                            round(interval[1], 1) if interval[1] != sympy.oo else '+∞')
        
        if sign_at_point is not None:
            if sign_at_point > 0:
                sign_intervals.append((rounded_interval, 'y > 0'))  # Додаємо інтервал з позитивним значенням
            elif sign_at_point < 0:
                sign_intervals.append((rounded_interval, 'y < 0'))  # Додаємо інтервал з негативним значенням
            else:
                sign_intervals.append((rounded_interval, 'y = 0'))  # Додаємо інтервал з нульовим значенням

    return sign_intervals  # Повертаємо список інтервалів
