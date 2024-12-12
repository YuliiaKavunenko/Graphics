'''
Файл для створення дочірнього вікна нашого main для вибору функції побудови і дослідження.
'''
# імпорт customtkinter для створення вікна і елементів для нього /
import customtkinter as ctk
# імпорт усіх елементів з main_elements /
from .main_elements import *
# імпорт PIL для роботи з зображеннями /
from PIL import Image
# імпорт os для пошуку шляху до файлів /
import os

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


# для пошуку абсолютного шляху до картинок /
PATH = os.path.abspath(__file__+"/../../img")

# Завантажуємо зображення для кнопок вибору функції /
# графік y = (x**2 - a)/(x - b) /
image_gr_2 = ctk.CTkImage(Image.open(os.path.join(PATH,"function2.png")), size=(250, 85))
# графік y = (x**2-a**2)/x /
image_gr_1 = ctk.CTkImage(Image.open(os.path.join(PATH,"function1.png")), size=(250, 85))
# графік у = x/(x**2 + a) /
image_gr_3 = ctk.CTkImage(Image.open(os.path.join(PATH,"function3.png")), size=(250, 85))

# запуск вікна /
def functions_window():
    global window_with_fun
    # створення поверхневого вікна для вікна main /
    window_with_fun = ctk.CTkToplevel(main)
    # задаємо розмір вікна /
    window_with_fun.geometry("630x510")
    # робимо, щоб не можна було змінити розмір вікна /
    window_with_fun.resizable(False, False)
    # задаємо назву для вікна /
    window_with_fun.title("Вікно вибору функції для дослідження")
    # задаємо колір фону для вікна /
    window_with_fun.configure(
        fg_color = background,
        bg_color = background
    )
    window_with_fun.attributes('-topmost', True)

    # створення кнопки для першого графіку, у = ax³ + bx² + cx + d /
    first_fun_button = ctk.CTkButton(
        # задаємо вікно до якого прив'язана кнопка /
        master = window_with_fun,
        # ширина кнопки /
        width = 300,
        # висота кнопки /
        height = 40
    )
    # задаємо стилі для кнопки /
    first_fun_button.configure(
        # задаємо колір фону /
        bg_color = background,
        # колір самої кнопки /
        fg_color = frame_background,
        # внутрішній текст кнопки /
        text = 'у = ax³ + bx² + cx + d',
        # колір при наведенні на кнопку /
        hover_color = button_hover_color,
        # зкруглюємо угли /
        corner_radius = 10,
        # колір тексту кнопки /
        text_color = text_color,
        # шрифт тексту кнопки /
        font = ("Roboto Slab", 20),
        # відцентрування тексту кнопки /
        anchor = "center",
        # функція, яка визивається при натисканні на кнопку /
        command = first_fn_on
    )

    # створення кнопки для другого графіку, y = (x**2 - a)/(x - b) /
    second_fun_button = ctk.CTkButton(
        # задаємо вікно до якого прив'язана кнопка /
        master = window_with_fun,
        # ширина кнопки /
        width = 300,
        # висота кнопки /
        height = 90
    )
    # задаємо стилі для кнопки /
    second_fun_button.configure(
        # задаємо колір фону /
        bg_color = background,
        # колір самої кнопки /
        fg_color = frame_background,
        # внутрішній текст кнопки /
        text = '',
        # колір при наведенні на кнопку /
        hover_color = button_hover_color,
        # зкруглюємо угли /
        corner_radius = 10,
        # колір тексту кнопки /
        text_color = text_color,
        # шрифт тексту кнопки /
        font = ("Roboto Slab", 20),
        # відцентрування тексту кнопки /
        anchor = "center",
        # функція, яка визивається при натисканні на кнопку /
        command = second_fn_on,
        # зображення для кнопки /
        image = image_gr_2
    )

    # створення кнопки для третього графіку, y = (x**2 - a**2)/x /
    third_fun_button = ctk.CTkButton(
        # задаємо вікно до якого прив'язана кнопка /
        master = window_with_fun,
        # ширина кнопки /
        width = 300,
        # висота кнопки /
        height = 90
    )
    # задаємо стилі для кнопки /
    third_fun_button.configure(
        # задаємо колір фону /
        bg_color = background,
        # колір самої кнопки /
        fg_color = frame_background,
        # внутрішній текст кнопки /
        text = '',
        # колір при наведенні на кнопку /
        hover_color = button_hover_color,
        # зкруглюємо угли /
        corner_radius = 10,
        # колір тексту кнопки /
        text_color = text_color,
        # шрифт тексту кнопки /
        font = ("Roboto Slab", 20),
        # відцентрування тексту кнопки /
        anchor = "center",
        # функція, яка визивається при натисканні на кнопку /
        command = third_fn_on,
        # зображення для кнопки /
        image = image_gr_1
    )

    # створення кнопки для четвертого графіку, у = x/(x**2 + a) /
    fourth_fun_button = ctk.CTkButton(
        # задаємо вікно до якого прив'язана кнопка /
        master = window_with_fun,
        # ширина кнопки /
        width = 300,
        # висота кнопки /
        height = 90
    )
    # задаємо стилі для кнопки /
    fourth_fun_button.configure(
        # задаємо колір фону /
        bg_color = background,
        # колір самої кнопки /
        fg_color = frame_background,
        # внутрішній текст кнопки /
        text = '',
        # колір при наведенні на кнопку /
        hover_color = button_hover_color,
        # зкруглюємо угли /
        corner_radius = 10,
        # колір тексту кнопки /
        text_color = text_color,
        # шрифт тексту кнопки /
        font = ("Roboto Slab", 20),
        # відцентрування тексту кнопки /
        anchor = "center",
        # функція, яка визивається при натисканні на кнопку /
        command = fourth_fn_on,
        # зображення для кнопки /
        image = image_gr_3
    )

    # поки неготові графіки: /

    a_fun_button = ctk.CTkButton(
    master = window_with_fun,
    width = 300,
    height = 40
    )
    # задаємо стилі для кнопки
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
    # задаємо стилі для кнопки /
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
    # задаємо стилі для кнопки /
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
    # задаємо стилі для кнопки /
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

    # розміщення усіх кнопок на вікні /
    # кнопка для функції у = ax³ + bx² + cx + d /
    first_fun_button.place(x = 10, y = 10)
    # кнопка для функції y = (x**2 - a)/(x - b) /
    second_fun_button.place(x = 320, y = 10)
    # кнопка для функції y = (x**2-a**2)/x /
    third_fun_button.place(x = 320, y = 110)
    # кнопка для функції у = x/(x**2 + a) /
    fourth_fun_button.place(x = 320, y = 210)

    # кнопки для майбутніх функцій /
    a_fun_button.place(x = 10, y = 60)
    b_fun_button.place(x = 10, y = 110)
    c_fun_button.place(x = 10, y = 160)
    d_fun_button.place(x = 10, y = 210)
    e_fun_button.place(x = 10, y = 260)

    h_fun_button.place(x = 320, y = 310)
    i_fun_button.place(x = 320, y = 410)
    j_fun_button.place(x = 10, y = 310)
    k_fun_button.place(x = 10, y = 410)

