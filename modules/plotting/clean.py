from ..main_elements import *
import customtkinter as ctk

# функція для очищення зайвих елементів на ДСК і старих коєфіцієнтів / function to clear unnecessary elements on the coordinate grid and old coefficients
def clean_button():
    from .build_DSK import build_DSK
    ax.clear()  # очищаємо вісь графіка / clearing the graph axis
    red_gr.place_forget()
    green_gr.place_forget()
    blue_gr.place_forget()


    first_dev.deselect()
    second_dev.deselect()
    first_dev_fdrob.deselect()
    second_dev_fdrob.deselect()
    first_dev_sdrob.deselect()
    second_dev_sdrob.deselect()
    first_dev_fourth.deselect()
    second_dev_fourth.deselect()
    first_dev_fifth.deselect()
    second_dev_fifth.deselect()
    first_dev_sixth.deselect()
    second_dev_sixth.deselect()
    first_dev_seventh.deselect()
    second_dev_seventh.deselect()
    base_dev_checkbox1.deselect()
    base_dev_checkbox2.deselect()
    
    a_1.delete(0,"end")  # очищаємо поле для коефіцієнта a / clearing the field for coefficient a
    b_1.delete(0,"end")  # очищаємо поле для коефіцієнта b / clearing the field for coefficient b
    c_1.delete(0,"end")  # очищаємо поле для коефіцієнта c / clearing the field for coefficient c
    d_1.delete(0,"end")  # очищаємо поле для коефіцієнта d / clearing the field for coefficient d

    a_2.delete(0,"end")  # очищаємо поле для коефіцієнта a у' похідної / clearing the field for coefficient a of the second derivative
    b_2.delete(0,"end")  # очищаємо поле для коефіцієнта b у' похідної / clearing the field for coefficient b of the second derivative
    c_2.delete(0,"end")  # очищаємо поле для коефіцієнта c у' похідної / clearing the field for coefficient c of the second derivative

    a_3.delete(0,"end")  # очищаємо поле для коефіцієнта a у'' похідної / clearing the field for coefficient a of the third derivative
    b_3.delete(0,"end")  # очищаємо поле для коефіцієнта b у'' похідної / clearing the field for coefficient b of the third derivative

    a_drob_1.delete(0,"end")  # очищаємо поле для коефіцієнта a дробової функції / clearing the field for coefficient a of the fractional function
    a_drob_3.delete(0,"end")  # очищаємо поле для коефіцієнта b дробової функції / clearing the field for coefficient b of the fractional function

    a_th_drob.delete(0,"end")  # очищаємо поле для коефіцієнта a третьої дробової функції / clearing the field for coefficient a of the third fractional function

    a4_drob.delete(0,"end")  # очищаємо поле для коефіцієнта a четвертої дробової функції / clearing the field for coefficient a of the fourth fractional function

    input_graphic.delete(0,"end")  # очищаємо поле вводу графіка / clearing the graph input field

    local_max_min_label.configure(text = '4) Локальний макс. і мін. функції')  # оновлюємо текст лейблу локальних макс. і мін. / updating the label text for local max. and min.

    even_or_odd_func_l.configure(text = '2) Парна чи непарна ф-ція')  # оновлюємо текст лейблу для парності функції / updating the label text for function parity

    zn_function_label.configure(text = '5) Мін. і макс. значення функції')  # оновлюємо текст лейблу для мін. і макс. значень функції / updating the label text for min. and max. function values

    interval_label.configure(text = '3) Проміжок спадання і зростання функції')  # оновлюємо текст лейблу для інтервалів зростання та спадання функції / updating the label text for intervals of increase and decrease

    scope_label.configure(text = '1) Область визначення функції')  # оновлюємо текст лейблу області визначення функції / updating the label text for the function domain

    drob_first_dev_lable.configure(text = "y' = очікування введення даних")  # очищаємо текст лейблу першої похідної дробової функції / clearing the label text for the first derivative of the fractional function
    drob_second_dev_lable.configure(text = "y'' = очікування введення даних")  # очищаємо текст лейблу другої похідної дробової функції / clearing the label text for the second derivative of the fractional function

    third_f_dev_label.configure(text = "y' = очікування введення даних")  # очищаємо текст лейблу першої похідної третьої функції / clearing the label text for the first derivative of the third function
    third_s_dev_label.configure(text = "y'' = очікування введення даних")  # очищаємо текст лейблу другої похідної третьої функції / clearing the label text for the second derivative of the third function

    fourth_f_dev_label.configure(text = "y' = очікування введення даних")  # очищаємо текст лейблу першої похідної четвертої функції / clearing the label text for the first derivative of the fourth function
    fourth_s_dev_label.configure(text = "y'' = очікування введення даних")  # очищаємо текст лейблу другої похідної четвертої функції / clearing the label text for the second derivative of the fourth function

    points_ox_oy_label.configure(text="6) Точки перетину з осями ох і оу")  # оновлюємо текст лейблу для точок перетину з осями / updating the label text for intersection points with axes

    points_zero_label.configure(text="7) Нулі функції")  # оновлюємо текст лейблу для нулів функції / updating the label text for function zeros

    intervals_identity_l.configure(text = '8) Проміжки знакосталості ф-ції')  # оновлюємо текст лейблу для інтервалів знакосталості / updating the label text for intervals of constancy

    inflection_points_label.configure(text = '9) Точки перегину')  # оновлюємо текст лейблу для точок перегину / updating the label text for inflection points

    convexity_intervals_label.configure(text = '10) Проміжки опуклості')  # оновлюємо текст лейблу для інтервалів опуклості / updating the label text for convexity intervals

    slope_asymptote.configure(text = '11) Похила асимптота')  # оновлюємо текст лейблу для похилої асимптоти / updating the label text for the oblique asymptote

    main_graphic_label.place_forget()  # приховуємо лейбл головного графіка / hiding the main graph label
    a1_function5.delete(0,"end")
    a2_function5.delete(0,"end")
    fifth_f_dev_label.configure(text = "y' = очікування введення даних")  # очищаємо текст лейблу першої похідної п'ятої функції / clearing the label text for the first derivative of the fifth function
    fifth_s_dev_label.configure(text = "y'' = очікування введення даних")  # очищаємо текст лейблу другої похідної п'ятої функції / clearing the label text for the second derivative of the fifth function

    sixth_s_dev_label.configure(text = "y'' = очікування введення даних")  # очищаємо текст лейблу другої похідної шостої функції / clearing the label text for the second derivative of the sixth function
    sixth_f_dev_label.configure(text = "y' = очікування введення даних")  # очищаємо текст лейблу першої похідної шостої функції / clearing the label text for the first derivative of the sixth function

    a1_sixth.delete(0,"end")
    a2_sixth.delete(0,"end")

    first_dev.place_forget()
    second_dev.place_forget()
    first_dev_fdrob.place_forget()
    second_dev_fdrob.place_forget()
    first_dev_sdrob.place_forget()
    second_dev_sdrob.place_forget()
    first_dev_fourth.place_forget()
    second_dev_fourth.place_forget()
    first_dev_fifth.place_forget()
    second_dev_fifth.place_forget()
    first_dev_sixth.place_forget()
    second_dev_sixth.place_forget()
    base_dev_checkbox1.place_forget()
    base_dev_checkbox2.place_forget()


    a1_seventh.delete(0,"end")

    seventh_f_dev_label.configure(text = "y' = очікування введення даних")  # очищаємо текст лейблу першої похідної сьомої функції / clearing the label text for the first derivative of the seventh function
    seventh_s_dev_label.configure(text = "y'' = очікування введення даних")  # очищаємо текст лейблу другої похідної сьомої функції / clearing the label text for the second derivative of the seventh function

    first_dev_seventh.place_forget()
    second_dev_seventh.place_forget()
    constant_function_label.place_forget()
    build_DSK()

