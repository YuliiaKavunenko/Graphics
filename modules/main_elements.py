'''
Файл для створення головних елементів на вікні.
'''
# 
import customtkinter as ctk
# 
import matplotlib.pyplot as plot
# 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# створення головного вікна main
main = ctk.CTk()
# створення титульного вікна програми
intrd_window = ctk.CTk()

# створення фрейму для роботи і побудови функцій
frame_first = ctk.CTkFrame(
    master = main,
    width = 343,
    height = 345
)
# створення фрейму для позначення відображення і не скриття похідних (checkbox)
frame_for_options = ctk.CTkFrame(
    master = main,
    width = 360,
    height = 345
)
# створення фрейму для виведення дослідження функцій
frame_exploration = ctk.CTkFrame(
    master = main,
    width = 710,
    height = 420
)

# кнопка для отримання даних малювання графика
button_get = ctk.CTkButton(
    master=main,
    width= 40,
    height=40
)
# input для введення любих графіків
input_graphic = ctk.CTkEntry(
    master=main,
    width=230,
    height=40
)
# фрейм для вибору базових функцій
frame_menu = ctk.CTkScrollableFrame(
    master = main,
    width = 205,
    height = 80,
    orientation="vertical"
)

# створення фігури і осей ох, оу
fig, ax = plot.subplots(figsize=(6, 6), facecolor='white')
# Створення холста для розміщення побудови графіків
canvas = FigureCanvasTkAgg(figure = fig, master=main)
# лейбл "y =" для введення різних графіків
label_y = ctk.CTkLabel(
    master = main,
    width = 22,
    height = 40,
    text = 'y ='
)
# створення лейблу для першого нашого графіку функції
y_1 = ctk.CTkLabel(
    master = main,
    width = 325,
    height = 40,
    text = 'y =          х³ +          x² +          x +'
)
# 
y_2 = ctk.CTkLabel(
    master = main,
    width = 325,
    height = 40,
    text = "y’ = 3*          x² + 2*          x +"
)
# 
y_3 = ctk.CTkLabel(
    master = main,
    width = 325,
    height = 40,
    text = "y'' = 6*          *x + 2*           "
)
# 
a_1 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
# 
b_1 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
# 
c_1 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
d_1 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)

a_2 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)

b_2 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)

c_2 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)

a_3 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)

b_3 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)

get_grachic_1 = ctk.CTkButton(
    master = main,
    width = 40,
    height = 40
)

clean_graphic = ctk.CTkButton(
    master = main,
    width = 85,
    height = 35
)

l_exploration = ctk.CTkLabel(
    master = main,
    width = 220,
    height = 26
)
interval_label = ctk.CTkLabel(
    master = main,
    width = 250,
    height = 35
)
scope_label = ctk.CTkLabel(
    master = main,
    width = 250,
    height = 35
)
drob_y_ch = ctk.CTkLabel(
    master = main,
    width = 160,
    height = 45,
    text = '      х²  -          '
)
drob_y_zn = ctk.CTkLabel(
    master = main,
    width = 160,
    height = 45,
    text = 'х -'
)
drob_y = ctk.CTkLabel(
    master = main,
    width = 23,
    height = 40,
    text = 'y ='
)
drob = ctk.CTkLabel(
    master = main,
    width = 209,
    height = 5,
    text = '————————————'
)
a_drob_1 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)

a_drob_3 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
get_drob_grachic = ctk.CTkButton(
    master = main,
    width = 40,
    height = 40
)
drob_first_dev_lable = ctk.CTkLabel(
    master = main,
    width = 275,
    height = 40
)

drob_second_dev_lable = ctk.CTkLabel(
    master = main,
    width = 275,
    height = 40
)

local_max_min_label = ctk.CTkLabel(
    master = main,
    width = 350,
    height = 35
)
zn_function_label = ctk.CTkLabel(
    master = main,
    width = 350,
    height = 35
)


points_ox_oy_label = ctk.CTkLabel(
    master = main,
    width = 350,
    height = 35
)

range_of_function = ctk.CTkLabel(
    master = main,
    width = 350,
    height = 35
)

