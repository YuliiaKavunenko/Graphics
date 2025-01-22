dictionary_of_variables = {
    'func1': 0,
    'ax': 0,
    'canvas': 0,
    # листи для збереження графіку і його похідних, y = ax**3 + bx**2 + cx + d / lists for storing the graph and its derivatives, y = ax**3 + bx**2 + cx + d
    'plots': [],
    'plot_2': None,
    'plot_3': None,
    # листи для збереження графіку і його похідних, у = (x**2 - a)/(x - b) / lists for storing the graph and its derivatives, y = (x**2 - a)/(x - b)
    'plots_2d': [],
    'plot_2_2': None,
    'plot_3_2': None,

    # листи для збереження точок перетину, перегину і пунктирних ліній, y = ax**3 + bx**2 + cx + d / lists for storing intersection points, inflection points, and dashed lines, y = ax**3 + bx**2 + cx + d
    'ox_points_first': [],
    'h_lines_first':[],

    'ox_points_second':[],
    'h_lines_second':[],
    'inflection_points_scatter':[],

    # листи для збереження точок локального макс. і мін. функції, y = ax**3 + bx**2 + cx + d / lists for storing local max and min points of the function, y = ax**3 + bx**2 + cx + d
    'local_max_scatter': None,
    'local_min_scatter': None,

    'local_max_scatter_s': None,
    'local_min_scatter_s':None,

    'local_min_scatter_text': None,
    'local_max_scatter_text': None,

    # листи для збереження точок локального макс. і мін. функції, у = (x**2 - a)/(x - b) / lists for storing local max and min points of the function, y = (x**2 - a)/(x - b)
    'local_max_scatter_2': None,
    'local_min_scatter_2': None,

    'local_max_scatter_text_2': None,
    'local_min_scatter_text_2': None,

    # листи для збереження точок перетину, перегину і пунктирних ліній, y = (x**2 - a**2)/x / lists for storing intersection points, inflection points, and dashed lines, y = (x**2 - a**2)/x
    'ox_points_third_first': [],
    'ox_points_third_second': [],
    'h_lines_third_first': [],
    'h_lines_third_second': [],
    'inflection_points_third_scatter': [],

    # листи для збереження графіку і його похідних, y = (x**2 - a**2)/x / lists for storing the graph and its derivatives, y = (x**2 - a**2)/x
    'plot_third_first': None,
    'plot_third_second': None,

    # листи для збереження точок локального макс. і мін. функції, y = (x**2 - a**2)/x / lists for storing local max and min points of the function, y = (x**2 - a**2)/x
    'local_max_third_first': None,
    'local_min_third_first': None,
    'local_max_text_third_first': None,
    'local_min_text_third_first': None,

    # листи для збереження графіку і його похідних, y = x/(x**2 + a) / lists for storing the graph and its derivatives, y = x/(x**2 + a)
    'plot_fourth_first': None,
    'plot_fourth_second': None,

    # листи для збереження точок перетину, перегину і пунктирних ліній, y = x/(x**2 + a) / lists for storing intersection points, i=nflection points, and dashed lines, y = x/(x**2 + a)
    'ox_points_fourth_first': [],
    'h_lines_fourth_first': [],

    'ox_points_fourth_second': [],
    'h_lines_fourth_second': [],
    'inflection_points_fourth_scatter': [],

    # листи для збереження точок локального макс. і мін. функції, y = x/(x**2 + a) / lists for storing local max and min points of the function, y = x/(x**2 + a)
    'local_max_fourth_first': None,
    'local_min_fourth_first': None,
    'local_max_text_fourth_first': None,
    'local_min_text_fourth_first': None,
    # для створення підсказки кнопок / to create a tooltip for buttons
    'tooltip_window': None,
    'inflection_points_scatter': [],  # Список для точок перегину / List for inflection points
    'inflection_points_l' : [],  # Список для підписів точок перегину / List for inflection points labels
    'inflection_points_l_3': [],
    # для п'ятого графіку / for the fifth graph
    'plot_fifth_first' : [],
    'ox_points_fifth_first' : [],
    'h_lines_fifth_first' : [],
    'local_max_fifth_first': None,
    'local_max_text_fifth_first': None,
    'local_min_fifth_first': None,
    'local_min_text_fifth_first' : None,

    'ox_points_second_5' : [],  # Збереження точок перетину з віссю x / Storing intersection points with the x-axis
    'h_lines_second_5' : [],  # Збереження пунктирних ліній / Storing dashed lines
    'plot_fifth_second': [],  # Збереження графіку другої похідної / Storing the second derivative graph
    'inflection_points_scatter_5': [],  # Збереження точок перегину / Storing inflection points
    'inflection_points_label_5': [],  # Збереження лейблу з точками перегину / Storing the label with inflection points 

    #для шостого графіку / for the sixth graph
    'plot_sixth_first': [],
    'ox_points_sixth_first':[],
    'h_lines_sixth_first' :[],
    'local_max_sixth_first': None,
    'local_max_text_sixth_first': None,
    'local_min_sixth_first': None,
    'local_min_text_sixth_first': None,
    
    'ox_points_second_6': [],  # Збереження точок перетину з віссю x / Storing intersection points with the x-axis
    'h_lines_second_6': [], # Збереження пунктирних ліній / Storing dashed lines
    'plot_sixth_second': [],  # Збереження графіку другої похідної / Storing the second derivative graph
    'inflection_points_scatter_6': [],  # Збереження точок перегину / Storing inflection points
    'inflection_points_label_6' : [],# Збереження лейблу з точками перегину / Storing the label with inflection points

    'plot_seventh_first'  : [], 
    'ox_points_seventh_first' : [], 
    'h_lines_seventh_first' : [],   
    'local_max_seventh_first' : None, 
    'local_max_text_seventh_first' : None,    
    'local_min_seventh_first'  : None,    
    'local_min_text_seventh_first' : None,

    'ox_points_second_7' : [],  
    'h_lines_second_7' : [],    
    'plot_seventh_second' : [], 
    'inflection_points_scatter_7' : [], 
    'inflection_points_label_7' : [],   
}