"""
Sitas headeris turi atlikti sitas funkcijas:
1. lengvai braizyti grafikus, tokiu stilium koks patinka man.
2. grafikai gali buti su ivariai isdestytais axsais, jis turi handlint kaip atrodys, t.y labelsai, asys, t.t.
3. turi sugeneruoti ticksus ir tick labelsus pvz is sekundziu i minutes arba is metru i km arba is km i m ir t.t.
4. turi sugebeti prifitinti funkcija, kuri bus pateikiama vartotojo, t.y sugeneruoti Y_FIT vertes
5. turi sugebeti diferencijuoti funkcijas pateiktuose taskuose kai yra pateiktos Y_FIT vertes ir kai nera jos pateiktos 
"""

from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

title_font_size = 24
label_font_size = 20
tick_font_size = 13
legend_font_size = 12
label_gap = 10

def subplots(fig_w_h):
    fig, ax = plt.subplots(figsize=fig_w_h)
    return fig, ax

# defines the look of figure, is able to stylize multi ax figs
def define_fig(fig, com_title="", com_x_lab="", com_y_lab="", wspace=0.2, hspace=0.005):
    fig.subplots_adjust(
        top=0.9,
        bottom=0.11,
        left=0.09,
        right=0.981,
        hspace=0.05,
        wspace=wspace
    )
    fig.patch.set_linewidth(3)
    fig.patch.set_edgecolor('black')

    fig.suptitle(com_title,fontsize=label_font_size)
    fig.supxlabel(com_x_lab,fontsize=label_font_size)
    fig.supylabel(com_y_lab,fontsize=label_font_size)

    return fig

# basically can convert one unit to another
def calculate_tick_labels(ticks, tick_div):
    tick_labels = ticks / tick_div
    # creates a boolean array mask on whether any of the generated tick labels arent ints
    tick_labels_int_mask = np.array([(tick).is_integer() for tick in tick_labels])
    any_non_ints = np.any(tick_labels_int_mask == False)

    if any_non_ints:
        tick_labels = np.round(tick_labels, 1)
    else:
        tick_labels = np.int32(tick_labels)

    
    return tick_labels

def define_ticks(ax, 
                 tick_min, tick_max, 
                 maj_tick_step, min_tick_step = None, 
                 axis='x',
                 tick_div=1):
    
    major_ticks = np.arange(tick_min, tick_max, maj_tick_step)

    if tick_div != 1:
        major_tick_labels = calculate_tick_labels(major_ticks, tick_div)
    else:
        major_tick_labels = major_ticks

    if min_tick_step != None:
        minor_ticks = np.arange(tick_min, tick_max, min_tick_step)
    
    # pasiziuret kaip sita galima pakeist pvz funkcija ax.tick_params

    if axis == 'x':
        ax.set_xticks(major_ticks, labels=major_tick_labels)
        if min_tick_step != None:
            ax.set_xticks(minor_ticks, minor=True)
        else:
            ax.set_xticks([], minor=True)
    else:
        ax.set_yticks(major_ticks, labels=major_tick_labels)
        if min_tick_step != None:
            ax.set_yticks(minor_ticks, minor=True)
        else:
            ax.set_yticks([], minor=True)

def define_ax(ax, 
              x_tick_labels=True,
              y_tick_labels=True, 
              title="", x_lab="", y_lab="",
              x_min=None, y_min=None, 
              x_max=None, y_max=None,
              x_tick_min=None, y_tick_min=None,
              x_tick_max=None, y_tick_max=None,
              x_maj_tick_step=None, x_min_tick_step=None,
              y_maj_tick_step=None, y_min_tick_step=None,
              x_maj_tick_div = 1, y_maj_tick_div = 1):
    
    ax.set_title(title, fontsize=title_font_size, pad=label_gap)
    ax.set_xlabel(x_lab, fontsize=label_font_size, labelpad=label_gap)
    ax.set_ylabel(y_lab, fontsize=label_font_size, labelpad=label_gap)


    # pakeist visa sita baisulini if kodu bloka
    if x_min != None and x_max != None:
        ax.set_xlim(xmin = x_min, xmax = x_max)
    if y_min != None and y_max != None: 
        ax.set_ylim(ymin = y_min, ymax = y_max)

    if x_tick_labels:
        if x_tick_min == None and x_min != None:
            x_tick_min = x_min
        if x_tick_max == None and x_max != None:
            x_tick_max = x_max
        if (x_tick_min != None and x_tick_max != None and 
            x_maj_tick_step != None):
            define_ticks(ax,  
                         tick_min=x_tick_min, tick_max=x_tick_max,
                         maj_tick_step=x_maj_tick_step, min_tick_step=x_min_tick_step,
                         axis='x', tick_div=x_maj_tick_div)
        else: 
            print("Can't define X ticks, not enough arguments were provided\n")

    if y_tick_labels:
        if y_tick_min == None and y_min != None:
            y_tick_min = y_min
        if y_tick_max == None and y_max != None:
            y_tick_max = y_max
        if (y_tick_min != None and y_tick_max != None and 
            y_maj_tick_step != None):
            define_ticks(ax,  
                         tick_min=y_tick_min, tick_max=y_tick_max,
                         maj_tick_step=y_maj_tick_step, min_tick_step=y_min_tick_step,
                         axis='y', tick_div=y_maj_tick_div)
        else: 
            print("Can't define Y ticks, not enough arguments were provided\n")
        

    # ax grids
    ax.grid(which='major', axis='both', visible=True, alpha=0.5)
    ax.grid(which='minor', axis='both', visible=True, linestyle='--', alpha=0.2)

    return ax

# tries to fit a given function to X, Y, returns fitted parameters
def fit(X, Y, func, init_params):
    popt, _ = curve_fit(func, X, Y, p0=init_params)
    Y_fit = func(X,  *popt)
    return Y_fit, popt


# reikia sugalvot kaip padaryt kad is ivariu duomenu butu galima diferencijuot funkcja
# pvz duoda funkcijos taskus, bet neduoda fit, tada reikia fitint ir diferencijuot
# visokiu variantu gali but reikia apgalvot kuo daugiau
# def diferentiate_in_given_points(dif_x_points=None, dif_y_points=None, inv_func=None, func_params=None):
#     if dif_x_points == None and dif_y_points == None:
#         raise ValueError("Neither x or y points were given to differentiation function\n")
    
#     if dif_x_points == None and inv_func == None:
#         raise ValueError("Neither x points or inverse function was given to differentiation function\n")
#     elif inv_func != None and func_params == None:
#         raise ValueError("Functoin parameters were not provided to differentiation function\n")
#     else:
#         inv_func()

