import sympy
# функція для знаходження області визначення функції / function to find the domain of the function
def format_intervals(intervals):
    formatted_intervals = []  # створення списку для збереження відформатованих інтервалів / creating a list to store formatted intervals
    
    for interval in intervals:  # перебираємо кожен інтервал у списку intervals / iterating through each interval in the intervals list
        # визначення типу дужки для лівої границі інтервала / determining the type of bracket for the left boundary of the interval
        left_bracket = "[" if interval.left_open == False else "("
        left = f"{left_bracket}{round(interval.start)}" if interval.start != -sympy.oo else "(-∞"

        # визначення типу дужки для правої границі інтервала / determining the type of bracket for the right boundary of the interval
        right_bracket = "]" if interval.right_open == False else ")"
        right = f"{round(interval.end)}{right_bracket}" if interval.end != sympy.oo else "∞)"
        
        formatted_intervals.append(f"{left}; {right}")  # форматування інтервалу і додавання до списку formatted_intervals / formatting the interval and adding to the formatted_intervals list
    
    if not formatted_intervals:  # якщо список formatted_intervals порожній / if the formatted_intervals list is empty
        return "∅"  # повертаємо рядок, який вказує на порожню область визначення / returning a string indicating an empty domain
    elif len(formatted_intervals) == 1 and formatted_intervals[0] == "(-∞; ∞)":  # якщо є тільки один інтервал і це весь діапазон дійсних чисел / if there is only one interval and it is the entire range of real numbers
        return "R"  # повертаємо рядок, що на область є дійсною для усіх чисел / returning a string indicating the domain is all real numbers
    else:
        return " ∪ ".join(formatted_intervals)  # об'єднання всіх інтервалів за допомогою символа "∪" і повернення у типі строки / joining all intervals with the symbol "∪" and returning as a string

# функція яка перетворює отриману відповідь у математичну потрібну для Д(у) / function that converts the obtained answer into the mathematical one needed for D(y)
def scope_of_function(expr):
    x = sympy.symbols('x')  # створення символа x / creating the symbol x
    domain = sympy.calculus.util.continuous_domain(expr, x, sympy.S.Reals)  # визначення області визначення виразу / determining the domain of the expression
    intervals = []  # створення листу для збереження інтервалів області визначення (D(y)) / creating a list to store intervals of the domain (D(y))
    
    if isinstance(domain, sympy.Set):  # перевірка, що domain є об'єктом Set в sympy / checking that domain is a Set object in sympy
        if domain.is_Interval:  # перевірка, що domain є інтервалом / checking that domain is an interval
            intervals.append(domain)  # додавання інтервала в лист intervals / adding the interval to the intervals list
        elif domain.is_Union:  # перевірка, що domain є об'єднанням інтервалів / checking that domain is a union of intervals
            for subdomain in domain.args:  # перебираємо кожен підінтервал в об'єднанні / iterating through each subinterval in the union
                if subdomain.is_Interval:  # перевірка, що підінтервал є інтервалом / checking that subinterval is an interval
                    intervals.append(subdomain)  # додавання підінтервала до списку intervals / adding the subinterval to the intervals list

    print(intervals)
                    
    return intervals  # повертаємо список інтервалів області визначення / returning the list of domain intervals
