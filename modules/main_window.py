'''
Файл для розміщення елементів СTK на головному вікні. / File for placing CTK elements on the main window.
'''
# імпортуємо модуль customtkinter для створення Desktop додатку й елементів для нього / import the customtkinter module for creating Desktop application and elements for it
import customtkinter as ctk
# імпортуємо усі елементи з файлу main_elements / import all elements from the main_elements file
from .main_elements import *

print('MAIN')
# функція для запуску нашого головного вікна у роботу / function to start our main window
def run_main():
    # імортуємо функції для побудови ДСК, відображення і зникнення меню базових функцій, зміни фокусу / import functions for building DSK, showing and hiding the basic functions menu, and changing focus
    from .elements_functions import build_DSK, appear_menu, disappear_menu, focus_on_elements
    global button_get, input_graphic, main, canvas, fig, ax, label_y

    # Встановлюємо тему і тему за замовчуванням для вікна / Set theme and default theme for the window
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    # Встановлюємо назву для вікна / Set window title
    main.title("Випускна робота")
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

    # РАЗМЕЩЕНИЕ / PLACEMENT

    button_get.place(x = 978, y = 15)

    input_graphic.place(x = 743, y = 15)

    func_t_or_f.place(x = 688, y = 65)
    choose_gr.place(x = 688, y = 96)

    input_graphic.bind('<FocusIn>', appear_menu) #привязка к ктк ентри, что когда каретка внутри, то меню появляется / bind to ctk entry, so when the cursor is inside, the menu appears
    input_graphic.bind('<FocusOut>', disappear_menu) #привязка к ктк ентри, что когда каретка не в нем, то меню исчезает / bind to ctk entry, so when the cursor is not in it, the menu disappears

    label_y.place(x = 711, y = 15)

    clean_graphic.place(x = 580, y = 730)

    frame_first.place(x = 680, y = 5)
    frame_for_options.place(x = 1030, y = 5)
    frame_exploration.place(x = 680, y = 355)

    frame_first.bind('<Button-1>', focus_on_elements)
    frame_for_options.bind('<Button-1>', focus_on_elements)
    frame_exploration.bind('<Button-1>', focus_on_elements)

    l_exploration.place(x = 925, y = 360)
    l_exploration.bind('<Button-1>', focus_on_elements)

    # Label для виводу області визначення функції / Label to display the function domain
    scope_label.place(x = 690, y = 390)
    # зміна фокусу за допомогою функції при натисканні на Label лівою кнопкою миші / change focus using the function by clicking on the Label with the left mouse button
    scope_label.bind('<Button-1>', focus_on_elements)
    # Label для виводу таких даних: парна чи не парна функція / Label to display such data: whether the function is even or odd
    even_or_odd_func_l.place(x = 690, y = 420)
    # Label для виводу проміжків спадання і проміжків зростання функції / Label to display intervals of decrease and increase of the function
    interval_label.place(x = 690, y = 450)
    # 
    interval_label.bind('<Button-1>', focus_on_elements)

    # Label для виводу локального максимуму і локального мінімуму / Label to display the local maximum and local minimum
    local_max_min_label.place(x = 690, y = 515)
    local_max_min_label.bind('<Button-1>', focus_on_elements)
    # Label для виводу мінімального і максимального знач. функції / Label to display the minimum and maximum values of the function
    zn_function_label.place(x = 690, y = 600)
    zn_function_label.bind('<Button-1>', focus_on_elements)
    # Label для виводу точок перетину графіку з осями ох і оу / Label to display the points of intersection of the graph with the x and y axes
    points_ox_oy_label.place(x = 690, y = 640)
    # Label для виводу нулів функцій / Label to display the zeros of the functions
    points_zero_label.place(x = 690, y = 725)
    # Label для виводу проміжків знакосталості / Label to display intervals of constancy
    intervals_identity_l.place(x = 1060, y = 390)
    # Label для виводу точок перегину / Label to display inflection points
    inflection_points_label.place(x = 1060, y = 475)
    # Label для виводу проміжків опуклості функції / Label to display intervals of convexity of the function
    convexity_intervals_label.place(x = 1060, y = 540)
    # Label для виводу похилої асимптоти / Label to display the slant asymptote
    slope_asymptote.place(x = 1060, y = 625)

    # Label для виводу кольору побудови базових функцій / Label to display the color of basic function construction
    purple_gr.place(x = 685, y = 15)

    # Виконуємо побудову ДСК / Perform DSK construction
    build_DSK()
    
    canvas.get_tk_widget().place(x=10, y=10, width=830, height=955)  # Редагування холста / Edit canvas
    canvas.get_tk_widget().configure(bg='#FAF0E6') # Встановлюємо фон для ДСК / Set background for DSK
    # запускаємо додаток у роботу / start the application
    main.mainloop()