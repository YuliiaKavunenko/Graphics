import customtkinter as ctk
from .windows import main
from .frame import frame_first
# input на головному вікні для введення любих графіків / input on the main window for entering any graphs
input_graphic = ctk.CTkEntry(
    master=frame_first,
    width=230,
    height=40
)
# створення input на головному вікні для введення коєфіцієнта "а" для першого графіку функції / creating input on the main window for entering coefficient "a" for the first function graph
a_1 = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# створення input на головному вікні для введення коєфіцієнта "b" для першого графіку функції / creating input on the main window for entering coefficient "b" for the first function graph
b_1 = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# створення input на головному вікні для введення коєфіцієнта "c" для першого графіку функції / creating input on the main window for entering coefficient "c" for the first function graph
c_1 = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# створення input на головному вікні для введення коєфіцієнта "d" для першого графіку функції / creating input on the main window for entering coefficient "d" for the first function graph
d_1 = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# створення input на головному вікні для заповнення коєфіцієнта "а" для y' першого графіку функції / creating input on the main window for entering coefficient "a" for the y' of the first function graph
a_2 = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# створення input на головному вікні для заповнення коєфіцієнта "b" для y' першого графіку функції / creating input on the main window for entering coefficient "b" for the y' of the first function graph
b_2 = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# створення input на головному вікні для заповнення коєфіцієнта "c" для y' першого графіку функції / creating input on the main window for entering coefficient "c" for the y' of the first function graph
c_2 = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# створення input на головному вікні для заповнення коєфіцієнта "a" для y'' першого графіку функції / creating input on the main window for entering coefficient "a" for the y'' of the first function graph
a_3 = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# створення input на головному вікні для заповнення коєфіцієнта "b" для y'' першого графіку функції / creating input on the main window for entering coefficient "b" for the y'' of the first function graph
b_3 = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)

# створення input для введення коєфіцієнта "а" функції у = (x**2 - a)/(x - b) / creating input for entering coefficient "a" of the function y = (x**2 - a)/(x - b)
a_drob_1 = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# створення input для введення коєфіцієнта "b" функції у = (x**2 - a)/(x - b) / creating input for entering coefficient "b" of the function y = (x**2 - a)/(x - b)
a_drob_3 = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# створення input для введення коєфіцієнта "а" функції y = (x**2 - a**2)/x / creating input for entering coefficient "a" of the function y = (x**2 - a**2)/x
a_th_drob = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# елементи для четвертої функції y = x/(x**2 + a) / elements for the fourth function y = x/(x**2 + a)
# створення input для введення коєфіцієнту "a" функції y = x/(x**2 + a) / creating input for entering coefficient "a" of the function y = x/(x**2 + a)
a4_drob = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# створення input для введення коєфіцієнту "a" в чисельнику функції y = (x**2 + a)/(x**2 - a) / creating input for entering coefficient "a" in the numerator of the function y = (x**2 + a)/(x**2 - a)
a1_function5 = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# створення input для введення коєфіцієнту "a" в знаменнику функції y = (x**2 + a)/(x**2 - a) / creating input for entering coefficient "a" in the denominator of the function y = (x**2 + a)/(x**2 - a)
a2_function5 = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# створення input для введення коєфіцієнту "a" функції y = a/x**2 + x/a / creating input for entering coefficient "a" of the function y = a/x**2 + x/a
a1_sixth = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# створення input для введення другого коєфіцієнту "a" функції y = a/x**2 + x/a / creating input for entering coefficient "a" of the function y = a/x**2 + x/a
a2_sixth = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)
# створення input для введення коєфіцієнта "a" функції y = (x**2 + x + a)/x / creating input for entering coefficient "a" of the function y = (x**2 + x + a)/x
a1_seventh = ctk.CTkEntry(
    master=frame_first,
    width = 30,
    height = 30
)