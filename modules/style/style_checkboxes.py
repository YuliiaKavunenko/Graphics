import customtkinter as ctk
from ..main_elements import *
from ..plotting import *

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

# задаємо стиль для checkbox похідної y' / setting the style for the derivative y' label
first_dev.configure(
    bg_color = frame_background, # фоновий колір лейблу / label background color
    text = "Графік першої похідної y'", # текст на лейблі / label text
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки лейблу / label border width
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    border_color = input_border_color, # колір рамки лейблу / label border color
    command = check_first_dev, # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
    checkmark_color = text_color # колір галочки / checkmark color
)
# задаємо стиль для checkbox похідної y'' / setting the style for the derivative y'' label
second_dev.configure(
    bg_color = frame_background, # фоновий колір лейблу / label background color
    text = "Графік другої похідної y''", # текст на лейблі / label text
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки лейблу / label border width
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    border_color = input_border_color, # колір рамки лейблу / label border color
    command = check_second_dev, # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
    checkmark_color = text_color # колір галочки / checkmark color
)
# задаємо стиль для чекбоксу похідної у' четвертої функції / setting the style for the checkbox displaying the derivative y' of the fourth function
first_dev_fourth.configure(
    bg_color = frame_background, # колір фону чекбоксу / checkbox background color
    text = "Графік першої похідної y'", # текст на чекбоксі / checkbox text
    font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
    text_color = text_color, # колір тексту чекбоксу / checkbox text color
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки чекбоксу / checkbox border width
    border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
    command = fourth_first_dev, # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
    checkmark_color = text_color # колір галочки / checkmark color
)
# задаємо стиль для чекбоксу похідної у'' четвертої функції / setting the style for the checkbox displaying the derivative y'' of the fourth function
second_dev_fourth.configure(
    bg_color = frame_background, # колір фону чекбоксу / checkbox background color
    text = "Графік другої похідної y''", # текст на чекбоксі / checkbox text
    font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
    text_color = text_color, # колір тексту чекбоксу / checkbox text color
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки чекбоксу / checkbox border width
    border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
    command = fourth_second_dev, # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
    checkmark_color = text_color # колір галочки / checkmark color
)
# задаємо стилі для чекбоксів для похідних кожної функції / setting the styles for the checkboxes for the derivatives of each function
# похідна y' функції y = (x**2 - a**2)/x / derivative y' of the function y = (x**2 - a**2)/x
first_dev_fdrob.configure(
    bg_color = frame_background, # колір фону чекбоксу / checkbox background color
    text = "Графік першої похідної y'", # текст на чекбоксі / checkbox text
    fg_color = input_color, # колір фону інпуту / input background color
    font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
    text_color = text_color, # колір тексту чекбоксу / checkbox text color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки чекбоксу / checkbox border width
    border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
    checkmark_color = text_color, # колір галочки / checkmark color
    command = drob_first_dev # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
)
# похідна y'' функції y = (x**2 - a**2)/x / derivative y'' of the function y = (x**2 - a**2)/x
first_dev_sdrob.configure(
    bg_color = frame_background, # колір фону чекбоксу / checkbox background color
    text = "Графік першої похідної y'", # текст на чекбоксі / checkbox text
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
    text_color = text_color, # колір тексту чекбоксу / checkbox text color
    border_width = 2, # ширина рамки чекбоксу / checkbox border width
    border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
    checkmark_color = text_color, # колір галочки / checkmark color
    command = third_first_dev # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
)
# похідна y' функції y = x/(x**2 + a) / derivative y' of the function y = x/(x**2 + a)
second_dev_sdrob.configure(
    bg_color = frame_background, # колір фону чекбоксу / checkbox background color
    text = "Графік другої похідної y''", # текст на чекбоксі / checkbox text
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки чекбоксу / checkbox border width
    font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
    text_color = text_color, # колір тексту чекбоксу / checkbox text color
    border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
    checkmark_color = text_color, # колір галочки / checkmark color
    command = third_second_dev # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
)
# похідна y'' функції y = x/(x**2 + a) / derivative y'' of the function y = x/(x**2 + a)
second_dev_fdrob.configure(
    bg_color = frame_background, # колір фону чекбоксу / checkbox background color
    text = "Графік другої похідної y''", # текст на чекбоксі / checkbox text
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки чекбоксу / checkbox border width
    border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
    checkmark_color = text_color, # колір галочки / checkmark color
    command = drob_second_dev, # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
    font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
    text_color = text_color # колір тексту чекбоксу / checkbox text color
)
# похідна y' функції y = (x**2 - a)/(x - b) / derivative y'' of the function y = (x**2 - a)/(x - b)
first_dev_fifth.configure(
    bg_color = frame_background, # колір фону чекбоксу / checkbox background color
    text = "Графік першої похідної y'", # текст на чекбоксі / checkbox text
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки чекбоксу / checkbox border width
    font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
    text_color = text_color, # колір тексту чекбоксу / checkbox text color
    border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
    checkmark_color = text_color, # колір галочки / checkmark color
    command = fifth_first_dev # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
)
# похідна y'' функції y = (x**2 - a)/(x - b) / derivative y'' of the function y = (x**2 - a)/(x - b)
second_dev_fifth.configure(
    bg_color = frame_background, # колір фону чекбоксу / checkbox background color
    text = "Графік другої похідної y''", # текст на чекбоксі / checkbox text
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки чекбоксу / checkbox border width
    font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
    text_color = text_color, # колір тексту чекбоксу / checkbox text color
    border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
    checkmark_color = text_color, # колір галочки / checkmark color
    command = fifth_second_dev # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
)
# похідна y' функції y = a/x**2 + x/a / derivative y' of the function y = (x**2 - a)/(x - b)
first_dev_sixth.configure(
    bg_color = frame_background, # колір фону чекбоксу / checkbox background color
    text = "Графік першої похідної y'", # текст на чекбоксі / checkbox text
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки чекбоксу / checkbox border width
    font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
    text_color = text_color, # колір тексту чекбоксу / checkbox text color
    border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
    checkmark_color = text_color, # колір галочки / checkmark color
    command = sixth_first_dev # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
)
# похідна y'' функції y = a/x**2 + x/a / derivative y'' of the function y = (x**2 - a)/(x - b)
second_dev_sixth.configure(
    bg_color = frame_background, # колір фону чекбоксу / checkbox background color
    text = "Графік другої похідної y''", # текст на чекбоксі / checkbox text
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки чекбоксу / checkbox border width
    font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
    text_color = text_color, # колір тексту чекбоксу / checkbox text color
    border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
    checkmark_color = text_color, # колір галочки / checkmark color
    command = sixth_second_dev # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
)
# похідна y' функції y = (x**2 + x + a)/x / derivative y' of the function y = (x**2 - a)/(x - b)
first_dev_seventh.configure(
    bg_color = frame_background, # колір фону чекбоксу / checkbox background color
    text = "Графік першої похідної y'", # текст на чекбоксі / checkbox text
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки чекбоксу / checkbox border width
    font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
    text_color = text_color, # колір тексту чекбоксу / checkbox text color
    border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
    checkmark_color = text_color, # колір галочки / checkmark color
    command = seventh_first_dev # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
)
# похідна y'' функції y = (x**2 + x + a)/x / derivative y'' of the function y = (x**2 - a)/(x - b)
second_dev_seventh.configure(
    bg_color = frame_background, # колір фону чекбоксу / checkbox background color
    text = "Графік другої похідної y''", # текст на чекбоксі / checkbox text
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки чекбоксу / checkbox border width
    font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
    text_color = text_color, # колір тексту чекбоксу / checkbox text color
    border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
    checkmark_color = text_color, # колір галочки / checkmark color
    command = seventh_second_dev # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
)
# # чекбокси базових функцій
# base_dev_checkbox1.configure(
#     bg_color = frame_background, # колір фону чекбоксу / checkbox background color
#     text = "Графік першої похідної y'", # текст на чекбоксі / checkbox text
#     fg_color = input_color, # колір фону інпуту / input background color
#     hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
#     border_width = 2, # ширина рамки чекбоксу / checkbox border width
#     font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
#     text_color = text_color, # колір тексту чекбоксу / checkbox text color
#     border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
#     checkmark_color = text_color, # колір галочки / checkmark color
#     command = base_first_dev # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
# )
# base_dev_checkbox2.configure(
#     bg_color = frame_background, # колір фону чекбоксу / checkbox background color
#     text = "Графік другої похідної y''", # текст на чекбоксі / checkbox text
#     fg_color = input_color, # колір фону інпуту / input background color
#     hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
#     border_width = 2, # ширина рамки чекбоксу / checkbox border width
#     font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
#     text_color = text_color, # колір тексту чекбоксу / checkbox text color
#     border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
#     checkmark_color = text_color, # колір галочки / checkmark color
#     command = base_second_dev # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
# )