import sympy
# Функція для визначення парності функції / Function to determine if a function is even or odd
def check_even_odd_func(function):
    x = sympy.symbols('x')  # Створюємо символ x / Create the symbol x
    neg_x_func = function.subs(x, -x)  # Підставляємо -x у функцію / Substitute -x into the function

    # Перевірка на парність функції / Checking if the function is even
    if sympy.simplify(function - neg_x_func) == 0:  # Якщо різниця функцій дорівнює нулю / If the difference between functions is zero
        return "2) Функція парна"  # Функція парна / The function is even
    
    # Перевірка на непарність функції / Checking if the function is odd
    if sympy.simplify(function + neg_x_func) == 0:  # Якщо сума функцій дорівнює нулю / If the sum of the functions is zero
        return "2) Функція непарна"  # Функція непарна / The function is odd
    
    return "2) Функція загального вигляду"  # Функція загального вигляду / The function is of general form