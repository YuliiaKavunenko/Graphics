import sympy
# Функція для знаходження точок перегину графіку функцій / Function to find inflection points of function graphs
def find_inflection_points(second_derivative):
    x = sympy.symbols('x')  # Створюємо символ x / Create the symbol x

    # Знаходимо нулі другої похідної (тобто потенційні точки перегину) / Find the zeros of the second derivative (potential inflection points)
    inflection_points = sympy.solve(second_derivative, x)  # Розв'язуємо рівняння для другої похідної / Solve the equation for the second derivative

    # Округлюємо кожну точку до заданої точності / Round each point to the specified precision
    inflection_points_rounded = [round(point, 1) for point in inflection_points]  # Округлення точок перегину / Rounding inflection points

    # Повертаємо список точок перегину / Return the list of inflection points
    return inflection_points_rounded