# функція для видалення непотрібних елементів з вікна при зміні вибору функції /
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
    third_s_dev_label.place_forget()
    third_f_dev_label.place_forget()
    second_dev_sdrob.place_forget()
    first_dev_sdrob.place_forget()

    fourth_func_l.place_forget()
    fourth_func_drob_label.place_forget()
    fourth_func_up_label.place_forget()
    fourth_func_up_label.lift()
    fourth_func_down_label.place_forget()
    a4_drob.place_forget()
    a4_drob.lift()
    fourth_func_button.place_forget()
    second_dev_fourth.place_forget()
    first_dev_fourth.place_forget()
    fourth_f_dev_label.place_forget()
    fourth_s_dev_label.place_forget()

    get_grachic_1.place_forget()

    main_graphic_label.place_forget()

# розміщення елементів для першого графіку, у = ax³ + bx² + cx + d /
def first_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main /
    clean_old_gr()
    # розміщуємо на main label "y =" /
    y_1.place(x = 688, y = 173)
    # розміщуємо на main label "y' =" /
    y_2.place(x = 688, y = 223)
    # розміщуємо на main label "y'' =" /
    y_3.place(x = 688, y = 273)

    # розміщуємо на main input для коєфіцієнта a /
    a_1.place(x = 715, y = 178)
    # розміщуємо на main input для коєфіцієнта b /
    b_1.place(x = 784, y = 178)
    # розміщуємо на main input для коєфіцієнта c /
    c_1.place(x = 851, y = 178)
    # розміщуємо на main input для коєфіцієнта d /
    d_1.place(x = 911, y = 178)

    # розміщуємо на main input для коєфіцієнта a /
    a_2.place(x = 735, y = 228)
    # розміщуємо на main input для коєфіцієнта b /
    b_2.place(x = 822, y = 228)
    # розміщуємо на main input для коєфіцієнта c /
    c_2.place(x = 884, y = 228)

    # розміщуємо на main input для коєфіцієнта a /
    a_3.place(x = 740, y = 278)
    # розміщуємо на main input для коєфіцієнта b /
    b_3.place(x = 827, y = 278)

    # розміщуємо на main кнопку для побудови графіку /
    get_grachic_1.place(x = 978, y = 173)

    # прибираємо лейбл на вікні main "Графік для побудови не обрано!" /
    func_t_or_f.place_forget()
    # закриваємо вікно з функціями /
    window_with_fun.destroy()
