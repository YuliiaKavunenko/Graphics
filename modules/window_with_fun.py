'''
Файл для створення дочірнього вікна нашого main для вибору функції побудови і дослідження.
'''

import customtkinter as ctk
from .main_elements import *
from PIL import Image
import os

background = "#A76E56"
frame_background = "#BA7D65"
text_color = "#392D20"
button_color = "#7B4C39"
text_button_color = "#F1D5BA"
input_color = "#FAF0E6"
input_border_color = "#EAD1B8"
input_textholder_color = "#CAA37D"
hover_color_menu = "#F3E4D5"
button_hover_color = "#9D6249"
checkbox_hover_color = "#EBCDAE"
# для пошуку абс
PATH = os.path.abspath(__file__+"/../../img")

# Завантажуємо зображення
image_gr_2 = ctk.CTkImage(Image.open(os.path.join(PATH,"function2.png")), size=(250, 85))
image_gr_1 = ctk.CTkImage(Image.open(os.path.join(PATH,"function1.png")), size=(250, 85))
image_gr_3 = ctk.CTkImage(Image.open(os.path.join(PATH,"function3.png")), size=(250, 85))


def functions_window():
    global window_with_fun

    window_with_fun = ctk.CTkToplevel(main)
    window_with_fun.geometry("630x510")
    window_with_fun.resizable(False, False)
    window_with_fun.title("Вікно вибору функції для дослідження")
    window_with_fun.configure(
        fg_color = background,
        bg_color = background
    )
    window_with_fun.attributes('-topmost', True)

    # перший графік
    first_fun_button = ctk.CTkButton(
    master = window_with_fun,
    width = 300,
    height = 40
    )
    first_fun_button.configure(
    bg_color = background,
    fg_color = frame_background,
    text = 'у = ax³ + bx² + cx + d',
    hover_color = button_hover_color,
    corner_radius = 10,
    text_color = text_color,
    font = ("Roboto Slab", 20),
    anchor = "center",
    command = first_fn_on
    )

    # другий графік
    second_fun_button = ctk.CTkButton(
    master = window_with_fun,
    width = 300,
    height = 90
    )
    second_fun_button.configure(
    bg_color = background,
    fg_color = frame_background,
    text = '',
    hover_color = button_hover_color,
    corner_radius = 10,
    text_color = text_color,
    font = ("Roboto Slab", 20),
    anchor = "center",
    command = second_fn_on,
    image = image_gr_2
    )
    third_fun_button = ctk.CTkButton(
    master = window_with_fun,
    width = 300,
    height = 90
    )
    third_fun_button.configure(
    bg_color = background,
    fg_color = frame_background,
    text = '',
    hover_color = button_hover_color,
    corner_radius = 10,
    text_color = text_color,
    font = ("Roboto Slab", 20),
    anchor = "center",
    command = third_fn_on,
    image = image_gr_1
    )

    fourth_fun_button = ctk.CTkButton(
    master = window_with_fun,
    width = 300,
    height = 90
    )
    fourth_fun_button.configure(
    bg_color = background,
    fg_color = frame_background,
    text = '',
    hover_color = button_hover_color,
    corner_radius = 10,
    text_color = text_color,
    font = ("Roboto Slab", 20),
    anchor = "center",
    command = fourth_fn_on,
    image = image_gr_3
    )
    # поки неготові графіки:

    a_fun_button = ctk.CTkButton(
    master = window_with_fun,
    width = 300,
    height = 40
    )
    a_fun_button.configure(
    bg_color = background,
    fg_color = frame_background,
    text = 'у =',
    hover_color = button_hover_color,
    corner_radius = 10,
    text_color = text_color,
    font = ("Roboto Slab", 20),
    anchor = "center",
    command = fourth_fn_on
    )

    b_fun_button = ctk.CTkButton(
    master = window_with_fun,
    width = 300,
    height = 40
    )
    b_fun_button.configure(
    bg_color = background,
    fg_color = frame_background,
    text = 'у =',
    hover_color = button_hover_color,
    corner_radius = 10,
    text_color = text_color,
    font = ("Roboto Slab", 20),
    anchor = "center",
    command = b_fn_on
    )

    c_fun_button = ctk.CTkButton(
    master = window_with_fun,
    width = 300,
    height = 40
    )
    c_fun_button.configure(
    bg_color = background,
    fg_color = frame_background,
    text = 'у =',
    hover_color = button_hover_color,
    corner_radius = 10,
    text_color = text_color,
    font = ("Roboto Slab", 20),
    anchor = "center",
    command = c_fn_on
    )

    d_fun_button = ctk.CTkButton(
    master = window_with_fun,
    width = 300,
    height = 40
    )
    d_fun_button.configure(
    bg_color = background,
    fg_color = frame_background,
    text = 'у =',
    hover_color = button_hover_color,
    corner_radius = 10,
    text_color = text_color,
    font = ("Roboto Slab", 20),
    anchor = "center",
    command = d_fn_on
    )

    e_fun_button = ctk.CTkButton(
    master = window_with_fun,
    width = 300,
    height = 40
    )
    e_fun_button.configure(
    bg_color = background,
    fg_color = frame_background,
    text = 'у =',
    hover_color = button_hover_color,
    corner_radius = 10,
    text_color = text_color,
    font = ("Roboto Slab", 20),
    anchor = "center",
    command = e_fn_on
    )

    j_fun_button = ctk.CTkButton(
    master = window_with_fun,
    width = 300,
    height = 90
    )
    j_fun_button.configure(
    bg_color = background,
    fg_color = frame_background,
    text = 'у =',
    hover_color = button_hover_color,
    corner_radius = 10,
    text_color = text_color,
    font = ("Roboto Slab", 20),
    anchor = "center",
    command = j_fn_on
    )
    
    k_fun_button = ctk.CTkButton(
    master = window_with_fun,
    width = 300,
    height = 90
    )
    k_fun_button.configure(
    bg_color = background,
    fg_color = frame_background,
    text = 'у =',
    hover_color = button_hover_color,
    corner_radius = 10,
    text_color = text_color,
    font = ("Roboto Slab", 20),
    anchor = "center",
    command = k_fn_on
    )
    
    

    
    h_fun_button = ctk.CTkButton(
    master = window_with_fun,
    width = 300,
    height = 90
    )
    h_fun_button.configure(
    bg_color = background,
    fg_color = frame_background,
    text = 'у =',
    hover_color = button_hover_color,
    corner_radius = 10,
    text_color = text_color,
    font = ("Roboto Slab", 20),
    anchor = "center",
    command = h_fn_on
    )
    
    i_fun_button = ctk.CTkButton(
    master = window_with_fun,
    width = 300,
    height = 90
    )
    i_fun_button.configure(
    bg_color = background,
    fg_color = frame_background,
    text = 'у =',
    hover_color = button_hover_color,
    corner_radius = 10,
    text_color = text_color,
    font = ("Roboto Slab", 20),
    anchor = "center",
    command = i_fn_on
    )

    # розміщення
    first_fun_button.place(x = 10, y = 10)
    second_fun_button.place(x = 320, y = 10)
    third_fun_button.place(x = 320, y = 110)
    fourth_fun_button.place(x = 320, y = 210)

    a_fun_button.place(x = 10, y = 60)
    b_fun_button.place(x = 10, y = 110)
    c_fun_button.place(x = 10, y = 160)
    d_fun_button.place(x = 10, y = 210)
    e_fun_button.place(x = 10, y = 260)

    h_fun_button.place(x = 320, y = 310)
    i_fun_button.place(x = 320, y = 410)
    j_fun_button.place(x = 10, y = 310)
    k_fun_button.place(x = 10, y = 410)

