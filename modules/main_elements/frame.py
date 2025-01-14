import customtkinter as ctk
from .windows import main

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

