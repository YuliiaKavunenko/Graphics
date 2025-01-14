import customtkinter as ctk
from .windows import main
from .frame import frame_first

# Ініціалізація змінної tooltip_window / Initializing the tooltip_window variable
from ..variables_constants import dictionary_of_variables
tooltip_window = dictionary_of_variables["tooltip_window"]

# функція для відображення підказки / function to show tooltip
def show_tooltip(event, text):
    global tooltip_window
    # Якщо вікно вже існує, знищити його / If the window exists, destroy it
    if tooltip_window:
        tooltip_window.destroy()
    # Отримання координат курсора / Getting cursor coordinates
    x = event.x_root + 10 # +10 - зміщення від курсора / +10 - offset from the cursor
    y = event.y_root + 10
    # Створення вікна підказки / Creating a tooltip window
    tooltip_window = ctk.CTkToplevel(event.widget)
    # Налаштування вікна підказки / Setting up the tooltip window
    tooltip_window.wm_overrideredirect(True)  # Вікно без рамки / Window without frame
    tooltip_window.wm_geometry(f"+{x}+{y}") # Розміщення вікна за координатами курсора / Placing the window at the cursor coordinates
    # Створення мітки з текстом підказки / Creating a label with tooltip text
    label = ctk.CTkLabel(tooltip_window, text = text, bg_color = "white", text_color = "#392D20",font = ('Roboto', 12), corner_radius = 10)
    # Розміщення мітки в вікні / Placing the label in the window
    label.pack()

# функція для приховування підказки / function to hide tooltip
def hide_tooltip(event):
    global tooltip_window
    # Якщо вікно існує, знищити його / If the window exists, destroy it
    if tooltip_window:
        # Знищення вікна / Destroying the window
        tooltip_window.destroy()
        # Присвоєння значення None змінній tooltip_window / Assigning the value None to the tooltip_window variable
        tooltip_window = None
        
# кнопка на головному вікні для отримання даних який графік малювати і досліджувати / button on the main window to get data on which graph to draw and research
button_get = ctk.CTkButton(
    master= frame_first,
    width= 40,
    height=40
)
# робота функції відображення підсказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
button_get.bind("<Enter>", lambda event: show_tooltip(event, "Побудова вибраного або введеного вами графіку функції /\nBuild the selected or entered by you function graph"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
button_get.bind("<Leave>", hide_tooltip)
# створення кнопки на головному вікні для побудови і дослідження першого графіку / creating a button on the main window for building and researching the first graph
get_grachic_1 = ctk.CTkButton(
    master = frame_first,
    width = 40,
    height = 40
)
# робота функції відображення підсказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
get_grachic_1.bind("<Enter>", lambda event: show_tooltip(event, "Побудова і дослідження графіку функції y = ax**3 + bx**2 + cx + d /\nBuild and research the graph of the function y = ax**3 + bx**2 + cx + d"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
get_grachic_1.bind("<Leave>", hide_tooltip)
# створення кнопки на головному вікні для очищення ДСК / creating a button on the main window for clearing the system
clean_graphic = ctk.CTkButton(
    master = main,
    width = 85,
    height = 35
)
# робота функції відображення підсказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
clean_graphic.bind("<Enter>", lambda event: show_tooltip(event, "Очищення поля побудови графіків функцій і введених користувачем даних  /\nClearing the field for building function graphs and user-entered data"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
clean_graphic.bind("<Leave>", hide_tooltip)

# створення кнопки для побудови і дослідження графіку функції у = (x**2 - a)/(x - b) / creating a button for building and researching the graph of the function y = (x**2 - a)/(x - b)
get_drob_grachic = ctk.CTkButton(
    master = frame_first,
    width = 40,
    height = 40
)
# робота функції відображення підсказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
get_drob_grachic.bind("<Enter>", lambda event: show_tooltip(event, "Побудова і дослідження графіку функції у = (x**2 - a)/(x - b) /\nBuild and research the graph of the function y = (x**2 - a)/(x - b)"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
get_drob_grachic.bind("<Leave>", hide_tooltip)
# створення кнопки для побудови і дослідження графіку функції y = (x**2 - a**2)/x / creating a button for building and researching the graph of the function y = (x**2 - a**2)/x
third_func_button = ctk.CTkButton(
    master = frame_first,
    width = 40,
    height = 40
)
# робота функції відображення підсказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
third_func_button.bind("<Enter>", lambda event: show_tooltip(event, "Побудова і дослідження графіку функції y = (x**2 - a**2)/x /\nBuild and research the graph of the function y = (x**2 - a**2)/x"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
third_func_button.bind("<Leave>", hide_tooltip)

# створення кнопки для відкриття вікна з вибором функцій / creating a button to open the window for selecting functions
choose_gr = ctk.CTkButton(
    master=frame_first,
    width= 327,
    height = 40
)
# робота функції відображення підказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
choose_gr.bind("<Enter>", lambda event: show_tooltip(event, "Оберіть більш складний графік функції з списку для побудови і його дослідження /\nChoose a more complex function graph from the list for building and researching"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
choose_gr.bind("<Leave>", hide_tooltip)
# створення кнопки для побудови і дослідження функції y = x/(x**2 + a) / creating a button for building and researching the function y = x/(x**2 + a)
fourth_func_button = ctk.CTkButton(
    master = frame_first,
    width = 40,
    height = 40
)
# робота функції відображення підказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
fourth_func_button.bind("<Enter>", lambda event: show_tooltip(event, "Побудова і дослідження графіку функції y = x/(x**2 + a) /\nBuild and research the graph of the function y = x/(x**2 + a)"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
fourth_func_button.bind("<Leave>", hide_tooltip)
# створення кнопки для побудови і дослідження графіку функції y = (x**2 + a)/(x**2 - a) / creating a button for building and researching the graph of the function y = (x**2 + a)/(x**2 - a)
fifth_func_button = ctk.CTkButton(
    master = frame_first,
    width = 40,
    height = 40
)
# робота функції відображення підказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
fifth_func_button.bind("<Enter>", lambda event: show_tooltip(event, "Побудова і дослідження графіку функції y = (x**2 + a)/(x**2 - a) /\nBuild and research the graph of the function y = (x**2 + a)/(x**2 - a)"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
fifth_func_button.bind("<Leave>", hide_tooltip)
# створення кнопки для побудови і дослідження графіку функції y = a/x**2 + x/a / creating a button for building and researching the graph of the function y = a/x**2 + x/a
sixth_func_button = ctk.CTkButton(
    master = frame_first,
    width = 40,
    height = 40
)
# робота функції відображення підказки при наведенні курсора на кнопку / function to show tooltip when hovering over the button
sixth_func_button.bind("<Enter>", lambda event: show_tooltip(event, "Побудова і дослідження графіку функції y = a/x**2 + x/a /\nBuild and research the graph of the function y = a/x**2 + x/a"))
# робота функції приховування підказки при відведенні курсора від кнопки / function to hide the tooltip when the cursor is removed from the button
sixth_func_button.bind("<Leave>", hide_tooltip) 