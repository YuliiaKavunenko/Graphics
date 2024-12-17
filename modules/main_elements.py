'''
Файл для створення головних елементів на вікні /
'''
# імпортуємо модуль customtkinter для створення елементів для додатку / import the customtkinter module for creating elements for application
import customtkinter as ctk
# імпортуємо модуль plot з pyplot для роботи з графіками / import the plot module from pyplot to work with graphs
import matplotlib.pyplot as plot
# імпортуємо модуль для відображення графіків у вікні Tkinter / Importing module for displaying graphs in the Tkinter window
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# створення головного вікна main / creating the main window main
main = ctk.CTk()
# створення титульного вікна програми / creating the title window of the program
intrd_window = ctk.CTk()

# створення фрейму на головному вікні для роботи і побудови функцій / creating a frame on the main window for working and building functions
frame_first = ctk.CTkFrame(
    master = main,
    width = 343,
    height = 345
)
# створення фрейму на головному вікні для позначення відображення і не скриття похідних (checkbox) / creating a frame on the main window for marking the display and not hiding derivatives (checkbox)
frame_for_options = ctk.CTkFrame(
    master = main,
    width = 360,
    height = 345
)
# створення фрейму на головному вікні для виведення дослідження функцій / creating a frame on the main window for outputting function research
frame_exploration = ctk.CTkFrame(
    master = main,
    width = 710,
    height = 420
)

# кнопка на головному вікні для отримання даних який графік малювати і досліджувати / button on the main window to get data on which graph to draw and research
button_get = ctk.CTkButton(
    master=main,
    width= 40,
    height=40
)
# input на головному вікні для введення любих графіків / input on the main window for entering any graphs
input_graphic = ctk.CTkEntry(
    master=main,
    width=230,
    height=40
)
# фрейм на головному вікні для вибору базових функцій, прив'язаний до input_graphic / frame on the main window for selecting basic functions, linked to input_graphic
frame_menu = ctk.CTkScrollableFrame(
    master = main,
    width = 205,
    height = 80,
    orientation="vertical"
)

