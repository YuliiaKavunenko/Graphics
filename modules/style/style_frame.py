import customtkinter as ctk
from ..main_elements import *

# кольори для елементів у вікні  / colors for elements in the window
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

# задаємо стиль для фрейму з даними про функцію на головному вікні / setting the style for the frame with function data on the main window
frame_first.configure(
    fg_color = frame_background, # колір фону фрейму / frame background color
    corner_radius = 10 # радіус кутів фрейму / frame corner radius
)
# задаємо стиль для фрейму з чекбоксами графіку на головному вікні / setting the style for the frame with graph checkboxes on the main window
frame_for_options.configure(
    fg_color = frame_background, # колір фону фрейму / frame background color
    corner_radius = 10 # радіус кутів фрейму / frame corner radius
)
# задаємо стиль для фрейму з дослідженнями графіку на головному вікні / setting the style for the frame with graph research on the main window
frame_exploration.configure(
    fg_color = frame_background, # колір фону фрейму / frame background color
    corner_radius = 10 # радіус кутів фрейму / frame corner radius
)