'''
Файл для створення дочірнього вікна нашого main для вибору функції побудови і дослідження /
A file to create a child window of our main to select the build and explore function
'''
# імпорт customtkinter для створення вікна і елементів для нього / import customtkinter for creating a window and its elements
import customtkinter as ctk
# імпорт усіх елементів з main_elements / import all elements from main_elements
from .main_elements import *
# імпорт PIL для роботи з зображеннями / import PIL for working with images
from PIL import Image
# імпорт os для пошуку шляху до файлів / import os for finding file paths
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


# для пошуку абсолютного шляху до картинок / for finding the absolute path to images
PATH = os.path.abspath(__file__+"/../../img")

# Завантажуємо зображення для кнопок вибору функції / loading images for function selection buttons
# графік y = (x**2 - a)/(x - b) / graph y = (x**2 - a)/(x - b)
image_gr_2 = ctk.CTkImage(Image.open(os.path.join(PATH,"function2.png")), size=(250, 85))
# графік y = (x**2-a**2)/x / graph y = (x**2 - a**2)/x
image_gr_1 = ctk.CTkImage(Image.open(os.path.join(PATH,"function1.png")), size=(250, 85))
# графік у = x/(x**2 + a) / graph y = x/(x**2 + a)
image_gr_3 = ctk.CTkImage(Image.open(os.path.join(PATH,"function3.png")), size=(250, 85))

image_gr_5 = ctk.CTkImage(Image.open(os.path.join(PATH,"function5.png")), size=(250, 85))
image_gr_6 = ctk.CTkImage(Image.open(os.path.join(PATH,"function6.png")), size=(250, 85))
image_gr_7 = ctk.CTkImage(Image.open(os.path.join(PATH,"function7.png")), size=(250, 85))