# створення фігури і осей ох, оу / creating the figure and axes ox, oy
fig, ax = plot.subplots(figsize=(6, 6), facecolor='white')
# Створення холста на головному вікні для розміщення побудови графіків / creating the canvas on the main window for displaying the graphs
canvas = FigureCanvasTkAgg(figure = fig, master=main)
# для першого графіку y = ax**3 + bx**2 + cx + d
# лейбл на головному вікні "y =" для введення різних графіків / label on the main window "y =" for entering different graphs
label_y = ctk.CTkLabel(
    master = main,
    width = 22,
    height = 40,
    text = 'y ='
)
# створення лейблу на головному вікні для першого нашого графіку функції / creating a label on the main window for our first function graph
y_1 = ctk.CTkLabel(
    master = main,
    width = 325,
    height = 40,
    text = 'y =          х³ +          x² +          x +'
)
# створення лейблу на головному вікні для y' похідної першого нашого графіку функції / creating a label on the main window for the y' derivative of our first function graph
y_2 = ctk.CTkLabel(
    master = main,
    width = 325,
    height = 40,
    text = "y’ = 3*          x² + 2*          x +"
)
# створення лейблу на головному вікні для y'' похідної першого нашого графіку функції / creating a label on the main window for the y'' derivative of our first function graph
y_3 = ctk.CTkLabel(
    master = main,
    width = 325,
    height = 40,
    text = "y'' = 6*          *x + 2*           "
)
# створення input на головному вікні для введення коєфіцієнта "а" для першого графіку функції / creating input on the main window for entering coefficient "a" for the first function graph
a_1 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
# створення input на головному вікні для введення коєфіцієнта "b" для першого графіку функції / creating input on the main window for entering coefficient "b" for the first function graph
b_1 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
# створення input на головному вікні для введення коєфіцієнта "c" для першого графіку функції / creating input on the main window for entering coefficient "c" for the first function graph
c_1 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
# створення input на головному вікні для введення коєфіцієнта "d" для першого графіку функції / creating input on the main window for entering coefficient "d" for the first function graph
d_1 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
# створення input на головному вікні для заповнення коєфіцієнта "а" для y' першого графіку функції / creating input on the main window for entering coefficient "a" for the y' of the first function graph
a_2 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
# створення input на головному вікні для заповнення коєфіцієнта "b" для y' першого графіку функції / creating input on the main window for entering coefficient "b" for the y' of the first function graph
b_2 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
# створення input на головному вікні для заповнення коєфіцієнта "c" для y' першого графіку функції / creating input on the main window for entering coefficient "c" for the y' of the first function graph
c_2 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
# створення input на головному вікні для заповнення коєфіцієнта "a" для y'' першого графіку функції / creating input on the main window for entering coefficient "a" for the y'' of the first function graph
a_3 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
# створення input на головному вікні для заповнення коєфіцієнта "b" для y'' першого графіку функції / creating input on the main window for entering coefficient "b" for the y'' of the first function graph
b_3 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
# створення кнопки на головному вікні для побудови і дослідження першого графіку / creating a button on the main window for building and researching the first graph
get_grachic_1 = ctk.CTkButton(
    master = main,
    width = 40,
    height = 40
)
# створення кнопки на головному вікні для очищення ДСК / creating a button on the main window for clearing the system
clean_graphic = ctk.CTkButton(
    master = main,
    width = 85,
    height = 35
)
# створення лейблу на головному вікні для підпису зони дослідження графіку / creating a label on the main window to mark the graph research area
l_exploration = ctk.CTkLabel(
    master = main,
    width = 220,
    height = 26
)
# створення лейблу на головному вікні для відображення даних про інтервали спадання/зростання / creating a label on the main window for displaying data on decreasing/increasing intervals
interval_label = ctk.CTkLabel(
    master = main,
    width = 250,
    height = 35
)
# створення лейблу на головному вікні для відображення даних про область визначення функції / creating a label on the main window for displaying data on the domain of the function
scope_label = ctk.CTkLabel(
    master = main,
    width = 250,
    height = 35
)
# створення лейблу для відображення чисельника функції у = (x**2 - a)/(x - b) / creating a label for displaying the numerator of the function y = (x**2 - a)/(x - b)
drob_y_ch = ctk.CTkLabel(
    master = main,
    width = 160,
    height = 45,
    text = '      х²  -          '
)
# створення лейблу для відображення знаменника функції у = (x**2 - a)/(x - b) / creating a label for displaying the denominator of the function y = (x**2 - a)/(x - b)
drob_y_zn = ctk.CTkLabel(
    master = main,
    width = 160,
    height = 45,
    text = 'х -'
)
# створення лейблу для відображення "у = " функції у = (x**2 - a)/(x - b) / creating a label for displaying "y =" of the function y = (x**2 - a)/(x - b)
drob_y = ctk.CTkLabel(
    master = main,
    width = 23,
    height = 40,
    text = 'y ='
)
# створення лейблу для відображення дробового знаку функції у = (x**2 - a)/(x - b) / creating a label for displaying the fraction sign of the function y = (x**2 - a)/(x - b)
drob = ctk.CTkLabel(
    master = main,
    width = 209,
    height = 5,
    text = '————————————'
)
# створення input для введення коєфіцієнта "а" функції у = (x**2 - a)/(x - b) / creating input for entering coefficient "a" of the function y = (x**2 - a)/(x - b)
a_drob_1 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
# створення input для введення коєфіцієнта "b" функції у = (x**2 - a)/(x - b) / creating input for entering coefficient "b" of the function y = (x**2 - a)/(x - b)
a_drob_3 = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
# створення кнопки для побудови і дослідження графіку функції у = (x**2 - a)/(x - b) / creating a button for building and researching the graph of the function y = (x**2 - a)/(x - b)
get_drob_grachic = ctk.CTkButton(
    master = main,
    width = 40,
    height = 40
)
# створення лейблу для відображення похідної у' функції у = (x**2 - a)/(x - b) / creating a label for displaying the derivative y' of the function y = (x**2 - a)/(x - b)
drob_first_dev_lable = ctk.CTkLabel(
    master = main,
    width = 275,
    height = 40
)
# створення лейблу для відображення похідної у'' функції у = (x**2 - a)/(x - b) / creating a label for displaying the derivative y'' of the function y = (x**2 - a)/(x - b)
drob_second_dev_lable = ctk.CTkLabel(
    master = main,
    width = 275,
    height = 40
)
# створення лейблу для відображення локального макс. і мін. функції / creating a label for displaying the local max and min of the function
local_max_min_label = ctk.CTkLabel(
    master = main,
    width = 350,
    height = 35
)
# створення лейблу для відображення макс. і мін. графіку функції / creating a label for displaying the max and min of the graph function
zn_function_label = ctk.CTkLabel(
    master = main,
    width = 350,
    height = 35
)
# створення лейблу для відображення точок 0х і 0у функції / creating a label for displaying the points 0x and 0y of the function
points_ox_oy_label = ctk.CTkLabel(
    master = main,
    width = 350,
    height = 35
)
# створення лейблу для відображення нулів функції / creating a label for displaying the zeros of the function
points_zero_label = ctk.CTkLabel(
    master = main,
    width = 350,
    height = 35
)
# створення лейблу для відображення парна чи непарна функція / creating a label for displaying whether the function is even or odd
even_or_odd_func_l = ctk.CTkLabel(
    master = main,
    width = 250,
    height = 35
)
# створення лейблу для відображення інтервалів знакосталості функції / creating a label for displaying the intervals of constancy of the function
intervals_identity_l = ctk.CTkLabel(
    master = main,
    width = 300,
    height = 35
) 
# елементи для функції y = (x**2 - a**2)/x / elements for the function y = (x**2 - a**2)/x
# створення лейблу для відображення "у = " функції y = (x**2 - a**2)/x / creating a label for displaying "y =" of the function y = (x**2 - a**2)/x
third_func_l = ctk.CTkLabel(
    master = main,
    width = 23,
    height = 40,
    text = 'y ='
)
# створення лейблу для відображення чисельнику функції y = (x**2 - a**2)/x / creating a label for displaying the numerator of the function y = (x**2 - a**2)/x
third_func_up_label = ctk.CTkLabel(
    master = main,
    width = 160,
    height = 43
)
# створення лейблу для відображення знаменнику функції y = (x**2 - a**2)/x / creating a label for displaying the denominator of the function y = (x**2 - a**2)/x
third_func_down_label = ctk.CTkLabel(
    master = main,
    width = 160,
    height = 43
)
# створення лейблу для відображення дробового знаку функції y = (x**2 - a**2)/x / creating a label for displaying the fraction sign of the function y = (x**2 - a**2)/x
third_func_drob_label = ctk.CTkLabel(
    master = main,
    width = 209,
    height = 2,
    text = '————————————'
)
# створення лейблу для відображення похідної у' функції y = (x**2 - a**2)/x / creating a label for displaying the derivative y' of the function y = (x**2 - a**2)/x
third_f_dev_label = ctk.CTkLabel(
    master = main,
    width = 275,
    height = 40
)
# створення лейблу для відображення похідної у'' функції y = (x**2 - a**2)/x / creating a label for displaying the derivative y'' of the function y = (x**2 - a**2)/x
third_s_dev_label = ctk.CTkLabel(
    master = main,
    width = 275,
    height = 40
)
# створення кнопки для побудови і дослідження графіку функції y = (x**2 - a**2)/x / creating a button for building and researching the graph of the function y = (x**2 - a**2)/x
third_func_button = ctk.CTkButton(
    master = main,
    width = 40,
    height = 40
)
# створення input для введення коєфіцієнта "а" функції y = (x**2 - a**2)/x / creating input for entering coefficient "a" of the function y = (x**2 - a**2)/x
a_th_drob = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)

