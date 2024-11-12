import customtkinter as ctk
import matplotlib.ticker as ticker
from .main_elements import *

background = "#A76E56"
frame_background = "#BA7D65"
text_color = "#392D20"
button_color = "#7B4C39"
text_button_color = "#F1D5BA"
input_color = "#FAF0E6"
input_border_color = "#EAD1B8"
input_textholder_color = "#CAA37D"
# hover_color_menu = "#F3E4D5"
button_hover_color = "#9D6249"
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

    def open_main_window(event):
        run_main()
        intrd_window.destroy()
    intrd_window.bind("<Double-Button-1>", open_main_window)

    intrd_window.mainloop()