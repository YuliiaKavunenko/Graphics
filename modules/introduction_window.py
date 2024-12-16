'''
Файл, де створюється і відображається титульне / The file where the title is created and displayed.
'''

# / імпортуємо customtkinter для створення додатку у елементів для нього / import customtkinter to create an application in elements for it
import customtkinter as ctk
# / імпортуємо усі елементи для додатку з файлу main_elements / import all elements for the application from the main elements file
from .main_elements import *

# кольори для елементів у вікні / colors for elements in the window
# колір для фону вікна / color for window background
background = "#A76E56"
# колір для фону фреймів / color for frame background
frame_background = "#BA7D65"
# колір для тексту label / color for label text
text_color = "#392D20"
# колір для фону кнопки / color for button background
button_color = "#7B4C39"
# колір для тексту кнопки / color for button text
text_button_color = "#F1D5BA"
# колір для фону input / color for input background
input_color = "#FAF0E6"
# колір для бортиків input / color for input borders
input_border_color = "#EAD1B8"
# колір для внутрішнього тексту input / color for input placeholder text
input_textholder_color = "#CAA37D"
# колір при наведенні на кнопку scroll frame (меню усіх базових функцій) / color when hovering over the scroll frame button (menu of all basic functions)
hover_color_menu = "#F3E4D5"
# колір при наведенні на кнопку / color when hovering over the button
button_hover_color = "#9D6249"
# колір при наведенні на checkbox / color when hovering over the checkbox
checkbox_hover_color = "#EBCDAE"

# функція для запуску роботи додатку титульного вікна / function to start the title window application
def introduction():
    # імпортуємо функцію запуску основного додатку / import the function to launch the main application
    from .main_window import run_main
    # створюємо титульний додаток / create the title application
    intrd_window = ctk.CTk()
    # задаємо ім'я для титульного додатку / set the name for the title application
    intrd_window.title("Титульна сторінка")
    # задаємо неможливість змінювати розмір вікна / make the window size non-resizable
    intrd_window.resizable(False, False)

    # встановлюємо колір тла для титульного додатку / set the background color for the title application
    intrd_window.configure(
        fg_color = background
    )
    # зберігаємо ширину вікна / save the window width
    window_width = 950
    # зберігаємо висоту вікна / save the window height
    window_height = 650

    # отримуємо розміри нашого екрана / get the dimensions of our screen
    screen_width = intrd_window.winfo_screenwidth()
    screen_height = intrd_window.winfo_screenheight()

    # обчислюємо позицію вікна для центрування / calculate the window position for centering
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # встановлюємо розмір і позицію вікна / set the window size and position
    intrd_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # створюємо Label для відображення навчального закладу на титульному вікні / create a Label to display the educational institution on the title window
    school_name_l = ctk.CTkLabel(
        master = intrd_window, 
        width = 800, 
        height = 65, 
        text = "Дніпровський науковий ліцей інформаційних\nтехнологій Дніпровської міської ради"
    )
    # створюємо Label для відображення теми випускної роботи на титульному вікні / create a Label to display the graduation project topic on the title window
    proj_title_l = ctk.CTkLabel(
        master = intrd_window, 
        width = 800, height = 98, 
        text = "ВИПУСКНА РОБОТА\nна тему:\n“Дослідження графіків функцій  за допомогою похідної”"
        )
    # задаємо стилі для Label / set styles for the Label
    school_name_l.configure(
        fg_color = background, 
        font = ("Roboto Slab", 22), 
        text_color = text_color, 
        anchor = "center"
        )
    # задаємо стилі для Label / set styles for the Label
    proj_title_l.configure(
        fg_color = background, 
        font = ("Roboto Slab", 24), 
        text_color = text_color, 
        anchor = "center"
        )
    # створюємо Label для відображення свого ім'я і ім'я вчителів на титульному вікні / create a Label to display your name and teacher names on the title window
    teachers_names_l = ctk.CTkLabel(
        master = intrd_window, 
        width = 800, 
        height = 145, 
        text = "Виконала учениця 11-Г класу,\nКавуненко Юлія Сергіївна\nКерівники роботи –\nБоровик Людмила Іванівна,\nЯкименко Наталія Михайлівна"
        )
    # задаємо стилі для Label / set styles for the Label
    teachers_names_l.configure(
        fg_color = background, 
        font = ("Roboto Slab", 22), 
        text_color = text_color, 
        anchor = "e", 
        justify = "left"
        )
    # створюємо Label для відображення міста на титульному вікні / create a Label to display the city on the title window
    city_data_l = ctk.CTkLabel(
        master = intrd_window, 
        width = 101, 
        height = 52, 
        text = "м. Дніпро\n2024"
        )
    # задаємо стилі для Label / set styles for the Label
    city_data_l.configure(
        fg_color = background, 
        font = ("Roboto Slab", 20), 
        text_color = text_color, 
        anchor = "e"
        )
    # розташовуємо на титульному додатку усі елементи / place all elements on the title application
    school_name_l.place(x = 75, y = 74)
    proj_title_l.place(x = 75, y = 273)
    teachers_names_l.place(x = 75, y = 421)
    city_data_l.place(x = 425, y = 582)

    # створюємо функцію для запуску основного додатку / create a function to start the main application
    def open_main_window(event):
        run_main()
    # встановлюємо, що запуск відбувається по двійному кліку на титульний додаток / set the start to occur on a double-click on the title application
    intrd_window.bind("<Double-Button-1>", open_main_window)
    # запуск титульного додатку / run the title application
    intrd_window.mainloop()
