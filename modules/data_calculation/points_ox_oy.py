import sympy
from ..main_elements import canvas, ax
from matplotlib.offsetbox import AnnotationBbox, TextArea

def points_ox_oy(graphic, color, label=False, lines=False, include_oy=True):
    x = sympy.symbols('x')
    y_intercept = graphic.subs(x, 0)
    x_intercepts = sympy.solve(graphic, x)
    x_intercepts = [root.evalf() for root in x_intercepts if root.is_real and not root.has(sympy.I)]
    x_intercepts = [round(float(root), 1) for root in x_intercepts]

    points_zero = []
    ox_points = []
    dashed_lines = []
    annotations = []

    if x_intercepts:
        for x_cor in x_intercepts:
            point = ax.scatter(x_cor, 0, color=color, s=40, picker=5)
            ox_points.append(point)
            points_zero.append(x_cor)

            if label:
                annotation = ax.annotate(f'({x_cor:.2f}, 0)',
                                         (x_cor, 0),
                                         textcoords="offset points",
                                         xytext=(10, 10),
                                         ha='center',
                                         visible=False)
                annotations.append(annotation)

            if lines:
                line = ax.axvline(x=x_cor, color=color, linestyle='--', linewidth=1)
                dashed_lines.append(line)

    oy_point = None
    if include_oy and y_intercept.is_real:
        y_cor = round(float(y_intercept), 2)
        oy_point = ax.scatter(0, y_cor, color=color, s=40, picker=5)
        if label:
            annotation = ax.annotate(f'(0, {y_cor})',
                                     (0, y_cor),
                                     textcoords="offset points",
                                     xytext=(10, 10),
                                     ha='center',
                                     visible=False)
            annotations.append(annotation)

    def on_hover(event):
        if event.inaxes == ax:
            all_points = ox_points + ([oy_point] if oy_point else [])
            for i, point in enumerate(all_points):
                if i < len(annotations):  # Проверка, чтобы избежать выхода за границы списка
                    cont, _ = point.contains(event)
                    if cont:
                        annotations[i].set_visible(True)
                    else:
                        annotations[i].set_visible(False)
                else:
                    pass
            canvas.draw_idle()
    canvas.mpl_connect('motion_notify_event', on_hover)

    canvas.draw()

    return {
        '0y': oy_point,
        '0x': ox_points,
        'points_zero': points_zero,
        'lines': dashed_lines,
        'annotations': annotations
    }