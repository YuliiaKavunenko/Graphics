from ..main_elements import ax, canvas
# Імпортуємо бібліотеку ticker з matplotlib для роботи з графіками / Importing library ticker from matplotlib for working with graphs
import matplotlib.ticker as ticker
# функція для побудови ДСК на холсті / function to build the coordinate grid on the canvas
def build_DSK():
    # Встановлюємо сітку (фон в клітинку) / setting the grid (background in grid)
    ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='black')

    # Створюємо осі ох та оу / creating the x and y axes
    ax.axhline(y=0, color='black', linewidth=1.5)
    ax.axvline(x=0, color='black', linewidth=1.5)

    # Діапазон значень по осях / setting the range of values on the axes
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])

    # Встановлюємо положення міток на осях (з обох боків осей) / setting the position of labels on the axes (on both sides of the axes)
    ax.xaxis.set_ticks_position('both')
    ax.yaxis.set_ticks_position('both')

    # Додаємо мітки до осей / adding labels to the axes
    ax.set_xlabel('x', color='black')
    ax.set_ylabel('y', color='black', rotation=0, labelpad=15, ha='right')

    # Встановлюємо колір міток на осях / setting the color of labels on the axes
    ax.tick_params(axis='x', colors='black')
    ax.tick_params(axis='y', colors='black')

    # Встановлюємо крок сітки / setting the grid step
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

    # Встановлюємо положення міток осей поруч з осями / setting the position of axis labels next to the axes
    ax.xaxis.set_label_coords(1.05, 0.5)
    ax.yaxis.set_label_coords(0.5, 1.05)

    # Переміщення значення по осям / moving value along the axes
    ax.xaxis.set_tick_params(pad=-260)
    ax.yaxis.set_tick_params(pad=-225)

    # Колір для фона ДСК / color for the coordinate grid background
    ax.set_facecolor('#FAF0E6')

    canvas.draw()