# убіраєм лішніє лейблі
def clean_old_gr():
    first_dev.place_forget()
    second_dev.place_forget()
    first_dev_fdrob.place_forget()
    second_dev_fdrob.place_forget()
    first_dev_sdrob.place_forget()
    second_dev_sdrob.place_forget()
    
    red_gr.place_forget()
    green_gr.place_forget()
    blue_gr.place_forget()

    func_t_or_f.place_forget()

    drob_y_ch.place_forget()
    drob.place_forget()
    drob_y_zn.place_forget()


    a_drob_1.place_forget()
    a_drob_3.place_forget()
    
    get_drob_grachic.place_forget()

    drob_first_dev_lable.place_forget()
    drob_second_dev_lable.place_forget()

    y_1.place_forget()
    y_2.place_forget()
    y_3.place_forget()

    a_1.place_forget()
    b_1.place_forget()
    c_1.place_forget()
    d_1.place_forget()

    a_2.place_forget()
    b_2.place_forget()
    c_2.place_forget()

    a_3.place_forget()
    b_3.place_forget()

    third_func_l.place_forget()
    third_func_drob_label.place_forget()
    third_func_up_label.place_forget()
    third_func_down_label.place_forget()
    a_th_drob.place_forget()
    third_func_button.place_forget()

    fourth_func_l.place_forget()
    fourth_func_drob_label.place_forget()
    fourth_func_up_label.place_forget()
    fourth_func_up_label.lift()
    fourth_func_down_label.place_forget()
    a4_drob.place_forget()
    a4_drob.lift()
    fourth_func_button.place_forget()

    get_grachic_1.place_forget()

