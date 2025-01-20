import sympy

def find_simple_convexity_intervals(second_derivative):
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
            intervals.append(((left, right), "опуклість вниз"))  # Інтервал де функція опукла вгору / Interval where the function is concave up
        elif value < 0:
            intervals.append(((left, right), "опуклість вверх"))  # Інтервал де функція опукла вниз / Interval where the function is concave down

    return intervals  # Повертаємо список інтервалів опуклості / Return the list of concavity intervals