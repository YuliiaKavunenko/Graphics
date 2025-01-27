# імпортуємо бібліотеку customtkinter для розширених можливостей інтерфейсу користувача / imports the customtkinter library for advanced user interface capabilities
import customtkinter as ctk
# імпортуємо бібліотеку fitz (PyMuPDF) для роботи з PDF-документами / imports the fitz (PyMuPDF) library for working with PDF documents
import fitz
# імпортуємо бібліотеку tkinter для створення графічного інтерфейсу користувача / imports the tkinter library for creating graphical user interfaces
import tkinter as tk
# імпортуємо scrolledtext з tkinter для створення текстових віджетів з прокруткою / imports scrolledtext from tkinter for creating scrolled text widgets
from tkinter import scrolledtext
# імпортуємо Image та ImageTk з бібліотеки PIL для обробки та відображення зображень / imports Image and ImageTk from the PIL library for handling and displaying images
from PIL import Image, ImageTk
# імпортуємо os для роботи з операційною системою, наприклад для перевірки існування файлів / imports os for interacting with the operating system, such as checking for file existence
import os
# кольори для елементів у вікні  / colors for elements in the window
# колір для фону вікна / color for window background
background = "#A76E56"
# колір для фону фреймів / color for frame background
frame_background = "#BA7D65"
# колір для тексту label / color for label text
text_color = "#392D20"
# колір для фону кнопки / color for button background
button_color = "#7B4C39"
# колір для тексту кнопки / color for button text
text_button_color = "#F1D5BA"
# колір для фону input / color for input background
input_color = "#FAF0E6"
# колір для бортиків input / color for input borders
input_border_color = "#EAD1B8"
# колір для внутрішнього тексту input / color for input placeholder text
input_textholder_color = "#CAA37D"
# колір при наведенні на кнопку scroll frame (меню усіх базових функцій) / color when hovering over the scroll frame button (menu of all basic functions)
hover_color_menu = "#F3E4D5"
# колір при наведенні на кнопку / color when hovering over the button
button_hover_color = "#9D6249"
# колір при наведенні на checkbox / color when hovering over the checkbox
checkbox_hover_color = "#EBCDAE"
# шлях до поточної директорії / path to the current directory
PATH = os.path.abspath(os.path.join(__file__, '..'))
# функція для відображення документа / function to display the document
# визначаємо функцію display_document з параметрами master і file_path / defines the function display_document with parameters master and file_path
def display_document(master, file_path, label_starttext, label_text):
    label_starttext.configure(text=label_text)
    # видаляємо всі підлеглі елементи типу ctk.CTkFrame з майстра / destroys all child widgets of type ctk.CTkFrame from the master
    for widget in master.winfo_children():
        if isinstance(widget, ctk.CTkFrame):
            widget.destroy()

    # створюємо новий фрейм ctk.CTkFrame для відображення документу / creates a new frame ctk.CTkFrame for displaying the document
    viewer_frame = ctk.CTkFrame(master=master, width=955, height=780, fg_color=input_color)
    # задаємо розташування фрейму на екрані / places the frame at the specified position on the screen
    viewer_frame.place(x=292, y=94)

    if file_path.endswith('.pdf'):
        # відкриваємо PDF-документ з допомогою fitz / opens the PDF document using fitz
        doc = fitz.open(file_path)
        # створюємо Canvas для відображення PDF-сторінок / creates a Canvas to display PDF pages
        pdf_viewer = tk.Canvas(viewer_frame, width=910, height=800, bg=input_color)
        # розташовуємо Canvas і дозволяємо йому розширюватися / packs the Canvas and allows it to expand
        pdf_viewer.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)

        # створюємо вертикальну прокрутку і прив'язуємо її до Canvas / creates a vertical scrollbar and links it to the Canvas
        scrollbar = tk.Scrollbar(viewer_frame, orient = ctk.VERTICAL, command = pdf_viewer.yview)
        scrollbar.pack(side = ctk.RIGHT, fill = ctk.Y)
        # налаштовуємо Canvas для роботи з прокруткою / configures the Canvas to work with the scrollbar
        pdf_viewer.config(yscrollcommand=scrollbar.set)

        # змінні для загальної висоти, коефіцієнта збільшення і збереження зображень сторінок / variables for total height, zoom factor, and storing page images
        total_height = 0
        zoom_factor = 1.5
        images = []

        # визначаємо функцію для відображення сторінок і використовуємо змінну з зовнішнього контексту / defines a function to render pages using a variable from the outer context
        def render_page(master = master):
            nonlocal total_height

            for page_num in range(len(doc)):
                page = doc[page_num]
                # отримуємо піксельну карту сторінки з заданим коефіцієнтом збільшення / retrieves the pixel map of the page with the specified zoom factor
                pix = page.get_pixmap(matrix=fitz.Matrix(zoom_factor, zoom_factor))
                # конвертуємо піксельну карту в формат ImageTk для відображення / converts the pixel map to ImageTk format for displaying
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
   
                img_tk = ImageTk.PhotoImage(img)
                # розраховуємо горизонтальне зміщення для центрування зображення на Canvas / calculates horizontal offset to center the image on the Canvas
                canvas_width = pdf_viewer.winfo_width()
                x_offset = max((canvas_width - pix.width) // 2, 0)
                # відображаємо зображення на Canvas у відповідному місці / displays the image on the Canvas at the specified location
                pdf_viewer.create_image(x_offset,  total_height,image =  img_tk, anchor = ctk.NW)

                # зберігаємо зображення і оновлюємо загальну висоту / stores the image and updates the total height
                images.append(img_tk)
                total_height += pix.height

            # зберігаємо посилання на зображення для запобігання їх збору сміття / stores image references to prevent garbage collection
            pdf_viewer.config(scrollregion = (0, 0, 955, total_height))
            pdf_viewer.images = images

        # викликаємо render_page через 100 мілісекунд / calls render_page after 100 milliseconds
        master.after(100, render_page)

    else:
        # відкриваємо текстовий файл і читаємо його вміст / opens a text file and reads its contents
        with open(file_path, "r", encoding = "utf-8") as file:
            content = file.read()

        # створюємо текстовий віджет з прокруткою для відображення тексту / creates a scrolled text widget for displaying the text
        text_widget = scrolledtext.ScrolledText(master = viewer_frame, width = 95, height = 35, wrap = ctk.WORD)
        # додаємо текст у віджет, робимо його тільки для читання і розташовуємо на екрані / inserts text into the widget, sets it to read-only, and packs it on the screen
        text_widget.insert(ctk.END, content)
        # робимо текстовий віджет доступним тільки для читання / makes the text widget read-only
        text_widget.configure(state="disabled")
        # додаємо текстовий віджет у фрейм і дозволяємо йому розширюватися у відповідні напрямки / adds the text widget to the frame and allows it to expand in both directions
        text_widget.pack(side=ctk.LEFT, fill = ctk.BOTH, expand = True)


# визначаємо функцію run_document для створення вікна документу / defines the function run_document to create the document window
def run_document():
    from .main_elements import intrd_window
    # створюємо новий екземпляр вікна ctk.CTk / creates a new instance of ctk.CTk window
    document_window = ctk.CTkToplevel(intrd_window)
    # встановлюємо заголовок вікна "Документація" / sets the window title to "Документація"
    document_window.title("Випускна робота. Документація")
    # забороняємо зміну розмірів вікна / disables window resizing
    document_window.resizable(False, False)
    # налаштовуємо колір фону вікна / configures the window background color
    document_window.configure(fg_color = background)
    document_window.grab_set()
    intrd_window.lower()
    # задаємо ширину та висоту вікна / sets the window width and height
    window_width = 1082
    window_height = 780
    # отримуємо ширину та висоту екрану / retrieves the screen width and height
    screen_width = document_window.winfo_screenwidth()
    screen_height = document_window.winfo_screenheight()
    # обчислюємо координати для центрування вікна на екрані / calculates coordinates to center the window on the screen
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    # задаємо геометрію вікна, щоб розташувати його по центру / sets the window geometry to position it at the center
    document_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # створюємо мітку ctk.CTkLabel з текстом "Документація до проєкту" / creates a ctk.CTkLabel with the text "Документація до проєкту"
    label_starttext = ctk.CTkLabel(master = document_window, width = 770, height = 45, text = "", anchor = "center")
    # налаштовуємо властивості мітки, такі як колір фону, шрифт, колір тексту та розташування / configures the label properties such as background color, font, text color, and alignment
    label_starttext.configure(fg_color = background, font = ("Roboto Slab", 24), text_color = text_color, anchor="center")
    # розташовуємо мітку на вказаних координатах / places the label at the specified coordinates
    label_starttext.place(x=305, y=25)

    # створюємо кнопку ctk.CTkButton для читання додатку до проєкту / creates a ctk.CTkButton for reading the project appendix
    button_app = ctk.CTkButton(master = document_window, width = 252, height = 60, text = "Додаток",
                               fg_color = button_color, text_color = text_button_color, hover_color = button_hover_color, font = ("Roboto Slab", 20),
                               command = lambda: display_document(document_window, os.path.join(PATH, "Kursova_robota.pdf"), label_starttext = label_starttext, label_text = "Додаток до проєкту"))
    # розташовуємо кнопку на вказаних координатах / places the button at the specified coordinates
    button_app.place(x = 20, y = 394)

    # створюємо кнопку ctk.CTkButton для читання документації до проєкту / creates a ctk.CTkButton for reading the project documentation
    button_readme = ctk.CTkButton(master = document_window, width = 252, height = 60, text="Документація",
                                  fg_color = button_color, text_color = text_button_color, hover_color = button_hover_color, font = ("Roboto Slab", 20),
                                  command = lambda: display_document(document_window, os.path.join(PATH, "Documentation.pdf"), label_starttext = label_starttext, label_text = "Документація до проєкту"))
    # розташовуємо кнопку на вказаних координатах / places the button at the specified coordinates
    button_readme.place(x = 20, y = 169)

    # створюємо кнопку ctk.CTkButton для читання посібника користувача до проєкту / creates a ctk.CTkButton for reading the project documentation
    button_manual = ctk.CTkButton(master = document_window, width = 252, height = 60, text="Посібник користувача",
                                  fg_color = button_color, text_color = text_button_color, hover_color = button_hover_color, font = ("Roboto Slab", 20),
                                  command = lambda: display_document(document_window, os.path.join(PATH, "user_posibnik.pdf"), label_starttext = label_starttext, label_text = "Посібник користувача"))
    # розташовуємо кнопку на вказаних координатах / places the button at the specified coordinates
    button_manual.place(x = 20, y = 94)

    # створюємо кнопку ctk.CTkButton для читання теоретичної частини з математики / creates a ctk.CTkButton for reading the project appendix
    button_math = ctk.CTkButton(master = document_window, width = 252, height = 60, text = "Теоретична частина\nз математики",
                               fg_color = button_color, text_color = text_button_color, hover_color = button_hover_color, font = ("Roboto Slab", 20),
                               command = lambda: display_document(document_window, os.path.join(PATH, "math_part.pdf"), label_starttext = label_starttext, label_text = "Теоретична частина з математики"))
    # розташовуємо кнопку на вказаних координатах / places the button at the specified coordinates
    button_math.place(x = 20, y = 244)

    # створюємо кнопку ctk.CTkButton для читання теоретичної частини з інформатики / creates a ctk.CTkButton for reading the project documentation
    button_it = ctk.CTkButton(master = document_window, width = 252, height = 60, text="Теоретична частина\nз інформатики",
                                  fg_color = button_color, text_color = text_button_color, hover_color = button_hover_color, font = ("Roboto Slab", 20),
                                  command = lambda: display_document(document_window, os.path.join(PATH, "it_part.pdf"), label_starttext = label_starttext, label_text = "Теоретична частина з інформатики"))
    # розташовуємо кнопку на вказаних координатах / places the button at the specified coordinates
    button_it.place(x = 20, y = 319)
    # створюємо кнопку ctk.CTkButton для повернення до титульної сторінки / 
    button_it = ctk.CTkButton(master = document_window, width = 252, height = 60, text="Повернутися до\nтитульного вікна",
                                  fg_color = button_color, text_color = text_button_color, hover_color = button_hover_color, font = ("Roboto Slab", 20),
                                  command = lambda: document_window.destroy())
    # розташовуємо кнопку на вказаних координатах / places the button at the specified coordinates
    button_it.place(x = 20, y = 473)


    # запускаємо головний цикл обробки подій вікна / starts the main event loop of the window
    document_window.mainloop()