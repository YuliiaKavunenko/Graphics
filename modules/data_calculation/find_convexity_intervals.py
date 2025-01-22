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
    fixed_points = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    # Check the sign of the second derivative in each interval
    for i in range(len(test_points) - 1):
        left, right = test_points[i], test_points[i + 1]

        # Filter fixed points that belong to the current interval
        points_in_interval = [point for point in fixed_points if left < point < right]

        if not points_in_interval:
            continue

        # Check the second derivative at the points within the interval
        is_convex_up = all(second_derivative.subs(x, point) > 0 for point in points_in_interval)
        is_convex_down = all(second_derivative.subs(x, point) < 0 for point in points_in_interval)

        if is_convex_up:
            if not any(interval == ((left, right), "опуклість вниз") for interval in intervals):
                intervals.append(((left, right), "опуклість вниз"))
        elif is_convex_down:
            if not any(interval == ((left, right), "опуклість вгору") for interval in intervals):
                intervals.append(((left, right), "опуклість вгору"))

    return intervals
