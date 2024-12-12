'''
Файл, де створюється і відображається титульне вікно
'''
# /
import customtkinter as ctk
# /
from .main_elements import *

# кольори для елементів у вікні  / # colors for elements in the window
# колір для фону вікна / # color for window background
background = "#A76E56"
# колір для фону фреймів / # color for frame background
frame_background = "#BA7D65"
# колір для тексту label / # color for label text
text_color = "#392D20"
# колір для фону кнопки / # color for button background
button_color = "#7B4C39"
# колір для тексту кнопки / # color for button text
text_button_color = "#F1D5BA"
# колір для фону input / # color for input background
input_color = "#FAF0E6"
# колір для бортиків input / # color for input borders
input_border_color = "#EAD1B8"
# колір для внутрішнього тексту input / # color for input placeholder text
input_textholder_color = "#CAA37D"
# колір при наведенні на кнопку scroll frame (меню усіх базових функцій) / # color when hovering over the scroll frame button (menu of all basic functions)
hover_color_menu = "#F3E4D5"
# колір при наведенні на кнопку / # color when hovering over the button
button_hover_color = "#9D6249"
# колір при наведенні на checkbox / # color when hovering over the checkbox
checkbox_hover_color = "#EBCDAE"

def introdaction():
    from .main_window import run_main
    
    intrd_window = ctk.CTk()

    intrd_window.title("Титульна сторінка")
    # intrd_window.geometry("900x650")
    intrd_window.resizable(False, False)

    intrd_window.configure(
        fg_color = background
    )
    # Задать желаемый размер окна
    window_width = 950
    window_height = 650

    # Получаем размеры экрана
    screen_width = intrd_window.winfo_screenwidth()
    screen_height = intrd_window.winfo_screenheight()

    # Вычисляем позицию окна для центрирования
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Устанавливаем размеры и позицию окна
    intrd_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    school_name_l = ctk.CTkLabel(
        master = intrd_window,
        width = 800,
        height = 65,
        text = "Дніпровський науковий ліцей інформаційних\nтехнологій Дніпровської міської ради"
    )

    proj_title_l = ctk.CTkLabel(
        master = intrd_window,
        width = 800,
        height = 98,
        text = "ВИПУСКНА РОБОТА\nна тему:\n“Дослідження графіків функцій  за допомогою похідної”"
    )

    school_name_l.configure(
        fg_color = background,
        # bg_color = ,
        font = ("Roboto Slab", 22),
        text_color = text_color,
        anchor = "center"
    )
    proj_title_l.configure(
        fg_color = background,
        # bg_color = ,
        font = ("Roboto Slab", 24),
        text_color = text_color,
        anchor = "center"
    )
    teachers_names_l = ctk.CTkLabel(
        master = intrd_window,
        width = 800,
        height = 145,
        text = "Виконала учениця 11-Г класу,\nКавуненко Юлія Сергіївна\nКерівники роботи –\nБоровик Людмила Іванівна,\nЯкименко Наталія Михайлівна",
        # сделать по левому краю
    )

    teachers_names_l.configure(
        fg_color = background,
        # bg_color = ,
        font = ("Roboto Slab", 22),
        # 
        text_color = text_color,
        # 
        anchor = "e",
        # тіпа по одной лініі с начальним текстом слєва
        justify="left"
    )
    city_data_l = ctk.CTkLabel(
        master = intrd_window,
        width = 101,
        height = 52,
        text = "м. Дніпро\n2024"
    )

    city_data_l.configure(
        fg_color = background,
        # bg_color = ,
        font = ("Roboto Slab", 20),
        text_color = text_color,
        anchor = "e"
    )



    school_name_l.place(x = 75, y = 74)
    proj_title_l.place(x = 75, y = 273)
    teachers_names_l.place(x = 75, y = 421)
    city_data_l.place(x = 425, y = 582)
    

    def open_main_window(event):
        run_main()
        
    intrd_window.bind("<Double-Button-1>", open_main_window)

    intrd_window.mainloop()