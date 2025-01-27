import customtkinter as ctk
from .windows import main
from .frame import frame_first

# Ініціалізація змінної tooltip_window / Initializing the tooltip_window variable
from ..variables_constants import dictionary_of_variables
tooltip_window = dictionary_of_variables["tooltip_window"]
# Ініціалізація таймера / Initializing the timer
tooltip_timer = None

def show_tooltip_with_delay(event, text, delay=500):
    global tooltip_timer
    # Встановлення таймера для відображення підказки / Setting up a timer to show the tooltip
    tooltip_timer = event.widget.after(delay, show_tooltip, event, text)

def show_tooltip(event, text):
    global tooltip_window
    if tooltip_window:
        tooltip_window.destroy()
    x = event.x_root + 10 
    y = event.y_root + 10
    tooltip_window = ctk.CTkToplevel(event.widget)
    tooltip_window.wm_overrideredirect(True)
    tooltip_window.wm_geometry(f"+{x}+{y}")
    label = ctk.CTkLabel(tooltip_window, text = text, bg_color = "white", text_color = "#392D20", font = ('Roboto', 12), corner_radius = 10)
    label.pack()

def hide_tooltip(event):
    global tooltip_window, tooltip_timer
    if tooltip_timer:
        # Скасування таймера якщо курсор залишає кнопку / Cancel the timer if the cursor leaves the button
        event.widget.after_cancel(tooltip_timer)
        tooltip_timer = None
    if tooltip_window:
        tooltip_window.destroy()
        tooltip_window = None
        
# кнопка на головному вікні для отримання даних який графік малювати і досліджувати / button on the main window to get data on which graph to draw and research
button_get = ctk.CTkButton(
    master= frame_first,
    width= 40,
    height=40
)
# робота функції відображення підсказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
button_get.bind("<Enter>", lambda event: show_tooltip_with_delay(event, "Побудова вибраного або введеного вами графіку функції"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
button_get.bind("<Leave>", hide_tooltip)
# створення кнопки на головному вікні для побудови і дослідження першого графіку / creating a button on the main window for building and researching the first graph
get_grachic_1 = ctk.CTkButton(
    master = frame_first,
    width = 40,
    height = 40
)
# робота функції відображення підсказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
get_grachic_1.bind("<Enter>", lambda event: show_tooltip_with_delay(event, "Побудова і дослідження графіку функції y = ax**3 + bx**2 + cx + d"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
get_grachic_1.bind("<Leave>", hide_tooltip)
# створення кнопки на головному вікні для очищення ДСК / creating a button on the main window for clearing the system
clean_graphic = ctk.CTkButton(
    master = main,
    width = 85,
    height = 35
)
# робота функції відображення підсказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
clean_graphic.bind("<Enter>", lambda event: show_tooltip_with_delay(event, "Очищення поля побудови графіків функцій і введених користувачем даних"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
clean_graphic.bind("<Leave>", hide_tooltip)

# створення кнопки для побудови і дослідження графіку функції у = (x**2 - a)/(x - b) / creating a button for building and researching the graph of the function y = (x**2 - a)/(x - b)
get_drob_grachic = ctk.CTkButton(
    master = frame_first,
    width = 40,
    height = 40
)
# робота функції відображення підсказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
get_drob_grachic.bind("<Enter>", lambda event: show_tooltip_with_delay(event, "Побудова і дослідження графіку функції у = (x**2 - a)/(x - b)"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
get_drob_grachic.bind("<Leave>", hide_tooltip)
# створення кнопки для побудови і дослідження графіку функції y = (x**2 - a**2)/x / creating a button for building and researching the graph of the function y = (x**2 - a**2)/x
third_func_button = ctk.CTkButton(
    master = frame_first,
    width = 40,
    height = 40
)
# робота функції відображення підсказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
third_func_button.bind("<Enter>", lambda event: show_tooltip_with_delay(event, "Побудова і дослідження графіку функції y = (x**2 - a**2)/x"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
third_func_button.bind("<Leave>", hide_tooltip)

# створення кнопки для відкриття вікна з вибором функцій / creating a button to open the window for selecting functions
choose_gr = ctk.CTkButton(
    master=frame_first,
    width= 327,
    height = 40
)
# робота функції відображення підказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
choose_gr.bind("<Enter>", lambda event: show_tooltip_with_delay(event, "Оберіть більш складний графік функції з списку для побудови і його дослідження"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
choose_gr.bind("<Leave>", hide_tooltip)
# створення кнопки для побудови і дослідження функції y = x/(x**2 + a) / creating a button for building and researching the function y = x/(x**2 + a)
fourth_func_button = ctk.CTkButton(
    master = frame_first,
    width = 40,
    height = 40
)
# робота функції відображення підказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
fourth_func_button.bind("<Enter>", lambda event: show_tooltip_with_delay(event, "Побудова і дослідження графіку функції y = x/(x**2 + a)"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
fourth_func_button.bind("<Leave>", hide_tooltip)
# створення кнопки для побудови і дослідження графіку функції y = (x**2 + a)/(x**2 - a) / creating a button for building and researching the graph of the function y = (x**2 + a)/(x**2 - a)
fifth_func_button = ctk.CTkButton(
    master = frame_first,
    width = 40,
    height = 40
)
# робота функції відображення підказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
fifth_func_button.bind("<Enter>", lambda event: show_tooltip_with_delay(event, "Побудова і дослідження графіку функції y = (x**2 + a)/(x**2 - a)"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
fifth_func_button.bind("<Leave>", hide_tooltip)
# створення кнопки для побудови і дослідження графіку функції y = a/x**2 + x/a / creating a button for building and researching the graph of the function y = a/x**2 + x/a
sixth_func_button = ctk.CTkButton(
    master = frame_first,
    width = 40,
    height = 40
)
# робота функції відображення підказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
sixth_func_button.bind("<Enter>", lambda event: show_tooltip_with_delay(event, "Побудова і дослідження графіку функції y = a/x**2 + x/a"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
sixth_func_button.bind("<Leave>", hide_tooltip) 

# створення кнопки для побудови і дослідження графіку функції y = (x**2 + x + a)/x / creating a button for building and researching the graph of the function y = (x**2 + x + a)/x
seventh_func_button = ctk.CTkButton(
    master = frame_first,
    width = 40,
    height = 40
)
# робота функції відображення підказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
seventh_func_button.bind("<Enter>", lambda event: show_tooltip_with_delay(event, "Побудова і дослідження графіку функції y = (x**2 + x + a)/x"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
seventh_func_button.bind("<Leave>", hide_tooltip) 

#кнопки для змінення маштабування ДСК
button_plus = ctk.CTkButton(
    master= main,
    width= 40,
    height=40
)
button_plus.bind("<Enter>", lambda event: show_tooltip_with_delay(event, "Збільшення маштабу ДСК"))
button_plus.bind("<Leave>", hide_tooltip) 
button_minus = ctk.CTkButton(
    master= main,
    width= 40,
    height=40
)
button_minus.bind("<Enter>", lambda event: show_tooltip_with_delay(event, "Зменшення маштабу ДСК"))
button_minus.bind("<Leave>", hide_tooltip) 