# запуск вікна / window launch
def functions_window():
    # створення поверхневого вікна для вікна main / creating a top-level window for the main window
    window_with_fun = ctk.CTkToplevel(main)
    # задаємо розмір вікна / setting the window size
    window_with_fun.geometry("630x360")
    # робимо, щоб не можна було змінити розмір вікна / making the window size unchangeable
    window_with_fun.resizable(False, False)
    # задаємо назву для вікна / setting the window title
    window_with_fun.title("Вікно вибору функції для дослідження / Function Selection Window for Research")
    # задаємо колір фону для вікна / setting the background color for the window
    window_with_fun.configure(
        fg_color = background,
        bg_color = background
    )
    window_with_fun.attributes('-topmost', True)
    # створення кнопки для першого графіку, у = ax³ + bx² + cx + d / creating a button for the first graph, y = ax³ + bx² + cx + d
    first_fun_button = ctk.CTkButton(
        # задаємо вікно до якого прив'язана кнопка / setting the window to which the button is linked
        master = window_with_fun,
        # ширина кнопки / button width
        width = 300,
        # висота кнопки / button height
        height = 40
    )
    # задаємо стилі для кнопки / setting styles for the button
    first_fun_button.configure(
        # задаємо колір фону / setting the background color
        bg_color = background,
        # колір самої кнопки / button color
        fg_color = frame_background,
        # внутрішній текст кнопки / button text
        text = 'у = ax³ + bx² + cx + d',
        # колір при наведенні на кнопку / hover color for the button
        hover_color = button_hover_color,
        # зкруглюємо угли / rounding the corners
        corner_radius = 10,
        # колір тексту кнопки / button text color
        text_color = text_color,
        # шрифт тексту кнопки / button text font
        font = ("Roboto Slab", 20),
        # відцентрування тексту кнопки / button text alignment
        anchor = "center",
        # функція, яка визивається при натисканні на кнопку / function called when the button is pressed
        command = first_fn_on
    )

    # створення кнопки для другого графіку, y = (x**2 - a)/(x - b) / creating a button for the second graph, y = (x**2 - a)/(x - b)
    second_fun_button = ctk.CTkButton(
        # задаємо вікно до якого прив'язана кнопка / setting the window to which the button is linked
        master = window_with_fun,
        # ширина кнопки / button width
        width = 300,
        # висота кнопки / button height
        height = 90
    )
    # задаємо стилі для кнопки / setting styles for the button
    second_fun_button.configure(
        # задаємо колір фону / setting the background color
        bg_color = background,
        # колір самої кнопки / button color
        fg_color = frame_background,
        # внутрішній текст кнопки / button text
        text = '',
        # колір при наведенні на кнопку / hover color for the button
        hover_color = button_hover_color,
        # зкруглюємо угли / rounding the corners
        corner_radius = 10,
        # колір тексту кнопки / button text color
        text_color = text_color,
        # шрифт тексту кнопки / button text font
        font = ("Roboto Slab", 20),
        # відцентрування тексту кнопки / button text alignment
        anchor = "center",
        # функція, яка визивається при натисканні на кнопку / function called when the button is pressed
        command = second_fn_on,
        # зображення для кнопки / image for the button
        image = image_gr_2
    )

    # створення кнопки для третього графіку, y = (x**2 - a**2)/x / creating a button for the third graph, y = (x**2 - a**2)/x
    third_fun_button = ctk.CTkButton(
        # задаємо вікно до якого прив'язана кнопка / setting the window to which the button is linked
        master = window_with_fun,
        # ширина кнопки / button width
        width = 300,
        # висота кнопки / button height
        height = 90
    )
    # задаємо стилі для кнопки / setting styles for the button
    third_fun_button.configure(
        # задаємо колір фону / setting the background color
        bg_color = background,
        # колір самої кнопки / button color
        fg_color = frame_background,
        # внутрішній текст кнопки / button text
        text = '',
        # колір при наведенні на кнопку / hover color for the button
        hover_color = button_hover_color,
        # зкруглюємо угли / rounding the corners
        corner_radius = 10,
        # колір тексту кнопки / button text color
        text_color = text_color,
        # шрифт тексту кнопки / button text font
        font = ("Roboto Slab", 20),
        # відцентрування тексту кнопки / button text alignment
        anchor = "center",
        # функція, яка визивається при натисканні на кнопку / function called when the button is pressed
        command = third_fn_on,
        # зображення для кнопки / image for the button
        image = image_gr_1
    )

    # створення кнопки для четвертого графіку, у = x/(x**2 + a) / creating a button for the fourth graph, y = x/(x**2 + a)
    fourth_fun_button = ctk.CTkButton(
        # задаємо вікно до якого прив'язана кнопка / setting the window to which the button is linked
        master = window_with_fun,
        # ширина кнопки / button width
        width = 300,
        # висота кнопки / button height
        height = 90
    )
    # задаємо стилі для кнопки / setting styles for the button
    fourth_fun_button.configure(
        # задаємо колір фону / setting the background color
        bg_color = background,
        # колір самої кнопки / button color
        fg_color = frame_background,
        # внутрішній текст кнопки / button text
        text = '',
        # колір при наведенні на кнопку / hover color for the button
        hover_color = button_hover_color,
        # зкруглюємо угли / rounding the corners
        corner_radius = 10,
        # колір тексту кнопки / button text color
        text_color = text_color,
        # шрифт тексту кнопки / button text font
        font = ("Roboto Slab", 20),
        # відцентрування тексту кнопки / button text alignment
        anchor = "center",
        # функція, яка визивається при натисканні на кнопку / function called when the button is pressed
        command = fourth_fn_on,
        # зображення для кнопки / image for the button
        image = image_gr_3
    )

    fifth_fun_button = ctk.CTkButton(
        master = window_with_fun,
        width = 300,
        height = 90
    )
    # задаємо стилі для кнопки / set styles for the button
    fifth_fun_button.configure(
        bg_color = background,
        fg_color = frame_background,
        text = '',
        hover_color = button_hover_color,
        corner_radius = 10,
        text_color = text_color,
        font = ("Roboto Slab", 20),
        anchor = "center",
        command = fifth_fn_on,
        # зображення для кнопки / image for the button
        image = image_gr_5
    )

    sixth_fun_button = ctk.CTkButton(
        master = window_with_fun,
        width = 300,
        height = 90
    )
    # задаємо стилі для кнопки / set styles for the button
    sixth_fun_button.configure(
        bg_color = background,
        fg_color = frame_background,
        text = '',
        hover_color = button_hover_color,
        corner_radius = 10,
        text_color = text_color,
        font = ("Roboto Slab", 20),
        anchor = "center",
        command = sixth_fn_on,
        # зображення для кнопки / image for the button
        image = image_gr_6
    )

    seventh_fun_button = ctk.CTkButton(
        master = window_with_fun,
        width = 300,
        height = 90
    )
    # задаємо стилі для кнопки / set styles for the button
    seventh_fun_button.configure(
        bg_color = background,
        fg_color = frame_background,
        text = '',
        hover_color = button_hover_color,
        corner_radius = 10,
        text_color = text_color,
        font = ("Roboto Slab", 20),
        anchor = "center",
        command = seventh_fn_on,
        # зображення для кнопки / image for the button
        image = image_gr_7
    )

    # розміщення усіх кнопок на вікні / Placement of all buttons on the window
    # кнопка для функції у = ax³ + bx² + cx + d / Button for the function y = ax³ + bx² + cx + d
    first_fun_button.place(x = 10, y = 10)
    # кнопка для функції y = (x**2 - a)/(x - b) / Button for the function y = (x**2 - a)/(x - b)
    second_fun_button.place(x = 320, y = 10)
    # кнопка для функції y = (x**2-a**2)/x / Button for the function y = (x**2-a**2)/x
    third_fun_button.place(x = 320, y = 110)
    # кнопка для функції у = x/(x**2 + a) / Button for the function y = x/(x**2 + a)
    fourth_fun_button.place(x = 320, y = 210)


    fifth_fun_button.place(x = 10, y = 60)
    sixth_fun_button.place(x = 10, y = 160)
    seventh_fun_button.place(x = 10, y = 260)


