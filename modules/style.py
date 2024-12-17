'''
Файл для задання стилю елементам / File for styling elements
'''
# імпортуємо усі елементи customtkinter для задання стилю їм / importing all customtkinter elements for styling
from .main_elements import *
# імпортуємо усі функції для побудови графіків і похідних для прив'язки їх до кнопок або чекбоксів / importing all functions for building graphs and derivatives to bind them to buttons or checkboxes
from .elements_functions import build_graphic, build_graphic_1, clean_button, check_second_dev, check_first_dev, build_drob_graphic, build_third_func, build_fourth_func, drob_first_dev, drob_second_dev, third_first_dev, third_second_dev, fourth_first_dev, fourth_second_dev
# імпортуємо функцію для роботи з вікном вибору функцій / importing function for working with the function selection window
from .window_with_fun import functions_window

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

# задаємо стиль для кнопки побудови базових або введенних графіків / setting the style for the button to build basic or custom graphs
button_get.configure(
    bg_color = frame_background, # фонова кольорова кнопка / button background color
    text='✎', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Roboto Slab", 15), # шрифт тексту кнопки / button text font
    command = build_graphic # команда для виконання при натисканні кнопки / command to execute on button press
)
# задаємо стиль для головного вікна / setting the style for the main window
main.configure(
    fg_color= background # фоновий колір головного вікна / main window background color
)
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
# задаємо стиль для фрейму з базовими функціями / setting the style for the frame with basic functions
frame_menu.configure(
    fg_color= input_border_color, # колір рамки фрейму / frame border color
    bg_color=frame_background, # фоновий колір фрейму / frame background color
    scrollbar_button_color="#B58B61", # колір кнопки прокрутки / scrollbar button color
    scrollbar_button_hover_color = '#A8825B', # колір кнопки прокрутки при наведенні / scrollbar button hover color
    corner_radius = 10 # радіус кутів фрейму / frame corner radius
)
# задаємо стиль для нашого холста / setting the style for our canvas
canvas.get_tk_widget().configure(bg=text_color) # колір фону холста / canvas background color

