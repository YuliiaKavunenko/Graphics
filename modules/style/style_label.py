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

# для першої функції y = ax**3 + bx**2 + cx + d / for the first function y = ax**3 + bx**2 + cx + d
# задаємо стиль для лейблу визначення "у =" функції / setting the style for the label defining "y =" of the function
label_y.configure(
    bg_color = frame_background, # фоновий колір лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Roboto Slab", 15) # шрифт тексту лейблу / label text font
)
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
# стиль для лейблу який зазначає якого кольору основний графік функції / setting the style for the label indicating the color of the main function graph
main_graphic_label.configure(
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'w', # прив'язка тексту лейблу / label text anchor
    text = 'Головний графік' # текст на лейблі / label text
)
# стиль для лейблу який зазначає "y = " для п'ятої функції y = (x**2 + a)/(x**2 - a) / setting the style for the label indicating "y = " for the fifth function y = (x**2 + a)/(x**2 - a)
fifth_func_l.configure(
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)
# стиль для лейблу відображення чисельника функції y = (x**2 + a)/(x**2 - a) / setting the style for the label displaying the numerator of the function y = (x**2 + a)/(x**2 - a)
fifth_func_up_label.configure(
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)
# стиль для лейблу відображення знаменника функції y = (x**2 + a)/(x**2 - a) / setting the style for the label displaying the denominator of the function y = (x**2 + a)/(x**2 - a)
fifth_func_down_label.configure(
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)
# стиль для лейблу дробового знаку функції y = (x**2 + a)/(x**2 - a) / setting the style for the label displaying the fraction sign of the function y = (x**2 + a)/(x**2 - a)
fifth_func_drob_label.configure(
    bg_color = frame_background, # колір фону лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Normal", 12), # шрифт тексту лейблу / label text font
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)
# стиль для лейблу відображення похідної y' функції y = (x**2 + a)/(x**2 - a) / setting the style for the label displaying the derivative y' of the function y = (x**2 + a)/(x**2 - a)
fifth_f_dev_label.configure(
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'w', # прив'язка тексту лейблу / label text anchor
    wraplength = 327 # задаємо максимальну ширину тексту до переносу / setting the maximum text width before wrapping
)
# стиль для лейблу відображення похідної y'' функції y = (x**2 + a)/(x**2 - a) / setting the style for the label displaying the derivative y'' of the function y = (x**2 + a)/(x**2 - a)
fifth_s_dev_label.configure(
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'w', # прив'язка тексту лейблу / label text anchor
    wraplength = 327 # задаємо максимальну ширину тексту до переносу / setting the maximum text width before wrapping
)

sixth_func_l.configure(
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)
sixth_first_func_up_label.configure(
    text = 'x', # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)
sixth_first_func_down_label.configure(
    text = 'x²', # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)
sixth_func_drob_label.configure(
    bg_color = frame_background, # колір фону лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Normal", 12), # шрифт тексту лейблу / label text font
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)


sixth_func_drob_label_2.configure(
    bg_color = frame_background, # колір фону лейблу / label background color
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Normal", 12), # шрифт тексту лейблу / label text font
    anchor = 'center' # прив'язка тексту лейблу / label text anchor
)

sixth_f_dev_label.configure(
    text = "y' = очікування введення даних", # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'w', # прив'язка тексту лейблу / label text anchor
    wraplength = 327 # задаємо максимальну ширину тексту до переносу / setting the maximum text width before wrapping
)
sixth_s_dev_label.configure(
    text = "y'' = очікування введення даних", # текст на лейблі / label text
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    text_color = text_color, # колір тексту лейблу / label text color
    bg_color = frame_background, # колір фону лейблу / label background color
    fg_color = frame_background, # колір переднього плану лейблу / label foreground color
    anchor = 'w', # прив'язка тексту лейблу / label text anchor
    wraplength = 327 # задаємо максимальну ширину тексту до переносу / setting the maximum text width before wrapping
)

sixth_func_plus.configure(
    text_color = text_color, # колір тексту лейблу / label text color
    font = ("Roboto Slab", 15), # шрифт тексту лейблу / label text font
    bg_color = frame_background # колір фону лейблу / label background color
)