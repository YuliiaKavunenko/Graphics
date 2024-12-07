'''
Файл для задання стилю елементам.
'''

from .main_elements import *
from .elements_functions import build_graphic, build_graphic_1, clean_button, check_second_dev, check_first_dev, build_drob_graphic, build_third_func, build_fourth_func, drob_first_dev, drob_second_dev, third_first_dev, third_second_dev, fourth_first_dev, fourth_second_dev
from .window_with_fun import functions_window

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


print('STYLE.PY')
# СТИЛЬ КНОПКИ
button_get.configure(
    bg_color = frame_background,
    text='✎',
    fg_color=button_color,
    text_color=text_button_color,
    hover_color=button_hover_color,
    font=("Roboto Slab", 15),
    command = build_graphic
)
# СТИЛЬ ГЛАВНОГО ОКНА
main.configure(
    fg_color= background
)
# СТИЛЬ ИНПУТА
input_graphic.configure(
    bg_color = frame_background,
    placeholder_text='Введіть функцію',
    placeholder_text_color = input_textholder_color,
    fg_color = input_color,
    text_color= text_color,
    font=("Roboto Slab", 15),
    corner_radius=10,
    border_width=3,
    border_color= input_border_color

)
# Scroll frame!
frame_menu.configure(
    fg_color= input_border_color,
    bg_color=frame_background,
    scrollbar_button_color="#B58B61",
    scrollbar_button_hover_color = '#A8825B',	
    corner_radius = 10
)
# style Холст
canvas.get_tk_widget().configure(bg=text_color)

label_y.configure(
    bg_color = frame_background,
    text_color = text_color,
    font = ("Roboto Slab", 15)
)

y_1.configure(
    bg_color = frame_background,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    anchor = "w"
)
y_2.configure(
    bg_color = frame_background,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    anchor = "w"
)
y_3.configure(
    bg_color = frame_background,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    anchor = "w"
)
a_1.configure(
    bg_color = frame_background,
    placeholder_text= 'a',
    placeholder_text_color = input_textholder_color,
    fg_color = input_color,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    border_width = 3,
    border_color = input_border_color
)

b_1.configure(
    bg_color = frame_background,
    placeholder_text= 'b',
    placeholder_text_color = input_textholder_color,
    fg_color = input_color,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    border_width = 3,
    border_color = input_border_color
)
c_1.configure(
    bg_color = frame_background,
    placeholder_text= 'c',
    placeholder_text_color = input_textholder_color,
    fg_color = input_color,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    border_width = 3,
    border_color = input_border_color
)
d_1.configure(
    bg_color = frame_background,
    placeholder_text= 'd',
    placeholder_text_color = input_textholder_color,
    fg_color = input_color,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    border_width = 3,
    border_color = input_border_color
)

a_2.configure(
    bg_color = frame_background,
    placeholder_text= 'a',
    placeholder_text_color = input_textholder_color,
    fg_color = input_color,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    border_width = 3,
    border_color = input_border_color
)

b_2.configure(
    bg_color = frame_background,
    placeholder_text= 'b',
    placeholder_text_color = input_textholder_color,
    fg_color = input_color,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    border_width = 3,
    border_color = input_border_color
)
c_2.configure(
    bg_color = frame_background,
    placeholder_text= 'c',
    placeholder_text_color = input_textholder_color,
    fg_color = input_color,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    border_width = 3,
    border_color = input_border_color
)

a_3.configure(
    bg_color = frame_background,
    placeholder_text= 'a',
    placeholder_text_color = input_textholder_color,
    fg_color = input_color,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    border_width = 3,
    border_color = input_border_color
)

b_3.configure(
    bg_color = frame_background,
    placeholder_text= 'b',
    placeholder_text_color = input_textholder_color,
    fg_color = input_color,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    border_width = 3,
    border_color = input_border_color
)

get_grachic_1.configure(
    bg_color = frame_background,
    text='✎',
    fg_color=button_color,
    text_color=text_button_color,
    hover_color=button_hover_color,
    font=("Arrial", 15),
    command = build_graphic_1,
)

clean_graphic.configure(
    text='очистити',
    fg_color=button_color,
    text_color=text_button_color,
    hover_color=button_hover_color,
    font = ("Roboto Slab", 15),
    bg_color = 'white',
    command = clean_button
)

first_dev.configure(
    bg_color = frame_background,
    text = "Відображення похідної y'",
    fg_color = input_color,
    # bg_color = 'green',
    hover_color=checkbox_hover_color,
    border_width = 2,
    font = ("Roboto Slab", 15),
    text_color = text_color,
    border_color = input_border_color,
    command = check_first_dev,
    # цвет галочки
    checkmark_color = text_color
)
second_dev.configure(
    bg_color = frame_background,
    text = "Відображення похідної y''",
    fg_color = input_color,
    hover_color=checkbox_hover_color,
    border_width = 2,
    font = ("Roboto Slab", 15),
    text_color = text_color,
    border_color = input_border_color,
    command = check_second_dev,
    checkmark_color = text_color
)

