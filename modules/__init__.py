''' 
Ініціалізація усіх файлів до пакету. / Initialization of all files to the package. 
'''
from .variables_constants import *
# імпортуємо функцію introduction з файлу introduction_window для запуску титульного вікна / import the introduction function from introduction_window to run the title window
from .introduction_window import introduction
# імпортуємо з main_window функцію run_main для можливості запуску головного додатку / import the run_main function from main_window to be able to run the main application
from .main_window import run_main, on_close
# імпортуємо вікно документації для його роботи і відображення під час використання проєкту/
from .document_window import *
# імпортуємо з plotting усі функції для кнопок або чекбоксів для подальшого використання / import all functions for buttons or checkboxes from elements_functions for further use
from .plotting import *
# імпортуємо з data_calculation усі функції для виконання дослідження графіків функцій /
from .data_calculation import *
# імпортуємо усі зміни стилів для елементів з файлу style / import all style changes for elements from the style file
from .style import *
# імпортуємо функцію functions_window з файлу window_with_fun для запуску вікна для вибору функцій / import the functions_window function from window_with_fun to run the function selection window
from .window_with_fun import functions_window, clean_old_gr
# імпортуємо вікно помилки для його подальшого відображення при необхідності /
from .error_window import show_error_window