# функція для видалення непотрібних елементів з вікна при зміні вибору функції / function to remove unnecessary elements from the window when changing the function selection
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

    fifth_func_l.place_forget()
    fifth_func_up_label.place_forget()
    fifth_func_down_label.place_forget()
    fifth_func_drob_label.place_forget()
    fifth_f_dev_label.place_forget()
    fifth_s_dev_label.place_forget()

    a1_function5.place_forget()
    fifth_func_button.place_forget()

    a2_function5.place_forget()
    first_dev_fifth.place_forget()
    second_dev_fifth.place_forget()

    sixth_func_button.place_forget()
    sixth_f_dev_label.place_forget()
    sixth_func_drob_label.place_forget()
    sixth_func_drob_label_2.place_forget()
    sixth_func_l.place_forget()
    sixth_func_plus.place_forget()
    sixth_s_dev_label.place_forget()
    sixth_first_func_down_label.place_forget()
    sixth_first_func_up_label.place_forget()


    a1_sixth.place_forget()
    a2_sixth.place_forget()

    seventh_func_l.place_forget()
    seventh_func_up_label.place_forget()
    seventh_func_down_label.place_forget()
    seventh_func_drob_label.place_forget()
    seventh_f_dev_label.place_forget()
    seventh_s_dev_label.place_forget()

    first_dev_seventh.place_forget()
    second_dev_seventh.place_forget()
    a1_seventh.place_forget()
    seventh_func_button.place_forget()

# розміщення елементів для першого графіку, у = ax³ + bx² + cx + d / placing elements for the first graph, y = ax³ + bx² + cx + d
def first_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main / removing all unnecessary elements from the main window using the function
    clean_old_gr()
    # розміщуємо на main label "y =" / placing on main label "y ="
    y_1.place(x = 8, y = 168)
    # розміщуємо на main label "y' =" / placing on main label "y' ="
    y_2.place(x = 8, y = 218)
    # розміщуємо на main label "y'' =" / placing on main label "y'' ="
    y_3.place(x = 8, y = 268)

    # розміщуємо на main input для коєфіцієнта a / placing on main input for coefficient a
    a_1.place(x = 35, y = 173)
    # розміщуємо на main input для коєфіцієнта b / placing on main input for coefficient b
    b_1.place(x = 104, y = 173)
    # розміщуємо на main input для коєфіцієнта c / placing on main input for coefficient c
    c_1.place(x = 171, y = 173)
    # розміщуємо на main input для коєфіцієнта d / placing on main input for coefficient d
    d_1.place(x = 231, y = 173)

    # розміщуємо на main input для коєфіцієнта a / placing on main input for coefficient a
    a_2.place(x = 55, y = 223)
    # розміщуємо на main input для коєфіцієнта b / placing on main input for coefficient b
    b_2.place(x = 142, y = 223)
    # розміщуємо на main input для коєфіцієнта c / placing on main input for coefficient c
    c_2.place(x = 204, y = 223)

    # розміщуємо на main input для коєфіцієнта a / placing on main input for coefficient a
    a_3.place(x = 60, y = 273)
    # розміщуємо на main input для коєфіцієнта b / placing on main input for coefficient b
    b_3.place(x = 147, y = 273)

    # розміщуємо на main кнопку для побудови графіку / placing on main button for building the graph
    get_grachic_1.place(x = 298, y = 168)

    # прибираємо лейбл на вікні main "Графік для побудови не обрано!" / removing the label on the main window "Graph for building not selected!"
    func_t_or_f.place_forget()
    # закриваємо вікно з функціями / closing the window with functions
    # window_with_fun.destroy()
   

