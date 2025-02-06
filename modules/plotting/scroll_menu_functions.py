from ..main_elements import *
# кольори для елементів у вікні  / colors for elements in the window
# колір для фону вікна / color for window background
background = "#CC9C87"
# колір для фону фреймів / color for frame background
frame_background = "#E2B09A"
# колір для тексту label / color for label text
text_color = "#392D20"
# колір для фону кнопки / color for button background
button_color = "#6F4E40"
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
button_hover_color = "#4D362C"
# колір при наведенні на checkbox / color when hovering over the checkbox
checkbox_hover_color = "#EBCDAE"
# Функція для кнопок меню базових функцій, при натисканні обирається базовий графік функції у input / Function for menu buttons of basic functions, selecting a basic graph of the function in input on click
def frame_buttons_func(funct): 
    input_graphic.insert(0,f"{funct}")  # Вставка функції у поле введення / Inserting the function into the input field
    frame_menu.place_forget()  # Приховування меню після вибору функції / Hiding the menu after selecting the function
# функція для зникнення меню базових функцій / function to hide the menu of basic functions
def disappear_menu(event):
    frame_menu.place_forget()

# функція для відображення фрейму базових функцій для побудови / function to display the frame with basic functions for building
def appear_menu(event):
    # Очищення frame_menu від існуючих кнопок всередині / clearing frame_menu from existing buttons inside
    for button in frame_menu.winfo_children(): # winfo_children to get all child widgets of frame_menu
        button.destroy()
    frame_menu.place(x = 743, y = 59)
    # Фрейм поверх всіх елементів вікна / frame above all window elements
    frame_menu.lift()
    # input_graphic.lift(frame_menu)
    # список наших базових функцій / a list of our core features
    el_functions = [
                    'x', '1/x', 'x**2', 'x**3', 
                    'x**-2', 'x**-3'
                    ]
    # створення кнопок для вибору функцій / creation of buttons for selecting functions
    for func in el_functions:
        func_button = ctk.CTkButton(
            master=frame_menu,
            text=func,
            width=195, 
            height=40,
            anchor='w',
            fg_color=input_border_color,
            hover_color=hover_color_menu,
            text_color=text_color,
            font=("Roboto Slab", 15),
            command=lambda f=func: frame_buttons_func(f)  # Використання lambda для передачі тексту функції / using lambda to pass function text
        )
        func_button.pack(pady=2, anchor='w')