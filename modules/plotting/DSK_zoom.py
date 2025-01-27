"""
    Масштабування осей графіка залежно від дії (прокрутки або натискання кнопок).
    Параметри:
    - event: подія масштабування (scroll_event або key_press_event).
    - key: натискана клавіша ('+' або '-').
"""
# Імпортуємо ax і canvas із файлу з функцією побудови ДСК
from ..main_elements import ax, canvas
from ..variables_constants import dictionary_of_variables

# Глобальні змінні для відстеження стану панорамування
panning = False
start_x = 0
start_y = 0

def zoom(event=None, key=None):
    global panning, start_x, start_y

    # Обработка перемещения (панорамирования) графика
    if event and event.name == "button_press_event" and event.button == 1:  # Левая кнопка мыши
        if event.xdata is not None and event.ydata is not None:  # Проверка на None
            panning = True
            start_x, start_y = event.xdata, event.ydata
        return

    if event and event.name == "button_release_event" and event.button == 1:
        panning = False
        return

    if event and event.name == "motion_notify_event" and panning:
        if event.xdata is not None and event.ydata is not None:  # Проверка на None
            dx = event.xdata - start_x
            dy = event.ydata - start_y
            x_min, x_max = ax.get_xlim()
            y_min, y_max = ax.get_ylim()
            ax.set_xlim(x_min - dx, x_max - dx)
            ax.set_ylim(y_min - dy, y_max - dy)
            canvas.draw()
        return

    # Обработка масштабирования через колесо мыши или кнопки
    if key in ('+', '-') or (event and event.name == "scroll_event"):
        # Получаем текущие границы осей
        x_min, x_max = ax.get_xlim()
        y_min, y_max = ax.get_ylim()

        # Определяем коэффициент масштабирования
        if key == '+':
            scale_factor = 0.9
        elif key == '-':
            scale_factor = 1.1
        elif event and event.name == "scroll_event":
            scale_factor = 0.9 if event.button == 'up' else 1.1
        else:
            return

        # Рассчитываем новые границы для осей
        x_range = (x_max - x_min) * scale_factor
        y_range = (y_max - y_min) * scale_factor

        # Центрируем масштабирование относительно текущего окна
        x_center = (x_max + x_min) / 2
        y_center = (y_max + y_min) / 2

        # Обновляем границы осей
        ax.set_xlim([x_center - x_range / 2, x_center + x_range / 2])
        ax.set_ylim([y_center - y_range / 2, y_center + y_range / 2])

        # Обновляем график
        canvas.draw()
