import sympy
from sympy import Symbol, S, oo

def find_convexity_intervals(expr):
    x = Symbol('x')
    intervals = []

    # Calculate the second derivative
    second_derivative = sympy.diff(expr, x, 2)

    # Find critical points (roots of second derivative and potential discontinuities)
    critical_points = set()
    
    # Roots of second derivative
    try:
        critical_points.update(sympy.solve(second_derivative, x))
    except NotImplementedError:
        # If symbolic solving fails, try numerical
        try:
            numerical_roots = sympy.nroots(second_derivative, n=100, maxsteps=500)
            critical_points.update(root for root in numerical_roots if root.is_real)
        except Exception as e:
            print(f"Error finding roots: {e}")

    # Add potential discontinuities (denominators equal to zero)
    denominators = [denom for denom in second_derivative.as_numer_denom()[1].as_ordered_factors() if denom.has(x)]
    for denom in denominators:
        try:
            critical_points.update(sympy.solve(denom, x))
        except NotImplementedError:
            try:
                numerical_roots = sympy.nroots(denom, n=100, maxsteps=500)
                critical_points.update(root for root in numerical_roots if root.is_real)
            except Exception as e:
                print(f"Error finding discontinuities: {e}")

    # Convert to float and sort
    critical_points = sorted(float(point.evalf()) for point in critical_points if point.is_real)

    # Create test points
    test_points = [-oo] + critical_points + [oo]

    # Check the sign of the second derivative in each interval
    for i in range(len(test_points) - 1):
        left, right = test_points[i], test_points[i+1]
        mid = (left + right) / 2 if left != -oo and right != oo else 0 if left == -oo else left

        try:
            value = second_derivative.subs(x, mid)
            if value.is_real:
                if value > 0:
                    intervals.append(((left, right), "опуклість вниз"))
                elif value < 0:
                    intervals.append(((left, right), "опуклість вверх"))
                else:
                    intervals.append(((left, right), "невизначена опуклість"))
            else:
                intervals.append(((left, right), "комплексне значення"))
        except (sympy.core.expr.ExpressionException, TypeError, ValueError):
            intervals.append(((left, right), "невизначена опуклість"))

    return intervals