frame_first.configure(
    fg_color = frame_background,
    corner_radius = 10
)

frame_for_options.configure(
    fg_color = frame_background,
    corner_radius = 10
)

frame_exploration.configure(
    fg_color = frame_background,
    corner_radius = 10
)
l_exploration.configure(
    text = 'Дослідження графіку',
    font = ("Roboto Slab", 20),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background
)
interval_label.configure(
    text = '3) Проміжок спадання і зростання функції',
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'w'
)
scope_label.configure(
    text = '1) Область визначення функції',
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'w'
)
drob_y_ch.configure(
    bg_color = frame_background,
    text_color = text_color,
    font = ("Roboto Slab", 16)
)
drob_y_zn.configure(
    bg_color = frame_background,
    text_color = text_color,
    font = ("Roboto Slab", 16)
)
drob.configure(
    bg_color = frame_background,
    text_color = text_color,
    font = ("Arial", 10)
)

a_drob_1.configure(
    bg_color = frame_background,
    placeholder_text= 'a',
    placeholder_text_color = input_textholder_color,
    fg_color = input_color,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    border_width = 3,
    border_color = input_border_color
)
a_drob_3.configure(
    bg_color = frame_background,
    placeholder_text= 'b',
    placeholder_text_color = input_textholder_color,
    fg_color = input_color,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    border_width = 3,
    border_color = input_border_color
)
get_drob_grachic.configure(
    bg_color = frame_background,
    text='✎',
    fg_color=button_color,
    text_color=text_button_color,
    hover_color=button_hover_color,
    font=("Arrial", 15),
    command = build_drob_graphic
)
drob_first_dev_lable.configure(
    bg_color = frame_background,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    text = "y' = очікування введення даних",
    anchor = 'w',
    wraplength = 327 # задаємо максимальну ширину тексту до переносу
)
local_max_min_label.configure(
    text = '4) Локальний макс. і мін. функції',
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'w'
)
zn_function_label.configure(
    text = '5) Мін. і макс. значення функції',
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'w'
)
drob_second_dev_lable.configure(
    bg_color = frame_background,
    text_color = text_color,
    font = ("Roboto Slab", 16),
    text = "y'' = очікування введення даних",
    anchor = 'w',
    wraplength = 327 # задаємо максимальну ширину тексту до переносу
)
points_ox_oy_label.configure(
    bg_color = frame_background,
    text_color = text_color,
    font = ("Roboto Slab", 16),
    text = "6) Точки перетину з осями ох і оу",
    anchor = 'w'
)

points_zero_label.configure(
    bg_color = frame_background,
    text_color = text_color,
    font = ("Roboto Slab", 16),
    text = "7) Нулі функції",
    anchor = 'w'
)
even_or_odd_func_l.configure(
    bg_color = frame_background,
    text_color = text_color,
    font = ("Roboto Slab", 16),
    text = "2) Парна чи непарна ф-ція",
    anchor = 'w'    
)
intervals_identity_l.configure(
    bg_color = frame_background,
    text_color = text_color,
    font = ("Roboto Slab", 16),
    text = "8) Проміжки знакосталості ф-ції",
    anchor = 'w'
)

#СТИЛЬ ТРЕТЬОЇ ФУНКЦІЇ
third_func_l.configure(
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'center'
)
third_func_up_label.configure(
    text = 'x² -          ²',
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'center'
)
third_func_down_label.configure(
    text = 'x',
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'center'
)
third_func_drob_label.configure(
    bg_color = frame_background,
    text_color = text_color,
    font = ("Normal", 12),
    anchor = 'center'
)
third_f_dev_label.configure(
    text = "y' = очікування введення даних",
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'w',
    wraplength = 327 # задаємо максимальну ширину тексту до переносу
)
third_s_dev_label.configure(
    text = "y'' = очікування введення даних",
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'w',
    wraplength = 327 # задаємо максимальну ширину тексту до переносу
)
third_func_button.configure(
    bg_color = frame_background,
    text='✎',
    fg_color=button_color,
    text_color=text_button_color,
    hover_color=button_hover_color,
    font=("Arrial", 15),
    command = build_third_func
)

a_th_drob.configure(
    bg_color = frame_background,
    placeholder_text= 'a',
    placeholder_text_color = input_textholder_color,
    fg_color = input_color,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    border_width = 3,
    border_color = input_border_color
)