# розміщення елементів для другого графіку, y = (x**2 - a)/(x - b) /
def second_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main /
    clean_old_gr()
    # розміщуємо на main label "y =" /
    drob_y.place(x = 688, y = 173)
    # розміщуємо на main label чисельника функції "x**2 - a" /
    drob_y_ch.place(x = 737, y = 148)
    # розміщуємо на main label з знаком дробу "-------" /
    drob.place(x = 720, y = 188)
    # розміщуємо на main label значенника функції "x - b" /
    drob_y_zn.place(x = 734, y = 196)

    # розміщуємо на main input для коєфіцієнта a /
    a_drob_1.place(x = 829, y = 156)
    # розміщуємо на main input для коєфіцієнта b /
    a_drob_3.place(x = 826, y = 202)

    # розміщуємо на main кнопку для побудови графіку /
    get_drob_grachic.place(x = 978, y = 173)

    # розміщуємо на main label з похідною y' /
    drob_first_dev_lable.place(x = 688, y = 234)
    # розміщуємо на main label з похідною y'' /
    drob_second_dev_lable.place(x = 688, y = 288)
    # закриваємо вікно з функціями /
    window_with_fun.destroy()
# розміщення елементів для третього графіку, y = (x**2-a**2)/x /
def third_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main /
    clean_old_gr()
    # розміщуємо на main label "y =" /
    third_func_l.place(x = 688, y = 173)

    # розміщуємо на main label знаку дробу "------" /
    third_func_drob_label.place(x = 711, y = 190)
    # розміщуємо на main label чисельника функції "x**2 - a**2" /
    third_func_up_label.place(x = 737, y = 148)
    # переміщуємо лейбл чисельнику на передній план /
    third_func_up_label.lift()
    # розміщуємо на main label значенника функції "x" /
    third_func_down_label.place(x = 736, y = 196)

    # розміщуємо на main input для коєфіцієнту a /
    a_th_drob.place(x = 812, y = 156)
    # переміщуємо input на передній план /
    a_th_drob.lift()

    # розміщуємо на main кнопку для побудови графіку /
    third_func_button.place(x = 978, y = 173)

    # розміщуємо на main label з похідною y' /
    third_f_dev_label.place(x = 688, y = 234)
    # розміщуємо на main label з похідною y'' /
    third_s_dev_label.place(x = 688, y = 288)
    # закриваємо вікно з функціями /
    window_with_fun.destroy()
# розміщення елементів для четвертого графіку, у = x/(x**2 + a) /
def fourth_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main /
    clean_old_gr()
    # розміщуємо на main label "y =" /
    fourth_func_l.place(x = 688, y = 173)
    
    # розміщуємо на main label знаку дробу "------" /
    fourth_func_drob_label.place(x = 711, y = 190)
    # розміщуємо на main label чисельника функції "x" /
    fourth_func_up_label.place(x = 737, y = 150)
    # розміщуємо на main  /
    fourth_func_up_label.lift()
    # розміщуємо на main label значенника функції "x**2 + a" /
    fourth_func_down_label.place(x = 736, y = 200)

    # розміщуємо на main input для коєфіцієнту a /
    a4_drob.place(x = 812, y = 208)

    # розміщуємо на main label з похідною y' /
    fourth_f_dev_label.place(x = 688, y = 234)
    # розміщуємо на main label з похідною y'' /
    fourth_s_dev_label.place(x = 688, y = 288)

    # переміщуємо input коєфіцієнту а чисельнику на передній план /
    a4_drob.lift()
    
    # розміщуємо на main кнопку для побудови графіку /
    fourth_func_button.place(x = 978, y = 173)
    # закриваємо вікно з функціями /
    window_with_fun.destroy()
#  на майбутнє розміщення елементів для останніх графіків /
def b_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main /
    clean_old_gr()
    # закриваємо вікно з функціями /
    window_with_fun.destroy()

def c_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main /
    clean_old_gr()
    # закриваємо вікно з функціями /
    window_with_fun.destroy()

def d_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main /
    clean_old_gr()
    # закриваємо вікно з функціями /
    window_with_fun.destroy()

def e_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main /
    clean_old_gr()
    # закриваємо вікно з функціями /
    window_with_fun.destroy()


def g_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main /
    clean_old_gr()
    # закриваємо вікно з функціями /
    window_with_fun.destroy()

def h_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main /
    clean_old_gr()
    # закриваємо вікно з функціями /
    window_with_fun.destroy()

def i_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main /
    clean_old_gr()
    # закриваємо вікно з функціями /
    window_with_fun.destroy()

def j_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main /
    clean_old_gr()
    # закриваємо вікно з функціями /
    window_with_fun.destroy()

def k_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main /
    clean_old_gr()
    # закриваємо вікно з функціями /
    window_with_fun.destroy()