import customtkinter as ctk
from .windows import main
from .frame import frame_first, frame_exploration, frame_for_options

# для першого графіку y = ax**3 + bx**2 + cx + d
# лейбл на головному вікні "y =" для введення різних графіків / label on the main window "y =" for entering different graphs
label_y = ctk.CTkLabel(
    master = frame_first,
    width = 22,
    height = 40,
    text = 'y ='
)
# створення лейблу на головному вікні для першого нашого графіку функції / creating a label on the main window for our first function graph
y_1 = ctk.CTkLabel(
    master = frame_first,
    width = 285,
    height = 40,
    text = 'y =           х³ +          x² +          x +  '
)
# створення лейблу на головному вікні для y' похідної першого нашого графіку функції / creating a label on the main window for the y' derivative of our first function graph
y_2 = ctk.CTkLabel(
    master = frame_first,
    width = 325,
    height = 40,
    text = "y' = 3*          x² + 2*          x +"
)
# створення лейблу на головному вікні для y'' похідної першого нашого графіку функції / creating a label on the main window for the y'' derivative of our first function graph
y_3 = ctk.CTkLabel(
    master = frame_first,
    width = 325,
    height = 40,
    text = "y'' = 6*          *x + 2*           "
)
# створення лейблу на головному вікні для підпису зони дослідження графіку / creating a label on the main window to mark the graph research area
l_exploration = ctk.CTkLabel(
    master = frame_exploration,
    width = 220,
    height = 26
)
# створення лейблу на головному вікні для відображення даних про інтервали спадання/зростання / creating a label on the main window for displaying data on decreasing/increasing intervals
interval_label = ctk.CTkLabel(
    master = frame_exploration,
    width = 250,
    height = 35
)
# створення лейблу на головному вікні для відображення даних про область визначення функції / creating a label on the main window for displaying data on the domain of the function
scope_label = ctk.CTkLabel(
    master = frame_exploration,
    width = 250,
    height = 35
)
# створення лейблу для відображення чисельника функції у = (x**2 - a)/(x - b) / creating a label for displaying the numerator of the function y = (x**2 - a)/(x - b)
drob_y_ch = ctk.CTkLabel(
    master = frame_first,
    width = 160,
    height = 45,
    text = '      х²  -          '
)
# створення лейблу для відображення знаменника функції у = (x**2 - a)/(x - b) / creating a label for displaying the denominator of the function y = (x**2 - a)/(x - b)
drob_y_zn = ctk.CTkLabel(
    master = frame_first,
    width = 160,
    height = 45,
    text = 'x -  '
)
# створення лейблу для відображення "у = " функції у = (x**2 - a)/(x - b) / creating a label for displaying "y =" of the function y = (x**2 - a)/(x - b)
drob_y = ctk.CTkLabel(
    master = frame_first,
    width = 23,
    height = 40,
    text = 'y ='
)
# створення лейблу для відображення дробового знаку функції у = (x**2 - a)/(x - b) / creating a label for displaying the fraction sign of the function y = (x**2 - a)/(x - b)
drob = ctk.CTkLabel(
    master = frame_first,
    width = 209,
    height = 5,
    text = '————————————'
)
# створення лейблу для відображення похідної у' функції у = (x**2 - a)/(x - b) / creating a label for displaying the derivative y' of the function y = (x**2 - a)/(x - b)
drob_first_dev_lable = ctk.CTkLabel(
    master = frame_first,
    width = 275,
    height = 40
)
# створення лейблу для відображення похідної у'' функції у = (x**2 - a)/(x - b) / creating a label for displaying the derivative y'' of the function y = (x**2 - a)/(x - b)
drob_second_dev_lable = ctk.CTkLabel(
    master = frame_first,
    width = 275,
    height = 40
)
# створення лейблу для відображення локального макс. і мін. функції / creating a label for displaying the local max and min of the function
local_max_min_label = ctk.CTkLabel(
    master = frame_exploration,
    width = 350,
    height = 35
)
# створення лейблу для відображення макс. і мін. графіку функції / creating a label for displaying the max and min of the graph function
zn_function_label = ctk.CTkLabel(
    master = frame_exploration,
    width = 350,
    height = 35
)
# створення лейблу для відображення точок 0х і 0у функції / creating a label for displaying the points 0x and 0y of the function
points_ox_oy_label = ctk.CTkLabel(
    master = frame_exploration,
    width = 350,
    height = 35
)
# створення лейблу для відображення нулів функції / creating a label for displaying the zeros of the function
points_zero_label = ctk.CTkLabel(
    master = frame_exploration,
    width = 300,
    height = 35
)
# створення лейблу для відображення парна чи непарна функція / creating a label for displaying whether the function is even or odd
even_or_odd_func_l = ctk.CTkLabel(
    master = frame_exploration,
    width = 250,
    height = 35
)
# створення лейблу для відображення інтервалів знакосталості функції / creating a label for displaying the intervals of constancy of the function
intervals_identity_l = ctk.CTkLabel(
    master = frame_exploration,
    width = 300,
    height = 35
) 
# елементи для функції y = (x**2 - a**2)/x / elements for the function y = (x**2 - a**2)/x
# створення лейблу для відображення "у = " функції y = (x**2 - a**2)/x / creating a label for displaying "y =" of the function y = (x**2 - a**2)/x
third_func_l = ctk.CTkLabel(
    master = frame_first,
    width = 23,
    height = 40,
    text = 'y ='
)
# створення лейблу для відображення чисельнику функції y = (x**2 - a**2)/x / creating a label for displaying the numerator of the function y = (x**2 - a**2)/x
third_func_up_label = ctk.CTkLabel(
    master = frame_first,
    width = 160,
    height = 43
)
# створення лейблу для відображення знаменнику функції y = (x**2 - a**2)/x / creating a label for displaying the denominator of the function y = (x**2 - a**2)/x
third_func_down_label = ctk.CTkLabel(
    master = frame_first,
    width = 160,
    height = 43
)
# створення лейблу для відображення дробового знаку функції y = (x**2 - a**2)/x / creating a label for displaying the fraction sign of the function y = (x**2 - a**2)/x
third_func_drob_label = ctk.CTkLabel(
    master = frame_first,
    width = 209,
    height = 2,
    text = '————————————'
)
# створення лейблу для відображення похідної у' функції y = (x**2 - a**2)/x / creating a label for displaying the derivative y' of the function y = (x**2 - a**2)/x
third_f_dev_label = ctk.CTkLabel(
    master = frame_first,
    width = 275,
    height = 40
)
# створення лейблу для відображення похідної у'' функції y = (x**2 - a**2)/x / creating a label for displaying the derivative y'' of the function y = (x**2 - a**2)/x
third_s_dev_label = ctk.CTkLabel(
    master = frame_first,
    width = 275,
    height = 40
)
# створення лейблів для позначення кольору функції / creating labels for denoting the color of the function
# базові функції або свого введення - фіолетовий / basic functions or custom input - orange
orange_gr = ctk.CTkLabel(
    master = frame_first,
    height = 40,
    width = 22,
    anchor = "center",
    text = "●"
)
# основна вибрана функція / main selected function
red_gr = ctk.CTkLabel(
    master = frame_for_options,
    height = 40,
    width = 22,
    anchor = "center",
    text = "●"
)
# похідна функції у'/ derivative of the function y'
green_gr = ctk.CTkLabel(
    master = frame_for_options,
    height = 40,
    width = 22,
    anchor = "center",
    text = "●"
)
# похідна функції y'' / derivative of the function y''
blue_gr = ctk.CTkLabel(
    master = frame_for_options,
    height = 40,
    width = 22,
    anchor = "center",
    text = "●"
)
# створення лейблу для відображення чи обрано графік функції для побудови чи ні / creating a label to display whether the function graph is selected for building or not
func_t_or_f = ctk.CTkLabel(
    master = frame_first,
    height = 26,
    width = 328,
    anchor = "center",
    text = "Графік для побудови не обрано!"
)
# створення лейблу для відображення "у = " функції y = x/(x**2 + a) / creating a label for displaying "y =" of the function y = x/(x**2 + a)
fourth_func_l = ctk.CTkLabel(
    master = frame_first,
    width = 23,
    height = 40,
    text = 'y ='
)
# створення лейблу для відображення чисельнику функції y = x/(x**2 + a) / creating a label for displaying the numerator of the function y = x/(x**2 + a)
fourth_func_up_label = ctk.CTkLabel(
    master = frame_first,
    width = 160,
    height = 43
)
# створення лейблу для відображення знаменнику функції y = x/(x**2 + a) / creating a label for displaying the denominator of the function y = x/(x**2 + a)
fourth_func_down_label = ctk.CTkLabel(
    master = frame_first,
    width = 160,
    height = 43
)
# створення лейблу для відображення дробового знаку функції y = x/(x**2 + a) / creating a label for displaying the fraction sign of the function y = x/(x**2 + a)
fourth_func_drob_label = ctk.CTkLabel(
    master = frame_first,
    width = 209,
    height = 2,
    text = '————————————'
)
# створення лейблу для відображення похідної y' функції y = x/(x**2 + a) / creating a label for displaying the derivative y' of the function y = x/(x**2 + a)
fourth_f_dev_label = ctk.CTkLabel(
    master = frame_first,
    width = 275,
    height = 40
)
# створення лейблу для відображення похіднох y'' функції y = x/(x**2 + a) / creating a label for displaying the derivative y'' of the function y = x/(x**2 + a)
fourth_s_dev_label = ctk.CTkLabel(
    master = frame_first,
    width = 275,
    height = 40
)
# створення лейблу для відображення перегину опуклості функції / creating a label for displaying the inflection points of the function
inflection_points_label = ctk.CTkLabel(
    master = frame_exploration,
    width = 300,
    height = 35
)
# створення лейблу для відображення інтервалів опуклості функції / creating a label for displaying the intervals of convexity of the function
convexity_intervals_label = ctk.CTkLabel(
    master = frame_exploration,
    width = 300,
    height = 35
)
# створення лейблу для відображення похилої асимптоти функції / creating a label for displaying the oblique asymptote of the function
slope_asymptote = ctk.CTkLabel(
    master = frame_exploration,
    width = 300,
    height = 35
)
# створення лейблу для відображення поточного головного графіку функції / creating a label for displaying the current main graph of the function
main_graphic_label = ctk.CTkLabel(
    master = frame_for_options,
    width = 300,
    height = 35
)
# Функція y = (x**2 + a)/(x**2 - a) / Function y = (x**2 + a)/(x**2 - a)
# створення лейблу для відображення "у = " функції y = (x**2 + a)/(x**2 - a) / creating a label for displaying "y =" of the function y = (x**2 + a)/(x**2 - a)
fifth_func_l = ctk.CTkLabel(
    master = frame_first,
    width = 23,
    height = 40,
    text = 'y ='
)
# створення лейблу для відображення чисельника функції y = (x**2 + a)/(x**2 - a) / creating a label for displaying the numerator of the function y = (x**2 + a)/(x**2 - a)
fifth_func_up_label = ctk.CTkLabel(
    master = frame_first,
    width = 160,
    height = 43,
    text = 'х² +'
)
# створення лейблу для відображення знаменника функції y = (x**2 + a)/(x**2 - a) / creating a label for displaying the denominator of the function y = (x**2 + a)/(x**2 - a)
fifth_func_down_label = ctk.CTkLabel(
    master = frame_first,
    width = 160,
    height = 43,
    text = 'х² -'
)
# створення лейблу для відображення дробового знаку функції y = (x**2 + a)/(x**2 - a) / creating a label for displaying the fraction sign of the function y = (x**2 + a)/(x**2 - a)
fifth_func_drob_label = ctk.CTkLabel(
    master = frame_first,
    width = 209,
    height = 2,
    text = '————————————'
)
# створення лейблу для відображення похідної y' функції y = (x**2 + a)/(x**2 - a) / creating a label for displaying the derivative y' of the function y = (x**2 + a)/(x**2 - a)
fifth_f_dev_label = ctk.CTkLabel(
    master = frame_first,
    width = 275,
    height = 40,
    text = "y' = очікування введення даних"
)
# створення лейблу для відображення похідної y'' функції y = (x**2 + a)/(x**2 - a) / creating a label for displaying the derivative y'' of the function y = (x**2 + a)/(x**2 - a)
fifth_s_dev_label = ctk.CTkLabel(
    master = frame_first,
    width = 275,
    height = 40,
    text = "y'' = очікування введення даних"
)
# Функція y = a/x**2 + x/a / Function y = a/x**2 + x/a
# створення лейблу для відображення "у =" шостого графік функції / creating a label for displaying "y =" of the sixth function graph
sixth_func_l = ctk.CTkLabel(
    master = frame_first,
    width = 23,
    height = 40,
    text = 'y ='
)
# створення лейблу для відображення чисельника функції y = a/x**2 + x/a / creating a label for displaying the numerator of the function y = a/x**2 + x/a
sixth_first_func_up_label = ctk.CTkLabel(
    master = frame_first,
    width = 47,
    height = 31
)
# створення лейблу для відображення знаменника функції y = a/x**2 + x/a / creating a label for displaying the denominator of the function y = a/x**2 + x/a
sixth_first_func_down_label = ctk.CTkLabel(
    master = frame_first,
    width = 47,
    height = 31
)
# створення лейблу для відображення дробового знаку №1 функції y = a/x**2 + x/a / creating a label for displaying the fraction sign of the function y = a/x**2 + x/a
sixth_func_drob_label = ctk.CTkLabel(
    master = frame_first,
    width = 49,
    height = 2,
    text = '________'
)
# створення лейблу для відображення дробового знаку №2 функції y = a/x**2 + x/a / creating a label for displaying the fraction sign of the function y = a/x**2 + x/a
sixth_func_drob_label_2 = ctk.CTkLabel(
    master = frame_first,
    width = 49,
    height = 2,
    text = '________'
)
# створення лейблу для відображення похідної y' функції y = a/x**2 + x/a / creating a label for displaying the derivative y' of the function y = a/x**2 + x/a
sixth_f_dev_label = ctk.CTkLabel(
    master = frame_first,
    width = 275,
    height = 40
)
# створення лейблу для відображення похідної y'' функції y = a/x**2 + x/a / creating a label for displaying the derivative y'' of the function y = a/x**2 + x/a
sixth_s_dev_label = ctk.CTkLabel(
    master = frame_first,
    width = 275,
    height = 40
)
# створення лейблу для відображення дробового знаку №2 функції y = a/x**2 + x/a / creating a label for displaying the fraction sign of the function y = a/x**2 + x/a
sixth_func_plus = ctk.CTkLabel(
    master = frame_first,
    width = 11,
    height = 16,
    text = '+'
)
# Функція y = (x**2 + x + a)/x / Function y = (x**2 + x + a)/x
# створення лейблу для відображення "у = " сьомого графік функції / creating a label for displaying "y =" of the seventh function graph
seventh_func_l = ctk.CTkLabel(
    master = frame_first,
    width = 23,
    height = 40,
    text = 'y ='
)
# створення лейблу для відображення чисельника функції y = (x**2 + x + a)/x / creating a label for displaying the numerator of the function y = (x**2 + x + a)/x
seventh_func_up_label = ctk.CTkLabel(
    master = frame_first,
    width = 160,
    height = 43
)
# створення лейблу для відображення знаменника функції y = (x**2 + x + a)/x / creating a label for displaying the denominator of the function y = (x**2 + x + a)/x
seventh_func_down_label = ctk.CTkLabel(
    master = frame_first,
    width = 160,
    height = 43
)
# створення лейблу для відображення дробового знаку функції y = (x**2 + x + a)/x / creating a label for displaying the fraction sign of the function y = (x**2 + x + a)/x
seventh_func_drob_label = ctk.CTkLabel(
    master = frame_first,
    width = 209,
    height = 2,
    text = '————————————'
)
# створення лейблу для відображення похідної y' функції y = (x**2 + x + a)/x / creating a label for displaying the derivative y' of the function y = (x**2 + x + a)/x
seventh_f_dev_label = ctk.CTkLabel(
    master = frame_first,
    width = 275,
    height = 40
)
# створення лейблу для відображення похідної y'' функції y = (x**2 + x + a)/x / creating a label for displaying the derivative y'' of the function y = (x**2 + x + a)/x
seventh_s_dev_label = ctk.CTkLabel(
    master = frame_first,
    width = 275,
    height = 40
)
# створення лейблу для відображення того, що функція є сталою / creating a label for displaying that we have constant function
constant_function_label = ctk.CTkLabel(
    master = frame_for_options,
    height = 52,
    width = 360,
    anchor = "center",
    text = "Функція є сталою. У побудові похідних немає сенсу",
    wraplength = 360
)