points_zero_label = ctk.CTkLabel(
    master = main,
    width = 350,
    height = 35
)

even_or_odd_func_l = ctk.CTkLabel(
    master = main,
    width = 250,
    height = 35
)

intervals_identity_l = ctk.CTkLabel(
    master = main,
    width = 300,
    height = 35
) 
# ЕЛЕМЕНТИ ДЛЯ ТРЕТЬОЇ ФУНКЦІЇ!!!
third_func_l = ctk.CTkLabel(
    master = main,
    width = 23,
    height = 40,
    text = 'y ='
)
third_func_up_label = ctk.CTkLabel(
    master = main,
    width = 160,
    height = 43
)
third_func_down_label = ctk.CTkLabel(
    master = main,
    width = 160,
    height = 43
)
third_func_drob_label = ctk.CTkLabel(
    master = main,
    width = 209,
    height = 2,
    text = '————————————'
)
third_f_dev_label = ctk.CTkLabel(
    master = main,
    width = 275,
    height = 40
)
third_s_dev_label = ctk.CTkLabel(
    master = main,
    width = 275,
    height = 40
)
third_func_button = ctk.CTkButton(
    master = main,
    width = 40,
    height = 40
)

a_th_drob = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)

# ЧЕКБОКСІ
# першій графік
first_dev = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
second_dev = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
# другій графік
first_dev_fdrob = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
second_dev_fdrob = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
# третій графік
first_dev_sdrob = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
second_dev_sdrob = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
# четвертій графік
first_dev_fourth = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
second_dev_fourth = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
# ЛЕЙБЛІ ДЛЯ ПОЗНАЧЕННЯ КОЛЬОРУ ФУНКЦІЇ
purple_gr = ctk.CTkLabel(
    master = main,
    height = 40,
    width = 22,
    anchor = "center",
    text = "●"
)
red_gr = ctk.CTkLabel(
    master = main,
    height = 40,
    width = 22,
    anchor = "center",
    text = "●"
)
green_gr = ctk.CTkLabel(
    master = main,
    height = 40,
    width = 22,
    anchor = "center",
    text = "●"
)
blue_gr = ctk.CTkLabel(
    master = main,
    height = 40,
    width = 22,
    anchor = "center",
    text = "●"
)
# ЛЕЙБЛ ДЛЯ ПОКАЗАНІЯ ЕСТЬ ФУНКЦІЯ ЧИ НЄ
func_t_or_f = ctk.CTkLabel(
    master = main,
    height = 26,
    width = 328,
    anchor = "center",
    text = "Графік для побудови не обрано!"
)
# КНОПКА ДЛЯ ОТКРІТІЯ НОВОГО ОКОШИЧКА
choose_gr = ctk.CTkButton(
    master=main,
    width= 327,
    height = 40
)

# ЧЕТВЕРТА ФУНКЦІЯ!!!!!!!!!!!!!!!!!!!!!!!

a4_drob = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)

fourth_func_l = ctk.CTkLabel(
    master = main,
    width = 23,
    height = 40,
    text = 'y ='
)
fourth_func_up_label = ctk.CTkLabel(
    master = main,
    width = 160,
    height = 43
)
fourth_func_down_label = ctk.CTkLabel(
    master = main,
    width = 160,
    height = 43
)
fourth_func_drob_label = ctk.CTkLabel(
    master = main,
    width = 209,
    height = 2,
    text = '————————————'
)
fourth_f_dev_label = ctk.CTkLabel(
    master = main,
    width = 275,
    height = 40
)
fourth_s_dev_label = ctk.CTkLabel(
    master = main,
    width = 275,
    height = 40
)
fourth_func_button = ctk.CTkButton(
    master = main,
    width = 40,
    height = 40
)

inflection_points_label = ctk.CTkLabel(
    master = main,
    width = 300,
    height = 35
)
convexity_intervals_label = ctk.CTkLabel(
    master = main,
    width = 300,
    height = 35
)
slope_asymptote = ctk.CTkLabel(
    master = main,
    width = 300,
    height = 35
)
main_graphic_label = ctk.CTkLabel(
    master = main,
    width = 300,
    height = 35
)