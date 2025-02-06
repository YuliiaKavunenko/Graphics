import customtkinter as ctk
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

# задаємо стиль для фрейму з базовими функціями / setting the style for the frame with basic functions
frame_menu.configure(
    fg_color= input_border_color, # колір рамки фрейму / frame border color
    bg_color=frame_background, # фоновий колір фрейму / frame background color
    scrollbar_button_color="#B58B61", # колір кнопки прокрутки / scrollbar button color
    scrollbar_button_hover_color = '#A8825B', # колір кнопки прокрутки при наведенні / scrollbar button hover color
    corner_radius = 10 # радіус кутів фрейму / frame corner radius
)