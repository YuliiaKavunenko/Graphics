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

# задаємо стиль для інпуту своїх або базових графіків функцій / setting the style for custom or basic function graph inputs
input_graphic.configure(
    bg_color = frame_background, # фоновий колір інпуту / input background color
    placeholder_text='Введіть функцію', # текст підказки / placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки / placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color= text_color, # колір тексту інпуту / input text color
    font=("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    corner_radius=10, # радіус кутів інпуту / input corner radius
    border_width=3, # ширина рамки інпуту / input border width
    border_color= input_border_color # колір рамки інпуту / input border color
)

a_1.configure(
    bg_color = frame_background, # фоновий колір інпуту / input background color
    placeholder_text= 'a', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
b_1.configure(
    bg_color = frame_background, # фоновий колір інпуту / input background color
    placeholder_text= 'b', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
c_1.configure(
    bg_color = frame_background, # фоновий колір інпуту / input background color
    placeholder_text= 'c', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
d_1.configure(
    bg_color = frame_background, # фоновий колір інпуту / input background color
    placeholder_text= 'd', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
a_2.configure(
    bg_color = frame_background, # фоновий колір інпуту / input background color
    placeholder_text= 'a', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
b_2.configure(
    bg_color = frame_background, # фоновий колір інпуту / input background color
    placeholder_text= 'b', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
c_2.configure(
    bg_color = frame_background, # фоновий колір інпуту / input background color
    placeholder_text= 'c', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
a_3.configure(
    bg_color = frame_background, # фоновий колір інпуту / input background color
    placeholder_text= 'a', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
b_3.configure(
    bg_color = frame_background, # фоновий колір інпуту / input background color
    placeholder_text= 'b', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
# задаємо стиль для інпутів введення коєфіцієнтів другої функції / setting the style for the inputs for entering the coefficients of the second function
a_drob_1.configure(
    bg_color = frame_background, # колір фону інпуту / input background color
    placeholder_text= 'a', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
a_drob_3.configure(
    bg_color = frame_background, # колір фону інпуту / input background color
    placeholder_text= 'b', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
# задаємо стиль для інпуту введення коєфіцієнту "а" функції / setting the style for the input to enter the coefficient "a" of the function
a_th_drob.configure(
    bg_color = frame_background, # колір фону інпуту / input background color
    placeholder_text= 'a', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
# задаємо стиль для елементів четвертої функції y = x/(x**2 + a) / setting the style for the elements of the fourth function y = x/(x**2 + a)
# задаємо стиль інпуту для коєфіцієнту "а" четвертої функції / setting the style for the input to enter the coefficient "a" of the fourth function
a4_drob.configure(
    bg_color = frame_background, # колір фону інпуту / input background color
    placeholder_text= 'a', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
# задаємо стиль для елементів п'ятої функції y = (x**2 + a)/(x**2 - a) / setting the style for the elements of the fifth function y = (x**2 + a)/(x**2 - a)
# задаємо стиль інпуту для коєфіцієнту "a" чисельника п'ятої функції / setting the style for the input to enter the coefficient "a" of the fifth function
a1_function5.configure(
    bg_color = frame_background, # колір фону інпуту / input background color
    placeholder_text= 'a', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
# задаємо стиль для інпуту введення коєфіцієнту "a" знаменника функції / setting the style for the input to enter the coefficient "a" of the function
a2_function5.configure(
    bg_color = frame_background, # колір фону інпуту / input background color
    placeholder_text= 'a', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
# задаємо стиль для інпуту введення коєфіцієнту 1 "a" знаменника функції / setting the style for the input to enter the coefficient "a" of the function
a1_sixth.configure(
    bg_color = frame_background, # колір фону інпуту / input background color
    placeholder_text= 'a', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)
# задаємо стиль для інпуту введення коєфіцієнту 2 "a" знаменника функції / setting the style for the input to enter the coefficient "a" of the function
a2_sixth.configure(
    bg_color = frame_background, # колір фону інпуту / input background color
    placeholder_text= 'a', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)

a1_seventh.configure(
    bg_color = frame_background, # колір фону інпуту / input background color
    placeholder_text= 'a', # текст підказки для інпуту / input placeholder text
    placeholder_text_color = input_textholder_color, # колір тексту підказки для інпуту / input placeholder text color
    fg_color = input_color, # колір інпуту / input color
    text_color = text_color, # колір тексту інпуту / input text color
    font = ("Roboto Slab", 15), # шрифт тексту інпуту / input text font
    border_width = 3, # ширина рамки інпуту / input border width
    border_color = input_border_color # колір рамки інпуту / input border color
)