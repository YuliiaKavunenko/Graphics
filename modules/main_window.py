'''
Файл для розміщення елементів СTK на головному вікні. / File for placing CTK elements on the main window.
'''
# імпортуємо модуль customtkinter для створення Desktop додатку й елементів для нього / import the customtkinter module for creating Desktop application and elements for it
import customtkinter as ctk
# імпортуємо усі елементи з файлу main_elements / import all elements from the main_elements file
from .main_elements import *
from .plotting import *

def on_close():
    main.withdraw()

# функція для запуску нашого головного вікна у роботу / function to start our main window
def run_main():
    # Встановлюємо тему і тему за замовчуванням для вікна / Set theme and default theme for the window
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    # Встановлюємо назву для вікна / Set window title
    main.title("Програмна частина")
    # Задаємо ширину для вікна / Set window width
    window_width = 1400
    # Задаємо висоту для вікна / Set window height
    window_height = 780

    # Отримуємо розмір вікна / Get window size
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()

    # Обчислюємо розмір вікна для позиціювання / Calculate window size for positioning
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Встановлюємо розміри і розташування вікна / Set window size and position
    main.geometry(f"{window_width}x{window_height}+{x}+{y}")
    # Встановлюємо неможливість змінити розміри вікна / Disable resizing of the window
    main.resizable(False, False)

    main.lift()
    main.focus_set()

    # розташування усіх елементів на вікні / location of all elements on the window

    frame_first.place(x = 680, y = 5)
    frame_for_options.place(x = 1030, y = 5)
    frame_exploration.place(x = 680, y = 355)

    frame_first.bind('<Button-1>', focus_on_elements)
    frame_for_options.bind('<Button-1>', focus_on_elements)
    frame_exploration.bind('<Button-1>', focus_on_elements)
    
    button_get.place(x = 298, y = 10)

    input_graphic.place(x = 63, y = 10)

    func_t_or_f.place(x = 10, y = 55)
    choose_gr.place(x = 8, y = 91)

    input_graphic.bind('<FocusIn>', appear_menu) #прив'язка до ктк ентрі, коли каретка всередині, то меню з'являється / bind to ctk entry, so when the cursor is inside, the menu appears
    input_graphic.bind('<FocusOut>', disappear_menu) #прив'язка до ктк ентрі, що коли каретка не в ньому, то меню зникає / bind to ctk entry, so when the cursor is not in it, the menu disappears

    label_y.place(x = 31, y = 10)

    clean_graphic.place(x = 575, y = 730)

    l_exploration.place(x = 245, y = 10)
    l_exploration.bind('<Button-1>', focus_on_elements)

    # Label для виводу області визначення функції / Label to display the function domain
    scope_label.place(x = 10, y = 35)
    # зміна фокусу за допомогою функції при натисканні на Label лівою кнопкою миші / change focus using the function by clicking on the Label with the left mouse button
    scope_label.bind('<Button-1>', focus_on_elements)
    # Label для виводу таких даних: парна чи не парна функція / Label to display such data: whether the function is even or odd
    even_or_odd_func_l.place(x = 10, y = 70)
    # Label для виводу проміжків спадання і проміжків зростання функції / Label to display intervals of decrease and increase of the function
    interval_label.place(x = 10, y = 105)
    # 
    interval_label.bind('<Button-1>', focus_on_elements)

    # # Label для виводу локального максимуму і локального мінімуму / Label to display the local maximum and local minimum
    local_max_min_label.place(x = 10, y = 195)
    local_max_min_label.bind('<Button-1>', focus_on_elements)
    # Label для виводу мінімального і максимального знач. функції / Label to display the minimum and maximum values of the function
    zn_function_label.place(x = 10, y = 280)
    zn_function_label.bind('<Button-1>', focus_on_elements)
    # Label для виводу точок перетину графіку з осями ох і оу / Label to display the points of intersection of the graph with the x and y axes
    points_ox_oy_label.place(x = 10, y = 330)
    # Label для виводу нулів функцій / Label to display the zeros of the functions
    points_zero_label.place(x = 400, y = 35)
    # Label для виводу проміжків знакосталості / Label to display intervals of constancy
    intervals_identity_l.place(x = 400, y = 80)
    # Label для виводу точок перегину / Label to display inflection points
    inflection_points_label.place(x = 400, y = 190)
    # Label для виводу проміжків опуклості функції / Label to display intervals of convexity of the function
    convexity_intervals_label.place(x = 400, y = 245)
    # Label для виводу похилої асимптоти / Label to display the slant asymptote
    slope_asymptote.place(x = 400, y = 370)

    # Label для виводу кольору побудови базових функцій / Label to display the color of basic function construction
    base_gr.place(x = 5, y = 10)

    # Виконуємо побудову ДСК / Perform DSK construction
    build_DSK()
    
    canvas.get_tk_widget().place(x=10, y=10, width=830, height=955)  # Редагування холста / Edit canvas
    canvas.get_tk_widget().configure(bg='#FAF0E6') # Встановлюємо фон для ДСК / Set background for DSK

    button_plus.place(x = 625, y = 15)
    button_minus.place(x = 580, y = 15)

    posibnik_button.place(x = 16, y = 11)
    # запускаємо додаток у роботу / start the application
    main.protocol("WM_DELETE_WINDOW", on_close)
    main.deiconify()