# першій графік
def first_fn_on():
    clean_old_gr()
    
    y_1.place(x = 688, y = 173)
    y_2.place(x = 688, y = 223)
    y_3.place(x = 688, y = 273)

    a_1.place(x = 715, y = 178)
    b_1.place(x = 784, y = 178)
    c_1.place(x = 851, y = 178)
    d_1.place(x = 911, y = 178)

    a_2.place(x = 735, y = 228)
    b_2.place(x = 822, y = 228)
    c_2.place(x = 884, y = 228)

    a_3.place(x = 740, y = 278)
    b_3.place(x = 827, y = 278)

    get_grachic_1.place(x = 978, y = 173)

    func_t_or_f.place_forget()
    window_with_fun.destroy()
# другій графік
def second_fn_on():
    clean_old_gr()

    drob_y.place(x = 688, y = 173)
    drob_y_ch.place(x = 737, y = 148)
    drob.place(x = 720, y = 188)
    drob_y_zn.place(x = 734, y = 196)


    a_drob_1.place(x = 829, y = 156)
    a_drob_3.place(x = 826, y = 202)

    get_drob_grachic.place(x = 978, y = 173)

    drob_first_dev_lable.place(x = 688, y = 234)
    drob_second_dev_lable.place(x = 688, y = 288)
    
    window_with_fun.destroy()
# третій графік
def third_fn_on():
    clean_old_gr()

    third_func_l.place(x = 688, y = 173)

    third_func_drob_label.place(x = 711, y = 190)
    third_func_up_label.place(x = 737, y = 148)
    third_func_up_label.lift()
    third_func_down_label.place(x = 736, y = 196)
    a_th_drob.place(x = 812, y = 156)

    a_th_drob.lift()

    third_func_button.place(x = 978, y = 173)

    third_f_dev_label.place(x = 688, y = 234)
    third_s_dev_label.place(x = 688, y = 288)
    
    window_with_fun.destroy()
# четвертий графік
def fourth_fn_on():
    clean_old_gr()

    fourth_func_l.place(x = 688, y = 173)
    
    fourth_func_drob_label.place(x = 711, y = 190)
    fourth_func_up_label.place(x = 737, y = 150)
    fourth_func_up_label.lift()
    fourth_func_down_label.place(x = 736, y = 200)
    a4_drob.place(x = 812, y = 208)

    fourth_f_dev_label.place(x = 688, y = 234)
    fourth_s_dev_label.place(x = 688, y = 288)

    a4_drob.lift()
    
    fourth_func_button.place(x = 978, y = 173)
    
    window_with_fun.destroy()

def b_fn_on():
    clean_old_gr()
    
    window_with_fun.destroy()

def c_fn_on():
    clean_old_gr()
    
    window_with_fun.destroy()

def d_fn_on():
    clean_old_gr()
    
    window_with_fun.destroy()

def e_fn_on():
    clean_old_gr()
    
    window_with_fun.destroy()


def g_fn_on():
    clean_old_gr()
    
    window_with_fun.destroy()

def h_fn_on():
    clean_old_gr()
    
    window_with_fun.destroy()

def i_fn_on():
    clean_old_gr()
    
    window_with_fun.destroy()

def j_fn_on():
    clean_old_gr()
    
    window_with_fun.destroy()

def k_fn_on():
    clean_old_gr()
    
    window_with_fun.destroy()