# розміщення елементів для другого графіку, y = (x**2 - a)/(x - b) / placing elements for the second graph, y = (x**2 - a)/(x - b)
def second_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main / removing all unnecessary elements from the main window using the function
    clean_old_gr()
    # розміщуємо на main label "y =" / placing on main label "y ="
    drob_y.place(x = 8, y = 168)
    # розміщуємо на main label чисельника функції "x**2 - a" / placing on main label numerator of the function "x**2 - a"
    drob_y_ch.place(x = 57, y = 143)
    # розміщуємо на main label з знаком дробу "-------" / placing on main label with the fraction sign "-------"
    drob.place(x = 31, y = 185)
    # розміщуємо на main label значенника функції "x - b" / placing on main label denominator of the function "x - b"
    drob_y_zn.place(x = 56, y = 191)

    # розміщуємо на main input для коєфіцієнта a / placing on main input for coefficient a
    a_drob_1.place(x = 149, y = 151)
    # розміщуємо на main input для коєфіцієнта b / placing on main input for coefficient b
    a_drob_3.place(x = 146, y = 197)

    # розміщуємо на main кнопку для побудови графіку / placing on main button for building the graph
    get_drob_grachic.place(x = 298, y = 168)

    # розміщуємо на main label з похідною y' / placing on main label with the derivative y'
    drob_first_dev_lable.place(x = 8, y = 229)
    # розміщуємо на main label з похідною y'' / placing on main label with the derivative y''
    drob_second_dev_lable.place(x = 8, y = 283)
    # закриваємо вікно з функціями / closing the window with functions
    # window_with_fun.destroy()
   

# розміщення елементів для третього графіку, y = (x**2-a**2)/x / placing elements for the third graph, y = (x**2-a**2)/x
def third_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main / removing all unnecessary elements from the main window using the function
    clean_old_gr()
    # розміщуємо на main label "y =" / placing on main label "y ="
    third_func_l.place(x = 8, y = 168)

    # розміщуємо на main label знаку дробу "------" / placing on main label with the fraction sign "------"
    third_func_drob_label.place(x = 31, y = 185)
    # розміщуємо на main label чисельника функції "x**2 - a**2" / placing on main label numerator of the function "x**2 - a**2"
    third_func_up_label.place(x = 60, y = 143)
    # переміщуємо лейбл чисельнику на передній план / moving the numerator label to the front
    third_func_up_label.lift()
    # розміщуємо на main label значенника функції "x" / placing on main label denominator of the function "x"
    third_func_down_label.place(x = 56, y = 191)

    # розміщуємо на main input для коєфіцієнту a / placing on main input for coefficient a
    a_th_drob.place(x = 137, y = 151)
    # переміщуємо input на передній план / moving the input to the front
    a_th_drob.lift()

    # розміщуємо на main кнопку для побудови графіку / placing on main button for building the graph
    third_func_button.place(x = 298, y = 168)

    # розміщуємо на main label з похідною y' / placing on main label with the derivative y'
    third_f_dev_label.place(x = 8, y = 229)
    # розміщуємо на main label з похідною y'' / placing on main label with the derivative y''
    third_s_dev_label.place(x = 8, y = 283)
    # закриваємо вікно з функціями / closing the window with functions
    # window_with_fun.destroy()
   
