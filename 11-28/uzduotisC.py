import numpy as np
from scipy import constants as c
from matplotlib import pyplot as plt
import math

import grafikai.grafikai as gf

def oribitine_lygtis(kampai, p, e):
    return (p * c.au)/(1 + e * np.cos(kampai))

planetu_duom = {
    "Marsas" : [1.6, 0.093],
    "Zeme" : [1, 0.017],
    "Venera" : [0.723, 0.007],
    "Merkurijus" : [0.4, 0.205]
}

kampai = np.arange(0, 361, 10)
kampai_rad = kampai * 0.0174533

planetu_atstumai = {}

for planeta, const in planetu_duom.items():
    planetu_atstumai[planeta] = oribitine_lygtis(kampai_rad, const[0], const[1])

fig, ax = gf.subplots((13, 10))
fig = gf.define_fig(fig)
ax = gf.define_ax(ax, 
                  x_min = 0, y_min = 0,
                  x_max=math.pi*2, y_max=300e+9,
                  title="Planetų atstumas nuo saulės",
                  x_lab="Kampas, rad",
                  y_lab= f"Atstumas mln, km",
                  x_maj_tick_step=math.pi/2, y_maj_tick_step=50e+9,
                  x_min_tick_step=math.pi/4, y_min_tick_step=25e+9,
                  x_maj_tick_div=math.pi, y_maj_tick_div=1e+9,)

for planeta, atstumas in planetu_atstumai.items():
    ax.plot(kampai_rad, atstumas)

    

plt.show()