# ЛЕЙБЛІ КОЛЬОРУ ГРАФІКА
purple_gr.configure(
    text_color = 'purple',
    font = ("Roboto Slab", 15),
    bg_color = frame_background
)
red_gr.configure(
    text_color = 'red',
    font = ("Roboto Slab", 15),
    bg_color = frame_background
)
green_gr.configure(
    text_color = 'green',
    font = ("Roboto Slab", 15),
    bg_color = frame_background
)
blue_gr.configure(
    text_color = 'blue',
    font = ("Roboto Slab", 15),
    bg_color = frame_background
)
# ЛЕЙБЛ Є ГРАФІК ЧИ НЄ
func_t_or_f.configure(
    text_color = text_color,
    font = ("Roboto Slab", 20),
    bg_color = frame_background
)
drob_y.configure(
    anchor = "center",
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background
)
# КНОПКА ДЛЯ ОТКРІТІЯ НОВОГО ОКОШИЧКА
choose_gr.configure(
    text_color = text_button_color,
    font = ("Roboto Slab", 15),
    bg_color = frame_background,
    fg_color = button_color,
    corner_radius = 10,
    anchor = "center",
    text = "Обрати функцію",
    hover_color = button_hover_color,
    command = functions_window
)

# ЧЕТВЕРТА ФУНКЦІЯ!!!!!!!!!!!!!!!!!!!!!!!

a4_drob.configure(
    bg_color = frame_background,
    placeholder_text= 'a',
    placeholder_text_color = input_textholder_color,
    fg_color = input_color,
    text_color = text_color,
    font = ("Roboto Slab", 15),
    border_width = 3,
    border_color = input_border_color
)

fourth_func_l.configure(
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'center'
)
fourth_func_up_label.configure(
    text = 'x',
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'center'
)
fourth_func_down_label.configure(
    text = 'x² +          ',
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'center'
)
fourth_func_drob_label.configure(
    bg_color = frame_background,
    text_color = text_color,
    font = ("Normal", 12),
    anchor = 'center'
)
fourth_f_dev_label.configure(
    text = "y' = очікування введення даних",
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'w',
    wraplength = 327 # задаємо максимальну ширину тексту до переносу
)
fourth_s_dev_label.configure(
    text = "y'' = очікування введення даних",
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'w',
    wraplength = 327 # задаємо максимальну ширину тексту до переносу
)

fourth_func_button.configure(
    bg_color = frame_background,
    text='✎',
    fg_color=button_color,
    text_color=text_button_color,
    hover_color=button_hover_color,
    font=("Arrial", 15),
    command = build_fourth_func
)
first_dev_fourth.configure(
    bg_color = frame_background,
    text = "Відображення похідної y'",
    font = ("Roboto Slab", 15),
    text_color = text_color,
    fg_color = input_color,
    # bg_color = 'green',
    hover_color=checkbox_hover_color,
    border_width = 2,
    border_color = input_border_color,
    command = fourth_first_dev,
    # цвет галочки
    checkmark_color = text_color
)
second_dev_fourth.configure(
    bg_color = frame_background,
    text = "Відображення похідної y''",
    font = ("Roboto Slab", 15),
    text_color = text_color,
    fg_color = input_color,
    # bg_color = 'green',
    hover_color=checkbox_hover_color,
    border_width = 2,
    border_color = input_border_color,
    command = fourth_second_dev,
    # цвет галочки
    checkmark_color = text_color
)

inflection_points_label.configure(
    text = '9) Точки перегину',
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'w'
)
convexity_intervals_label.configure(
    text = '10) Проміжки опуклості',
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'w'
)
slope_asymptote.configure(
    text = '11) Похила асимптота',
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'w'
)
# стілі для чекбоксів
first_dev_fdrob.configure(
    bg_color = frame_background,
    text = "Відображення похідної y'",
    fg_color = input_color,
    font = ("Roboto Slab", 15),
    text_color = text_color,
    # bg_color = 'green',
    hover_color=checkbox_hover_color,
    border_width = 2,
    border_color = input_border_color,
    # цвет галочки
    checkmark_color = text_color,
    command = drob_first_dev
)
first_dev_sdrob.configure(
    bg_color = frame_background,
    text = "Відображення похідної y'",
    fg_color = input_color,
    # bg_color = 'green',
    hover_color=checkbox_hover_color,
    font = ("Roboto Slab", 15),
    text_color = text_color,
    border_width = 2,
    border_color = input_border_color,
    # цвет галочки
    checkmark_color = text_color,
    command = third_first_dev
)

second_dev_sdrob.configure(
    bg_color = frame_background,
    text = "Відображення похідної y''",
    fg_color = input_color,
    # bg_color = 'green',
    hover_color=checkbox_hover_color,
    border_width = 2,
    font = ("Roboto Slab", 15),
    text_color = text_color,
    border_color = input_border_color,
    # цвет галочки
    checkmark_color = text_color,
    command = third_second_dev
)

second_dev_fdrob.configure(
    bg_color = frame_background,
    text = "Відображення похідної y''",
    fg_color = input_color,
    # bg_color = 'green',
    hover_color=checkbox_hover_color,
    border_width = 2,
    border_color = input_border_color,
    # цвет галочки
    checkmark_color = text_color,
    command = drob_second_dev,
    font = ("Roboto Slab", 15),
    text_color = text_color
)
main_graphic_label.configure(
    font = ("Roboto Slab", 15),
    text_color = text_color,
    bg_color = frame_background,
    fg_color = frame_background,
    anchor = 'w',
    text = 'Головний графік'
)