# для першої функції y = ax**3 + bx**2 + cx + d / for the first function y = ax**3 + bx**2 + cx + d
# задаємо стиль для лейблу визначення "у =" функції / setting the style for the label defining "y =" of the function
label_y.configure(
    bg_color = frame_background, # фоновий колір лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Roboto Slab", 15) # шрифт тексту лейблу / label text font
)
# задаємо стилі для інпутів коєфіцієнтів першої функції / setting the styles for the coefficient inputs of the first function
y_1.configure(
    bg_color = frame_background, # фоновий колір лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    anchor = "w" # прив'язка тексту лейблу / label text anchor
)
y_2.configure(
    bg_color = frame_background, # фоновий колір лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    anchor = "w" # прив'язка тексту лейблу / label text anchor
)
y_3.configure(
    bg_color = frame_background, # фоновий колір лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    anchor = "w" # прив'язка тексту лейблу / label text anchor
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
# задаємо стиль для кнопки побудови і дослідження першого графіку / setting the style for the button to build and research the first graph
get_grachic_1.configure(
    bg_color = frame_background, # фоновий колір кнопки / button background color
    text='✎', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Arrial", 15), # шрифт тексту кнопки / button text font
    command = build_graphic_1, # команда для виконання при натисканні кнопки / command to execute on button press
)
# задаємо стиль для кнопки очищення ДСК / setting the style for the button to clear the system
clean_graphic.configure(
    text='очистити', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font = ("Roboto Slab", 15), # шрифт тексту кнопки / button text font
    bg_color = 'white', # фоновий колір кнопки / button background color
    command = clean_button # команда для виконання при натисканні кнопки / command to execute on button press
)
# задаємо стиль для лейблу похідної y' / setting the style for the derivative y' label
first_dev.configure(
    bg_color = frame_background, # фоновий колір лейблу / label background color
    text = "Відображення похідної y'", # текст на лейблі / label text
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки лейблу / label border width
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    border_color = input_border_color, # колір рамки лейблу / label border color
    command = check_first_dev, # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
    checkmark_color = text_color # колір галочки / checkmark color
)
# задаємо стиль для лейблу похідної y'' / setting the style for the derivative y'' label
second_dev.configure(
    bg_color = frame_background, # фоновий колір лейблу / label background color
    text = "Відображення похідної y''", # текст на лейблі / label text
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки лейблу / label border width
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    border_color = input_border_color, # колір рамки лейблу / label border color
    command = check_second_dev, # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
    checkmark_color = text_color # колір галочки / checkmark color
)
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
# задаємо стиль для лейблу підпису фрейма з дослідженнями / setting the style for the frame title label with research
l_exploration.configure(
    text = 'Дослідження графіку', # текст на лейблі / label text
    font = ("Roboto Slab", 20), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background # колір фону лейблу / label foreground color
)
# задаємо стиль для лейблу з відображенням проміжків спадання і зростання функції / setting the style for the label displaying intervals of decrease and increase of the function
interval_label.configure(
    text = '3) Проміжок спадання і зростання функції', # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір фону лейблу / label foreground color
    anchor = 'w' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль для лейблу з відображенням області визначення функції / setting the style for the label displaying the domain of the function
scope_label.configure(
    text = '1) Область визначення функції', # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір фону лейблу / label foreground color
    anchor = 'w' # прив'язка тексту лейблу / label text anchor
)
# для другої функції у = (x**2 - a)/(x - b) / for the second function y = (x**2 - a)/(x - b)
# задаємо стиль для лейблу відображення чисельника другої функції / setting the style for the label displaying the numerator of the second function
drob_y_ch.configure(
    bg_color = frame_background, # колір фону лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Roboto Slab", 16) # шрифт тексту лейблу / label text font
)
# задаємо стиль для лейблу відображення знаменника другої функції / setting the style for the label displaying the denominator of the second function
drob_y_zn.configure(
    bg_color = frame_background, # колір фону лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Roboto Slab", 16) # шрифт тексту лейблу / label text font
)
# задаємо стиль для лейблу дробового знаку другої функції / setting the style for the label displaying the fraction sign of the second function
drob.configure(
    bg_color = frame_background, # колір фону лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Arial", 10) # шрифт тексту лейблу / label text font
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
# задаємо стиль для кнопки побудови і дослідження другої функції / setting the style for the button to build and research the second function
get_drob_grachic.configure(
    bg_color = frame_background, # колір фону кнопки / button background color
    text='✎', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Arrial", 15), # шрифт тексту кнопки / button text font
    command = build_drob_graphic # команда для виконання при натисканні кнопки / command to execute on button press
)
# задаємо стиль для лейблу з похідною y' другої функції / setting the style for the label with the derivative y' of the second function
drob_first_dev_lable.configure(
    bg_color = frame_background, # колір фону лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text = "y' = очікування введення даних", # текст на лейблі / label text
    anchor = 'w', # прив'язка тексту лейблу / label text anchor
    wraplength = 327 # задаємо максимальну ширину тексту до переносу / setting the maximum text width before wrapping
)
# задаємо стиль для відображення лейбу локального макс. і мін. / setting the style for the label displaying local max. and min.
local_max_min_label.configure(
    text = '4) Локальний макс. і мін. функції', # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'w' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль для відображення лейблу мін. і макс. значення функції / setting the style for the label displaying the min. and max. value of the function
zn_function_label.configure(
    text = '5) Мін. і макс. значення функції', # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'w' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль для лейблу відображення похідної y'' / setting the style for the label displaying the derivative y''
drob_second_dev_lable.configure(
    bg_color = frame_background, # колір фону лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Roboto Slab", 16), # шрифт тексту лейблу / label text font
    text = "y'' = очікування введення даних", # текст на лейблі / label text
    anchor = 'w', # прив'язка тексту лейблу / label text anchor
    wraplength = 327 # задаємо максимальну ширину тексту до переносу / setting the maximum text width before wrapping
)
# задаємо стиль для лейблу відображення точок перетину 0х, 0у / setting the style for the label displaying the intersection points 0x, 0y
points_ox_oy_label.configure(
    bg_color = frame_background, # колір фону лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Roboto Slab", 16), # шрифт тексту лейблу / label text font
    text = "6) Точки перетину з осями ох і оу", # текст на лейблі / label text
    anchor = 'w' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль для лейблу відображення нулів функції / setting the style for the label displaying the zeros of the function
points_zero_label.configure(
    bg_color = frame_background, # колір фону лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Roboto Slab", 16), # шрифт тексту лейблу / label text font
    text = "7) Нулі функції", # текст на лейблі / label text
    anchor = 'w' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль для лейблу відображення парності функції / setting the style for the label displaying the evenness of the function
even_or_odd_func_l.configure(
    bg_color = frame_background, # колір фону лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Roboto Slab", 16), # шрифт тексту лейблу / label text font
    text = "2) Парна чи непарна ф-ція", # текст на лейблі / label text
    anchor = 'w' # прив'язка тексту лейблу / label text anchor    
)
# задаємо стиль для лейблу відображення проміжків знакосталості функції / setting the style for the label displaying the intervals of constancy of the function
intervals_identity_l.configure(
    bg_color = frame_background, # колір фону лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Roboto Slab", 16), # шрифт тексту лейблу / label text font
    text = "8) Проміжки знакосталості ф-ції", # текст на лейблі / label text
    anchor = 'w' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль для елементів третьої функції y = (x**2 - a**2)/x / setting the style for the elements of the third function y = (x**2 - a**2)/x
# задаємо стиль для лейблу "у =" / setting the style for the label "y ="
third_func_l.configure(
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль для відображення чисельника функції / setting the style for the label displaying the numerator of the function
third_func_up_label.configure(
    text = 'x² -          ²', # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль для відображення знаменника функції / setting the style for the label displaying the denominator of the function
third_func_down_label.configure(
    text = 'x', # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль для відображення дробового знаку функції / setting the style for the label displaying the fraction sign of the function
third_func_drob_label.configure(
    bg_color = frame_background, # колір фону лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Normal", 12), # шрифт тексту лейблу / label text font
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль для відображення похідної y' функції / setting the style for the label displaying the derivative y' of the function
third_f_dev_label.configure(
    text = "y' = очікування введення даних", # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'w', # прив'язка тексту лейблу / label text anchor
    wraplength = 327 # задаємо максимальну ширину тексту до переносу / set the maximum width of the text before the transition
)
# задаємо стиль для відображення похідної y'' функції / setting the style for the label displaying the derivative y'' of the function
third_s_dev_label.configure(
    text = "y'' = очікування введення даних", # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'w', # прив'язка тексту лейблу / label text anchor
    wraplength = 327 # задаємо максимальну ширину тексту до переносу / setting the maximum text width before wrapping
)
# задаємо стиль для кнопки побудови і дослідження графіку функції / setting the style for the button to build and research the function graph
third_func_button.configure(
    bg_color = frame_background, # колір фону кнопки / button background color
    text='✎', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Arrial", 15), # шрифт тексту кнопки / button text font
    command = build_third_func # команда для виконання при натисканні кнопки / command to execute on button press
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

# лейблу для відображення кольорів графіку / setting the style for the labels displaying the graph colors
# для базових або введенних користувачем функцій - фіолетовий / for basic or user-defined functions - purple
purple_gr.configure(
    text_color = 'purple', # колір тексту лейблу / label text color
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    bg_color = frame_background # колір фону лейблу / label background color
)
# для основної функції з вибору функцій - червоний / for the main function from the function selection - red
red_gr.configure(
    text_color = 'red', # колір тексту лейблу / label text color
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    bg_color = frame_background # колір фону лейблу / label background color
)
# для похідної y' основної функції - зелений / for the main function's y' derivative - green
green_gr.configure(
    text_color = 'green', # колір тексту лейблу / label text color
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    bg_color = frame_background # колір фону лейблу / label background color
)
# для похідної y'' основної функції - синя / for the main function's y'' derivative - blue
blue_gr.configure(
    text_color = 'blue', # колір тексту лейблу / label text color
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    bg_color = frame_background # колір фону лейблу / label background color
)
# задаємо стиль для лейблу відображення чи обраний користувачем графік функції / setting the style for the label displaying whether the user-selected function graph is chosen
func_t_or_f.configure(
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Roboto Slab", 20), # шрифт тексту лейблу / label text font
    bg_color = frame_background # колір фону лейблу / label background color
)
# задаємо стиль для "у =" другого графіку у = (x**2 - a)/(x - b) / setting the style for "y =" of the second graph y = (x**2 - a)/(x - b)
drob_y.configure(
    anchor = "center", # прив'язка тексту лейблу / label text anchor
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background # колір переднього плану лейблу / label foreground color
)
# задаємо стиль для кнопки відкриття вікна для обирання графіку функцій / setting the style for the button to open the window for selecting function graphs
choose_gr.configure(
    text_color = text_button_color, # колір тексту кнопки / button text color
    font = ("Roboto Slab", 15), # шрифт тексту кнопки / button text font
    bg_color = frame_background, # колір фону кнопки / button background color
    fg_color = button_color, # колір переднього плану кнопки / button foreground color
    corner_radius = 10, # радіус кутів кнопки / button corner radius
    anchor = "center", # прив'язка тексту кнопки / button text anchor
    text = "Обрати функцію", # текст на кнопці / button text
    hover_color = button_hover_color, # колір кнопки при наведенні / button hover color
    command = functions_window # команда для виконання при натисканні кнопки / command to execute on button press
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
# задаємо стиль лейблу "у = " четвертої функції / setting the style for the label "y =" of the fourth function
fourth_func_l.configure(
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль лейблу відображення чисельнику четвертої функції / setting the style for the label displaying the numerator of the fourth function
fourth_func_up_label.configure(
    text = 'x', # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль лейблу відображення знаменнику четвертої функції / setting the style for the label displaying the denominator of the fourth function
fourth_func_down_label.configure(
    text = 'x² +          ', # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль лейблу дробового знаку четвертої функції / setting the style for the label displaying the fraction sign of the fourth function
fourth_func_drob_label.configure(
    bg_color = frame_background, # колір фону лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Normal", 12), # шрифт тексту лейблу / label text font
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль лейблу похідної y' четвертої функції / setting the style for the label displaying the derivative y' of the fourth function
fourth_f_dev_label.configure(
    text = "y' = очікування введення даних", # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'w', # прив'язка тексту лейблу / label text anchor
    wraplength = 327 # задаємо максимальну ширину тексту до переносу / setting the maximum text width before wrapping
)
# задаємо стиль лейблу похідної y'' четвертої функції / setting the style for the label displaying the derivative y'' of the fourth function
fourth_s_dev_label.configure(
    text = "y'' = очікування введення даних", # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'w', # прив'язка тексту лейблу / label text anchor
    wraplength = 327 # задаємо максимальну ширину тексту до переносу / setting the maximum text width before wrapping
)
# задаємо стиль для кнопки побудови і дослідження четвертої функції / setting the style for the button to build and research the fourth function
fourth_func_button.configure(
    bg_color = frame_background, # колір фону кнопки / button background color
    text='✎', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Arrial", 15), # шрифт тексту кнопки / button text font
    command = build_fourth_func # команда для виконання при натисканні кнопки / command to execute on button press
)
# задаємо стиль для чекбоксу похідної у' четвертої функції / setting the style for the checkbox displaying the derivative y' of the fourth function
first_dev_fourth.configure(
    bg_color = frame_background, # колір фону чекбоксу / checkbox background color
    text = "Відображення похідної y'", # текст на чекбоксі / checkbox text
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
    text = "Відображення похідної y''", # текст на чекбоксі / checkbox text
    font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
    text_color = text_color, # колір тексту чекбоксу / checkbox text color
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки чекбоксу / checkbox border width
    border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
    command = fourth_second_dev, # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
    checkmark_color = text_color # колір галочки / checkmark color
)
# задаємо стиль для лейблу відображення точок перегину функції / setting the style for the label displaying the inflection points of the function
inflection_points_label.configure(
    text = '9) Точки перегину', # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'w' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль для лейблу відображення проміжків опуклості функції / setting the style for the label displaying the intervals of convexity of the function
convexity_intervals_label.configure(
    text = '10) Проміжки опуклості', # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'w' # прив'язка тексту лейблу / label text anchor
)
# задаємо стиль для лейблу відображення похилої асимптоти функції / setting the style for the label displaying the oblique asymptote of the function
slope_asymptote.configure(
    text = '11) Похила асимптота', # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'w' # прив'язка тексту лейблу / label text anchor
)
# задаємо стилі для чекбоксів для похідних кожної функції / setting the styles for the checkboxes for the derivatives of each function
# похідна y' функції y = (x**2 - a**2)/x / derivative y' of the function y = (x**2 - a**2)/x
first_dev_fdrob.configure(
    bg_color = frame_background, # колір фону чекбоксу / checkbox background color
    text = "Відображення похідної y'", # текст на чекбоксі / checkbox text
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
    text = "Відображення похідної y'", # текст на чекбоксі / checkbox text
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
    text = "Відображення похідної y''", # текст на чекбоксі / checkbox text
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
    text = "Відображення похідної y''", # текст на чекбоксі / checkbox text
    fg_color = input_color, # колір фону інпуту / input background color
    hover_color=checkbox_hover_color, # колір чекбоксу при наведенні / checkbox hover color
    border_width = 2, # ширина рамки чекбоксу / checkbox border width
    border_color = input_border_color, # колір рамки чекбоксу / checkbox border color
    checkmark_color = text_color, # колір галочки / checkmark color
    command = drob_second_dev, # команда для виконання при натисканні чекбоксу / command to execute on checkbox press
    font = ("Roboto Slab", 15), # шрифт тексту чекбоксу / checkbox text font
    text_color = text_color # колір тексту чекбоксу / checkbox text color
)
# стиль для лейблу який зазначає якого кольору основний графік функції / setting the style for the label indicating the color of the main function graph
main_graphic_label.configure(
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'w', # прив'язка тексту лейблу / label text anchor
    text = 'Головний графік' # текст на лейблі / label text
)