# Чекбокси на головному вікні / Checkboxes on the main window
# першій графік у = ax**3 + bx**2 + cx + d / first graph y = ax**3 + bx**2 + cx + d
# створення чекбоксу для побудови або прибирання у' / creating a checkbox for building or removing y'
first_dev = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
# створення чекбоксу для побудови або прибирання у'' / creating a checkbox for building or removing y''
second_dev = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
# другий графік y = (x**2 - a)/(x - b) / second graph y = (x**2 - a)/(x - b)
# створення чекбоксу для побудови або прибирання у' / creating a checkbox for building or removing y'
first_dev_fdrob = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
# створення чекбоксу для побудови або прибирання у'' / creating a checkbox for building or removing y''
second_dev_fdrob = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
# третій графік y = (x**2 - a)/x / third graph y = (x**2 - a)/x
# створення чекбоксу для побудови або прибирання у' / creating a checkbox for building or removing y'
first_dev_sdrob = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
# створення чекбоксу для побудови або прибирання у'' / creating a checkbox for building or removing y''
second_dev_sdrob = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
# четвертий графік y = x/(x**2 + a) / fourth graph y = x/(x**2 + a)
# створення чекбоксу для побудови або прибирання у' / creating a checkbox for building or removing y'
first_dev_fourth = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
# створення чекбоксу для побудови або прибирання у'' / creating a checkbox for building or removing y''
second_dev_fourth = ctk.CTkCheckBox(
    master = main,
    checkbox_width = 35,
    checkbox_height = 35
)
# створення лейблів для позначення кольору функції / creating labels for denoting the color of the function
# базові функції або свого введення - фіолетовий / basic functions or custom input - purple
purple_gr = ctk.CTkLabel(
    master = main,
    height = 40,
    width = 22,
    anchor = "center",
    text = "●"
)
# основна вибрана функція / main selected function
red_gr = ctk.CTkLabel(
    master = main,
    height = 40,
    width = 22,
    anchor = "center",
    text = "●"
)
# похідна функції у'/ derivative of the function y'
green_gr = ctk.CTkLabel(
    master = main,
    height = 40,
    width = 22,
    anchor = "center",
    text = "●"
)
# похідна функції y'' / derivative of the function y''
blue_gr = ctk.CTkLabel(
    master = main,
    height = 40,
    width = 22,
    anchor = "center",
    text = "●"
)
# створення лейблу для відображення чи обрано графік функції для побудови чи ні / creating a label to display whether the function graph is selected for building or not
func_t_or_f = ctk.CTkLabel(
    master = main,
    height = 26,
    width = 328,
    anchor = "center",
    text = "Графік для побудови не обрано!"
)
# створення кнопки для відкриття вікна з вибором функцій / creating a button to open the window for selecting functions
choose_gr = ctk.CTkButton(
    master=main,
    width= 327,
    height = 40
)
# елементи для четвертої функції y = x/(x**2 + a) / elements for the fourth function y = x/(x**2 + a)
# створення input для введення коєфіцієнту "a" функції y = x/(x**2 + a) / creating input for entering coefficient "a" of the function y = x/(x**2 + a)
a4_drob = ctk.CTkEntry(
    master=main,
    width = 30,
    height = 30
)
# створення лейблу для відображення "у = " функції y = x/(x**2 + a) / creating a label for displaying "y =" of the function y = x/(x**2 + a)
fourth_func_l = ctk.CTkLabel(
    master = main,
    width = 23,
    height = 40,
    text = 'y ='
)
# створення лейблу для відображення чисельнику функції y = x/(x**2 + a) / creating a label for displaying the numerator of the function y = x/(x**2 + a)
fourth_func_up_label = ctk.CTkLabel(
    master = main,
    width = 160,
    height = 43
)
# створення лейблу для відображення знаменнику функції y = x/(x**2 + a) / creating a label for displaying the denominator of the function y = x/(x**2 + a)
fourth_func_down_label = ctk.CTkLabel(
    master = main,
    width = 160,
    height = 43
)
# створення лейблу для відображення дробового знаку функції y = x/(x**2 + a) / creating a label for displaying the fraction sign of the function y = x/(x**2 + a)
fourth_func_drob_label = ctk.CTkLabel(
    master = main,
    width = 209,
    height = 2,
    text = '————————————'
)
# створення лейблу для відображення похідної y' функції y = x/(x**2 + a) / creating a label for displaying the derivative y' of the function y = x/(x**2 + a)
fourth_f_dev_label = ctk.CTkLabel(
    master = main,
    width = 275,
    height = 40
)
# створення лейблу для відображення похіднох y'' функції y = x/(x**2 + a) / creating a label for displaying the derivative y'' of the function y = x/(x**2 + a)
fourth_s_dev_label = ctk.CTkLabel(
    master = main,
    width = 275,
    height = 40
)
# створення кнопки для побудови і дослідження функції y = x/(x**2 + a) / creating a button for building and researching the function y = x/(x**2 + a)
fourth_func_button = ctk.CTkButton(
    master = main,
    width = 40,
    height = 40
)
# створення лейблу для відображення перегину опуклості функції / creating a label for displaying the inflection points of the function
inflection_points_label = ctk.CTkLabel(
    master = main,
    width = 300,
    height = 35
)
# створення лейблу для відображення інтервалів опуклості функції / creating a label for displaying the intervals of convexity of the function
convexity_intervals_label = ctk.CTkLabel(
    master = main,
    width = 300,
    height = 35
)
# створення лейблу для відображення похілої асимптоти функції / creating a label for displaying the oblique asymptote of the function
slope_asymptote = ctk.CTkLabel(
    master = main,
    width = 300,
    height = 35
)
# створення лейблу для відображення поточного головного графіку функції / creating a label for displaying the current main graph of the function
main_graphic_label = ctk.CTkLabel(
    master = main,
    width = 300,
    height = 35
)