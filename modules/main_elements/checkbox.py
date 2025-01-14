import customtkinter as ctk
from .windows import main
from .frame import frame_for_options

# Чекбокси на головному вікні / Checkboxes on the main window
# першій графік у = ax**3 + bx**2 + cx + d / first graph y = ax**3 + bx**2 + cx + d
# створення чекбоксу для побудови або прибирання у' / creating a checkbox for building or removing y'
first_dev = ctk.CTkCheckBox(
    master = frame_for_options,
    checkbox_width = 35,
    checkbox_height = 35
)
# створення чекбоксу для побудови або прибирання у'' / creating a checkbox for building or removing y''
second_dev = ctk.CTkCheckBox(
    master = frame_for_options,
    checkbox_width = 35,
    checkbox_height = 35
)
# другий графік y = (x**2 - a)/(x - b) / second graph y = (x**2 - a)/(x - b)
# створення чекбоксу для побудови або прибирання у' / creating a checkbox for building or removing y'
first_dev_fdrob = ctk.CTkCheckBox(
    master = frame_for_options,
    checkbox_width = 35,
    checkbox_height = 35
)
# створення чекбоксу для побудови або прибирання у'' / creating a checkbox for building or removing y''
second_dev_fdrob = ctk.CTkCheckBox(
    master = frame_for_options,
    checkbox_width = 35,
    checkbox_height = 35
)
# третій графік y = (x**2 - a)/x / third graph y = (x**2 - a)/x
# створення чекбоксу для побудови або прибирання у' / creating a checkbox for building or removing y'
first_dev_sdrob = ctk.CTkCheckBox(
    master = frame_for_options,
    checkbox_width = 35,
    checkbox_height = 35
)
# створення чекбоксу для побудови або прибирання у'' / creating a checkbox for building or removing y''
second_dev_sdrob = ctk.CTkCheckBox(
    master = frame_for_options,
    checkbox_width = 35,
    checkbox_height = 35
)
# четвертий графік y = x/(x**2 + a) / fourth graph y = x/(x**2 + a)
# створення чекбоксу для побудови або прибирання у' / creating a checkbox for building or removing y'
first_dev_fourth = ctk.CTkCheckBox(
    master = frame_for_options,
    checkbox_width = 35,
    checkbox_height = 35
)
# створення чекбоксу для побудови або прибирання у'' / creating a checkbox for building or removing y''
second_dev_fourth = ctk.CTkCheckBox(
    master = frame_for_options,
    checkbox_width = 35,
    checkbox_height = 35
)
# п'ятий графік y = (x**2 + a)/(x**2 - a) / fifth graph y = (x**2 + a)/(x**2 - a)
# створення чекбоксу для побудови або прибирання у' / creating a checkbox for building or removing y'
first_dev_fifth = ctk.CTkCheckBox(
    master = frame_for_options,
    checkbox_width = 35,
    checkbox_height = 35
)
# створення чекбоксу для побудови або прибирання у'' / creating a checkbox for building or removing y''
second_dev_fifth = ctk.CTkCheckBox(
    master = frame_for_options,
    checkbox_width = 35,
    checkbox_height = 35
)
# шостий графік y = a/x**2 + x/a / sixth graph y = a/x**2 + x/a
# створення чекбоксу для побудови або прибирання у' / creating a checkbox for building or removing y'
first_dev_sixth = ctk.CTkCheckBox(
    master = frame_for_options,
    checkbox_width = 35,
    checkbox_height = 35
)
# створення чекбоксу для побудови або прибирання у'' / creating a checkbox for building or removing y''
second_dev_sixth = ctk.CTkCheckBox(
    master = frame_for_options,
    checkbox_width = 35,
    checkbox_height = 35
)