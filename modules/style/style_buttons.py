from ..main_elements import *
from ..plotting import *
from ..window_with_fun import functions_window

# кольори для елементів у вікні  / colors for elements in the window
# колір для фону вікна / color for window background
background = "#CC9C87"
# колір для фону фреймів / color for frame background
frame_background = "#E2B09A"
# колір для тексту label / color for label text
text_color = "#392D20"
# колір для фону кнопки / color for button background
button_color = "#6F4E40"
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
button_hover_color = "#8B7166"
# колір при наведенні на checkbox / color when hovering over the checkbox
checkbox_hover_color = "#EBCDAE"


# кнопка для побудови базових або введених графіків / button to build basic or custom graphs
button_get.configure(
    bg_color=frame_background, # фонова кольорова кнопка / button background color
    text='✎', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Roboto Slab", 15), # шрифт тексту кнопки / button text font
    command=build_graphic # команда для виконання при натисканні кнопки / command to execute on button press
)

# кнопка для побудови і дослідження першого графіку / button to build and research the first graph
get_grachic_1.configure(
    bg_color=frame_background, # фоновий колір кнопки / button background color
    text='✎', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Arrial", 15), # шрифт тексту кнопки / button text font
    command=build_graphic_1 # команда для виконання при натисканні кнопки / command to execute on button press
)


# кнопка для очищення графіку / button to clear the graph
clean_graphic.configure(
    text='очистити', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Roboto Slab", 15), # шрифт тексту кнопки / button text font
    bg_color='white', # фоновий колір кнопки / button background color
    command=clean_button # команда для виконання при натисканні кнопки / command to execute on button press
)

# кнопка для побудови і дослідження другого графіку / button to build and research the second graph
get_drob_grachic.configure(
    bg_color=frame_background, # колір фону кнопки / button background color
    text='✎', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Arrial", 15), # шрифт тексту кнопки / button text font
    command=build_drob_graphic # команда для виконання при натисканні кнопки / command to execute on button press
)

# кнопка для побудови і дослідження третього графіку / button to build and research the third graph
third_func_button.configure(
    bg_color=frame_background, # колір фону кнопки / button background color
    text='✎', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Arrial", 15), # шрифт тексту кнопки / button text font
    command=build_third_func # команда для виконання при натисканні кнопки / command to execute on button press
)

# кнопка для відкриття вікна для вибору графіку функцій / button to open the window for selecting function graphs
choose_gr.configure(
    text_color=text_button_color, # колір тексту кнопки / button text color
    font=("Roboto Slab", 15), # шрифт тексту кнопки / button text font
    bg_color=frame_background, # колір фону кнопки / button background color
    fg_color=button_color, # колір переднього плану кнопки / button foreground color
    corner_radius=10, # радіус кутів кнопки / button corner radius
    anchor="center", # прив'язка тексту кнопки / button text anchor
    text="Обрати функцію", # текст на кнопці / button text
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    command=functions_window # команда для виконання при натисканні кнопки / command to execute on button press
)


# кнопка для побудови і дослідження четвертого графіку / button to build and research the fourth graph
fourth_func_button.configure(
    bg_color=frame_background, # колір фону кнопки / button background color
    text='✎', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Arrial", 15), # шрифт тексту кнопки / button text font
    command=build_fourth_func # команда для виконання при натисканні кнопки / command to execute on
)

# кнопка для побудови і дослідження п'ятого графіку / button to build and research the fifth graph
fifth_func_button.configure(
    bg_color=frame_background, # колір фону кнопки / button background color
    text='✎', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Arrial", 15), # шрифт тексту кнопки / button text font
    command = build_fifth_func # команда для виконання при натисканні кнопки / command to execute on button press
)
# кнопка для побудови і дослідження шостого графіку / button to build and research the sixth graph
sixth_func_button.configure(
    bg_color=frame_background, # колір фону кнопки / button background color
    text='✎', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Arrial", 15), # шрифт тексту кнопки / button text font
    command = build_sixth_func # команда для виконання при натисканні кнопки / command to execute on button press
)
# кнопка для побудови і дослідження сьомого графіку / button to build and research the seventh graph
seventh_func_button.configure(
    bg_color=frame_background, # колір фону кнопки / button background color
    text='✎', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Arrial", 15), # шрифт тексту кнопки / button text font
    command = build_seventh_func # команда для виконання при натисканні кнопки / command to execute on button press
)

button_plus.configure(
    bg_color=frame_background, # фонова кольорова кнопка / button background color
    text='+', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Roboto Slab", 15), # шрифт тексту кнопки / button text font
)
button_minus.configure(
    bg_color=frame_background, # фонова кольорова кнопка / button background color
    text='-', # текст на кнопці / text on the button
    fg_color=button_color, # колір кнопки / button color
    text_color=text_button_color, # колір тексту кнопки / button text color
    hover_color=button_hover_color, # колір кнопки при наведенні / button hover color
    font=("Roboto Slab", 15), # шрифт тексту кнопки / button text font
)

button_plus.configure(command=lambda: zoom(key='+'))
button_minus.configure(command=lambda: zoom(key='-'))