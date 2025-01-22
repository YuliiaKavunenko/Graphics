import customtkinter as ctk
# створення титульного вікна програми / creating the title window of the program
intrd_window = ctk.CTk()
# створення головного вікна main / creating the main window main
main = ctk.CTkToplevel(intrd_window)
main.withdraw()  # Скрываем окно
# document_window = ctk.CTk()