# розміщення елементів для четвертого графіку, у = x/(x**2 + a) / placing elements for the fourth graph, y = x/(x**2 + a)
def fourth_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main / removing all unnecessary elements from the main window using the function
    clean_old_gr()
    # розміщуємо на main label "y =" / placing on main label "y ="
    fourth_func_l.place(x = 8, y = 168)
    
    # розміщуємо на main label знаку дробу "------" / placing on main label with the fraction sign "------"
    fourth_func_drob_label.place(x = 31, y = 185)
    # розміщуємо на main label чисельника функції "x" / placing on main label numerator of the function "x"
    fourth_func_up_label.place(x = 57, y = 143)
    # розміщуємо на main / placing on main
    fourth_func_up_label.lift()
    # розміщуємо на main label знаменника функції "x**2 + a" / placing on main label denominator of the function "x**2 + a"
    fourth_func_down_label.place(x = 59, y = 191)

    # розміщуємо на main input для коєфіцієнту a / placing on main input for coefficient a
    a4_drob.place(x = 143, y = 197)

    # розміщуємо на main label з похідною y' / placing on main label with the derivative y'
    fourth_f_dev_label.place(x = 8, y = 229)
    # розміщуємо на main label з похідною y'' / placing on main label with the derivative y''
    fourth_s_dev_label.place(x = 8, y = 283)

    # переміщуємо input коєфіцієнту а чисельнику на передній план / moving input for coefficient a numerator to the front
    a4_drob.lift()
    
    # розміщуємо на main кнопку для побудови графіку / placing on main button for building the graph
    fourth_func_button.place(x = 298, y = 168)
    # закриваємо вікно з функціями / closing the window with functions
    # window_with_fun.destroy()
   

#  на майбутнє розміщення елементів для останніх графіків / placing elements for future graphs
def fifth_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main / removing all unnecessary elements from the main window using the function
    clean_old_gr()
    fifth_func_l.place(x = 8, y = 168)
    fifth_func_up_label.place(x = 47, y = 147)
    fifth_func_down_label.place(x = 47, y = 191)
    fifth_func_drob_label.place(x = 31, y = 185)
    fifth_f_dev_label.place(x = 8, y = 229)
    fifth_s_dev_label .place(x = 8, y = 283)

    a1_function5.place(x = 146, y = 155)
    fifth_func_button.place(x = 298, y = 168)
    a1_function5.lift()

    a2_function5.place(x = 146, y = 197)
    a2_function5.lift()
    # закриваємо вікно з функціями / closing the window with functions
    # window_with_fun.destroy()
   

def sixth_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main / removing all unnecessary elements from the main window using the function
    clean_old_gr()
    sixth_func_button.place(x = 298, y = 168)
    sixth_f_dev_label.place(x = 8, y = 229)
    sixth_func_drob_label.place(x = 40, y = 174)
    sixth_func_drob_label_2.place(x = 122, y = 174)
    sixth_func_l.place(x = 8, y = 162)
    sixth_func_plus.place(x = 100, y = 174)
    sixth_s_dev_label.place(x = 8, y = 283)
    sixth_first_func_down_label.place(x = 42, y = 191)
    sixth_first_func_up_label.place(x = 122, y = 149)


    a1_sixth.place(x = 51, y = 150)
    a2_sixth.place(x = 132, y = 191)
    # закриваємо вікно з функціями / closing the window with functions
    # window_with_fun.destroy()
   

def seventh_fn_on():
    # прибираємо за допомогою функції усі зайві елементи на вікні main / removing all unnecessary elements from the main window using the function
    clean_old_gr()

    seventh_func_l.place(x = 8, y = 168)
    seventh_func_up_label.place(x = 57, y = 143)
    seventh_func_down_label.place(x = 56, y = 191)
    seventh_func_drob_label.place(x = 31, y = 185)
    seventh_f_dev_label.place(x = 8, y = 229)
    seventh_s_dev_label.place(x = 8, y = 283)

    a1_seventh.place(x = 162, y = 150)

    seventh_func_button.place(x = 298, y = 168)
    # закриваємо вікно з функціями / closing the window with functions
    # window_with_fun.destroy()