def clean_for_functions():

    red_gr.place_forget()
    green_gr.place_forget()
    blue_gr.place_forget()

    base_dev_checkbox1.place_forget()
    base_dev_checkbox2.place_forget()

    first_dev.deselect()
    second_dev.deselect()
    first_dev_fdrob.deselect()
    second_dev_fdrob.deselect()
    first_dev_sdrob.deselect()
    second_dev_sdrob.deselect()
    first_dev_fourth.deselect()
    second_dev_fourth.deselect()
    first_dev_fifth.deselect()
    second_dev_fifth.deselect()
    first_dev_sixth.deselect()
    second_dev_sixth.deselect()
    first_dev_seventh.deselect()
    second_dev_seventh.deselect()

    local_max_min_label.configure(text = '4) Локальний макс. і мін. функції')  # оновлюємо текст лейблу локальних макс. і мін. / updating the label text for local max. and min.

    even_or_odd_func_l.configure(text = '2) Парна чи непарна ф-ція')  # оновлюємо текст лейблу для парності функції / updating the label text for function parity

    zn_function_label.configure(text = '5) Мін. і макс. значення функції')  # оновлюємо текст лейблу для мін. і макс. значень функції / updating the label text for min. and max. function values

    interval_label.configure(text = '3) Проміжок спадання і зростання функції')  # оновлюємо текст лейблу для інтервалів зростання та спадання функції / updating the label text for intervals of increase and decrease

    scope_label.configure(text = '1) Область визначення функції')  # оновлюємо текст лейблу області визначення функції / updating the label text for the function domain

    drob_first_dev_lable.configure(text = "y' = очікування введення даних")  # очищаємо текст лейблу першої похідної дробової функції / clearing the label text for the first derivative of the fractional function
    drob_second_dev_lable.configure(text = "y'' = очікування введення даних")  # очищаємо текст лейблу другої похідної дробової функції / clearing the label text for the second derivative of the fractional function

    third_f_dev_label.configure(text = "y' = очікування введення даних")  # очищаємо текст лейблу першої похідної третьої функції / clearing the label text for the first derivative of the third function
    third_s_dev_label.configure(text = "y'' = очікування введення даних")  # очищаємо текст лейблу другої похідної третьої функції / clearing the label text for the second derivative of the third function

    fourth_f_dev_label.configure(text = "y' = очікування введення даних")  # очищаємо текст лейблу першої похідної четвертої функції / clearing the label text for the first derivative of the fourth function
    fourth_s_dev_label.configure(text = "y'' = очікування введення даних")  # очищаємо текст лейблу другої похідної четвертої функції / clearing the label text for the second derivative of the fourth function

    points_ox_oy_label.configure(text="6) Точки перетину з осями ох і оу")  # оновлюємо текст лейблу для точок перетину з осями / updating the label text for intersection points with axes

    points_zero_label.configure(text="7) Нулі функції")  # оновлюємо текст лейблу для нулів функції / updating the label text for function zeros

    intervals_identity_l.configure(text = '8) Проміжки знакосталості ф-ції')  # оновлюємо текст лейблу для інтервалів знакосталості / updating the label text for intervals of constancy

    inflection_points_label.configure(text = '9) Точки перегину')  # оновлюємо текст лейблу для точок перегину / updating the label text for inflection points

    convexity_intervals_label.configure(text = '10) Проміжки опуклості')  # оновлюємо текст лейблу для інтервалів опуклості / updating the label text for convexity intervals

    slope_asymptote.configure(text = '11) Похила асимптота')  # оновлюємо текст лейблу для похилої асимптоти / updating the label text for the oblique asymptote

    main_graphic_label.place_forget()  # приховуємо лейбл головного графіка / hiding the main graph label
    fifth_f_dev_label.configure(text = "y' = очікування введення даних")  # очищаємо текст лейблу першої похідної п'ятої функції / clearing the label text for the first derivative of the fifth function
    fifth_s_dev_label.configure(text = "y'' = очікування введення даних")  # очищаємо текст лейблу другої похідної п'ятої функції / clearing the label text for the second derivative of the fifth function

    sixth_s_dev_label.configure(text = "y'' = очікування введення даних")  # очищаємо текст лейблу другої похідної шостої функції / clearing the label text for the second derivative of the sixth function
    sixth_f_dev_label.configure(text = "y' = очікування введення даних")  # очищаємо текст лейблу першої похідної шостої функції / clearing the label text for the first derivative of the sixth function

    first_dev.place_forget()
    second_dev.place_forget()
    first_dev_fdrob.place_forget()
    second_dev_fdrob.place_forget()
    first_dev_sdrob.place_forget()
    second_dev_sdrob.place_forget()
    first_dev_fourth.place_forget()
    second_dev_fourth.place_forget()
    first_dev_fifth.place_forget()
    second_dev_fifth.place_forget()
    first_dev_sixth.place_forget()
    second_dev_sixth.place_forget()

    seventh_f_dev_label.configure(text = "y' = очікування введення даних")  # очищаємо текст лейблу першої похідної сьомої функції / clearing the label text for the first derivative of the seventh function
    seventh_s_dev_label.configure(text = "y'' = очікування введення даних")  # очищаємо текст лейблу другої похідної сьомої функції / clearing the label text for the second derivative of the seventh function

    first_dev_seventh.place_forget()
    second_dev_seventh.place_forget()
    constant_function_label.place_forget()

