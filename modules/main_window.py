'''
Файл для розміщення елементів СTK на головному вікні.
'''

import customtkinter as ctk
import matplotlib.ticker as ticker
from .main_elements import *

print('MAIN')

def run_main():
    from .elements_functions import build_DSK, appear_menu, disappear_menu, focus_on_elements
    global button_get, input_graphic, main, canvas, fig, ax, label_y

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    # главное окно приложения

    main.title("Випускна робота")
    main.geometry("1400x780")
    main.resizable(False, False)

    # РАЗМЕЩЕНИЕ 

    button_get.place(x = 978, y = 15)

    input_graphic.place(x = 743, y = 15)

    func_t_or_f.place(x = 688, y = 65)
    choose_gr.place(x = 688, y = 96)

    input_graphic.bind('<FocusIn>', appear_menu) #привязка к ктк ентри, что когда каретка внутри, то меню появляется
    input_graphic.bind('<FocusOut>', disappear_menu) #привязка к ктк ентри, что когда каретка не в нем, то меню исчезает

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

    # у = 245 норм
    scope_label.place(x = 690, y = 390)
    range_of_function.place(x = 690, y = 420)
    scope_label.bind('<Button-1>', focus_on_elements)
    even_or_odd_func_l.place(x = 690, y = 450)

    interval_label.place(x = 690, y = 480)
    interval_label.bind('<Button-1>', focus_on_elements)


    local_max_min_label.place(x = 690, y = 545)
    local_max_min_label.bind('<Button-1>', focus_on_elements)
    zn_function_label.place(x = 690, y = 630)
    zn_function_label.bind('<Button-1>', focus_on_elements)

    points_ox_oy_label.place(x = 690, y = 680)

    points_zero_label.place(x = 690, y = 725)

    intervals_identity_l.place(x = 1050, y = 390)


    purple_gr.place(x = 685, y = 15)

    # СТРОИМ ДСК!!!!1
    build_DSK()
    
    canvas.get_tk_widget().place(x=10, y=10, width=830, height=955)  # Редактирования холста
    canvas.get_tk_widget().configure(bg='#FAF0E6')

    main.mainloop()

