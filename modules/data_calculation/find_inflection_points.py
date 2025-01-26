import sympy
# Функція для знаходження точок перегину графіку функцій / Function to find inflection points of function graphs
def find_inflection_points(second_derivative):
    x = sympy.symbols('x')  # Створюємо символ x

    # Знаходимо нулі другої похідної (потенційні точки перегину)
    inflection_points = sympy.solve(second_derivative, x)

    # Створюємо список для зберігання реальних точок перегину
    inflection_points_real = []

    # Проходимо по знайдених точках і перевіряємо, чи є вони дійсними
    for point in inflection_points:
        if sympy.im(point) == 0:  # Якщо точка дійсна
            inflection_points_real.append(round(point.evalf(), 2))  # Округлюємо і додаємо до списку

    # Повертаємо список точок перегину
    return inflection_points_real
