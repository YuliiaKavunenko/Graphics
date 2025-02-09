import customtkinter as ctk
import os
from PIL import Image

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
# шлях до поточної директорії / path to the current directory
PATH = os.path.abspath(os.path.join(__file__, '..'))
image_name = 'error.png'
def show_error_window(error_message):
    from .plotting import clean_button
    error_window = ctk.CTkToplevel()
    error_window.title(" ")
    error_window.resizable(False, False)

    error_window.update_idletasks()
    screen_width = error_window.winfo_screenwidth()
    screen_height = error_window.winfo_screenheight()
    window_width = 350
    window_height = 150
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window_height // 2)
    error_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    error_window.grab_set()
    error_window.configure(fg_color = background)
    main_frame = ctk.CTkFrame(error_window)
    main_frame.configure(
        width = 340,
        height = 140,
        fg_color = frame_background,
        corner_radius = 10
    )
    main_frame.place(x = 5, y = 5)

    image_path = os.path.join(PATH,'..', "img/error.png")
    if image_path:
        image = ctk.CTkImage(
            light_image=Image.open(image_path),
            dark_image=Image.open(image_path),
            size=(51, 51)
        )
        image_label = ctk.CTkLabel(main_frame, image = image, text="")
        image_label.place(x = 15, y = 22)

    # Текст ошибки с выравниванием по правому краю
    label = ctk.CTkLabel(master = main_frame, width = 199, text = error_message, wraplength = 219, fg_color=frame_background, text_color=text_color, anchor="e", justify = 'left', font = ("Roboto Slab", 16))
    label.place(x = 76, y =22)

    # Кнопка закрытия окна
    close_button = ctk.CTkButton(master = main_frame, width = 94,height = 38, text="зрозуміло", command=error_window.destroy)
    close_button.configure(
        fg_color = button_color,
        corner_radius = 10,
        text_color = text_button_color,
        font = ("Roboto Slab", 14),
        hover_color = button_hover_color

    )
    close_button.place(x = 241, y = 97)
    clean_button()