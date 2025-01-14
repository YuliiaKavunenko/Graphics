import customtkinter as ctk
from .windows import main

# фрейм на головному вікні для вибору базових функцій, прив'язаний до input_graphic / frame on the main window for selecting basic functions, linked to input_graphic
frame_menu = ctk.CTkScrollableFrame(
    master = main,
    width = 205,
    height = 80,
    orientation="vertical"
)
